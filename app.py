import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Sistema Nutricional Inteligente",
    page_icon="🍎",
    layout="wide"
)

# =========================
# BANCO BASE DE ALIMENTOS
# Valores aproximados por porção padrão
# =========================

ALIMENTOS_BASE = {
    "Arroz cozido": {"grupo": "Carboidrato", "faixa": "Econômica", "porcao": "100g", "calorias": 130, "proteina": 2.7, "carbo": 28, "gordura": 0.3, "preco": 0.80},
    "Feijão cozido": {"grupo": "Carboidrato", "faixa": "Econômica", "porcao": "100g", "calorias": 76, "proteina": 4.8, "carbo": 13.6, "gordura": 0.5, "preco": 0.90},
    "Macarrão cozido": {"grupo": "Carboidrato", "faixa": "Econômica", "porcao": "100g", "calorias": 157, "proteina": 5.8, "carbo": 30.9, "gordura": 0.9, "preco": 0.90},
    "Batata cozida": {"grupo": "Carboidrato", "faixa": "Média", "porcao": "100g", "calorias": 86, "proteina": 1.7, "carbo": 20, "gordura": 0.1, "preco": 0.85},
    "Pão francês": {"grupo": "Carboidrato", "faixa": "Econômica", "porcao": "1 unidade", "calorias": 135, "proteina": 4.5, "carbo": 28, "gordura": 1.5, "preco": 0.90},
    "Pão integral": {"grupo": "Carboidrato", "faixa": "Média", "porcao": "2 fatias", "calorias": 140, "proteina": 6, "carbo": 24, "gordura": 2.5, "preco": 1.60},
    "Aveia": {"grupo": "Carboidrato", "faixa": "Média", "porcao": "30g", "calorias": 117, "proteina": 5, "carbo": 20, "gordura": 2.1, "preco": 0.75},
    "Banana": {"grupo": "Fruta", "faixa": "Econômica", "porcao": "1 unidade", "calorias": 90, "proteina": 1.1, "carbo": 23, "gordura": 0.3, "preco": 0.80},
    "Maçã": {"grupo": "Fruta", "faixa": "Média", "porcao": "1 unidade", "calorias": 80, "proteina": 0.4, "carbo": 21, "gordura": 0.2, "preco": 1.30},
    "Mamão": {"grupo": "Fruta", "faixa": "Média", "porcao": "1 fatia", "calorias": 70, "proteina": 0.6, "carbo": 18, "gordura": 0.2, "preco": 1.20},
    "Frutas vermelhas": {"grupo": "Fruta", "faixa": "Premium", "porcao": "100g", "calorias": 60, "proteina": 1, "carbo": 14, "gordura": 0.3, "preco": 4.50},
    "Ovo": {"grupo": "Proteína", "faixa": "Econômica", "porcao": "1 unidade", "calorias": 70, "proteina": 6, "carbo": 0.5, "gordura": 5, "preco": 0.90},
    "Frango grelhado": {"grupo": "Proteína", "faixa": "Econômica", "porcao": "100g", "calorias": 165, "proteina": 31, "carbo": 0, "gordura": 3.6, "preco": 3.20},
    "Carne moída": {"grupo": "Proteína", "faixa": "Média", "porcao": "100g", "calorias": 250, "proteina": 26, "carbo": 0, "gordura": 15, "preco": 4.50},
    "Peixe": {"grupo": "Proteína", "faixa": "Premium", "porcao": "100g", "calorias": 140, "proteina": 26, "carbo": 0, "gordura": 4, "preco": 5.50},
    "Leite": {"grupo": "Proteína", "faixa": "Econômica", "porcao": "200ml", "calorias": 120, "proteina": 6, "carbo": 9.5, "gordura": 6, "preco": 1.20},
    "Iogurte natural": {"grupo": "Proteína", "faixa": "Média", "porcao": "170g", "calorias": 110, "proteina": 7, "carbo": 12, "gordura": 3, "preco": 2.50},
    "Whey protein": {"grupo": "Proteína", "faixa": "Premium", "porcao": "30g", "calorias": 120, "proteina": 24, "carbo": 3, "gordura": 2, "preco": 4.00},
    "Azeite": {"grupo": "Gordura", "faixa": "Premium", "porcao": "1 colher", "calorias": 90, "proteina": 0, "carbo": 0, "gordura": 10, "preco": 0.70},
    "Pasta de amendoim": {"grupo": "Gordura", "faixa": "Média", "porcao": "1 colher", "calorias": 95, "proteina": 4, "carbo": 3, "gordura": 8, "preco": 0.90},
    "Castanhas": {"grupo": "Gordura", "faixa": "Premium", "porcao": "20g", "calorias": 120, "proteina": 4, "carbo": 4, "gordura": 10, "preco": 2.00},
    "Salada": {"grupo": "Legume/Verdura", "faixa": "Econômica", "porcao": "à vontade", "calorias": 30, "proteina": 1, "carbo": 6, "gordura": 0, "preco": 1.50},
    "Legumes": {"grupo": "Legume/Verdura", "faixa": "Média", "porcao": "100g", "calorias": 45, "proteina": 2, "carbo": 9, "gordura": 0.3, "preco": 1.50},
    "Brócolis": {"grupo": "Legume/Verdura", "faixa": "Premium", "porcao": "100g", "calorias": 35, "proteina": 2.4, "carbo": 7, "gordura": 0.4, "preco": 2.50},
}

