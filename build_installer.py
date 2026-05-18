#!/usr/bin/env python3
"""
Script para criar instalador do Sistema Nutricional Inteligente
Compatível com Windows, macOS e Linux
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

class AppPackager:
    def __init__(self):
        self.project_name = "Sistema Nutricional Inteligente"
        self.app_name = "SistemaNutricional"
        self.version = "1.0.0"
        self.dist_folder = Path("dist")
        self.build_folder = Path("build")
        self.output_folder = Path("Output")
        
    def clean(self):
        """Limpar builds anteriores"""
        print("🧹 Limpando builds anteriores...")
        for folder in [self.dist_folder, self.build_folder, Path("__pycache__"), Path(".pytest_cache")]:
            if folder.exists():
                shutil.rmtree(folder)
        print("✅ Limpeza concluída!\n")
    
    def install_dependencies(self):
        """Instalar dependências"""
        print("📦 Instalando dependências...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✅ Dependências instaladas!\n")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao instalar dependências: {e}")
            return False
        return True
    
    def create_icon(self):
        """Criar um ícone padrão se não existir"""
        icon_path = Path("icon.ico")
        if not icon_path.exists():
            print("📎 Criando ícone padrão...")
            try:
                # Tentar usar PIL para criar um ícone
                from PIL import Image, ImageDraw
                
                img = Image.new('RGB', (256, 256), color='#2E7D32')
                draw = ImageDraw.Draw(img)
                draw.text((80, 100), "🍎", fill='white')
                img.save("icon.ico")
                print("✅ Ícone criado!\n")
            except ImportError:
                print("⚠️  PIL não instalada. Icon será padrão.\n")
    
    def create_executable(self):
        """Criar executável com PyInstaller"""
        print("🔨 Gerando executável...")
        
        try:
            if sys.platform == "win32":
                cmd = [
                    "pyinstaller",
                    "--onefile",
                    "--windowed",
                    "--name", self.app_name,
                    "--icon=icon.ico" if Path("icon.ico").exists() else "",
                    "--add-data=.:.",
                    "app.py"
                ]
            elif sys.platform == "darwin":  # macOS
                cmd = [
                    "pyinstaller",
                    "--onefile",
                    "--windowed",
                    "--name", self.app_name,
                    "--icon=icon.icns" if Path("icon.icns").exists() else "",
                    "--add-data=.:.",
                    "app.py"
                ]
            else:  # Linux
                cmd = [
                    "pyinstaller",
                    "--onefile",
                    "--name", self.app_name,
                    "--add-data=.:.",
                    "app.py"
                ]
            
            # Remover strings vazias
            cmd = [c for c in cmd if c]
            
            subprocess.check_call(cmd)
            print("✅ Executável criado em ./dist/\n")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao criar executável: {e}\n")
            return False
    
    def create_windows_installer(self):
        """Criar instalador Windows com Inno Setup"""
        print("📦 Criando instalador Windows...")
        
        # Verificar se Inno Setup está instalado
        inno_paths = [
            Path("C:\\Program Files (x86)\\Inno Setup 6\\ISCC.exe"),
            Path("C:\\Program Files\\Inno Setup 6\\ISCC.exe"),
            Path("C:\\Program Files (x86)\\Inno Setup 5\\ISCC.exe"),
            Path("C:\\Program Files\\Inno Setup 5\\ISCC.exe"),
        ]
        
        inno_path = None
        for path in inno_paths:
            if path.exists():
                inno_path = path
                break
        
        # Criar script Inno Setup
        iss_content = f"""[Setup]
AppName={self.project_name}
AppVersion={self.version}
AppPublisher=Sistema Nutricional
AppPublisherURL=https://seu-site.com
DefaultDirName={{pf}}\\{self.app_name}
DefaultGroupName={self.project_name}
OutputDir=Output
OutputBaseFilename={self.app_name}-Setup-v{self.version}
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
SetupIconFile=icon.ico
UninstallDisplayIcon={{app}}\\{self.app_name}.exe

[Files]
Source: "dist\\{self.app_name}.exe"; DestDir: "{{app}}"; Flags: ignoreversion
Source: "dist\\_internal\\*"; DestDir: "{{app}}\\_internal"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{{group}}\\{self.project_name}"; Filename: "{{app}}\\{self.app_name}.exe"; IconIndex: 0; Comment: "Sistema Nutricional Inteligente"
Name: "{{commondesktop}}\\{self.project_name}"; Filename: "{{app}}\\{self.app_name}.exe"; IconIndex: 0; Comment: "Sistema Nutricional Inteligente"

