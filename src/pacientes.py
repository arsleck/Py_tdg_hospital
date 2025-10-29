from env.db_config import conectar

# =====================
# 🧍‍♂️ CRUD PACIENTES
# =====================

def registrar_paciente():
    conexion = conectar()
    if not conexion:
        return

    cedula = input("Ingrese la cédula del paciente: ")
    nombre = input("Ingrese el nombre completo: ")
    edad = input("Ingrese la edad: ")

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Pacientes (cedula, nombre_completo, edad)
            VALUES (?, ?, ?)
        """, (cedula, nombre, edad))
        conexion.commit()
        print("✅ Paciente registrado con éxito.")
    except Exception as e:
        print(f"⚠️ Error al registrar paciente: {e}")
    finally:
        conexion.close()


def mostrar_pacientes():
    conexion = conectar()
    if not conexion:
        return

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Pacientes")
        pacientes = cursor.fetchall()

        if pacientes:
            print("\n=== Lista de Pacientes ===")
            for p in pacientes:
                print(f"ID: {p.id_paciente} | Cédula: {p.cedula} | Nombre: {p.nombre_completo} | Edad: {p.edad}")
        else:
            print("No hay pacientes registrados.")
    except Exception as e:
        print(f"⚠️ Error al mostrar pacientes: {e}")
    finally:
        conexion.close()


def actualizar_paciente():
    conexion = conectar()
    if not conexion:
        return

    try:
        mostrar_pacientes()
        id_paciente = input("\nIngrese el ID del paciente que desea actualizar: ")

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Pacientes WHERE id_paciente = ?", (id_paciente,))
        paciente = cursor.fetchone()

        if not paciente:
            print("⚠️ No existe un paciente con ese ID.")
            return

        nuevo_nombre = input("Nuevo nombre (deje en blanco para mantener): ") or paciente.nombre_completo
        nueva_edad = input("Nueva edad (deje en blanco para mantener): ") or paciente.edad

        cursor.execute("""
            UPDATE Pacientes
            SET nombre_completo = ?, edad = ?
            WHERE id_paciente = ?
        """, (nuevo_nombre, nueva_edad, id_paciente))
        conexion.commit()
        print("✅ Paciente actualizado con éxito.")
    except Exception as e:
        print(f"⚠️ Error al actualizar paciente: {e}")
    finally:
        conexion.close()


def eliminar_paciente():
    conexion = conectar()
    if not conexion:
        return

    try:
        mostrar_pacientes()
        id_paciente = input("\nIngrese el ID del paciente que desea eliminar: ")

        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Pacientes WHERE id_paciente = ?", (id_paciente,))
        if cursor.rowcount == 0:
            print("⚠️ No se encontró un paciente con ese ID.")
        else:
            conexion.commit()
            print("✅ Paciente eliminado con éxito.")
    except Exception as e:
        print(f"⚠️ Error al eliminar paciente: {e}")
    finally:
        conexion.close()
