import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Consultor de Perfumaria Renner",
    page_icon="🛍️",
    layout="centered"
)

# --- ESTILOS VISUAIS IDÊNTICOS À REFERÊNCIA ---
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
    .perfume-result-card {
        background-color: #FFFFFF !important;
        padding: 24px;
        border-radius: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        border: 1px solid #EAE5E0 !important;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .perfume-top-flex {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        margin-bottom: 16px;
    }
    .letter-box {
        width: 48px;
        height: 48px;
        background-color: #F7F5F2;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        font-weight: 700;
        color: #2C2224;
        margin-right: 14px;
        flex-shrink: 0;
        border: 1px solid #EAE5E0;
    }
    .match-badge {
        background-color: #4A2E35;
        color: #FFFFFF !important;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 13px;
        letter-spacing: 0.5px;
    }
    .pill-tag {
        background-color: #F7F5F2 !important;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        color: #4A2E35 !important;
        font-weight: 600;
        display: inline-block;
        margin: 3px;
        border: 1px solid #EAE5E0;
    }
    .box-bloco {
        background-color: #FDFBF7 !important;
        border: 1px solid #EAE5E0 !important;
        border-radius: 16px;
        padding: 14px 16px;
        margin-top: 12px;
        margin-bottom: 12px;
    }
    .box-nota {
        background-color: #FAFAFA !important;
        border: 1px solid #EAE5E0 !important;
        border-radius: 16px;
        padding: 12px 16px;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .titulo-etiqueta {
        font-size: 10px;
        font-weight: 800;
        color: #888888 !important;
        letter-spacing: 1.2px;
        display: block;
        margin-bottom: 4px;
    }
    .texto-conteudo {
        margin: 0;
        font-size: 13px;
        color: #2C2224 !important;
        font-weight: 500;
        line-height: 1.4;
    }
    .metrics-container {
        display: flex;
        justify-content: space-between;
        margin-top: 16px;
        margin-bottom: 16px;
        background-color: #FAFAFA;
        padding: 12px 16px;
        border-radius: 16px;
        border: 1px solid #EAE5E0;
    }
    .metric-group {
        width: 48%;
    }
    .metric-header {
        display: flex;
        justify-content: space-between;
        font-size: 11px;
        font-weight: 800;
        color: #777777;
        margin-bottom: 6px;
        letter-spacing: 0.5px;
    }
    .bars-row {
        display: flex;
        gap: 4px;
    }
    .bar {
        flex: 1;
        height: 6px;
        border-radius: 3px;
        background-color: #E2DBD4;
    }
    .bar.active {
        background-color: #4A2E35;
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

# --- BASE DE DADOS COMPLETA (NOTAS OFICIAIS DO FRAGRANTICA + CATÁLOGO RENNER) ---
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
        "proj_val": "Moderada",
        "proj_bars": 3,
        "fix_val": "Moderada",
        "fix_bars": 3,
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
        "tags": ["Versátil", "Trabalho", "Dia a dia", "Eventos noturnos", "Dia e noite"],
        "saida": "Bergamota · Lavanda · Abacaxi · Verbena",
        "coracao": "Gerânio · Maçã · Musgo de Carvalho · Rosa",
        "fundo": "Fava Tonka · Sândalo",
        "proj_val": "Moderada",
        "proj_bars": 3,
        "fix_val": "Alta",
        "fix_bars": 4,
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
        "coracao": "Tuberosa · Jasmim Sambac · Flor de Laranjeira · Orris",
        "fundo": "Fava Tonka · Cacau · Baunilha · Pralinê · Sândalo",
        "proj_val": "Alta",
        "proj_bars": 4,
        "fix_val": "Muito Alta",
        "fix_bars": 4,
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
        "tags": ["Versátil", "Noite", "Dia a dia", "Poderoso", "Assinatura"],
        "saida": "Pimenta de Sichuan · Bergamota da Calábria",
        "coracao": "Gerânio · Lavanda · Pimenta Rosa · Vetiver · Patchouli",
        "fundo": "Ambroxan · Cedro · Ládano",
        "proj_val": "Forte",
        "proj_bars": 4,
        "fix_val": "Alta",
        "fix_bars": 4,
        "argumento": "Um fenômeno mundial de elogios. Extremamente magnético, ideal para clientes que buscam alta performance e projeção marcante."
    },
    {
        "letra": "2",
        "marca": "CAROLINA HERRERA",
        "nome": "212 VIP Black",
        "tipo": "Eau de Parfum · Aromatic Fougere",
        "genero": "Masculino",
        "match": "92%",
        "resumo": "Notas alcoólicas de absinto combinadas com especiarias e um fundo abaunilhado de almíscar negro.",
        "tags": ["Noite", "Balada", "Inverno", "Ousado", "Marcante"],
        "saida": "Absinto · Anis · Funcho",
        "coracao": "Lavanda",
        "fundo": "Almíscar Negro · Baunilha Negra",
        "proj_val": "Alta",
        "proj_bars": 4,
        "fix_val": "Alta",
        "fix_bars": 4,
        "argumento": "A escolha perfeita para baladas e noites frias. Tem excelente saída comercial na perfumaria masculina Renner."
    }
]

