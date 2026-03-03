# PROYECTO: HÁGASE TU VOLUNTAD | HTV GLOBAL AI
# MÓDULO: INTERFAZ_CAMARA_LEGADO_MVP.py

class CamaraDelLegado:
    def __init__(self, usuario, id_certificado):
        self.usuario = usuario
        self.cert_id = id_certificado
        self.modulos = {
            "Rituales": "0%",
            "Biografía": "0%",
            "Legado Verde": "0%",
            "Legado Animal": "0%",
            "Mensajes Finales": "0%"
        }

    def mostrar_dashboard(self):
        print(f"\n" + "="*40)
        print(f"   BIENVENIDO A TU CÁMARA, {self.usuario.upper()}")
        print(f"   ID: {self.cert_id} | ESTADO: PROTEGIDO")
        print("="*40)
        print("\nPROGRESO DE TU VOLUNTAD:")
        for mod, prog in self.modulos.items():
            print(f"[{prog}] - {mod}")
        print("\n[BOTÓN]: GRABAR MENSAJE DE VIDEO (SVP04)")
        print("[BOTÓN]: CONFIGURAR TESTIGOS")
        print("="*40)

# --- ACTIVACIÓN POST-PAGO ---
camara = CamaraDelLegado("Enrique", "HTV-CERT-9921")
camara.mostrar_dashboard()