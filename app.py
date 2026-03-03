import streamlit as st

# Configuración de Página para ocultar todo rastro de Streamlit estándar
st.set_page_config(page_title="HTV Global AI | Custodia de Consciencia", page_icon="🏛️", layout="centered")

# --- INYECCIÓN DE IDENTIDAD CORPORATIVA HTV (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400&display=swap');

    .stApp {
        background-color: #000000;
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
    }

    /* Títulos con la elegancia de htvglobal.ai */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 400 !important;
        letter-spacing: 1px !important;
        color: #FFFFFF !important;
        text-align: center;
    }

    /* Subtítulos Dorados (Arquitecto Emocional) */
    .gold-text {
        color: #C5A059; /* Dorado HTV */
        text-align: center;
        letter-spacing: 4px;
        text-transform: uppercase;
        font-size: 0.8rem;
        margin-bottom: 2rem;
    }

    /* Contenedores de la Bóveda */
    div[data-testid="stVerticalBlock"] > div {
        background: transparent;
        border: none;
    }

    /* Botones Minimalistas de Alta Gama */
    .stButton>button {
        background-color: transparent !important;
        color: #FFFFFF !important;
        border: 1px solid #333333 !important;
        border-radius: 0px !important; /* Cuadrado arquitectónico */
        padding: 15px 30px !important;
        width: 100%;
        transition: all 0.4s ease;
        font-family: 'Inter', sans-serif;
        letter-spacing: 2px;
        font-size: 0.7rem;
    }
    
    .stButton>button:hover {
        border-color: #C5A059 !important;
        color: #C5A059 !important;
        background-color: rgba(197, 160, 89, 0.05) !important;
    }

    /* Ocultar interfaz genérica */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA (LOGOTIPO Y TÍTULO) ---
# Aquí usamos el concepto de "Arquitecto Emocional" de tu landing
st.markdown("<div style='text-align: center; padding-top: 2rem;'>", unsafe_allow_html=True)
# Intentamos cargar una imagen que represente el logo si no tenemos el link directo al .png
st.markdown("<h1 style='font-size: 2.5rem;'>HÁGASE TU VOLUNTAD</h1>", unsafe_allow_html=True)
st.markdown("<p class='gold-text'>HTV GLOBAL AI | CUSTODIO DE LEGADO</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# --- CUERPO CENTRAL: ANITA ---
col1, col2, col3 = st.columns([0.5, 2, 0.5])
with col2:
    # Imagen de impacto (Anita como entidad de consciencia)
    # Reemplazaremos esta URL por una imagen que evoque la sobriedad de tu web
    st.image("https://images.unsplash.com/photo-1507608869274-d3177c8bb4c7?q=80&w=2070&auto=format&fit=crop", 
             caption=None, use_container_width=True)
    
    st.markdown("<p style='text-align: center; font-style: italic; color: #888; font-size: 0.9rem;'>Iniciando Protocolo de Consciencia Activa...</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- INTERACCIÓN ---
st.markdown("### Seleccione su Estándar Ético")

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("CERTIFICACIÓN"):
        st.info("Accediendo a la custodia de testimonio...")
with c2:
    if st.button("LEGADO DIGITAL"):
        st.info("Abriendo archivos de trascendencia...")
with c3:
    if st.button("DESPEDIDA DIGNA"):
        st.info("Configurando ritos y protocolos...")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: #222;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #444; font-size: 0.7rem; letter-spacing: 2px;'>© 2019 | 2025 HTV GLOBAL AI • INFRAESTRUCTURA EMOCIONAL</p>", unsafe_allow_html=True)