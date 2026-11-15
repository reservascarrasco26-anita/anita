import customtkinter as ctk
from PIL import Image
import os

# Configuración inicial del estilo global
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

# --- NÚMERO DE EMERGENCIA (MAMÁ Y PRUEBAS) ---
HIJO_1_NOMBRE = "Mamá"
HIJO_1_NUMERO = "51983385687" 

def disparar_sos(ventana_padre):
    # Ventana de confirmación visual limpia y directa para la computadora y futuro celular
    alerta_v = ctk.CTkToplevel(ventana_padre)
    alerta_v.title("ANITA - Emergencia")
    alerta_v.geometry("420x320")
    alerta_v.configure(fg_color="#FFCDD2")  # Rojo suave de alerta
    alerta_v.resizable(False, False)
    alerta_v.grab_set()

    ctk.CTkLabel(alerta_v, text="🚨", font=("Arial", 55)).pack(pady=15)
    ctk.CTkLabel(alerta_v, text="¡LLAMADA DE EMERGENCIA!", font=("Arial", 20, "bold"), text_color="#C62828").pack(pady=5)
    ctk.CTkLabel(alerta_v, text=f"Marcando al contacto de {HIJO_1_NOMBRE}.\nPor favor, mantén la calma.", font=("Arial", 14), text_color="#333333", justify="center").pack(pady=10)

    ctk.CTkButton(alerta_v, text="Entendido / Cerrar", font=("Arial", 15, "bold"), fg_color="#C62828", text_color="white", width=220, height=45, corner_radius=22, command=alerta_v.destroy).pack(pady=15)

def abrir_menu_hijos(ventana_padre):
    hijos_v = ctk.CTkToplevel(ventana_padre)
    hijos_v.title("ANITA - Mis Hijos")
    hijos_v.geometry("450x400")
    hijos_v.configure(fg_color="#E3F2FD")  # Azul de tranquilidad
    hijos_v.resizable(False, False)

    ctk.CTkLabel(hijos_v, text="📞 Contacto de Emergencia", font=("Arial", 22, "bold"), text_color="#0D47A1").pack(pady=25)
    ctk.CTkLabel(hijos_v, text=f"Contacto: {HIJO_1_NOMBRE}\nNúmero: {HIJO_1_NUMERO}", font=("Arial", 16), text_color="#333333", justify="center").pack(pady=20)

    ctk.CTkButton(hijos_v, text="Volver", font=("Arial", 14, "bold"), fg_color="#546E7A", text_color="white", width=180, height=40, corner_radius=20, command=hijos_v.destroy).pack(pady=20)

def abrir_lista_salida(ventana_padre):
    salida_v = ctk.CTkToplevel(ventana_padre)
    salida_v.title("ANITA - Lista de Salida")
    salida_v.geometry("450x600")
    salida_v.configure(fg_color="#F1F8E9")
    salida_v.resizable(False, False)

    ctk.CTkLabel(salida_v, text="Antes de salir, revisa:", font=("Arial", 22, "bold"), text_color="#1B5E20").pack(pady=25)

    v1, v2, v3, v4 = ctk.BooleanVar(), ctk.BooleanVar(), ctk.BooleanVar(), ctk.BooleanVar()
    estilo = {"font": ("Arial", 16, "bold"), "text_color": "#222222"}

    ctk.CTkCheckBox(salida_v, text=" 🔑 ¿Llevas tus llaves?", variable=v1, **estilo).pack(anchor="w", padx=50, pady=12)
    ctk.CTkCheckBox(salida_v, text=" 📱 ¿Llevas tu celular cargado?", variable=v2, **estilo).pack(anchor="w", padx=50, pady=12)
    ctk.CTkCheckBox(salida_v, text=" 🔥 ¿Cocina y gas apagados?", variable=v3, **estilo).pack(anchor="w", padx=50, pady=12)
    ctk.CTkCheckBox(salida_v, text=" 💡 ¿Luces y ventanas cerradas?", variable=v4, **estilo).pack(anchor="w", padx=50, pady=12)

    lbl_res = ctk.CTkLabel(salida_v, text="", font=("Arial", 15, "bold"))
    lbl_res.pack(pady=10)

    def verificar():
        if v1.get() and v2.get() and v3.get() and v4.get():
            lbl_res.configure(text="¡Todo listo! Que tengas un hermoso día 🌟", text_color="#2E7D32")
        else:
            lbl_res.configure(text="Por favor, marca todas las opciones.", text_color="#C62828")

    ctk.CTkButton(salida_v, text="¡ESTOY LISTA!", font=("Arial", 15, "bold"), fg_color="#4CAF50", text_color="white", width=280, height=50, corner_radius=25, command=verificar).pack(pady=15)
    ctk.CTkButton(salida_v, text="Cerrar", font=("Arial", 13, "bold"), fg_color="#546E7A", text_color="white", width=180, height=40, corner_radius=20, command=salida_v.destroy).pack(pady=5)

