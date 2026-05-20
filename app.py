import streamlit as st
from datetime import datetime
import os

# Configuração da página para celular
st.set_page_config(
    page_title="Nossa História ❤️",
    page_icon="💝",
    layout="centered"
)

# Estilização visual romântica completa e corrigida (Contador, Títulos e Cliques)
st.html("""
    <style>
    /* Fundo geral da página */
    .stApp { background-color: #fff5f5; }
    
    /* Títulos principais */
    h1, h2, h3 { color: #d6336c !important; font-family: 'Helvetica Neue', sans-serif; text-align: center; }
    
    /* Forçar a cor preta nos textos do contador de tempo */
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        color: #000000 !important;
    }
    
    /* --- CORREÇÃO DOS MOMENTOS (EXPANDERS) --- */
    /* Fundo sempre branco, borda rosa e cantos arredondados */
    .stExpander {
        background-color: white !important;
        border: 2px solid #ffdeeb !important;
        border-radius: 15px !important;
        margin-bottom: 15px !important;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.04) !important;
    }
    
    /* Forçar o título a ser SEMPRE preto e com letra bonita */
    .stExpander details summary p {
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 16px !important;
    }
    
    /* Remover o fundo preto/escuro quando clica ou passa o mouse */
    .stExpander details summary:hover, 
    .stExpander details summary:focus, 
    .stExpander details summary:active,
    .stExpander details[open] summary {
        background-color: transparent !important;
        color: #000000 !important;
    }
    
    /* Ajustar o botão principal lá embaixo */
    .stButton>button {
        background-color: #d6336c !important; color: white !important; border-radius: 20px !important;
        border: none !important; padding: 12px 25px !important; width: 100% !important; font-size: 18px !important; font-weight: bold !important;
    }
    </style>
""")

# Cabeçalho Principal
st.title("Feliz Dia dos Namorados! 🌹")
st.html("<p style='text-align: center; font-size: 16px; color: #555;'>Um cantinho especial para lembrar de cada pedacinho da nossa caminhada juntos...</p>")
st.write("---")

# ⏳ Contador de Tempo Ajustado: 17/08/2024
data_inicio = datetime(2024, 8, 17, 20, 0) 
agora = datetime.now()
diferenca = agora - data_inicio

st.html("<h3 style='text-align: center;'>⏳ Tempo ao seu lado:</h3>")
col1, col2, col3 = st.columns(3)
col1.metric("Dias", f"{diferenca.days}")
col2.metric("Horas", f"{diferenca.seconds // 3600}")
col3.metric("Minutos", f"{(diferenca.seconds % 3600) // 60}")
st.write("---")

# 📌 Seção das Memórias
st.write("## 📌 Nossos 12 Momentos Inesquecíveis")
st.html("<p style='text-align: center; color: #666; font-size: 14px;'>Clique nos momentos abaixo para abrir cada lembrança...</p>")

# Função para criar os blocos de fotos (Protegida contra fotos ausentes)
def criar_momento(numero, titulo, texto, nome_foto):
    with st.expander(f"✨ Momento {numero}: {titulo}"):
        st.html(f"<p style='font-size: 15px; color: #333; margin-top: 10px; margin-bottom: 15px;'>{texto}</p>")
        if os.path.exists(nome_foto):
            st.image(nome_foto, use_column_width=True)
        else:
            st.info(f"📸 (A foto '{nome_foto}' aparecerá aqui assim que você adicioná-la no GitHub)")

# --- SEUS 12 MOMENTOS ---
criar_momento("01", "PIX", "Dia que tivemos o nosso primeiro filho, ele era tão picutuchoo.", "foto1.jpg")
criar_momento("02", "Natal", "Agente sempre estiloso mas esse seu chinelo é muito feio ainda bem que vc não usa mais.", "foto2.jpg")
criar_momento("03", "Nossa Comecinho", "Olha a nossa cara de bobos apaixonados logo no início!", "foto3.jpg")
criar_momento("04", "Aquele Jantar Especial", "Comida boa, mas a sua companhia foi o prato principal.", "foto4.jpg")
criar_momento("05", "Nossa Primeira Viagem", "O perrengue valeu a pena só para ver esse seu sorriso de perto.", "foto5.jpg")
criar_momento("06", "Um Domingo Qualquer", "Até os dias mais simples e preguiçosos ficam perfeitos com você.", "foto6.jpg")
criar_momento("07", "Dia de Festa/Comemoração", "Celebrando a vida e as conquistas sempre um ao lado do outro.", "foto7.jpg")
criar_momento("08", "Aquele Rolê Aleatório", "Quem diria que a gente ia se divertir tanto fazendo absolutamente nada?", "foto8.jpg")
criar_momento("09", "Superando Desafios", "Obrigado por segurar a minha mão nos momentos difíceis. Somos um time.", "foto9.jpg")
criar_momento("10", "Nossos Aniversários", "Comemorar mais um ano de vida ao seu lado é o meu maior presente.", "foto10.jpg")
criar_momento("11", "Momento Carinho", "Um registro do seu abraço, que é o meu lugar favorito no mundo.", "foto11.jpg")
criar_momento("12", "Onde Estamos Hoje", "Doze momentos aqui guardados, e uma vida inteira pela frente para construir juntos.", "foto12.jpg")

st.write("---")

# 🎉 Surpresa Final
st.html("<h3 style='text-align: center;'>💌 Tenho um último recado...</h3>")
if st.button("Clique para abrir a surpresa final"):
    st.balloons() # Faz voar balões na tela
    st.success("Eu te amo daqui até a Lua! 🌙 EU VC NINO E PIX SEMPRE!!! Obrigado por esses 12 momentos e por todos os outros que ainda vamos viver. Nosso futuro vai ser lindo! ❤️")