# --- INTERFACE PRINCIPAL ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown("### 🛍️ Consultor de Perfumaria Renner")
st.markdown("<p style='font-size: 13px; color: #666666; margin-top: -5px;'>Informações técnicas oficiais do <b>Fragrantica</b> aplicadas ao stock Renner.</p>", unsafe_allow_html=True)

query_input = st.text_area(
    "Explorer",
    placeholder="Ex: Light Blue, Sauvage, perfume amadeirado noturno ou doce...",
    height=110,
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
                tags_html = "".join([f'<span class="pill-tag">{t}</span>' for t in p["tags"]])
                proj_bars_html = "".join([f'<div class="bar {"active" if i < p["proj_bars"] else ""}"></div>' for i in range(4)])
                fix_bars_html = "".join([f'<div class="bar {"active" if i < p["fix_bars"] else ""}"></div>' for i in range(4)])
                
                st.markdown(f"""
                    <div class="perfume-result-card">
                        <div class="perfume-top-flex">
                            <div style="display: flex; align-items: flex-start;">
                                <div class="letter-box">{p["letra"]}</div>
                                <div>
                                    <span style="font-size: 10px; font-weight: 800; color: #888888; letter-spacing: 1.2px; display: block;">{p["marca"]}</span>
                                    <h2 style="margin: 0; color: #2C2224 !important; font-size: 22px; font-weight: 700;">{p["nome"]}</h2>
                                    <p style="margin: 2px 0 0 0; font-size: 12px; color: #666666 !important;">
                                        {p["tipo"]} · <b style="color: #4A2E35 !important;">{p["genero"]}</b>
                                    </p>
                                </div>
                            </div>
                            <div class="match-badge">
                                {p["match"]}
                            </div>
                        </div>
                        
                        <div class="box-bloco">
                            <p class="texto-conteudo">{p["resumo"]}</p>
                        </div>
                        
                        <div style="margin-top: 10px; margin-bottom: 10px;">
                            {tags_html}
                        </div>
                        
                        <div class="box-nota">
                            <span class="titulo-etiqueta">SAÍDA (FRAGRANTICA)</span>
                            <p class="texto-conteudo">{p["saida"]}</p>
                        </div>
                        
                        <div class="box-nota">
                            <span class="titulo-etiqueta">CORAÇÃO (FRAGRANTICA)</span>
                            <p class="texto-conteudo">{p["coracao"]}</p>
                        </div>
                        
                        <div class="box-nota">
                            <span class="titulo-etiqueta">FUNDO (FRAGRANTICA)</span>
                            <p class="texto-conteudo">{p["fundo"]}</p>
                        </div>
                        
                        <div class="metrics-container">
                            <div class="metric-group">
                                <div class="metric-header">
                                    <span>PROJEÇÃO</span>
                                    <span>{p["proj_val"]}</span>
                                </div>
                                <div class="bars-row">
                                    {proj_bars_html}
                                </div>
                            </div>
                            <div class="metric-group">
                                <div class="metric-header">
                                    <span>FIXAÇÃO</span>
                                    <span>{p["fix_val"]}</span>
                                </div>
                                <div class="bars-row">
                                    {fix_bars_html}
                                </div>
                            </div>
                        </div>
                        
                        <div class="box-bloco">
                            <span class="titulo-etiqueta">ARGUMENTO DE VENDA (RENNER)</span>
                            <p class="texto-conteudo" style="margin-top: 4px;">{p["argumento"]}</p>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