def abrir_menu_principal(ventana_padre):
    menu_v = ctk.CTkToplevel(ventana_padre)
    menu_v.title("ANITA - Menú Principal")
    menu_v.geometry("450x640")
    menu_v.configure(fg_color="#E3F2FD")
    menu_v.resizable(False, False)

    ctk.CTkLabel(menu_v, text="¿Qué deseas hacer hoy?", font=("Arial", 22, "bold"), text_color="#0D47A1").pack(pady=20)

    ctk.CTkButton(menu_v, text="💬   CONVERSAR", font=("Arial", 16, "bold"), fg_color="#1E88E5", text_color="white", width=320, height=50, corner_radius=25, 
                  command=lambda: print("Módulo de conversación")).pack(pady=10)
    
    ctk.CTkButton(menu_v, text="🚪   SALIR DE CASA", font=("Arial", 16, "bold"), fg_color="#00ACC1", text_color="white", width=320, height=50, corner_radius=25, 
                  command=lambda: abrir_lista_salida(menu_v)).pack(pady=10)
    
    ctk.CTkButton(menu_v, text="📞   MIS HIJOS", font=("Arial", 16, "bold"), fg_color="#3949AB", text_color="white", width=320, height=50, corner_radius=25, 
                  command=lambda: abrir_menu_hijos(menu_v)).pack(pady=10)

    ctk.CTkButton(menu_v, text="🚨   S.O.S. / AYUDA", font=("Arial", 16, "bold"), fg_color="#C62828", text_color="white", width=320, height=50, corner_radius=25, 
                  command=lambda: disparar_sos(menu_v)).pack(pady=10)

    ctk.CTkButton(menu_v, text="⬅ Volver", font=("Arial", 14, "bold"), fg_color="#546E7A", text_color="white", width=180, height=40, corner_radius=20, command=menu_v.destroy).pack(pady=15)

def iniciar():
    ventana = ctk.CTk()
    ventana.title("ANITA - Tu Compañera")
    ventana.geometry("450x550")
    ventana.configure(fg_color="#FFD700")  # Fondo amarillo principal original
    ventana.resizable(False, False)

    ruta_logo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
    if os.path.exists(ruta_logo):
        try:
            img = ctk.CTkImage(light_image=Image.open(ruta_logo), dark_image=Image.open(ruta_logo), size=(90, 90))
            ctk.CTkLabel(ventana, image=img, text="").pack(pady=15)
        except:
            pass

    ctk.CTkLabel(ventana, text="ANITA", font=("Arial", 34, "bold"), text_color="#111111").pack(pady=5)
    ctk.CTkLabel(ventana, text="Tu compañía y protección diaria", font=("Arial", 15, "bold"), text_color="#222222").pack(pady=5)

    ctk.CTkButton(ventana, text="INGRESAR", font=("Arial", 17, "bold"), fg_color="#00897B", text_color="white", width=280, height=55, corner_radius=28, command=lambda: abrir_menu_principal(ventana)).pack(pady=20)
    ctk.CTkButton(ventana, text="🚨 S.O.S. / AYUDA", font=("Arial", 17, "bold"), fg_color="#C62828", text_color="white", width=280, height=50, corner_radius=28, command=lambda: disparar_sos(ventana)).pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    iniciar()