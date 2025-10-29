from pacientes import registrar_paciente, mostrar_pacientes
from doctores import registrar_doctor, mostrar_doctores
from citas import agendar_cita, mostrar_citas

def menu():
    while True:
        print("\n=== SISTEMA DE GESTIÓN HOSPITALARIA ===")
        print("1. Registrar paciente")
        print("2. Mostrar pacientes")
        print("3. Registrar doctor")
        print("4. Mostrar doctores")
        print("5. Agendar cita")
        print("6. Mostrar citas")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            mostrar_pacientes()
        elif opcion == "3":
            registrar_doctor()
        elif opcion == "4":
            mostrar_doctores()
        elif opcion == "5":
            agendar_cita()
        elif opcion == "6":
            mostrar_citas()
        elif opcion == "0":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción no válida, intente nuevamente.")
