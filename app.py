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
        gap:
