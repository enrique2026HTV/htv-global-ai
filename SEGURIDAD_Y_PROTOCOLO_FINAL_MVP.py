# PROYECTO: HÁGASE TU VOLUNTAD | HTV GLOBAL AI
# MÓDULO: SEGURIDAD_Y_PROTOCOLO_FINAL_MVP.py

class ProtocoloSeguridad:
    def __init__(self, lista_testigos):
        self.testigos = lista_testigos # Lista de los 3 elegidos
        self.confirmaciones = 0
        self.bloqueado_por_etica = False

    def filtro_etico_avanzado(self, texto):
        """
        Analiza si el contenido infringe la ley o la ética de la obra.
        """
        keywords_peligro = ["fuegos artificiales", "odio", "venganza", "arma", "narc"]
        for palabra in keywords_peligro:
            if palabra in texto.lower():
                self.bloqueado_por_etica = True
                return "ALERTA: Contenido no certificable. Anita requiere re-enfoque de paz."
        return "Contenido validado éticamente."

    def solicitar_apertura_legado(self, id_testigo, certificado_defuncion_valido):
        """
        Protocolo de liberación de datos post-pago y post-mortem.
        """
        if not certificado_defuncion_valido:
            return "ERROR: Se requiere validación del Registro Civil."
        
        self.confirmaciones += 1
        if self.confirmaciones >= 2:
            return "SISTEMA: Umbral alcanzado (2/3). LIBERANDO LEGADO..."
        return f"SISTEMA: Confirmación 1/3 recibida. Esperando segundo testigo..."

# --- SIMULACIÓN DE SEGURIDAD ---
seguridad = ProtocoloSeguridad(["Juan", "Maria", "Carlos"])

# Caso 1: Prueba de Filtro Ético
print(seguridad.filtro_etico_avanzado("Deseo una despedida con fuegos artificiales"))

# Caso 2: Prueba de Apertura de Emergencia
print(seguridad.solicitar_apertura_legado("Juan", True))
print(seguridad.solicitar_apertura_legado("Maria", True))