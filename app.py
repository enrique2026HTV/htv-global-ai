import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA: ESTÉTICA DE ALTA GAMA ---
st.set_page_config(page_title="HTV Global | APAP AI", page_icon="🏛️", layout="centered")

# --- INYECCIÓN DE IDENTIDAD CORPORATIVA DE EXCELENCIA (CSS) ---
st.markdown("""
    <style>
    /* Importación de Fuentes de Autor */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;600&display=swap');

    /* Fondo Negro Obsidiana Profundo */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
    }

    /* Títulos Solemnes con Tipografía Serif (Elegancia HTV) */
    h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        font-family: 'Playfair Display', serif !important;
        font-weight: 400 !important;
        letter-spacing: 1px !important;
        color: #FFFFFF !important;
        text-align: center;
        margin-top: 1rem;
    }

    /* Subtítulos Dorados HTV (Acento de Autor) */
    .gold-text {
        color: #C5A059 !important; /* Dorado Mate Cepillado */
        text-align: center !important;
        letter-spacing: 3px !important;
        text-transform: uppercase !important;
        font-size: 0.8rem !important;
        margin-bottom: 2rem !important;
    }

    /* Tono Ético/Emocional */
    .ethical-prompt {
        color: #FFFFFF !important;
        font-family: 'Playfair Display', serif !important;
        font-style: italic !important;
        text-align: center !important;
        font-size: 1.1rem !important;
        line-height: 1.6 !important;
        margin-top: 1.5rem !important;
        margin-bottom: 2rem !important;
    }

    /* Botones Minimalistas de Alta Gama - No Planos */
    .stButton>button {
        background-color: #000000 !important;
        color: #FFFFFF !important;
        border: 1px solid #C5A059 !important; /* Borde Dorado */
        border-radius: 4px !important; /* Cuadrado Arquitectónico */
        padding: 15px 30px !important;
        width: 100%;
        transition: all 0.4s ease;
        font-family: 'Inter', sans-serif;
        letter-spacing: 2px;
        font-size: 0.75rem;
        text-transform: uppercase;
        font-weight: 300;
        box-shadow: 0 4px 6px rgba(197, 160, 89, 0.1); /* Sutil sombra dorada */
    }
    
    .stButton>button:hover {
        border-color: #FFFFFF !important;
        color: #C5A059 !important;
        background-color: rgba(197, 160, 89, 0.05) !important;
        box-shadow: 0 6px 12px rgba(197, 160, 89, 0.2);
    }

    /* Ocultar interfaz genérica de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    </style>
    """, unsafe_allow_html=True)

# --- MEMORIA DEL SISTEMA (ROADMAP Y ESTADOS) ---
if 'fase' not in st.session_state:
    st.session_state.fase = 'umbral'
if 'perfil_emocional' not in st.session_state:
    st.session_state.perfil_emocional = None

# =========================================================
# --- FASE 1: EL UMBRAL (INTERACCIÓN INICIAL) ---
# =========================================================
if st.session_state.fase == 'umbral':
    # --- CABECERA (LOGOTIPO Y TÍTULO SOLEMNE) ---
    st.markdown("<div style='text-align: center; padding-top: 2rem;'>", unsafe_allow_html=True)
    # Logotipo (Maquetado aquí como texto serif elegante)
    st.markdown("<h1 style='font-size: 3rem;'>HÁGASE TU VOLUNTAD</h1>", unsafe_allow_html=True)
    st.markdown("<p class='gold-text'>HTV GLOBAL AI | CUSTODIO DE LEGADO</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- CUERPO CENTRAL: ANITA (APAP) AI AVATAR INTERACTIVO ---
    col1, col2, col3 = st.columns([0.5, 2, 0.5])
    with col2:
        # Aquí se integrará el Avatar Hyper-realista de Anita (HeyGen o similar)
        # Por ahora usamos una imagen profesional integrada en la iluminación
        st.image("https://images.unsplash.com/photo-1596704017254-9b121068fb31?q=80&w=2070&auto=format&fit=crop", 
                 caption=None, use_container_width=True)
        
        # Diálogo Ético Inicial (Tono Pausado y Empático)
        st.markdown("<p class='ethical-prompt'>\"Hola. Soy Anita, tu Agente Personal de Acompañamiento del Proceso.<br>Antes de comenzar el protocolo sobre tu legado y trascendencia, necesito entender cómo te sientes hoy.\"</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================================================
    # --- FASE DE DIAGNÓSTICO EMOCIONAL (LA PPE EN ACCIÓN) ---
    # =========================================================
    # Basado en la Pauta de Preguntas Establecidas (PPE), capturamos el perfil.
    st.markdown("<h3>Seleccione su Estado de Consciencia</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 0.9rem;'>Por favor, elija la opción que mejor represente su sentimiento actual respecto al final de la vida.</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Diseño de botones minimalistas de alta gama
    c1, c2, c3 = st.columns(3)
    
    with c1:
        # BOTÓN A: DETECTA INDIFERENCIA
        if st.button("A - Es un tema que me da igual. Lo que pase, pasará."):
            st.session_state.perfil_emocional = 'Indiferencia'
            st.session_state.fase = 'abordaje_diagnostico'
            st.rerun()
            
    with c2:
        # BOTÓN B: DETECTA INCONSCIENCIA
        if st.button("B - A decir verdad, es algo en lo que nunca he pensado profundamente."):
            st.session_state.perfil_emocional = 'Inconsciencia'
            st.session_state.fase = 'abordaje_diagnostico'
            st.rerun()
            
    with c3:
        # BOTÓN C: DETECTA MIEDO
        if st.button("C - Me genera ansiedad, temor o incomodidad hablar de esto."):
            st.session_state.perfil_emocional = 'Miedo'
            st.session_state.fase = 'abordaje_diagnostico'
            st.rerun()

    # --- PIE DE PÁGINA PROFESIONAL ---
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color: #222;'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #444; font-size: 0.7rem; letter-spacing: 2px;'>© 2010 | 2025 HTV GLOBAL AI • PROTOCOLO ÉTICO CERTIFICADO • CHILE</p>", unsafe_allow_html=True)

# =========================================================
# --- FASE: ABORDAJE DIAGNÓSTICO (ESTRUCTURA DE CÓDIGO) ---
# =========================================================
elif st.session_state.fase == 'abordaje_diagnostico':
    # Esta sección se programará con los guiones exactos de contención que definiste en la PPE
    # para cada uno de los tres estados detectados.
    st.markdown(f"<h2>Análisis Completado: Perfil Detectado {st.session_state.perfil_emocional}</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#888;'>Aquí Anita (APAP) activará el guion de contención ética correspondiente antes de pasar al Módulo Legal...</p>", unsafe_allow_html=True)
    
    if st.button("Regresar al Umbral"):
        st.session_state.fase = 'umbral'
        st.rerun()
