# PROYECTO: HÁGASE TU VOLUNTAD | HTV GLOBAL AI
# MÓDULO: REGISTRO_TESTIGOS_MVP.py
# OBJETIVO: Validación de identidad y registro de los 3 custodios.

import re

class RegistroHTV:
    def __init__(self):
        self.datos_usuario = {}
        self.testigos = []

    def validar_rut(self, rut):
        """
        Valida formato de RUT chileno básico para el MVP.
        """
        patron = r"^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$"
        return bool(re.match(patron, rut))

    def agregar_testigo(self, nombre, email):
        """
        Registra un testigo. El sistema requiere exactamente 3.
        """
        if len(self.testigos) < 3:
            self.testigos.append({"nombre": nombre, "email": email})
            return True, f"Testigo {nombre} registrado exitosamente."
        return False, "Ya se han registrado los 3 testigos requeridos."

    def verificar_listo_para_pago(self):
        """
        Verifica que la fase de registro esté completa para saltar al checkout.
        """
        if self.datos_usuario and len(self.testigos) == 3:
            return True
        return False

# --- SIMULACIÓN DEL PILOTO ---
registro = RegistroHTV()
registro.datos_usuario = {"nombre": "Enrique", "rut": "12.345.678-K"}

# Simulando el ingreso de los 3 testigos
print(registro.agregar_testigo("Juan Perez", "juan@email.com")[1])
print(registro.agregar_testigo("Maria Soto", "maria@email.com")[1])
print(registro.agregar_testigo("Carlos Ruiz", "carlos@email.com")[1])

if registro.verificar_listo_para_pago():
    print("\n[SISTEMA]: Registro completo. Procediendo a Pantalla de Pago...")