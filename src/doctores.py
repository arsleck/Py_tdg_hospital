from env.db_config import conectar

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
