# Sistema Nutricional - Versão Desktop

## Executar no Python

No terminal, dentro da pasta do projeto:

```powershell
pip install -r requirements.txt
python desktop_app.py
```

## Gerar Executável Windows

```powershell
pyinstaller --clean --onefile --windowed --name "Sistema Nutricional" desktop_app.py
```

O executável será criado na pasta `dist`.

## O que esta versão faz

- Abre como aplicativo desktop, sem navegador
- Calcula IMC, classificação, calorias, água e macros
- Monta plano alimentar por objetivo e faixa de preço
- Tem modo automático por faixa de preço
- Tem modo personalizado com alimentos em casa
- Permite marcar/desmarcar os alimentos disponíveis
- Permite buscar alimento pelo nome
- Permite filtrar a base por grupo
- Permite adicionar alimentos que não estão na lista
- Permite atualizar o preço dos alimentos
- Mostra a mistura/proteína do prato separadamente
- Permite filtrar o cardápio por refeição, prato/alimento e mistura/proteína
- Mostra lista de compras estimada
- Exporta o plano em Excel
- Exporta relatório em PDF

## Observação

Esta ferramenta é educativa e não substitui nutricionista, médico ou orientação individualizada.
