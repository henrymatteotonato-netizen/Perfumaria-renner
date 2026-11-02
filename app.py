
def check_password():
    def password_entered():
        if st.session_state["password"] == SENHA_MESTRE:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # Tela de Login com Estilo Limpo
        st.markdown("""
            <div style='max-width: 360px; margin: 100px auto; text-align: center; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;'>
                <h2 style='color: #2C2224; margin-bottom: 8px;'>🛍️ Perfumaria Renner</h2>
                <p style='color: #666666; font-size: 14px; margin-bottom: 24px;'>Introduza a palavra-passe para aceder ao consultor exclusivo.</p>
            </div>
        """, unsafe_allow_html=True)
        st.text_input("Palavra-passe", type="password", on_change=password_entered, key="password", label_visibility="collapsed", placeholder="Digite a senha aqui...")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Palavra-passe", type="password", on_change=password_entered, key="password", label_visibility="collapsed", placeholder="Digite a senha aqui...")
        st.error("😕 Palavra-passe incorreta. Tente novamente.")
        return False
    else:
        return True

if not check_password():
    st.stop()

# --- APLICATIVO EM HTML/CSS PURO (APÓS A SENHA) ---
html_code = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consultor de Perfumaria Renner</title>
    <style>
        :root {
            --primary-color: #4A2E35;
            --primary-hover: #3b2329;
            --bg-color: #F7F5F2;
            --card-bg: #FFFFFF;
            --text-main: #2C2224;
            --text-muted: #666666;
            --border-color: #EAE5E0;
            --tag-bg: #F4F1EA;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            padding: 16px;
            display: flex;
            justify-content: center;
        }

        .container {
            width: 100%;
            max-width: 480px;
        }

        .header {
            margin-bottom: 20px;
        }

        .header h1 {
            font-size: 20px;
            color: var(--text-main);
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .header p {
            font-size: 13px;
            color: var(--text-muted);
            margin-top: 4px;
            line-height: 1.4;
        }

        /* Cartão Principal */
        .main-card {
            background-color: var(--card-bg);
            padding: 20px;
            border-radius: 24px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
            margin-bottom: 20px;
        }

        /* Seletor de Abas Estilizado */
        .tabs-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin-bottom: 16px;
        }

        .tab-btn {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            padding: 12px;
            border-radius: 16px;
            cursor: pointer;
            text-align: left;
            transition: all 0.2s ease;
        }

        .tab-btn.active {
            background-color: var(--primary-color);
            color: #FFFFFF;
            border-color: var(--primary-color);
        }

        .tab-btn.active .tab-title, 
        .tab-btn.active .tab-desc {
            color: #FFFFFF;
        }

        .tab-title {
            font-size: 13px;
            font-weight: 600;
            color: var(--text-main);
            margin-bottom: 2px;
        }

        .tab-desc {
            font-size: 11px;
            color: var(--text-muted);
        }

        /* Caixa de Texto */
        .search-box-container {
            position: relative;
            margin-bottom: 16px;
        }

        textarea {
            width: 100%;
            background-color: #FAFAFA;
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 14px;
            font-size: 14px;
            color: var(--text-main);
            resize: none;
            height: 110px;
            outline: none;
            transition: border-color 0.2s;
        }

        textarea:focus {
            border-color: var(--primary-color);
            background-color: #FFFFFF;
        }

        /* Chips / Sugestões rápidas */
        .chips-container {
            display: flex;
            gap: 6px;
            overflow-x: auto;
            padding-bottom: 6px;
            margin-bottom: 16px;
            scrollbar-width: none;
        }
        .chips-container::-webkit-scrollbar {
            display: none;
        }

        .chip {
            background-color: var(--tag-bg);
            border: none;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            color: var(--primary-color);
            font-weight: 500;
            white-space: nowrap;
            cursor: pointer;
        }

        /* Botão de Pesquisa */
        .submit-btn {
            background-color: var(--primary-color);
            color: #FFFFFF;
            border: none;
            width: 100%;
            padding: 14px;
            border-radius: 16px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(74, 46, 53, 0.2);
            transition: background-color 0.2s;
        }

        .submit-btn:hover {
            background-color: var(--primary-hover);
        }

        /* Resultados - Cartão de Perfume */
        .perfume-card {
            background-color: var(--card-bg);
            padding: 20px;
            border-radius: 24px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04);
            border: 1px solid var(--border-color);
            margin-top: 20px;
            display: none;
        }

        .perfume-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 12px;
        }

        .brand-name {
            font-size: 11px;
            font-weight: 700;
            color: var(--text-muted);
            letter-spacing: 1px;
        }

        .perfume-name {
            font-size: 22px;
            font-weight: 700;
            color: var(--text-main);
            margin: 2px 0;
        }

        .perfume-meta {
            font-size: 13px;
            color: var(--text-muted);
        }

        .perfume-meta b {
            color: var(--primary-color);
        }

        .match-badge {
            background-color: var(--primary-color);
            color: #FFFFFF;
            padding: 6px 12px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 13px;
        }

        .description-box {
            background-color: #FDFBF7;
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 12px 14px;
            font-size: 13px;
            color: #555555;
            line-height: 1.4;
            margin-bottom: 14px;
        }

        .tags-row {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 14px;
        }

        .pill-tag {
            background-color: var(--tag-bg);
            padding: 5px 12px;
            border-radius: 16px;
            font-size: 12px;
            color: var(--primary-color);
            font-weight: 500;
        }

        .note-box {
            background-color: #FAFAFA;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 10px 14px;
            margin-bottom: 10px;
        }

        .note-title {
            font-size: 10px;
            font-weight: 700;
            color: var(--text-muted);
            letter-spacing: 1px;
            display: block;
            margin-bottom: 2px;
        }

        .note-content {
            font-size: 13px;
            color: var(--text-main);
            font-weight: 500;
        }

        .metrics-row {
            display: flex;
            justify-content: space-between;
            font-size: 12px;
            color: var(--text-main);
            background-color: #FAFAFA;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 12px 14px;
            margin-top: 10px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="header">
            <h1>🛍️ Consultor Renner</h1>
            <p>Selecione o perfil ou ocasião. Encontramos a ficha técnica exata no catálogo com indicação de género.</p>
        </div>

        <div class="main-card">
            <!-- Abas -->
            <div class="tabs-grid">
                <button class="tab-btn active" id="tabPreferencias" onclick="switchTab('pref')">
                    <div class="tab-title">❤️ Preferências</div>
                    <div class="tab-desc">O que ele já usa e ama</div>
                </button>
                <button class="tab-btn" id="tabOcasiao" onclick="switchTab('ocas')">
                    <div class="tab-title">☀️ Ocasião</div>
                    <div class="tab-desc">Quando e onde usar</div>
                </button>
            </div>

            <!-- Caixa de Texto -->
            <div class="search-box-container">
                <textarea id="userInput" placeholder="Ex: O cliente adora o Legend da Montblanc ou procura um amadeirado marcante..."></textarea>
            </div>

            <!-- Sugestões Rápidas (Chips) -->
            <div class="chips-container">
                <button class="chip" onclick="selectChip('Gosta de doces gourmand')">Doces gourmand</button>
                <button class="chip" onclick="selectChip('Usa florais marcantes')">Florais marcantes</button>
                <button class="chip" onclick="selectChip('Procura amadeirado noturno')">Amadeirado noturno</button>
                <button class="chip" onclick="selectChip('Fresco cítrico para o dia')">Fresco cítrico</button>
            </div>

            <!-- Botão de Ação -->
            <button class="submit-btn" onclick="searchPerfume()">🔍 Encontrar fragrâncias</button>
        </div>

        <!-- Cartão de Resultado Exato -->
        <div class="perfume-card" id="resultCard">
            <div class="perfume-header">
                <div>
                    <span class="brand-name">MONTBLANC</span>
                    <h2 class="perfume-name">Legend</h2>
                    <div class="perfume-meta">Eau de Toilette · Aromático Fougére · <b>Masculino</b></div>
                </div>
                <div class="match-badge">78% Match</div>
            </div>

            <div class="description-box">
                Reúne notas de bergamota e lavanda com um fundo amadeirado, entregando um resultado equilibrado entre o frescor e a sobriedade.
            </div>

            <div class="tags-row">
                <span class="pill-tag">Versátil</span>
                <span class="pill-tag">Trabalho</span>
                <span class="pill-tag">Dia a dia</span>
                <span class="pill-tag">Eventos noturnos</span>
            </div>

            <div class="note-box">
                <span class="note-title">SAÍDA</span>
                <div class="note-content">Bergamota · Lavanda · Abacaxi</div>
            </div>

            <div class="note-box">
                <span class="note-title">CORAÇÃO</span>
                <div class="note-content">Gerânio · Maçã · Rosa</div>
            </div>

            <div class="note-box">
                <span class="note-title">FUNDO</span>
                <div class="note-content">Fava tonka · Sândalo · Baunilha</div>
            </div>

            <div class="metrics-row">
                <div><b>PROJEÇÃO:</b> Moderada</div>
                <div><b>FIXAÇÃO:</b> Alta</div>
            </div>

            <div class="description-box" style="margin-top: 10px; background-color: #FDFBF7;">
                <span class="note-title">ARGUMENTO DE VENDA</span>
                <div style="font-size: 13px; color: var(--text-main); margin-top: 2px;">
                    Bergamota com lavanda e fava tonka: aromático elegante e equilibrado, um dos masculinos de melhor aceitação na Renner.
                </div>
            </div>
        </div>
    </div>

    <script>
        function switchTab(type) {
            const btnPref = document.getElementById('tabPreferencias');
            const btnOcas = document.getElementById('tabOcasiao');
            const input = document.getElementById('userInput');

            if (type === 'pref') {
                btnPref.classList.add('active');
                btnOcas.classList.remove('active');
                input.placeholder = "Ex: O cliente adora o Legend da Montblanc ou procura um amadeirado marcante...";
            } else {
                btnOcas.classList.add('active');
                btnPref.classList.remove('active');
                input.placeholder = "Ex: Perfume fresco para o dia a dia no verão ou jantar romântico...";
            }
        }

        function selectChip(text) {
            document.getElementById('userInput').value = text;
        }

        function searchPerfume() {
            const inputVal = document.getElementById('userInput').value.trim();
            if (inputVal === "") {
                alert("Por favor, escreva uma preferência ou ocasião.");
                return;
            }
            const card = document.getElementById('resultCard');
            card.style.display = "block";
            card.scrollIntoView({ behavior: 'smooth' });
        }
    </script>
</body>
</html>
"""

# Renderiza a aplicação protegida
components.html(html_code, height=750, scrolling=True)
