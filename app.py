import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Consultor de Perfumaria Renner",
    page_icon="🛍️",
    layout="centered"
)

# --- ESTILOS VISUAIS PARA O LAYOUT MODERNO PERFEITO ---
st.markdown("""
    <style>
    .stApp {
        background-color: #F7F5F2 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .main-card {
        background-color: #FFFFFF !important;
        padding: 24px;
        border-radius: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .perfume-card {
        background-color: #FFFFFF !important;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04);
        border: 1px solid #EAE5E0 !important;
        margin-top: 16px;
        margin-bottom: 16px;
    }
    .pill-tag {
        background-color: #F4F1EA !important;
        padding: 5px 12px;
        border-radius: 16px;
        font-size: 12px;
        color: #4A2E35 !important;
        font-weight: 600;
        display: inline-block;
        margin: 2px;
    }
    .section-box {
        background-color: #FAFAFA !important;
        border: 1px solid #EAE5E0 !important;
        border-radius: 12px;
        padding: 10px 14px;
        margin-top: 8px;
        margin-bottom: 8px;
    }
    .section-title {
        font-size: 10px;
        font-weight: bold;
        color: #777777 !important;
        letter-spacing: 1px;
        display: block;
        margin-bottom: 2px;
    }
    .section-text {
        margin: 0;
        font-size: 13px;
        color: #222222 !important;
        font-weight: 500;
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

# --- BASE DE DADOS: DADOS DO FRAGRANTICA FILTRADOS PARA O CATÁLOGO RENNER ---
CATALOGO_RENNER = [
    {
        "marca": "DOLCE & GABBANA",
        "nome": "Light Blue EDT",
        "tipo": "Eau de Toilette · Floral Frutal · ",
        "genero": "Feminino",
        "match": "98%",
        "resumo": "Inspirado no verão mediterrâneo. Combina notas cítricas de limão siciliano com a leveza da maçã verde e bambu.",
        "tags": ["Fresco", "Verão", "Dia a dia", "Trabalho", "Casual"],
        "saida": "Limão Siciliano · Maçã Verde · Cedro · Campanula",
        "coracao": "Bambu · Jasmim · Rosa Branca",
        "fundo": "Madeira de Citrinos · Âmbar · Almíscar",
        "projecao": "Moderada",
        "fixacao": "Moderada (5h a 7h)",
        "argumento": "O perfume ícone de frescor. Ideal para clientes que buscam elegância leve em dias quentes. Um dos femininos importados mais vendidos na Renner."
    },
    {
        "marca": "MOSCHINO",
        "nome": "I Love Love",
        "tipo": "Eau de Toilette · Floral Cítrico · ",
        "genero": "Feminino",
        "match": "91%",
        "resumo": "Explosão cítrica e jovem com toranja e laranja. Tem a mesma estrutura olfativa e frescor vibrante do Light Blue.",
        "tags": ["Cítrico", "Verão", "Dia a dia", "Jovem"],
        "saida": "Toranja · Laranja · Groselha Preta · Limão",
        "coracao": "Lírio-do-Vale · Junco · Chá de Rosa · Canela",
        "fundo": "Almíscar · Cedro · Notas Amadeiradas",
        "projecao": "Moderada",
        "fixacao": "Moderada (5h a 6h)",
        "argumento": "Excelente contrapartida vibrante para quem ama o estilo do Light Blue com ótimo custo-benefício no catálogo Renner."
    },
    {
        "marca": "GIORGIO ARMANI",
        "nome": "Acqua Di Giò Pour Homme",
        "tipo": "Eau de Toilette · Aromático Aquático · ",
        "genero": "Masculino",
        "match": "89%",
        "resumo": "Referência mundial em perfumes aquáticos e frescos. Notas marinhas combinadas com bergamota e caqui.",
        "tags": ["Fresco", "Aquático", "Verão", "Trabalho", "Versátil"],
        "saida": "Bergamota · Limão · Lima · Jasmim · Laranja",
        "coracao": "Notas Marinhas · Pêssego · Calone · Ciclame · Alecrim",
        "fundo": "Almíscar · Cedro · Liquen · Âmbar · Patchouli",
        "projecao": "Moderada",
        "fixacao": "Moderada / Alta",
        "argumento": "Para quem quer o ápice da sensação de banho tomado e frescor marinho. Um clássico atemporal vendido na Renner."
    },
    {
        "marca": "CAROLINA HERRERA",
        "nome": "Good Girl EDP",
        "tipo": "Eau de Parfum · Oriental Floral · ",
        "genero": "Feminino",
        "match": "95%",
        "resumo": "Combinação marcante de tuberosa e fava tonka com toques de cacau e café. Doce, envolvente e sensual.",
        "tags": ["Noite", "Festas", "Inverno", "Marcante", "Doce"],
        "saida": "Amêndoa · Café · Bergamota · Limão",
        "coracao": "Tuberosa · Jasmim Sambac · Flor de Laranjeira · Orris",
        "fundo": "Fava Tonka · Cacau · Baunilha · Pralinê · Sândalo",
        "projecao": "Alta",
        "fixacao": "Muito Alta (8h+)",
        "argumento": "Famoso perfume do salto alto. Perfeito para clientes que querem marcar presença à noite com um rastro doce e sofisticado."
    },
    {
        "marca": "MONTBLANC",
        "nome": "Legend EDT",
        "tipo": "Eau de Toilette · Aromático Fougére · ",
        "genero": "Masculino",
        "match": "85%",
        "resumo": "Equilíbrio perfeito entre notas cítricas de saída e um fundo amadeirado macio com fava tonka.",
        "tags": ["Versátil", "Trabalho", "Dia a dia", "Elegante"],
        "saida": "Bergamota · Lavanda · Folhas de Abacaxi · Verbena",
        "coracao": "Maçã Vermelha · Gerânio · Rosa · Maçã",
        "fundo": "Fava Tonka · Sândalo · Evernyl",
        "projecao": "Moderada",
        "fixacao": "Alta (6h a 8h)",
        "argumento": "Aromático elegante e versátil de facílima aceitação. Uma das melhores escolhas masculinas para presente na Renner."
    }
]

# --- ESTRUTURA VISUAL CORRETA (DENTRO DO CARTÃO PRINCIPAL) ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown("### 🛍️ Consultor de Perfumaria Renner")
st.markdown("<p style='font-size: 13px; color: #666666; margin-top: -5px;'>Dados do <b>Fragrantica</b> filtrados exclusivamente para o catálogo Renner.</p>", unsafe_allow_html=True)

query_input = st.text_area(
    "Explorer",
    placeholder="Ex: Light Blue feminino, perfume amadeirado para o trabalho ou doce noturno...",
    height=110,
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Encontrar fragrâncias"):
    termo = query_input.strip().lower()
    
    if not termo:
        st.warning("Por favor, escreva a preferência ou ocasião do cliente.")
    else:
        with st.spinner("A cruzar dados do Fragrantica com o catálogo Renner..."):
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

            st.markdown(f"#### 📋 Encontradas {len(resultados)} Opções Compatíveis:")
            
            for p in resultados:
                tags_html = "".join([f'<span class="pill-tag">{t}</span>' for t in p["tags"]])
                
                st.markdown(f"""
                    <div class="perfume-card">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                            <div>
                                <span class="section-title">{p["marca"]}</span>
                                <h2 style="margin: 0; color: #2C2224 !important; font-size: 22px;">{p["nome"]}</h2>
                                <p style="margin: 2px 0 0 0; font-size: 13px; color: #555555 !important;">
                                    {p["tipo"]}<b style="color: #4A2E35 !important;">{p["genero"]}</b>
                                </p>
                            </div>
                            <div style="background-color: #4A2E35; color: #FFFFFF !important; padding: 6px 12px; border-radius: 12px; font-weight: bold; font-size: 13px;">
                                {p["match"]} Match
                            </div>
                        </div>
                        
                        <div class="section-box" style="margin-top: 12px; background-color: #FDFBF7 !important;">
                            <p class="section-text">{p["resumo"]}</p>
                        </div>
                        
                        <div style="margin-top: 8px; margin-bottom: 8px;">
                            {tags_html}
                        </div>
                        
                        <div class="section-box">
                            <span class="section-title">SAÍDA (FRAGRANTICA)</span>
                            <p class="section-text">{p["saida"]}</p>
                        </div>
                        
                        <div class="section-box">
                            <span class="section-title">CORAÇÃO (FRAGRANTICA)</span>
                            <p class="section-text">{p["coracao"]}</p>
                        </div>
                        
                        <div class="section-box">
                            <span class="section-title">FUNDO (FRAGRANTICA)</span>
                            <p class="section-text">{p["fundo"]}</p>
                        </div>
                        
                        <div style="display: flex; justify-content: space-between; margin-top: 10px; font-size: 12px; color: #444444 !important;">
                            <div><b style="color: #2C2224 !important;">PROJEÇÃO:</b> {p["projecao"]}</div>
                            <div><b style="color: #2C2224 !important;">FIXAÇÃO:</b> {p["fixacao"]}</div>
                        </div>
                        
                        <div class="section-box" style="margin-top: 12px; background-color: #FDFBF7 !important;">
                            <span class="section-title">ARGUMENTO DE VENDA (RENNER)</span>
                            <p class="section-text">{p["argumento"]}</p>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