# =========================
# FUNÇÕES
# =========================

def calcular_imc(peso, altura):
    altura_m = altura / 100
    return peso / (altura_m ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"


def calcular_calorias(peso, objetivo):
    if objetivo == "Emagrecer":
        return peso * 25
    elif objetivo == "Ganhar massa":
        return peso * 35
    return peso * 30


def calcular_macros(peso, objetivo):
    if objetivo == "Emagrecer":
        return round(peso * 1.8), round(peso * 2.5), round(peso * 0.8)
    elif objetivo == "Ganhar massa":
        return round(peso * 2.0), round(peso * 4.5), round(peso * 1.0)
    return round(peso * 1.6), round(peso * 3.5), round(peso * 0.9)


def multiplicador_refeicao(refeicao, objetivo):
    base = {
        "☕ Café da manhã": 1.0,
        "🍛 Almoço": 1.4,
        "🍌 Lanche da tarde": 0.8,
        "🍽️ Janta": 1.1,
        "🌙 Lanche da noite": 0.6,
    }
    if objetivo == "Emagrecer":
        return base[refeicao] * 0.8
    elif objetivo == "Ganhar massa":
        return base[refeicao] * 1.3
    return base[refeicao]


def escolher_alimento(df, grupos, faixa=None):
    filtrado = df[df["grupo"].isin(grupos)].copy()
    if faixa:
        filtrado_faixa = filtrado[filtrado["faixa"] == faixa].copy()
        if not filtrado_faixa.empty:
            filtrado = filtrado_faixa
    if filtrado.empty:
        return None
    return filtrado.sort_values("preco").iloc[0]


def montar_plano(df, objetivo, faixa=None):
    refeicoes = [
        "☕ Café da manhã",
        "🍛 Almoço",
        "🍌 Lanche da tarde",
        "🍽️ Janta",
        "🌙 Lanche da noite",
    ]
    plano = []

    for refeicao in refeicoes:
        mult = multiplicador_refeicao(refeicao, objetivo)

        if refeicao == "☕ Café da manhã":
            estrutura = [
                ("Proteína", ["Proteína"], 1.0 * mult),
                ("Carboidrato/Fruta", ["Carboidrato", "Fruta"], 1.0 * mult),
                ("Complemento", ["Gordura"], 0.5 * mult),
            ]
        elif refeicao == "🍛 Almoço":
            estrutura = [
                ("Carboidrato", ["Carboidrato"], 1.4 * mult),
                ("Proteína", ["Proteína"], 1.2 * mult),
                ("Legumes/Verduras", ["Legume/Verdura"], 1.0 * mult),
            ]
        elif refeicao == "🍌 Lanche da tarde":
            estrutura = [
                ("Fruta/Carboidrato", ["Fruta", "Carboidrato"], 1.0 * mult),
                ("Proteína", ["Proteína"], 0.8 * mult),
            ]
        elif refeicao == "🍽️ Janta":
            estrutura = [
                ("Proteína", ["Proteína"], 1.1 * mult),
                ("Carboidrato", ["Carboidrato"], 0.9 * mult),
                ("Legumes/Verduras", ["Legume/Verdura"], 1.0 * mult),
            ]
        else:
            estrutura = [
                ("Proteína leve", ["Proteína"], 0.6 * mult),
                ("Fruta/Gordura", ["Fruta", "Gordura"], 0.5 * mult),
            ]

        for tipo, grupos, qtd in estrutura:
            alimento = escolher_alimento(df, grupos, faixa)
            if alimento is not None:
                qtd = max(round(qtd, 1), 0.5)
                plano.append({
                    "Refeição": refeicao,
                    "Tipo": tipo,
                    "Alimento": alimento["alimento"],
                    "Faixa": alimento["faixa"],
                    "Porção base": alimento["porcao"],
                    "Quantidade sugerida": f"{qtd}x porção",
                    "Calorias aprox.": round(alimento["calorias"] * qtd),
                    "Proteína aprox. (g)": round(alimento["proteina"] * qtd, 1),
                    "Carbo aprox. (g)": round(alimento["carbo"] * qtd, 1),
                    "Gordura aprox. (g)": round(alimento["gordura"] * qtd, 1),
                    "Custo aprox. (R$)": round(alimento["preco"] * qtd, 2),
                })
    return pd.DataFrame(plano)


def montar_df_alimentos(alimentos_escolhidos):
    dados = []
    for alimento in alimentos_escolhidos:
        base = ALIMENTOS_BASE[alimento].copy()
        base["alimento"] = alimento
        base["preco"] = st.session_state.get(f"preco_{alimento}", base["preco"])
        dados.append(base)
    return pd.DataFrame(dados)


def mostrar_resumo_plano(plano_df):
    custo_diario = plano_df["Custo aprox. (R$)"].sum()
    custo_mensal = custo_diario * 30
    calorias_plano = plano_df["Calorias aprox."].sum()

    c1, c2, c3 = st.columns(3)
    c1.metric("Custo diário", f"R$ {custo_diario:.2f}")
    c2.metric("Custo mensal", f"R$ {custo_mensal:.2f}")
    c3.metric("Calorias do plano", f"{calorias_plano:.0f} kcal")


# =========================
# INTERFACE
# =========================

st.title("🍎 Sistema Nutricional Inteligente")
st.write("Monte uma dieta automática por faixa de preço ou personalize com os alimentos que a pessoa pode comprar e consumir.")
st.warning("Ferramenta educativa. Não substitui nutricionista, médico ou orientação individualizada.")

st.sidebar.header("👤 Dados da pessoa")
nome = st.sidebar.text_input("Nome", value="Fernando")
idade = st.sidebar.number_input("Idade", min_value=10, max_value=100, value=25)
peso = st.sidebar.number_input("Peso atual (kg)", min_value=30.0, max_value=300.0, value=80.0)
altura = st.sidebar.number_input("Altura (cm)", min_value=100, max_value=250, value=175)
objetivo = st.sidebar.selectbox("Objetivo", ["Emagrecer", "Manter peso", "Ganhar massa"])

st.sidebar.header("⚙️ Modo de montagem")
modo = st.sidebar.radio(
    "Escolha o modo",
    ["Automático por faixa de preço", "Personalizado com meus alimentos"]
)

# =========================
# DADOS GERAIS
# =========================

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
calorias = calcular_calorias(peso, objetivo)
agua = peso * 35 / 1000
proteina_meta, carbo_meta, gordura_meta = calcular_macros(peso, objetivo)

st.header(f"📊 Dashboard de {nome}")
col1, col2, col3, col4 = st.columns(4)
col1.metric("IMC", f"{imc:.1f}")
col2.metric("Classificação", classificacao)
col3.metric("Calorias estimadas", f"{calorias:.0f} kcal/dia")
col4.metric("Água estimada", f"{agua:.1f} L/dia")

st.subheader("📌 Metas de macros")
macros_df = pd.DataFrame({
    "Macro": ["Proteína", "Carboidrato", "Gordura"],
    "Meta em gramas": [proteina_meta, carbo_meta, gordura_meta]
})
col_tabela, col_grafico = st.columns(2)
with col_tabela:
    st.dataframe(macros_df, use_container_width=True)
with col_grafico:
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(macros_df["Macro"], macros_df["Meta em gramas"])
    ax.set_title("Meta diária de macros")
    ax.set_ylabel("Gramas")
    st.pyplot(fig, clear_figure=True)

st.divider()

# =========================
# MODO AUTOMÁTICO
# =========================

base_completa = montar_df_alimentos(list(ALIMENTOS_BASE.keys()))

if modo == "Automático por faixa de preço":
    st.header("🍽️ Dietas automáticas por faixa de preço")
    st.write("O sistema monta três versões: econômica, média e premium.")

    abas = st.tabs(["💸 Econômica", "💵 Média", "💎 Premium"])
    faixas = ["Econômica", "Média", "Premium"]

    for aba, faixa in zip(abas, faixas):
        with aba:
            plano_df = montar_plano(base_completa, objetivo, faixa=faixa)
            if plano_df.empty:
                st.error("Não foi possível montar este plano.")
            else:
                mostrar_resumo_plano(plano_df)
                for refeicao in plano_df["Refeição"].unique():
                    with st.expander(refeicao, expanded=True):
                        df_ref = plano_df[plano_df["Refeição"] == refeicao]
                        st.dataframe(df_ref.drop(columns=["Refeição"]), use_container_width=True)
                        st.write(f"**Custo da refeição:** R$ {df_ref['Custo aprox. (R$)'].sum():.2f}")

                lista = plano_df.groupby(["Alimento", "Porção base"], as_index=False).agg({
                    "Custo aprox. (R$)": "sum",
                    "Calorias aprox.": "sum"
                })
                lista["Custo mensal aprox. (R$)"] = lista["Custo aprox. (R$)"] * 30
                st.subheader("🛒 Lista de compras estimada")
                st.dataframe(lista, use_container_width=True)

# =========================
# MODO PERSONALIZADO
# =========================

else:
    st.header("🛒 Dieta personalizada com alimentos escolhidos")

    alimentos_escolhidos = st.multiselect(
        "Selecione os alimentos que a pessoa pode comprar/consumir",
        list(ALIMENTOS_BASE.keys()),
        default=[]
    )

    if not alimentos_escolhidos:
        st.info("Nenhum alimento selecionado. Selecione alguns alimentos ou use o modo automático por faixa de preço.")
        st.stop()

    with st.expander("💰 Editar preços médios", expanded=False):
        for alimento in alimentos_escolhidos:
            base = ALIMENTOS_BASE[alimento]
            st.number_input(
                f"{alimento} - preço médio da porção ({base['porcao']})",
                min_value=0.0,
                value=float(base["preco"]),
                step=0.10,
                key=f"preco_{alimento}"
            )

    alimentos_df = montar_df_alimentos(alimentos_escolhidos)
    plano_df = montar_plano(alimentos_df, objetivo, faixa=None)

    if plano_df.empty:
        st.error("Não foi possível montar o plano. Selecione alimentos de grupos diferentes, como proteína, carboidrato, fruta e legumes.")
    else:
        mostrar_resumo_plano(plano_df)

        for refeicao in plano_df["Refeição"].unique():
            with st.expander(refeicao, expanded=True):
                df_ref = plano_df[plano_df["Refeição"] == refeicao]
                st.dataframe(df_ref.drop(columns=["Refeição"]), use_container_width=True)
                st.write(f"**Custo da refeição:** R$ {df_ref['Custo aprox. (R$)'].sum():.2f}")

        st.subheader("🛒 Lista de compras estimada")
        lista = plano_df.groupby(["Alimento", "Porção base"], as_index=False).agg({
            "Custo aprox. (R$)": "sum",
            "Calorias aprox.": "sum"
        })
        lista["Custo mensal aprox. (R$)"] = lista["Custo aprox. (R$)"] * 30
        st.dataframe(lista, use_container_width=True)

st.success("Sistema atualizado com modo automático e modo personalizado 😄")

