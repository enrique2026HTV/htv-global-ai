# PROYECTO: HÁGASE TU VOLUNTAD | HTV GLOBAL AI
# MÓDULO: ANITA_INPUT_DISCERNIMIENTO.py
# OBJETIVO: Evaluar el estado vibracional del usuario para ajustar la pedagogía de Anita.

class DiscernimientoAnita:
    def __init__(self):
        # Patrones lingüísticos asociados a estados de consciencia
        self.patrones = {
            "MIEDO": ["no sé", "miedo", "difícil", "preocupado", "asusta", "temor", "muerte", "final"],
            "INDIFERENCIA": ["da igual", "lo mismo", "no importa", "después", "cualquiera", "me da lo mismo", "equis"],
            "INCONSCIENCIA": ["no entiendo", "para qué", "obligado", "tontería", "perder tiempo", "absurdo"]
        }

    def analizar_estado(self, texto_usuario):
        """
        Analiza el texto y devuelve el estado detectado junto con un 'Input de Sabiduría' de Anita.
        """
        if not texto_usuario:
            return "NEUTRAL", ""

        t = texto_usuario.lower()
        
        # 1. Detección de MIEDO
        if any(w in t for w in self.patrones["MIEDO"]):
            return "MIEDO", (
                "Percibo tu inquietud, Enrique. Es natural sentir el peso de lo eterno. "
                "Pero recuerda: este espacio no es sobre el final, es sobre la permanencia "
                "de tu propia luz. Respira, hagámoslo simple."
            )
        
        # 2. Detección de INDIFERENCIA
        if any(w in t for w in self.patrones["INDIFERENCIA"]):
            return "INDIFERENCIA", (
                "Tu huella es única en el universo. Si tú no eliges hoy tu legado, "
                "el azar lo hará por ti mañana. Recuperemos tu poder de decisión; "
                "cada detalle de tu voluntad cuenta."
            )
        
        # 3. Detección de INCONSCIENCIA / ESCEPTICISMO
        if any(w in t for w in self.patrones["INCONSCIENCIA"]):
            return "INCONSCIENCIA", (
                "Esta no es una encuesta más. Es el ejercicio de tu soberanía personal. "
                "Es el único derecho que nadie podrá arrebatarte: tu última palabra en la Tierra. "
                "Démosle la altura que merece."
            )
        
        # 4. CONSCIENCIA PLENA
        return "CONSCIENCIA_PLENA", "Tu claridad es la base de esta Supremacía Ética. Tu mensaje fluye con fuerza."