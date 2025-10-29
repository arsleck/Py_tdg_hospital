import tkinter as tk
from tkinter import ttk, messagebox
from pacientes import registrar_paciente, mostrar_pacientes, actualizar_paciente, eliminar_paciente
from doctores import registrar_doctor, mostrar_doctores, actualizar_doctor, eliminar_doctor
from citas import agendar_cita, mostrar_citas, actualizar_cita, eliminar_cita


def ejecutar_funcion(funcion):
    """Ejecuta la función seleccionada y muestra el resultado en una ventana emergente."""
    try:
        resultado = funcion()
        if resultado is None:
            messagebox.showinfo("Ejecución correcta", "La acción se completó con éxito.")
        else:
            messagebox.showinfo("Resultado", str(resultado))
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error:\n{e}")


def crear_boton(contenedor, texto, comando, fila, columna, color="#1D8348"):
    """Crea un botón estilizado."""
    boton = tk.Button(
        contenedor,
        text=texto,
        command=comando,
        bg=color,
        fg="white",
        font=("Segoe UI", 11, "bold"),
        relief="raised",
        padx=10,
        pady=5,
        width=22
    )
    boton.grid(row=fila, column=columna, padx=8, pady=8)
    return boton


# === INTERFAZ PRINCIPAL ===
root = tk.Tk()
root.title("Sistema de Gestión Hospitalaria")
root.geometry("700x600")
root.configure(bg="#F8F9F9")

titulo = tk.Label(root, text="🏥 Sistema de Gestión Hospitalaria", font=("Segoe UI", 16, "bold"), bg="#F8F9F9")
titulo.pack(pady=20)

# Marco principal con estilo
frame = tk.Frame(root, bg="#EAEDED", bd=2, relief="groove")
frame.pack(padx=20, pady=10, fill="both", expand=True)

# === SECCIÓN PACIENTES ===
tk.Label(frame, text="👤 Pacientes", font=("Segoe UI", 14, "bold"), bg="#EAEDED").grid(row=0, column=0, columnspan=2, pady=10)
crear_boton(frame, "Registrar Paciente", lambda: ejecutar_funcion(registrar_paciente), 1, 0)
crear_boton(frame, "Mostrar Pacientes", lambda: ejecutar_funcion(mostrar_pacientes), 1, 1)
crear_boton(frame, "Actualizar Paciente", lambda: ejecutar_funcion(actualizar_paciente), 2, 0)
crear_boton(frame, "Eliminar Paciente", lambda: ejecutar_funcion(eliminar_paciente), 2, 1)

# === SECCIÓN DOCTORES ===
tk.Label(frame, text="🩺 Doctores", font=("Segoe UI", 14, "bold"), bg="#EAEDED").grid(row=3, column=0, columnspan=2, pady=10)
crear_boton(frame, "Registrar Doctor", lambda: ejecutar_funcion(registrar_doctor), 4, 0)
crear_boton(frame, "Mostrar Doctores", lambda: ejecutar_funcion(mostrar_doctores), 4, 1)
crear_boton(frame, "Actualizar Doctor", lambda: ejecutar_funcion(actualizar_doctor), 5, 0)
crear_boton(frame, "Eliminar Doctor", lambda: ejecutar_funcion(eliminar_doctor), 5, 1)

# === SECCIÓN CITAS ===
tk.Label(frame, text="📅 Citas", font=("Segoe UI", 14, "bold"), bg="#EAEDED").grid(row=6, column=0, columnspan=2, pady=10)
crear_boton(frame, "Agendar Cita", lambda: ejecutar_funcion(agendar_cita), 7, 0)
crear_boton(frame, "Mostrar Citas", lambda: ejecutar_funcion(mostrar_citas), 7, 1)
crear_boton(frame, "Actualizar Cita", lambda: ejecutar_funcion(actualizar_cita), 8, 0)
crear_boton(frame, "Eliminar Cita", lambda: ejecutar_funcion(eliminar_cita), 8, 1)

# Botón de salir
tk.Button(root, text="Salir", command=root.destroy, bg="#922B21", fg="white", font=("Segoe UI", 12, "bold"), width=12).pack(pady=20)

root.mainloop()
