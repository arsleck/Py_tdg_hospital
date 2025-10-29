from env.db_config import conectar

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
