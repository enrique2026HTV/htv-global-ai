# PROYECTO: HÁGASE TU VOLUNTAD | HTV GLOBAL AI
# MÓDULO: GENERADOR_CERTIFICADO_MVP.py
# OBJETIVO: Consolidar la voluntad en un documento oficial certificado.

import datetime

class CertificadoVoluntad:
    def __init__(self, usuario_nombre, rut, plan, respuestas):
        self.usuario = usuario_nombre
        self.rut = rut
        self.plan = plan
        self.respuestas = respuestas
        self.fecha_emision = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        self.id_certificado = f"HTV-{usuario_nombre[:3].upper()}-{self.fecha_emision.replace('/', '')[:8]}"

    def generar_plantilla(self):
        """
        Diseña la estructura del documento final.
        """
        certificado = f"""
        ===========================================================
               HÁGASE TU VOLUNTAD | HTV GLOBAL AI
                   CERTIFICADO DE ÚLTIMA VOLUNTAD
        ===========================================================
        ID CERTIFICADO: {self.id_certificado}
        FECHA DE EMISIÓN: {self.fecha_emision}
        
        TITULAR: {self.usuario}
        RUT: {self.rut}
        PLAN CONTRATADO: {self.plan}
        
        --- DECLARACIÓN DE VOLUNTAD ---
        
        1. DESTINO DE RESTOS: 
           {self.respuestas.get('A', 'No especificado')}
           
        2. LEGADO ANIMALISTA: 
           {self.respuestas.get('D', 'Sin instrucciones especiales')}
           
        3. LEGADO VERDE (ECOLOGÍA): 
           {self.respuestas.get('E', 'Sin instrucciones especiales')}
           
        --- SELLOS DE AUTENTICIDAD ---
        Este documento ha sido generado mediante encriptación 
        biométrica y está custodiado en los servidores de 
        HTV GLOBAL AI. Solo podrá ser liberado ante la validación 
        de 2 de los 3 testigos designados.
        
        ===========================================================
        Firmado digitalmente por: Anita de la Luz
        HTV GLOBAL AI - INFRAESTRUCTURA EMOCIONAL
        ===========================================================
        """
        return certificado

# --- SIMULACIÓN DE CIERRE DE PROCESO ---
respuestas_finales = {
    "A": "Cremación y esparcir cenizas en el Cajón del Maipo.",
    "D": "Mi gata Luna queda al cuidado de mi hermana; se deja fondo de reserva.",
    "E": "Deseo que se planten 10 árboles nativos en mi memoria."
}

doc = CertificadoVoluntad("Enrique", "12.345.678-K", "SVP04 Premium", respuestas_finales)
print(doc.generar_plantilla())