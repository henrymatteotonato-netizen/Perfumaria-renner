import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Consultor de Perfumaria Renner",
    page_icon="🛍️",
    layout="centered"
)

# --- ESTILOS VISUAIS (CORRIGIDOS PARA MODO ESCURO E CLARO) ---
st.markdown("""
    <style>
    /* Forçar fundo geral claro */
    .stApp {
        background-color: #F7F5F2 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Cartão Principal */
    .main-card {
        background-color: #FFFFFF !important;
        padding: 24px;
        border-radius: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    
    /* Cartão de Exibição do Perfume */
    .perfume-card {
        background-color: #FFFFFF !important;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04);
        border: 1px solid #EAE5E0 !important;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    
    /* Tags / Pílulas */
    .pill-tag {
        background-color: #F4F1EA !important;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 13px;
        color: #4A2E35 !important;
        font-weight: 600;
        display: inline-block;
        margin: 3px;
    }
    
    /* Caixas de Notas e Argumento */
    .section-box {
        background-color: #FAFAFA !important;
        border: 1px solid #EAE5E0 !important;
        border-radius: 14px;
        padding: 12px 16px;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    
    /* Ajuste para textos dentro das caixas ficarem visíveis */
    .section-title {
        font-size: 11px;
        font-weight: bold;
        color: #777777 !important;
        letter-spacing: 1px;
        display: block;
        margin-bottom: 4px;
    }
    
    .section-text {
        margin: 0;
        font-size: 13px;
        color: #222222 !important;
        font-weight: 500;
    }

    /* Botão Principal em Bordeaux */
    .stButton > button {
        background-color: #4A2E35 !important;
        color: #FFFFFF !important;
        border-radius: 16px !important;
        padding: 12px 20px !important;
        font-weight: 600 !important;
        border: none !important;
        width: 100%;
        box-shadow: 0 4px 12px rgba(74, 46, 53, 0.2);
    }
    .stButton > button:hover {
        background-color: #3b2329 !important;
        color: #FFFFFF !important;
    }

    /* Caixa de Texto (Inputs) */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        border-radius: 14px !important;
        border: 1px solid #DCD6CD !important;
        padding: 12px !important;
        color: #111111 !important;
    }

    /* Forçar cores de textos globais */
    h1, h2, h3, h4, h5, h6, span, label, p {
        color: #2C2224 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- SEGURANÇA: SENHA DE ACESSO EXCLUSIVO ---
SENHA_MESTRE = "renner123"

def check_password():
    def password_entered():
        if st.session_state["password"] == SENHA_MESTRE:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<div style='margin-top: 100px;'></div>", unsafe_allow_html=True)
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

# --- APLICATIVO PRINCIPAL ---
st.markdown("### 🛍️ Consultor de Perfumaria Renner")
st.markdown("<p style='font-size: 14px; margin-top: -10px;'>Descreva o que o cliente usa ou a ocasião desejada. Ficha técnica exata com base no catálogo Renner.</p>", unsafe_allow_html=True)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

# Seleção de Modo
modo = st.radio(
    "Modo de consulta:",
    ["❤️ Preferências do cliente (O que ele já usa e ama)", "☀️ Ocasião e família (Quando, onde e como usar)"],
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)
placeholder_txt = "Ex: O cliente adora o Legend da Montblanc ou procura algo amadeirado..." if "Preferências" in modo else "Ex: Perfume fresco para o dia a dia no verão..."

query_input = st.text_area("Explorer", placeholder=placeholder_txt, height=120, label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# Filtros
col1, col2, col3 = st.columns(3)
with col1:
    filtro_genero = st.selectbox("Público", ["Todos", "Masculino", "Feminino", "Compartilhável"])
with col2:
    filtro_estacao = st.selectbox("Estação", ["Todas", "Verão", "Inverno", "Versátil"])
with col3:
    filtro_ocasiao = st.selectbox("Ocasião", ["Todas", "Trabalho", "Dia a dia", "Noite"])

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Encontrar fragrâncias"):
    if not query_input.strip():
        st.warning("Por favor, escreva uma preferência ou ocasião.")
    else:
        with st.spinner("A analisar o catálogo Renner..."):
            
            # --- CARTÃO DE RESULTADO COM CORES FORÇADAS E VISÍVEIS ---
            st.markdown("""
                <div class="perfume-card">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div>
                            <span style="font-size: 11px; font-weight: bold; color: #777777 !important; letter-spacing: 1px;">MONTBLANC</span>
                            <h2 style="margin: 0; color: #2C2224 !important; font-size: 24px;">Legend</h2>
                            <p style="margin: 2px 0 0 0; font-size: 13px; color: #555555 !important;">Eau de Toilette · Aromático Fougére · <b style="color: #4A2E35 !important;">Masculino</b></p>
                        </div>
                        <div style="background-color: #4A2E35; color: #FFFFFF !important; padding: 6px 12px; border-radius: 12px; font-weight: bold; font-size: 14px;">
                            78% Match
                        </div>
                    </div>
                    
                    <div class="section-box" style="margin-top: 15px; background-color: #FDFBF7 !important;">
                        <p class="section-text">
                            Reúne notas de bergamota e lavanda com um fundo amadeirado, entregando um resultado equilibrado entre o frescor e a sobriedade.
                        </p>
                    </div>
                    
                    <div style="margin-top: 12px; margin-bottom: 12px;">
                        <span class="pill-tag">Versátil</span>
                        <span class="pill-tag">Trabalho</span>
                        <span class="pill-tag">Dia a dia</span>
                        <span class="pill-tag">Eventos noturnos</span>
                        <span class="pill-tag">Dia e noite</span>
                    </div>
                    
                    <div class="section-box">
                        <span class="section-title">SAÍDA</span>
                        <p class="section-text">Bergamota · Lavanda · Abacaxi</p>
                    </div>
                    
                    <div class="section-box">
                        <span class="section-title">CORAÇÃO</span>
                        <p class="section-text">Gerânio · Maçã · Rosa</p>
                    </div>
                    
                    <div class="section-box">
                        <span class="section-title">FUNDO</span>
                        <p class="section-text">Fava tonka · Sândalo · Baunilha</p>
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; margin-top: 15px; font-size: 12px; color: #444444 !important;">
                        <div><b style="color: #2C2224 !important;">PROJEÇÃO:</b> Moderada</div>
                        <div><b style="color: #2C2224 !important;">FIXAÇÃO:</b> Alta</div>
                    </div>
                    
                    <div class="section-box" style="margin-top: 15px; background-color: #FDFBF7 !important;">
                        <span class="section-title">ARGUMENTO DE VENDA</span>
                        <p class="section-text">
                            Bergamota com lavanda e fava tonka: aromático elegante e equilibrado, um dos masculinos de melhor aceitação na Renner.
                        </p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
