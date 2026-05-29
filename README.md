# Sistema Nutricional

Sistema desktop educativo para gerar planos alimentares simples a partir dos dados da pessoa, objetivo, faixa de preco e alimentos disponiveis.

> Este projeto e uma ferramenta educativa e nao substitui nutricionista, medico ou orientacao individualizada.

## Funcionalidades

- Calculo de IMC, classificacao, calorias, agua e macronutrientes estimados.
- Geracao de cardapio por refeicao.
- Modo automatico por faixa de preco.
- Modo personalizado com alimentos disponiveis em casa.
- Base de alimentos editavel.
- Busca e filtro por alimento, grupo e refeicao.
- Ajuste manual de preco dos alimentos.
- Exportacao em Excel.
- Exportacao em PDF.
- Versao desktop com PySide6.

## Como executar

Instale as dependencias:

```powershell
pip install -r requirements.txt
```

Execute a versao desktop:

```powershell
python desktop_app.py
```

Tambem existe uma versao antiga em Streamlit no arquivo `app.py`.

## Gerar executavel Windows

```powershell
pyinstaller --onefile --windowed --name "Sistema Nutricional" desktop_app.py
```

O executavel sera criado na pasta `dist`.

## Arquivos principais

- `desktop_app.py`: aplicacao desktop atual.
- `app.py`: versao antiga em Streamlit.
- `COMO_USAR_DESKTOP.md`: instrucoes rapidas de uso desktop.
- `requirements.txt`: dependencias do projeto.

## Observacao sobre dados locais

Alimentos personalizados e precos alterados podem ser salvos localmente no arquivo `alimentos_personalizados.json`. Esse arquivo fica fora do Git porque representa dados de uso da maquina.
