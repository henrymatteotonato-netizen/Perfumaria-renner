import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Consultor de Perfumaria Renner",
    page_icon="🛍️",
    layout="centered"
)

# --- ESTILOS VISUAIS EXACTOS DA REFERÊNCIA ---
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

# --- BASE DE DADOS COMPLETA (FRAGRANTICA + CATÁLOGO RENNER) ---
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
        "coracao": "Tuberosa · Jasmim Sambac · Flor de Laranjeira",
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
        "tags": ["Versátil", "Noite", "Dia a dia", "Poderoso"],
        "saida": "Pimenta de Sichuan · Bergamota da Calábria",
        "coracao": "Gerânio · Lavanda · Pimenta Rosa · Vetiver",
        "fundo": "Ambroxan · Cedro · Ládano",
        "proj_val": "Forte",
        "proj_bars": 4,
        "fix_val": "Alta",
        "fix_bars": 4,
        "argumento": "Um fenômeno mundial de elogios. Extremamente magnético, ideal para clientes que buscam alta performance e projeção marcante."
    }
]

# --- INTERFACE PRINCIPAL ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)

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
                tags_html = "".join([f'<span style="background-color: #F7F5F2; padding: 6px 14px; border-radius: 20px; font-size: 12px; color: #4A2E35; font-weight: 600; display: inline-block; margin: 3px; border: 1px solid #EAE5E0;">{t}</span>' for t in p["tags"]])
                
                proj_bars = "".join([f'<div style="flex:1; height:6px; border-radius:3px; background-color:{"#4A2E35" if i < p["proj_bars"] else "#E2DBD4"};"></div>' for i in range(4)])
                fix_bars = "".join([f'<div style="flex:1; height:6px; border-radius:3px; background-color:{"#4A2E35" if i < p["fix_bars"] else "#E2DBD4"};"></div>' for i in range(4)])

                # Construção limpa em bloco HTML contínuo (renderiza sem virar código de texto na tela)
                card_html = f"""
                <div style="background-color: #FFFFFF; padding: 24px; border-radius: 24px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05); border: 1px solid #EAE5E0; margin-top: 20px; margin-bottom: 20px;">
                    <div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 16px;">
                        <div style="display: flex; align-items: flex-start;">
                            <div style="width: 48px; height: 48px; background-color: #F7F5F2; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: 700; color: #2C2224; margin-right: 14px; flex-shrink: 0; border: 1px solid #EAE5E0;">{p["letra"]}</div>
                            <div>
                                <span style="font-size: 10px; font-weight: 800; color: #888888; letter-spacing: 1.2px; display: block;">{p["marca"]}</span>
                                <h2 style="margin: 0; color: #2C2224; font-size: 22px; font-weight: 700;">{p["nome"]}</h2>
                                <p style="margin: 2px 0 0 0; font-size: 12px; color: #666666;">{p["tipo"]} · <b style="color: #4A2E35;">{p["genero"]}</b></p>
                            </div>
                        </div>
                        <div style="background-color: #4A2E35; color: #FFFFFF; padding: 6px 14px; border-radius: 20px; font-weight: 700; font-size: 13px;">{p["match"]}</div>
                    </div>
                    
                    <div style="background-color: #FDFBF7; border: 1px solid #EAE5E0; border-radius: 16px; padding: 14px 16px; margin-top: 12px; margin-bottom: 12px; font-size: 13px; color: #2C2224;">
                        {p["resumo"]}
                    </div>
                    
                    <div style="margin-top: 10px; margin-bottom: 10px;">
                        {tags_html}
                    </div>
                    
                    <div style="background-color: #FAFAFA; border: 1px solid #EAE5E0; border-radius: 16px; padding: 12px 16px; margin-top: 10px; margin-bottom: 10px;">
                        <span style="font-size: 10px; font-weight: 800; color: #888888; letter-spacing: 1.2px; display: block; margin-bottom: 4px;">SAÍDA (FRAGRANTICA)</span>
                        <p style="margin:0; font-size:13px; color:#2C2224; font-weight:500;">{p["saida"]}</p>
                    </div>
                    
                    <div style="background-color: #FAFAFA; border: 1px solid #EAE5E0; border-radius: 16px; padding: 12px 16px; margin-top: 10px; margin-bottom: 10px;">
                        <span style="font-size: 10px; font-weight: 800; color: #888888; letter-spacing: 1.2px; display: block; margin-bottom: 4px;">CORAÇÃO (FRAGRANTICA)</span>
                        <p style="margin:0; font-size:13px; color:#2C2224; font-weight:500;">{p["coracao"]}</p>
                    </div>
                    
                    <div style="background-color: #FAFAFA; border: 1px solid #EAE5E0; border-radius: 16px; padding: 12px 16px; margin-top: 10px; margin-bottom: 10px;">
                        <span style="font-size: 10px; font-weight: 800; color: #888888; letter-spacing: 1.2px; display: block; margin-bottom: 4px;">FUNDO (FRAGRANTICA)</span>
                        <p style="margin:0; font-size:13px; color:#2C2224; font-weight:500;">{p["fundo"]}</p>
                    </div>
                    
                    <div style="display: flex; justify-content: space-between; margin-top: 16px; margin-bottom: 16px; background-color: #FAFAFA; padding: 12px 16px; border-radius: 16px; border: 1px solid #EAE5E0;">
                        <div style="width: 48%;">
                            <div style="display:flex; justify-content:space-between; font-size:11px; font-weight:800; color:#777; margin-bottom:6px;">
                                <span>PROJEÇÃO</span><span>{p["proj_val"]}</span>
                            </div>
                            <div style="display:flex; gap:4px;">{proj_bars}</div>
                        </div>
                        <div style="width: 48%;">
                            <div style="display:flex; justify-content:space-between; font-size:11px; font-weight:800; color:#777; margin-bottom:6px;">
                                <span>FIXAÇÃO</span><span>{p["fix_val"]}</span>
                            </div>
                            <div style="display:flex; gap:4px;">{fix_bars}</div>
                        </div>
                    </div>
                    
                    <div style="background-color: #FDFBF7; border: 1px solid #EAE5E0; border-radius: 16px; padding: 14px 16px; margin-top: 12px;">
                        <span style="font-size: 10px; font-weight: 800; color: #888888; letter-spacing: 1.2px; display: block; margin-bottom: 4px;">ARGUMENTO DE VENDA (RENNER)</span>
                        <p style="margin:0; font-size:13px; color:#2C2224; font-weight:500;">{p["argumento"]}</p>
                    </div>
                </div>
                """
                
                # Renderiza o HTML puro sem quebrar a estrutura do Streamlit
                st.html(card_html)

st.markdown('</div>', unsafe_allow_html=True)
