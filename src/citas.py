from env.db_config import conectar

def agendar_cita():
    conexion = conectar()
    if not conexion:
        return

    try:
        id_paciente = input("Ingrese el ID del paciente: ")
        id_doctor = input("Ingrese el ID del doctor: ")
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        hora = input("Ingrese la hora (HH:MM): ")
        consultorio = input("Ingrese el consultorio: ")

        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Citas (id_paciente, id_doctor, fecha, hora, consultorio)
            VALUES (?, ?, ?, ?, ?)
        """, (id_paciente, id_doctor, fecha, hora, consultorio))
        conexion.commit()
        print("✅ Cita agendada con éxito.")
    except Exception as e:
        print(f"⚠️ Error al agendar cita: {e}")
    finally:
        conexion.close()


def mostrar_citas():
    conexion = conectar()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT C.id_cita, P.nombre_completo AS paciente, D.nombre_completo AS doctor,
                   D.especialidad, C.fecha, C.hora, C.consultorio
            FROM Citas C
            JOIN Pacientes P ON C.id_paciente = P.id_paciente
            JOIN Doctores D ON C.id_doctor = D.id_doctor
        """)
        citas = cursor.fetchall()

        if citas:
            print("\n=== Lista de Citas ===")
            for c in citas:
                print(f"ID: {c.id_cita} | Paciente: {c.paciente} | Doctor: {c.doctor} | "
                      f"Especialidad: {c.especialidad} | Fecha: {c.fecha} | Hora: {c.hora} | Consultorio: {c.consultorio}")
        else:
            print("No hay citas registradas.")
    except Exception as e:
        print(f"⚠️ Error al mostrar citas: {e}")
    finally:
        conexion.close()
