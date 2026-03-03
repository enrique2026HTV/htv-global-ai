# PROYECTO: HÁGASE TU VOLUNTAD | HTV GLOBAL AI
# MÓDULO: CORE_INTELLIGENCE_MVP.py
# OBJETIVO: Gestión de planes, precios y validación ética inicial.

class HagaseTuVoluntad:
    def __init__(self, usuario_nombre):
        self.usuario = usuario_nombre
        self.testigos = []
        self.plan_asignado = None
        self.pago_confirmado = False
        
        # Matriz de Precios Auditada (IVA Incluido)
        self.planes_disponibles = {
            "SVE01": {"nombre": "Voluntad Escrita", "precio_usd": 25},
            "SVA02": {"nombre": "Voluntad Audio", "precio_usd": 35},
            "SVV03": {"nombre": "Voluntad Video", "precio_usd": 45},
            "SVP04": {"nombre": "Voluntad Premium", "precio_usd": 89}
        }

    def validar_etica(self, intencion_usuario):
        """
        Filtro de seguridad contra narcocultura o violencia.
        """
        palabras_prohibidas = ["fuegos artificiales", "disparos", "venganza", "odio"]
        if any(palabra in intencion_usuario.lower() for palabra in palabras_prohibidas):
            return False, "Lo siento, Enrique. HTV Global solo certifica voluntades amparadas en la ley y la paz."
        return True, "Intención validada éticamente."

    def asignar_plan_y_cobrar(self, servicios_solicitados):
        """
        Lógica de bloqueo de pago antes de la entrevista profunda.
        """
        # (Lógica simplificada para el MVP)
        if "video" in servicios_solicitados:
            self.plan_asignado = "SVV03"
        elif "audio" in servicios_solicitados:
            self.plan_asignado = "SVA02"
        else:
            self.plan_asignado = "SVE01"
            
        # El Plan Premium es el recomendado por defecto
        if len(servicios_solicitados) > 2:
            self.plan_asignado = "SVP04"

        plan = self.planes_disponibles[self.plan_asignado]
        return f"Link de Pago Generado: Plan {plan['nombre']} - Valor: ${plan['precio_usd']} USD."

# --- TEST DEL PILOTO ---
app_htv = HagaseTuVoluntad("Enrique")
es_valido, mensaje = app_htv.validar_etica("Quiero una despedida tranquila con mi familia")
print(mensaje)
print(app_htv.asignar_plan_y_cobrar(["audio", "video", "biografia"]))