import streamlit as st
import os

# Configuração da Página
st.set_page_config(
    page_title="Assistente de Perfumaria Renner",
    page_icon="🛍️",
    layout="centered"
)

# --- SEGURANÇA: SENHA DE ACESSO EXCLUSIVO ---
# Podes alterar a senha abaixo para uma palavra-passe tua
SENHA_MESTRE = "renner123"

def check_password():
    """Retorna True se o utilizador inserir a senha correta."""
    def password_entered():
        if st.session_state["password"] == SENHA_MESTRE:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Não armazena a senha
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Insira a palavra-passe de acesso:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Insira a palavra-passe de acesso:", type="password", on_change=password_entered, key="password")
        st.error("😕 Senha incorreta")
        return False
    else:
        return True

if not check_password():
    st.stop()  # Para a execução se não estiver autenticado

# --- APLICATIVO PRINCIPAL ---
st.title("🛍️ Consultor de Perfumaria Renner")
st.markdown("Descreva o que o cliente usa ou a ocasião desejada. Devolvemos a ficha técnica completa, **apenas com o que está no catálogo Renner**.")

# Seletor de Modo (Abas)
modo = st.radio(
    "Escolha o modo de consulta:",
    ["❤️ Preferências do cliente (O que ele já usa e ama)", "☀️ Ocasião e família (Quando, onde e como usar)"],
    label_visibility="collapsed"
)

st.markdown("---")

# Caixa de texto de entrada
if "Preferências" in modo:
    placeholder_texto = "Ex: O cliente usa 212 VIP e Sauvage..."
    sugestoes = [
        "Gosta de doces gourmand", 
        "Usa florais marcantes", 
        "Prefere frescos e cítricos", 
        "Quer algo amadeirado"
    ]
else:
    placeholder_texto = "Ex: Perfume floral para uso diurno no verão..."
    sugestoes = [
        "Floral para o dia", 
        "Amadeirado para a noite", 
        "Fresco para o verão", 
        "Fixação alta para o trabalho"
    ]

# Chips / Botões de sugestão rápida (Interativos)
st.markdown("💡 **Sugestões rápidas:**")
cols = st.columns(2)
query_input = st.text_area("Explorer", placeholder=placeholder_texto, height=100)

# Filtros extras opcionais
col1, col2, col3 = st.columns(3)
with col1:
    filtro_marca = st.selectbox("Marca", ["Todas", "Importados", "Nacionais"])
with col2:
    filtro_estacao = st.selectbox("Estação", ["Todas", "Verão", "Inverno", "Versátil"])
with col3:
    filtro_ocasiao = st.selectbox("Ocasião", ["Todas", "Dia a dia", "Trabalho", "Noite/Balada"])

# Botão de Ação Principal
if st.button("🔍 Encontrar fragrâncias", type="primary", use_container_width=True):
    if not query_input.strip():
        st.warning("Por favor, escreva uma preferência ou ocasião antes de pesquisar.")
    else:
        with st.spinner("A cruzar dados do Fragrantica com o catálogo atual da Renner..."):
            
            # --- AQUI ENTRA A LÓGICA DA IA E BUSCA DA RENNER ---
            # (Podes ligar à tua API Key da OpenAI ou Gemini nas configurações do Streamlit Secrets)
            
            # Exemplo de prompt que a IA executará por trás:
            prompt_sistema = f"""
            Aja como um assistente de perfumaria para a Lojas Renner.
            O utilizador pediu: '{query_input}'
            Filtros aplicados: Marca: {filtro_marca}, Estação: {filtro_estacao}, Ocasião: {filtro_ocasiao}.
            
            REGRAS OBRIGATÓRIAS:
            1. Use sua base de conhecimento do Fragrantica para mapear as notas e o perfil olfativo.
            2. FILTRAGEM RIGOROSA: Retorne APENAS perfumes que são comercializados atualmente pelas Lojas Renner.
            3. Para cada perfume, traga a ficha técnica estruturada: Nome/Marca, Concentração, Família Olfativa, Principais Notas, Estação Ideal, Ocasião, Projeção/Fixação e um Resumo Explicativo (argumentos de vendas).
            """
            
            # Simulação de resposta estruturada (Aqui entra a chamada real à API da IA)
            st.success("Busca concluída com sucesso!")
            
            st.markdown("### 📋 Fichas Técnicas Encontradas (Catálogo Renner):")
            
            # Exemplo de card gerado
            with st.expander("✨ **Exemplo de Perfume: Sauvage - Dior** (Eau de Toilette)", expanded=True):
                st.markdown("""
                * **Concentração:** Eau de Toilette (EDT)
                * **Família Olfativa:** Aromático Fougére
                * **Principais Notas:** Bergamota da Calábria, Pimenta de Sichuan, Ambroxan.
                * **Estação Ideal:** Versátil / Primavera e Verão
                * **Ocasião de Uso:** Trabalho, Casual, Encontros
                * **Período:** Dia e Noite
                * **Projeção e Durabilidade:** Alta projeção nas primeiras 2 horas; fixação de 6h a 8h na pele.
                * **Resumo Comercial (Argumento de Venda):** *Um clássico moderno extremamente versátil. A saída cítrica da bergamota traz frescor imediato, enquanto o ambroxan garante uma assinatura marcante e elegante que atrai elogios. Excelente saída para clientes que buscam presença sem desrespeitar o ambiente de trabalho.*
                """)
