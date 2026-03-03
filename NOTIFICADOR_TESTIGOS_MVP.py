# PROYECTO: HÁGASE TU VOLUNTAD | HTV GLOBAL AI
# MÓDULO: NOTIFICADOR_TESTIGOS_MVP.py
# OBJETIVO: Automatizar la comunicación con testigos y activar marketing de atracción.

class NotificadorTestigos:
    def __init__(self, usuario_nombre, plan_contratado):
        self.usuario = usuario_nombre
        self.plan = plan_contratado
        self.remitente = "notificaciones@htvglobal.ai"

    def redactar_correo(self, nombre_testigo):
        """
        Crea el cuerpo del mensaje con el estándar de alta gama definido.
        """
        asunto = f"✉️ Misión Especial: {self.usuario} te ha confiado su legado"
        
        cuerpo = f"""
        Hola {nombre_testigo}:

        Te escribimos de 'Hágase Tu Voluntad | HTV GLOBAL AI'.
        Queremos informarte que {self.usuario} ha activado su certificación 
        de última voluntad bajo el plan {self.plan} y te ha nombrado 
        oficialmente como CUSTODIO DE SU LEGADO.

        Tu rol es fundamental para asegurar que sus deseos se cumplan con exactitud.
        
        ¿QUÉ DEBES HACER?
        Hoy, nada. Solo saber que este tesoro digital existe. En el futuro, 
        tú serás una de las llaves para liberar su mensaje.

        ¿QUIERES ASEGURAR TU PROPIO LEGADO?
        Mientras {self.usuario} completa su entrevista con Anita, te invitamos
        a conocer cómo proteger a tu familia también.
        
        [BOTÓN: Ver mi rol de Testigo]
        [BOTÓN: Iniciar mi propio Legado con 15% DCTO]

        Con respeto,
        Anita de la Luz
        Hágase Tu Voluntad | HTV GLOBAL AI
        """
        return asunto, cuerpo

    def enviar_notificaciones(self, lista_testigos):
        """
        Simula el envío masivo de correos una vez confirmado el pago.
        """
        print(f"\n[SISTEMA]: Pago confirmado para {self.usuario}. Iniciando secuencia de marketing...")
        for testigo in lista_testigos:
            asunto, mensaje = self.redactar_correo(testigo['nombre'])
            print(f"--- Enviando a: {testigo['email']} ---")
            print(f"ASUNTO: {asunto}")
            print(f"ESTADO: Correo enviado exitosamente.")
        return True

# --- SIMULACIÓN DEL FLUJO POST-PAGO ---
# Datos obtenidos de los módulos anteriores
testigos_enrique = [
    {"nombre": "Juan Perez", "email": "juan@email.com"},
    {"nombre": "Maria Soto", "email": "maria@email.com"},
    {"nombre": "Carlos Ruiz", "email": "carlos@email.com"}
]

notificador = NotificadorTestigos("Enrique", "SVP04 Premium")
notificador.enviar_notificaciones(testigos_enrique)