from pacientes import registrar_paciente, mostrar_pacientes, actualizar_paciente, eliminar_paciente
from doctores import registrar_doctor, mostrar_doctores, actualizar_doctor, eliminar_doctor
from citas import agendar_cita, mostrar_citas, actualizar_cita, eliminar_cita

def menu():
    while True:
        print("\n=== SISTEMA DE GESTIÓN HOSPITALARIA ===")
        print("1. Registrar paciente")
        print("2. Mostrar pacientes")
        print("3. Actualizar paciente")
        print("4. Eliminar paciente")
        print("5. Registrar doctor")
        print("6. Mostrar doctores")
        print("7. Actualizar doctor")
        print("8. Eliminar doctor")
        print("9. Agendar cita")
        print("10. Mostrar citas")
        print("11. Actualizar cita")
        print("12. Eliminar cita")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1": registrar_paciente()
        elif opcion == "2": mostrar_pacientes()
        elif opcion == "3": actualizar_paciente()
        elif opcion == "4": eliminar_paciente()
        elif opcion == "5": registrar_doctor()
        elif opcion == "6": mostrar_doctores()
        elif opcion == "7": actualizar_doctor()
        elif opcion == "8": eliminar_doctor()
        elif opcion == "9": agendar_cita()
        elif opcion == "10": mostrar_citas()
        elif opcion == "11": actualizar_cita()
        elif opcion == "12": eliminar_cita()
        elif opcion == "0":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción no válida, intente nuevamente.")
