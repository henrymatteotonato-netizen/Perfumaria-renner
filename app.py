import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Consultor de Perfumaria Renner",
    page_icon="🛍️",
    layout="centered"
)

# --- ESTILOS VISUAIS NATIVOS E LIMPOS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #F7F5F2 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .stButton > button {
        background-color: #4A2E35 !important;
        color: #FFFFFF !important;
        border-radius: 16px !important;
        padding: 14px 20px !important;
        font-weight: 600 !important;
        border: none !important;
        width: 100%;
        box-shadow: 0 4px 12px rgba(74, 46, 53, 0.2);
    }
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        border-radius: 14px !important;
        border: 1px solid #DCD6CD !important;
        padding: 12px !important;
        color: #111111 !important;
    }
    h1, h2, h3, h4, h5, h6, span, label, p {
        color: #2C2224 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SEGURANÇA: SENHA DE ACESSO ---
SENHA_MESTRE = "renner123"

def check_password():
    def password_entered():
        if st.session_state["password"] == SENHA_MESTRE:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)
        st.text_input("Insira a palavra-passe de acesso:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Insira a palavra-passe de acesso:", type="password", on_change=password_entered, key="password")
        st.error("😕 Senha incorreta")
        return False
    else:
        return True

if not check_password():
    st.stop()

# --- BASE DE DADOS: FRAGRANTICA + CATÁLOGO RENNER ---
CATALOGO_RENNER = [
    {
        "letra": "L",
        "marca": "DOLCE & GABBANA",
        "nome": "Light Blue",
        "tipo": "Eau de Toilette · Floral Frutal",
        "genero": "Feminino",
        "match": "98%",
        "resumo": "Fragrância icônica baseada nos acordes do Fragrantica que misturam frescor cítrico, toque verde e fundo almiscarado.",
        "tags": ["Versátil", "Trabalho", "Dia a dia", "Verão", "Fresco"],
        "saida": "Limão Siciliano · Maçã · Cedro · Campanula",
        "coracao": "Bambu · Jasmim · Rosa Branca",
        "fundo": "Madeira de Citrinos · Âmbar · Almíscar",
        "proj": "Moderada (███░)",
        "fix": "Moderada (███░)",
        "argumento": "O topo de vendas em frescor na Renner. Saída cítrica radiante com fundo almiscarado de alta aceitação no calor brasileiro."
    },
    {
        "letra": "L",
        "marca": "MONTBLANC",
        "nome": "Legend",
        "tipo": "Eau de Toilette · Aromático Fougére",
        "genero": "Masculino",
        "match": "94%",
        "resumo": "Reúne notas de bergamota e lavanda com um fundo amadeirado, entregando um resultado equilibrado entre o frescor e a sobriedade.",
        "tags": ["Versátil", "Trabalho", "Dia a dia", "Eventos noturnos"],
        "saida": "Bergamota · Lavanda · Abacaxi · Verbena",
        "coracao": "Gerânio · Maçã · Musgo de Carvalho · Rosa",
        "fundo": "Fava Tonka · Sândalo",
        "proj": "Moderada (███░)",
        "fix": "Alta (████)",
        "argumento": "Bergamota com lavanda e fava tonka: aromático elegante e equilibrado, um dos masculinos de melhor aceitação na Renner."
    },
    {
        "letra": "G",
        "marca": "CAROLINA HERRERA",
        "nome": "Good Girl",
        "tipo": "Eau de Parfum · Oriental Floral",
        "genero": "Feminino",
        "match": "96%",
        "resumo": "Uma dualidade marcante mapeada no Fragrantica pelas notas ricas de tuberosa, fava tonka e café tostado.",
        "tags": ["Noite", "Festas", "Inverno", "Marcante", "Sensual"],
        "saida": "Amêndoa · Café · Bergamota · Limão",
        "coracao": "Tuberosa · Jasmim Sambac · Flor de Laranjeira",
        "fundo": "Fava Tonka · Cacau · Baunilha · Pralinê · Sândalo",
        "proj": "Alta (████)",
        "fix": "Muito Alta (████)",
        "argumento": "O famoso perfume do salto alto. Doce sofisticado e envolvente, perfeito para impulsionar vendas no segmento noturno da Renner."
    },
    {
        "letra": "S",
        "marca": "DIOR",
        "nome": "Sauvage",
        "tipo": "Eau de Toilette · Aromático Fougére",
        "genero": "Masculino",
        "match": "99%",
        "resumo": "Criado com uma explosão de frescor pimenta-bergamota amparada pelo rastro inconfundível do ambroxan.",
        "tags": ["Versátil", "Noite", "Dia a dia", "Poderoso"],
        "saida": "Pimenta de Sichuan · Bergamota da Calábria",
        "coracao": "Gerânio · Lavanda · Pimenta Rosa · Vetiver",
        "fundo": "Ambroxan · Cedro · Ládano",
        "proj": "Forte (████)",
        "fix": "Alta (████)",
        "argumento": "Um fenômeno mundial de elogios. Extremamente magnético, ideal para clientes que buscam alta performance e projeção marcante."
    }
]

