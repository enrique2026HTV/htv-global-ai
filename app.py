import streamlit as st
import time
import os
from ENTREVISTA_CONSCIENCIA_PRO import AnitaCerebroConsciencia
from ANITA_INPUT_DISCERNIMIENTO import DiscernimientoAnita

# 1. CONFIGURACIÓN DE ALTA GAMA
st.set_page_config(page_title="HTV GLOBAL AI | SUPREMACÍA", page_icon="🕊️", layout="wide")

# 2. INYECCIÓN DE ESTÉTICA DE LUJO (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #1a3a3d 0%, #0a0f10 100%);
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }
    
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        color: #5fb1b7;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .anita-msg {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        color: #5fb1b7;
        font-style: italic;
    }

    .stButton>button {
        background: linear-gradient(90deg, #2C5D63 0%, #5fb1b7 100%);
        color: white; border-radius: 50px; border: none; padding: 12px;
        font-weight: bold; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover { box-shadow: 0px 0px 20px #5fb1b7; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

# 3. FUNCIÓN DE CARGA SEGURA DE ACTIVOS
def mostrar_activo(ruta, tipo="imagen", ancho=None):
    if os.path.exists(ruta):
        if tipo == "imagen":
            st.image(ruta, width=ancho)
        elif tipo == "video":
            st.video(ruta)
    else:
        st.warning(f"⚠️ Activo no encontrado: {ruta}")

# 4. GESTIÓN DE ESTADO
if 'cerebro' not in st.session_state:
    st.session_state.cerebro = AnitaCerebroConsciencia("Enrique")
    st.session_state.discernidor = DiscernimientoAnita()
    st.session_state.step = "BIENVENIDA"

# --- INTERFAZ CINEMATOGRÁFICA ---
st.markdown("<h1 class='main-title'>Hágase Tu Voluntad</h1>", unsafe_allow_html=True)

col_vid, col_ui = st.columns([1.7, 1])

with col_vid:
    mostrar_activo("assets/Anita_Bienvenida.mp4", tipo="video")

with col_ui:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    
    if st.session_state.step == "BIENVENIDA":
        mostrar_activo("assets/logo_firma_nueva.png", ancho=300)
        st.markdown("### Protocolo de Identidad")
        nombre = st.text_input("Nombre del Titular", placeholder="Tu nombre completo")
        if st.button("ABRIR BÓVEDA"):
            if nombre:
                st.session_state.usuario = nombre
                st.session_state.step = "ENTREVISTA"
                st.rerun()
                
    elif st.session_state.step == "ENTREVISTA":
        # Anita lanza la pregunta desde el cerebro de consciencia
        if 'current_q' not in st.session_state:
            st.session_state.current_q = st.session_state.cerebro.flujo_conversacion()
        
        st.markdown(f"<p class='anita-msg'>'{st.session_state.current_q}'</p>", unsafe_allow_html=True)
        
        user_reply = st.chat_input("Escribe o usa tu voz...")
        
        if user_reply:
            # Discernimiento de estado (Miedo/Indiferencia/Consciencia)
            estado, feedback = st.session_state.discernidor.analizar_estado(user_reply)
            
            if estado != "CONSCIENCIA_PLENA":
                st.info(feedback)
                time.sleep(1)
            
            # Avanzar en el árbol de decisión
            st.session_state.current_q = st.session_state.cerebro.flujo_conversacion(user_reply)
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# Sello final en el pie de página
st.markdown("---")
mostrar_activo("assets/Logo_Sello_HTV_3d_Oficial.jpg", ancho=120)
