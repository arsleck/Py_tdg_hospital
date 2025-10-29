import pyodbc

# =========================
# 🔗 CONEXIÓN A SQL SERVER
# =========================
def conectar():
    try:
        conexion = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'  # Cambia si tu servidor tiene otro nombre
            'DATABASE=HospitalDB;'  # Cambia al nombre real de tu base
            'Trusted_Connection=yes;'
        )
        return conexion
    except Exception as e:
        print(f"⚠️ Error al conectar con la base de datos: {e}")
        return None


# =========================
# 🧍‍♂️ PACIENTES
# =========================
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


# =========================
# 👨‍⚕️ DOCTORES
# =========================
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


# =========================
# 📅 CITAS
# =========================
def agendar_cita():
    conexion = conectar()
    if not conexion:
        return

    try:
        id_paciente = input("Ingrese el ID del paciente: ")
        id_doctor = input("Ingrese el ID del doctor: ")
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        hora = input("Ingrese la hora (HH:MM): ")
        consultorio = input("Ingrese el número o nombre del consultorio: ")

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


# =========================
# 🧭 MENÚ PRINCIPAL
# =========================
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


# =========================
# 🚀 INICIO DEL PROGRAMA
# =========================
if __name__ == "__main__":
    menu()
    input("\nPresione Enter para salir...")
