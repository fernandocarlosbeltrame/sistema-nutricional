# Guia de Uso - Sistema Nutricional Inteligente

## 📋 Índice

1. [Instalação](#instalação)
2. [Primeiro Acesso](#primeiro-acesso)
3. [Modo Automático](#modo-automático)
4. [Modo Personalizado](#modo-personalizado)
5. [Entendendo os Resultados](#entendendo-os-resultados)
6. [FAQ](#faq)
7. [Troubleshooting](#troubleshooting)

---

## 🚀 Instalação

### Windows

1. Baixe `SistemaNutricional-Setup-v1.0.0.exe`
2. Clique no arquivo para executar o instalador
3. Se aparecer aviso do Windows, clique "More info" → "Run anyway"
4. Siga as instruções do instalador
5. O app será instalado em: `C:\Program Files\SistemaNutricional`

### macOS

1. Baixe `SistemaNutricional-1.0.0.dmg`
2. Abra o arquivo DMG
3. Arraste o ícone para a pasta "Applications"
4. Na primeira execução, clique "Open" se houver aviso de segurança
5. Pronto! O app está instalado em: `/Applications/SistemaNutricional.app`

### Linux

1. Baixe `SistemaNutricional-1.0.0.AppImage`
2. Abra um terminal na pasta do download
3. Execute: `chmod +x SistemaNutricional-1.0.0.AppImage`
4. Execute: `./SistemaNutricional-1.0.0.AppImage`

---

## 📖 Primeiro Acesso

### Passo 1: Inserir Dados Básicos

Na barra lateral esquerda, preencha:

- **Nome**: Seu nome (usado nos relatórios)
- **Idade**: Sua idade em anos
- **Peso Atual**: Seu peso em quilogramas
- **Altura**: Sua altura em centímetros
- **Objetivo**: Escolha entre:
  - 🔴 **Emagrecer**: Redução calórica e proteína aumentada
  - 🟡 **Manter peso**: Ingestão equilibrada
  - 🟢 **Ganhar massa**: Superávit calórico e proteína alta

### Passo 2: Configurar Preferências

Ainda na barra lateral:

- **Alergias/Restrições**: Selecione quaisquer alergias ou restrições alimentares
- **Modo de Montagem**: Escolha entre automático ou personalizado

### Passo 3: Visualizar Dashboard

Na área principal, você verá:

```
📊 Dashboard de [Seu Nome]
├─ IMC: [Seu IMC]
├─ Classificação: [Classificação IMC]
├─ Calorias estimadas: [Calorias] kcal/dia
└─ Água estimada: [Litros] L/dia
```

---

## 🍽️ Modo Automático

Este modo gera automaticamente planos nutricionais completos por faixa de preço.

### Como Usar

1. Selecione "Automático por faixa de preço" na barra lateral
2. Clique na aba desejada:
   - **💸 Econômica**: Plano mais barato (~R$ 3-5/dia)
   - **💵 Média**: Opção intermediária (~R$ 8-12/dia)
   - **💎 Premium**: Melhor variedade (~R$ 15-20/dia)

### Entendendo os Resultados

#### Resumo do Plano

```
💰 Custo diário       | R$ 4,50
🔥 Calorias           | 2.100 kcal
💪 Proteína           | 120g
🥗 Carboidratos       | 280g
```

#### Refeições Detalhadas

Clique em cada refeição para expandir:

- **☕ Café da Manhã**: ~600 kcal
- **🍛 Almoço**: ~900 kcal
- **🍌 Lanche da Tarde**: ~450 kcal
- **🍽️ Janta**: ~800 kcal
- **🌙 Lanche da Noite**: ~350 kcal

#### Lista de Compras

No final da tela, encontre:

| Alimento | Porção | Custo Diário | Custo Mensal |
|----------|--------|------------|------------|
| Arroz | 100g | R$ 0,80 | R$ 24,00 |
| Frango | 100g | R$ 3,20 | R$ 96,00 |
| ... | ... | ... | ... |

### Exportar Plano

1. Clique em **"📥 Baixar como CSV"**
2. Arquivo será salvo em seu computador
3. Abra em Excel ou planilha similar

---

## 🎯 Modo Personalizado

Crie planos com alimentos específicos que você gosta ou tem acesso.

### Como Usar

1. Selecione "Personalizado com meus alimentos"
2. Escolha os alimentos que deseja:
   - Mínimo de 3 alimentos de grupos diferentes
   - Recomendado: Proteína, carboidrato, fruta/legume

### Exemplo de Seleção

```
✅ Frango grelhado (Proteína)
✅ Arroz cozido (Carboidrato)
✅ Banana (Fruta)
✅ Brócolis (Legume)
✅ Azeite (Gordura)
```

### Ajustar Preços

Se os preços padrão não correspondem à sua região:

1. Clique em "💰 Editar preços médios"
2. Modifique os valores conforme necessário
3. O plano será recalculado automaticamente

---

## 📊 Entendendo os Resultados

### O que é IMC?

IMC (Índice de Massa Corporal) = Peso / (Altura)²

**Classificações:**
- 🔵 Abaixo do peso: IMC < 18,5
- 🟢 Peso normal: 18,5 ≤ IMC < 25
- 🟡 Sobrepeso: 25 ≤ IMC < 30
- 🔴 Obesidade: IMC ≥ 30

### Metas de Macronutrientes

**Proteína**
- Emagrecer: 1.8g/kg de peso
- Manter: 1.6g/kg de peso
- Ganhar: 2.0g/kg de peso

**Carboidratos**
- Emagrecer: 2.5g/kg de peso
- Manter: 3.5g/kg de peso
- Ganhar: 4.5g/kg de peso

**Gordura**
- Emagrecer: 0.8g/kg de peso
- Manter: 0.9g/kg de peso
- Ganhar: 1.0g/kg de peso

### Cálculo de Calorias

**Fórmula por Objetivo:**
- Emagrecer: 25 kcal/kg
- Manter: 30 kcal/kg
- Ganhar: 35 kcal/kg

**Exemplo:** Pessoa com 80kg querendo emagrecer
- 80 × 25 = 2.000 kcal/dia

### Hidratação

**Fórmula:** (Peso em kg) × 35 / 1000 = Litros/dia

**Exemplo:** Pessoa com 80kg
- (80 × 35) / 1000 = 2,8 L/dia

---

## ❓ FAQ

### P: Qual é a melhor faixa de preço?
**R:** Depende de seu orçamento. Todas as faixas fornecem nutrição adequada. A diferença é na variedade de alimentos.

### P: Posso usar este app sem internet?
**R:** Sim! O app funciona 100% offline. Todos os dados são salvos em seu computador.

### P: Onde são salvos meus dados?
**R:** Tudo é salvo localmente em arquivos JSON no seu computador. Nenhum dado é enviado para internet.

### P: Como funciona o histórico?
**R:** Quando você clica "💾 Salvar este plano", o sistema salva um snapshot com:
- Data de criação
- Seus dados (nome, objetivo)
- Totais de custo e calorias

### P: Posso usar para outra pessoa?
**R:** Sim! Basta alterar o nome e dados na barra lateral. Sistema se ajusta automaticamente.

### P: O que significam as emojis?
**R:** São visuais para facilitar identificação das refeições e categorias.

### P: Posso exportar o histórico?
**R:** Sim! Arquivo `planos_historico.json` contém todos os planos. Você pode abrir com qualquer editor de texto.

---

## 🐛 Troubleshooting

### "Aplicação não abre"

**Windows:**
- Clique em "More info" → "Run anyway"
- Verifique se tem 150MB livres

**macOS:**
- Clique em "Open" na janela de segurança
- Ou execute no terminal:
  ```bash
  sudo xattr -rd com.apple.quarantine /Applications/SistemaNutricional.app
  ```

**Linux:**
- Abra terminal e execute:
  ```bash
  chmod +x ./SistemaNutricional-1.0.0.AppImage
  ./SistemaNutricional-1.0.0.AppImage
  ```

### "Porta 8501 já em uso"

Se aparecer erro sobre porta:
```bash
streamlit run app.py --server.port=8502
```

### "Erro ao gerar plano"

Possíveis causas:
- Menos de 3 alimentos selecionados
- Todos os alimentos de um mesmo grupo
- Preço negativo

**Solução:** Selecione alimentos de grupos diferentes.

### "Arquivo CSV não abre"

- Verifique se Excel/Planilha está instalado
- Tente abrir com aplicativo diferente
- Verifique se arquivo não está aberto já

### "Dashboard não atualiza"

- Clique em "R" para recarregar a página
- Feche e reabra o navegador
- Tente com outro navegador

---

## 💡 Dicas Úteis

1. **Salve seus planos regularmente** para comparar evolução
2. **Atualize preços periodicamente** conforme mudanças de mercado
3. **Use o modo automático** para inspiração
4. **Combine com modo personalizado** para customizar
5. **Imprima a lista de compras** ao ir ao supermercado
6. **Consulte nutricionista** para validar plano

---

## ⚠️ Lembrete Importante

Este é um **SISTEMA EDUCATIVO**. 

**Sempre consulte um profissional de saúde antes de:**
- Mudar hábitos alimentares significativamente
- Iniciar uma nova dieta
- Tomar suplementos
- Fazer mudanças drásticas de peso

---

## 📞 Precisa de Ajuda?

1. Verifique este guia
2. Abra um [Issue no GitHub](https://github.com/fernandocarlosbeltrame/sistema-nutricional/issues)
3. Descreva o problema com detalhes

---

**Desenvolvido com ❤️ para sua saúde**

*Sistema Nutricional Inteligente © 2025*