[Run]
Filename: "{{app}}\\{self.app_name}.exe"; Description: "Executar {self.project_name}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: dirifexists; Name: "{{app}}"
Type: files; Name: "{{app}}\\*"
"""
        
        with open("installer.iss", "w", encoding="utf-8") as f:
            f.write(iss_content)
        
        if inno_path and inno_path.exists():
            try:
                print(f"Usando Inno Setup: {inno_path}")
                subprocess.check_call([str(inno_path), "installer.iss"])
                print("✅ Instalador criado em ./Output/\n")
                return True
            except subprocess.CalledProcessError as e:
                print(f"❌ Erro ao compilar instalador: {e}")
                print("⚠️  Você pode compilar manualmente: Abra 'installer.iss' com Inno Setup\n")
                return False
        else:
            print("⚠️  Inno Setup não encontrado!")
            print("📥 Baixe em: https://jrsoftware.org/isinfo.php")
            print("   Após instalar, execute este script novamente.")
            print("   OU abra manualmente: installer.iss com Inno Setup\n")
            return False
    
    def create_macos_dmg(self):
        """Criar DMG para macOS"""
        print("📦 Criando DMG para macOS...")
        
        dmg_name = f"{self.app_name}-{self.version}.dmg"
        app_path = f"dist/{self.app_name}.app"
        
        if not Path(app_path).exists():
            print("❌ App não encontrado. Execute create_executable() primeiro.")
            return False
        
        try:
            subprocess.check_call([
                "hdiutil", "create",
                "-volname", self.app_name,
                "-srcfolder", "dist",
                "-ov", "-format", "UDZO",
                dmg_name
            ])
            print(f"✅ DMG criado: {dmg_name}\n")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao criar DMG: {e}\n")
            return False
    
    def create_linux_appimage(self):
        """Instruções para criar AppImage no Linux"""
        print("📦 Instruções para criar AppImage no Linux...\n")
        print("1️⃣  Instale AppImageTool:")
        print("   https://github.com/AppImage/AppImageKit/releases\n")
        print("2️⃣  Após instalar, execute:")
        print(f"   appimagetool dist/{self.app_name}.AppDir {self.app_name}.AppImage\n")
        print("3️⃣  Para tornar executável:")
        print(f"   chmod +x {self.app_name}.AppImage\n")
        print("✅ AppImage pronto para distribuição!\n")
        return True
    
    def show_summary(self):
        """Mostrar resumo do build"""
        print("\n" + "="*60)
        print("✨ BUILD CONCLUÍDO COM SUCESSO!")
        print("="*60 + "\n")
        
        if sys.platform == "win32":
            if (Path("Output") / f"{self.app_name}-Setup-v{self.version}.exe").exists():
                print(f"📦 Instalador: Output\\{self.app_name}-Setup-v{self.version}.exe")
                print(f"   Tamanho: ~{(Path('Output') / f'{self.app_name}-Setup-v{self.version}.exe').stat().st_size / (1024*1024):.1f} MB\n")
        elif sys.platform == "darwin":
            dmg_file = Path(f"{self.app_name}-{self.version}.dmg")
            if dmg_file.exists():
                print(f"📦 Instalador: {dmg_file}")
                print(f"   Tamanho: ~{dmg_file.stat().st_size / (1024*1024):.1f} MB\n")
        else:
            exe_file = Path("dist") / self.app_name
            if exe_file.exists():
                print(f"📦 Executável: dist/{self.app_name}")
                print(f"   Tamanho: ~{exe_file.stat().st_size / (1024*1024):.1f} MB\n")
        
        print("🚀 Próximas etapas:")
        print("   1. Teste o instalador/executável em seu computador")
        print("   2. Distribua para usuários")
        print("   3. Considere publicar no GitHub Releases\n")
    
    def run_all(self):
        """Executar todo o processo"""
        print("\n" + "="*60)
        print(f"🚀 INICIANDO BUILD: {self.project_name}")
        print("="*60 + "\n")
        
        self.clean()
        
        if not self.install_dependencies():
            return
        
        self.create_icon()
        
        if not self.create_executable():
            return
        
        if sys.platform == "win32":
            self.create_windows_installer()
        elif sys.platform == "darwin":
            self.create_macos_dmg()
        else:
            self.create_linux_appimage()
        
        self.show_summary()

if __name__ == "__main__":
    packager = AppPackager()
    packager.run_all()
