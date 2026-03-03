# PROYECTO: HÁGASE TU VOLUNTAD | HTV GLOBAL AI
# MÓDULO: PASARELA_PAGO_MVP.py
# OBJETIVO: Generar órdenes de pago y validar transacciones vía Flow/Webpay.

import uuid

class PasarelaFlow:
    def __init__(self):
        self.url_flow_api = "https://www.flow.cl/api/payment/create"
        self.secret_key_mock = "HTV_SECRET_K3Y_2026" # Credencial ficticia para el MVP
        self.pagos_registrados = {}

    def generar_orden_pago(self, usuario_id, plan_codigo, monto):
        """
        Crea una orden de pago única para el usuario.
        """
        token_pago = str(uuid.uuid4())[:8] # Simulador de token de Webpay
        orden = {
            "usuario": usuario_id,
            "monto_clp": monto * 950, # Conversión estimada de USD a CLP
            "plan": plan_codigo,
            "estado": "PENDIENTE",
            "token": token_pago
        }
        self.pagos_registrados[token_pago] = orden
        
        # Anita genera el enlace
        link_webpay = f"https://www.flow.cl/pago/webpay/htv-{token_pago}"
        return orden, link_webpay

    def confirmar_pago(self, token):
        """
        Simula la respuesta del Webhook de Flow una vez que el usuario paga.
        """
        if token in self.pagos_registrados:
            self.pagos_registrados[token]["estado"] = "ACEPTADO"
            return True, "Pago confirmado. Desbloqueando Cámara del Legado..."
        return False, "Error: Pago no encontrado o rechazado."

# --- SIMULACIÓN DEL MOMENTO DE PAGO ---
pasarela = PasarelaFlow()

# El usuario Enrique elige el Plan Premium (SVP04) de 89 USD
orden, link = pasarela.generar_orden_pago("Enrique_123", "SVP04", 89)

print(f"Anita dice: 'Perfecto, Enrique. Generando tu acceso seguro...'")
print(f"Orden de Pago: {orden['plan']} por ${orden['monto_clp']} CLP")
print(f"Enlace de pago: {link}")

# Simulamos que el usuario completa el pago en Webpay
exito, mensaje = pasarela.confirmar_pago(orden["token"])
if exito:
    print(f"\n[SISTEMA]: {mensaje}")
    print("[SISTEMA]: Acceso TOTAL concedido a la Entrevista Biográfica.")