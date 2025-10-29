import pyodbc

# =========================
# 🔗 CONEXIÓN A SQL SERVER
# =========================
def conectar():
    try:
        conexion = pyodbc.connect(
           'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=basededatostg.database.windows.net;'
            'DATABASE=Hospital;'
            'UID=Nick;'
            'PWD=Dn2006!?'
        )
        print("✅ Conexión exitosa a SQL Server")
        return conexion
    except Exception as e:
        print(f"⚠️ Error al conectar con la base de datos: {e}")
        return None