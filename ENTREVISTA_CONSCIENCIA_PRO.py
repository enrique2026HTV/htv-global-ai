# PROYECTO: HÁGASE TU VOLUNTAD | HTV GLOBAL AI
# MÓDULO: ENTREVISTA_CONSCIENCIA_PRO.py (CORREGIDO Y ALINEADO A LA PPE FINAL)

class AnitaCerebroConsciencia:
    def __init__(self, usuario_nombre):
        self.usuario = usuario_nombre
        self.fase = "BIENVENIDA"
        self.respuestas = {}
        
    def flujo_conversacion(self, respuesta_usuario=None):
        # 0. EL PACTO DE VERDAD
        if self.fase == "BIENVENIDA":
            self.fase = "PACTO_ETICO"
            return f"{self.usuario}, antes de abrir tu Bóveda, debemos establecer un Pacto de Verdad. ¿Aceptas la responsabilidad ética de que cada palabra aquí vertida es el reflejo fiel de tu consciencia?"

        # A. DONACIÓN A LA CIENCIA
        if self.fase == "PACTO_ETICO":
            if respuesta_usuario and ("si" in respuesta_usuario.lower() or "acepto" in respuesta_usuario.lower()):
                self.fase = "PPE_A_CIENCIA"
                return "Perfecto. Iniciamos el protocolo. Respecto a tu trascendencia física (Letra A): ¿Deseas donar tu cuerpo a la investigación científica (ej. U. de Chile / U. Católica), o prefieres los ritos tradicionales?"
            else:
                return "Para alcanzar la Supremacía, es vital que aceptes este pacto de responsabilidad. ¿Aceptas continuar bajo la verdad?"

        # B. LEY DE DONACIÓN DE ÓRGANOS
        if self.fase == "PPE_A_CIENCIA":
            self.respuestas['A_Ciencia'] = respuesta_usuario
            self.fase = "PPE_B_ORGANOS"
            return "Comprendido y registrado. Ahora (Letra B), respecto a la Ley de Donación de Órganos en Chile: ¿Deseas mantener tu condición de donante universal o prefieres revocarla formalmente en este acto?"

        # C. DESTINO DE LOS RESTOS
        if self.fase == "PPE_B_ORGANOS":
            self.respuestas['B_Organos'] = respuesta_usuario
            self.fase = "PPE_C_RESTOS"
            return "Queda bajo custodia tu decisión. Avanzamos al destino de tus restos (Letra C): ¿Eliges la cremación, o prefieres el descanso en sepultura, nicho o parque cementerio?"

        # D. SERVICIOS FÚNEBRES Y DOCUMENTALES
        if self.fase == "PPE_C_RESTOS":
            self.respuestas['C_Restos'] = respuesta_usuario
            self.fase = "PPE_D_SERVICIOS"
            return "Registrado. Sobre los servicios fúnebres (Letra D): ¿Deseas dejar redactado tu obituario, una biografía oficial o un libro digital de condolencias para tu linaje?"

        # E. PERSONALIZACIÓN DEL VELORIO
        if self.fase == "PPE_D_SERVICIOS":
            self.respuestas['D_Servicios'] = respuesta_usuario
            self.fase = "PPE_E_VELORIO"
            return "Es un acto de gran soberanía. Hablemos del velorio (Letra E): ¿Tienes indicaciones sobre la música, homenajes artísticos, o si prefieres que la urna permanezca abierta o cerrada?"

        # F. PERSONALIZACIÓN DEL FUNERAL
        if self.fase == "PPE_E_VELORIO":
            self.respuestas['E_Velorio'] = respuesta_usuario
            self.fase = "PPE_F_FUNERAL"
            return "El rito toma forma. Para el momento del funeral (Letra F): ¿Cuál será tu epitafio, quién será el maestro de ceremonias, y cuál es la canción final con la que te despedirán?"

        # G. LEGADO VERDE Y ANIMALISTA
        if self.fase == "PPE_F_FUNERAL":
            self.respuestas['F_Funeral'] = respuesta_usuario
            self.fase = "FINALIZACION"
            return "El rito humano está cubierto. Finalmente (Letra G), la vida que dejas: ¿Deseas establecer un Legado Verde (reforestación de especies nativas) y/o designar custodios legales para tus mascotas?"

        # CIERRE Y PASE A PAGOS
        if self.fase == "FINALIZACION":
            self.respuestas['G_Legado_Vida'] = respuesta_usuario
            self.fase = "COMPLETADO"
            return "Tu voluntad ha sido blindada, Enrique. Hemos completado el diseño de tu legado. Ahora, el sistema generará tu acceso seguro a la Bóveda y la orden de custodia (Pago)."

        return "El proceso ha concluido."