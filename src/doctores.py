from env.db_config import conectar

# =====================
# 👨‍⚕️ CRUD DOCTORES
# =====================

def registrar_doctor():
    conexion = conectar()
    if not conexion:
        return

    nombre = input("Ingrese el nombre completo del doctor: ")
    especialidad = input("Ingrese la especialidad: ")

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Doctores (nombre_completo, especialidad)
            VALUES (?, ?)
        """, (nombre, especialidad))
        conexion.commit()
        print("✅ Doctor registrado con éxito.")
    except Exception as e:
        print(f"⚠️ Error al registrar doctor: {e}")
    finally:
        conexion.close()


def mostrar_doctores():
    conexion = conectar()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Doctores")
        doctores = cursor.fetchall()

        if doctores:
            print("\n=== Lista de Doctores ===")
            for d in doctores:
                print(f"ID: {d.id_doctor} | Nombre: {d.nombre_completo} | Especialidad: {d.especialidad}")
        else:
            print("No hay doctores registrados.")
    except Exception as e:
        print(f"⚠️ Error al mostrar doctores: {e}")
    finally:
        conexion.close()


def actualizar_doctor():
    conexion = conectar()
    if not conexion:
        return

    try:
        mostrar_doctores()
        id_doctor = input("\nIngrese el ID del doctor que desea actualizar: ")

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Doctores WHERE id_doctor = ?", (id_doctor,))
        doctor = cursor.fetchone()

        if not doctor:
            print("⚠️ No existe un doctor con ese ID.")
            return

        nuevo_nombre = input("Nuevo nombre (deje en blanco para mantener): ") or doctor.nombre_completo
        nueva_especialidad = input("Nueva especialidad (deje en blanco para mantener): ") or doctor.especialidad

        cursor.execute("""
            UPDATE Doctores
            SET nombre_completo = ?, especialidad = ?
            WHERE id_doctor = ?
        """, (nuevo_nombre, nueva_especialidad, id_doctor))
        conexion.commit()
        print("✅ Doctor actualizado con éxito.")
    except Exception as e:
        print(f"⚠️ Error al actualizar doctor: {e}")
    finally:
        conexion.close()


def eliminar_doctor():
    conexion = conectar()
    if not conexion:
        return

    try:
        mostrar_doctores()
        id_doctor = input("\nIngrese el ID del doctor que desea eliminar: ")

        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Doctores WHERE id_doctor = ?", (id_doctor,))
        if cursor.rowcount == 0:
            print("⚠️ No se encontró un doctor con ese ID.")
        else:
            conexion.commit()
            print("✅ Doctor eliminado con éxito.")
    except Exception as e:
        print(f"⚠️ Error al eliminar doctor: {e}")
    finally:
        conexion.close()
