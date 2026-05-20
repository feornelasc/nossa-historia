import streamlit as st
from datetime import datetime

# Configuração da página para celular
st.set_page_config(
    page_title="Nossa História ❤️",
    page_icon="💝",
    layout="centered"
)

# Estilização visual romântica
st.markdown("""
    <style>
    .main { background-color: #fff5f5; }
    h1, h2, h3 { color: #d6336c !important; font-family: 'Helvetica Neue', sans-serif; text-align: center; }
    .stButton>button {
        background-color: #d6336c; color: white; border-radius: 20px;
        border: none; padding: 12px 25px; width: 100%; font-size: 18px; font-weight: bold;
    }
    .stButton>button:hover { background-color: #c2255c; color: white; }
    .timeline-card {
        background-color: white; padding: 18px; border-radius: 15px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.06); border-left: 6px solid #d6336c; margin-bottom: 20px;
    }
    </style>
""", unsafe_with_html=True)

# Cabeçalho Principal
st.title("Feliz Dia dos Namorados! 🌹")
st.write("<p style='text-align: center; font-size: 16px;'>Um cantinho especial para lembrar de cada pedacinho da nossa caminhada juntos...</p>", unsafe_with_html=True)
st.write("---")

# ⏳ Contador de Tempo Ajustado: 17/08/2024 (Início às 20h padrão, você pode mudar o horário se souber)
data_inicio = datetime(2024, 8, 17, 20, 0) 
agora = datetime.now()
diferenca = agora - data_inicio

st.write("<h3 style='text-align: center;'>⏳ Tempo ao seu lado:</h3>", unsafe_with_html=True)
col1, col2, col3 = st.columns(3)
col1.metric("Dias", f"{diferenca.days}")
col2.metric("Horas", f"{diferenca.seconds // 3600}")
col3.metric("Minutos", f"{(diferenca.seconds % 3600) // 60}")
st.write("---")

# 📌 Seção das Memórias
st.write("## 📌 Nossos 12 Momentos Inesquecíveis")
st.write("<p style='text-align: center; color: #666;'>Clique nos momentos abaixo para abrir cada lembrança...</p>", unsafe_with_html=True)

# Função para criar os blocos de fotos de forma rápida e organizada
def criar_momento(numero, titulo, texto, nome_foto):
    with st.expander(f"✨ Momento {numero}: {titulo}"):
        st.markdown('<div class="timeline-card">', unsafe_with_html=True)
        st.write(f"<p style='font-size: 15px;'>{texto}</p>", unsafe_with_html=True)
        try:
            st.image(nome_foto, use_column_width=True)
        except:
            st.info(f"📸 (A foto '{nome_foto}' aparecerá aqui quando você subir o arquivo)")
        st.markdown('</div>', unsafe_with_html=True)

# --- PROGRAME SEUS 12 MOMENTOS AQUI ---
# Dica: Personalize os textos entre as aspas com as histórias reais de vocês!
criar_momento("01", "O Começo de Tudo", "17 de agosto de 2024. O dia em que a nossa história começou oficialmente e minha vida mudou para melhor.", "foto1.jpg")
criar_momento("02", "Primeiro Encontro Oficial", "O dia em que eu tive certeza de que você era diferente de todo mundo.", "foto2.jpg")
criar_momento("03", "Nossa Primeira Foto Juntos", "Olha a nossa cara de bobos apaixonados logo no início!", "foto3.jpg")
criar_momento("04", "Aquele Jantar Especial", "Comida boa, mas a sua companhia foi o prato principal.", "foto4.jpg")
criar_momento("05", "Nossa Primeira Viagem", "O perrengue valeu a pena só para ver esse seu sorriso de perto.", "foto5.jpg")
criar_momento("06", "Um Domingo Qualquer", "Até os dias mais simples e preguiçosos ficam perfeitos com você.", "foto6.jpg")
criar_momento("07", "Dia de Festa/Comemoração", "Celebrando a vida e as conquistas sempre um ao lado do outro.", "foto7.jpg")
criar_momento("08", "Aquele Rolê Aleatório", "Quem diria que a gente ia se divertir tanto fazendo absolutamente nada?", "foto8.jpg")
criar_momento("09", "Superando Desafios", "Obrigado por segurar a minha mão nos momentos difíceis. Somos um time.", "foto9.jpg")
criar_momento("10", "Nossos Aniversários", "Comemorar mais um ano de vida ao seu lado é o meu maior presente.", "foto10.jpg")
criar_momento("11", "Momento Carinho", "Um registro do seu abraço, que é o meu lugar favorito no mundo.", "foto11.jpg")
criar_momento("12", "Onde Estamos Hoje", "Doze momentos aqui guardados, e uma vida inteira pela frente para construir.", "foto12.jpg")

st.write("---")

# 🎉 Surpresa Final
st.write("<h3 style='text-align: center;'>💌 Tenho um último recado...</h3>", unsafe_with_html=True)
if st.button("Clique para abrir a surpresa final"):
    st.balloons() # Faz voar balões na tela do celular dela
    st.success("Eu te amo daqui até a Lua! 🌙 Obrigado por esses 12 momentos e por todos os outros que ainda vamos viver. Prepara o coração porque nosso futuro vai ser lindo! ❤️")