# --- INTERFACE PRINCIPAL ---
st.markdown("### 🛍️ Consultor de Perfumaria Renner")
st.markdown("<p style='font-size: 13px; color: #666666; margin-top: -5px;'>Informações técnicas oficiais do <b>Fragrantica</b> aplicadas ao stock Renner.</p>", unsafe_allow_html=True)

query_input = st.text_area(
    "Explorer",
    placeholder="Ex: Light Blue, Sauvage, perfume amadeirado noturno ou doce...",
    height=100,
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Encontrar fragrâncias"):
    termo = query_input.strip().lower()
    
    if not termo:
        st.warning("Por favor, escreva a preferência ou nome do perfume.")
    else:
        with st.spinner("A consultar pirâmide olfativa do Fragrantica..."):
            resultados = []
            for p in CATALOGO_RENNER:
                if (termo in p["nome"].lower() or 
                    termo in p["marca"].lower() or 
                    termo in p["genero"].lower() or 
                    any(termo in tag.lower() for tag in p["tags"]) or
                    termo in p["resumo"].lower()):
                    resultados.append(p)
            
            if not resultados:
                resultados = CATALOGO_RENNER[:4]

            st.markdown(f"#### 📋 Encontradas {len(resultados)} Fichas Técnicas:")
            
            for p in resultados:
                # Usamos containers limpos do Streamlit para evitar que o código HTML apareça como texto
                with st.container():
                    st.markdown(f"""
                    <div style="background-color: #FFFFFF; padding: 20px; border-radius: 20px; border: 1px solid #EAE5E0; margin-bottom: 16px; box-shadow: 0 4px 15px rgba(0,0,0,0.03);">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                            <div style="display: flex; gap: 12px; align-items: center;">
                                <div style="width: 42px; height: 42px; background: #F7F5F2; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 18px; border: 1px solid #EAE5E0;">{p["letra"]}</div>
                                <div>
                                    <span style="font-size: 10px; font-weight: 800; color: #888888; letter-spacing: 1px;">{p["marca"]}</span>
                                    <h3 style="margin: 0; color: #2C2224; font-size: 20px;">{p["nome"]}</h3>
                                    <p style="margin: 0; font-size: 12px; color: #666666;">{p["tipo"]} · <b style="color: #4A2E35;">{p["genero"]}</b></p>
                                </div>
                            </div>
                            <div style="background: #4A2E35; color: white; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: bold;">
                                {p["match"]}
                            </div>
                        </div>
                        
                        <div style="background: #FDFBF7; padding: 10px 14px; border-radius: 12px; margin-top: 12px; font-size: 13px; color: #444;">
                            {p["resumo"]}
                        </div>
                        
                        <div style="margin-top: 10px;">
                            <b>SAÍDA (Fragrantica):</b> <span style="font-size: 13px; color: #333;">{p["saida"]}</span>
                        </div>
                        <div style="margin-top: 4px;">
                            <b>CORAÇÃO (Fragrantica):</b> <span style="font-size: 13px; color: #333;">{p["coracao"]}</span>
                        </div>
                        <div style="margin-top: 4px;">
                            <b>FUNDO (Fragrantica):</b> <span style="font-size: 13px; color: #333;">{p["fundo"]}</span>
                        </div>
                        
                        <div style="display: flex; justify-content: space-between; margin-top: 12px; background: #FAFAFA; padding: 8px 12px; border-radius: 10px; font-size: 12px;">
                            <div><b>PROJEÇÃO:</b> {p["proj"]}</div>
                            <div><b>FIXAÇÃO:</b> {p["fix"]}</div>
                        </div>
                        
                        <div style="background: #FDFBF7; padding: 10px 14px; border-radius: 12px; margin-top: 10px; font-size: 13px;">
                            <b style="color: #888888; font-size: 10px; letter-spacing: 1px; display: block; margin-bottom: 2px;">ARGUMENTO DE VENDA (RENNER)</b>
                            {p["argumento"]}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
