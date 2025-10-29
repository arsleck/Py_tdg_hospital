from env.db_config import conectar

# =====================
# 📅 CRUD CITAS
# =====================

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

        # Verificar existencia
        cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE id_paciente = ?", (id_paciente,))
        result = cursor.fetchone()
        if result is None or result[0] == 0:
            print(f"⚠️ No existe un paciente con ID {id_paciente}.")
            return
        cursor.execute("SELECT COUNT(*) FROM Doctores WHERE id_doctor = ?", (id_doctor,))
        result = cursor.fetchone()
        if result is None or result[0] == 0:
            print(f"⚠️ No existe un doctor con ID {id_doctor}.")
            return
            return

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


def actualizar_cita():
    conexion = conectar()
    if not conexion:
        return

    try:
        mostrar_citas()
        id_cita = input("\nIngrese el ID de la cita que desea actualizar: ")

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Citas WHERE id_cita = ?", (id_cita,))
        cita = cursor.fetchone()

        if not cita:
            print("⚠️ No existe una cita con ese ID.")
            return

        nueva_fecha = input("Nueva fecha (YYYY-MM-DD, deje en blanco para mantener): ") or cita.fecha
        nueva_hora = input("Nueva hora (HH:MM, deje en blanco para mantener): ") or cita.hora
        nuevo_consultorio = input("Nuevo consultorio (deje en blanco para mantener): ") or cita.consultorio

        cursor.execute("""
            UPDATE Citas
            SET fecha = ?, hora = ?, consultorio = ?
            WHERE id_cita = ?
        """, (nueva_fecha, nueva_hora, nuevo_consultorio, id_cita))
        conexion.commit()
        print("✅ Cita actualizada con éxito.")
    except Exception as e:
        print(f"⚠️ Error al actualizar cita: {e}")
    finally:
        conexion.close()


def eliminar_cita():
    conexion = conectar()
    if not conexion:
        return

    try:
        mostrar_citas()
        id_cita = input("\nIngrese el ID de la cita que desea eliminar: ")

        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Citas WHERE id_cita = ?", (id_cita,))
        if cursor.rowcount == 0:
            print("⚠️ No se encontró una cita con ese ID.")
        else:
            conexion.commit()
            print("✅ Cita eliminada con éxito.")
    except Exception as e:
        print(f"⚠️ Error al eliminar cita: {e}")
    finally:
        conexion.close()
