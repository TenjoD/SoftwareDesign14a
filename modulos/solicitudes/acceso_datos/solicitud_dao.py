
from modulos.solicitudes.acceso_datos.solicitud_dto import SolicitudDTO
from modulos.solicitudes.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()
class SolicitudDAOMySQL:
    def guardar(self, solicitud_dto):
        with conn.cursor() as cursor:
<<<<<<< HEAD
            sql = "INSERT INTO solicitudes (emp_id, jefe_id, sol_fecha_inicio, sol_fecha_fin, sol_motivo, sol_fecha_creacion) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (solicitud_dto.emp_id, solicitud_dto.jefe_id, solicitud_dto.sol_fecha_inicio, solicitud_dto.sol_fecha_fin, solicitud_dto.sol_motivo, solicitud_dto.sol_fecha_creacion))
=======
            sql = """
                INSERT INTO solicitudes (emp_id, jefe_id, sol_fecha_inicio, sol_fecha_fin, sol_motivo, sol_fecha_creacion)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                solicitud_dto.emp_id,
                solicitud_dto.jefe_id,
                solicitud_dto.sol_fecha_inicio,
                solicitud_dto.sol_fecha_fin,
                solicitud_dto.sol_motivo,
                solicitud_dto.sol_fecha_creacion
            ))
>>>>>>> c75b52b121baee9151621703c6952b7a17960336
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
<<<<<<< HEAD
            cursor.execute("SELECT sol_id, emp_id, jefe_id, sol_fecha_inicio, sol_fecha_fin, sol_motivo, sol_fecha_creacion FROM solicitudes")
            rows = cursor.fetchall()
        return [SolicitudDTO(sol_id=row[0], emp_id=row[1], jefe_id=row[2], sol_fecha_inicio=row[3], sol_fecha_fin=row[4], sol_motivo=row[5], sol_fecha_creacion=row[6]) for row in rows]

    def obtener_por_id(self, sol_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT sol_id, emp_id, jefe_id, sol_fecha_inicio, sol_fecha_fin, sol_motivo, sol_fecha_creacion FROM solicitudes WHERE sol_id = %s", (sol_id,))
            row = cursor.fetchone()
        if row:
            return SolicitudDTO(sol_id=row[0], emp_id=row[1], jefe_id=row[2], sol_fecha_inicio=row[3], sol_fecha_fin=row[4], sol_motivo=row[5], sol_fecha_creacion=row[6])
=======
            cursor.execute("""
                SELECT sol_id, emp_id, jefe_id, sol_fecha_inicio, sol_fecha_fin, sol_motivo, sol_fecha_creacion
                FROM solicitudes
            """)
            rows = cursor.fetchall()
        return [SolicitudDTO(
            sol_id=row[0], emp_id=row[1], jefe_id=row[2],
            sol_fecha_inicio=row[3], sol_fecha_fin=row[4],
            sol_motivo=row[5], sol_fecha_creacion=row[6]
        ) for row in rows]

    def obtener_por_id(self, sol_id):
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT sol_id, emp_id, jefe_id, sol_fecha_inicio, sol_fecha_fin, sol_motivo, sol_fecha_creacion
                FROM solicitudes WHERE sol_id = %s
            """, (sol_id,))
            row = cursor.fetchone()
        if row:
            return SolicitudDTO(
                sol_id=row[0], emp_id=row[1], jefe_id=row[2],
                sol_fecha_inicio=row[3], sol_fecha_fin=row[4],
                sol_motivo=row[5], sol_fecha_creacion=row[6]
            )
>>>>>>> c75b52b121baee9151621703c6952b7a17960336
        return None

    def actualizar(self, solicitud_dto):
        with conn.cursor() as cursor:
<<<<<<< HEAD
            sql = "UPDATE solicitud SET emp_id = %s, jefe_id = %s, sol_fecha_inicio = %s, sol_fecha_fin = %s, sol_motivo = %s, sol_fecha_creacion = %s WHERE sol_id = %s"
            cursor.execute(sql, (solicitud_dto.emp_id, solicitud_dto.jefe_id, solicitud_dto.sol_fecha_inicio, solicitud_dto.sol_fecha_fin, solicitud_dto.sol_motivo))
        conn.commit()

    def eliminar(self, sol_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM solicitud WHERE sol_id = %s", (sol_id,))
        conn.commit()

class SolicitudDAOPostgres:
    def guardar(self, solicitud_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO solicitudes (emp_id, jefe_id, sol_fecha_inicio, sol_fecha_fin, sol_motivo, sol_fecha_creacion) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (solicitud_dto.emp_id, solicitud_dto.jefe_id, solicitud_dto.sol_fecha_inicio, solicitud_dto.sol_fecha_fin, solicitud_dto.sol_motivo, solicitud_dto.sol_fecha_creacion))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT sol_id, emp_id, jefe_id, sol_fecha_inicio, sol_fecha_fin, sol_motivo, sol_fecha_creacion FROM solicitudes")
            rows = cursor.fetchall()
        return [SolicitudDTO(sol_id=row[0], emp_id=row[1], jefe_id=row[2], sol_fecha_inicio=row[3], sol_fecha_fin=row[4], sol_motivo=row[5], sol_fecha_creacion=row[6]) for row in rows]

    def obtener_por_id(self, sol_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT sol_id, emp_id, jefe_id, sol_fecha_inicio, sol_fecha_fin, sol_motivo, sol_fecha_creacio FROM solicitudes WHERE id = %s", (sol_id,))
            row = cursor.fetchone()
        if row:
            return SolicitudDTO(sol_id=row[0], emp_id=row[1], jefe_id=row[2], sol_fecha_inicio=row[3], sol_fecha_fin=row[4], sol_motivo=row[5], sol_fecha_creacion=row[6])
        return None

    def actualizar(self, solicitud_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE solicitudes SET emp_id = %s, jefe_id = %s, sol_fecha_inicio = %s, sol_fecha_fin = %s, sol_motivo = %s, sol_fecha_creacion =%s WHERE sol_id = %s"
            cursor.execute(sql, (solicitud_dto.nombre, solicitud_dto.descripcion, solicitud_dto.precio, solicitud_dto.categoria,solicitud_dto.id))
=======
            sql = """
                UPDATE solicitudes
                SET emp_id = %s, jefe_id = %s, sol_fecha_inicio = %s,
                    sol_fecha_fin = %s, sol_motivo = %s, sol_fecha_creacion = %s
                WHERE sol_id = %s
            """
            cursor.execute(sql, (
                solicitud_dto.emp_id,
                solicitud_dto.jefe_id,
                solicitud_dto.sol_fecha_inicio,
                solicitud_dto.sol_fecha_fin,
                solicitud_dto.sol_motivo,
                solicitud_dto.sol_fecha_creacion,
                solicitud_dto.sol_id
            ))
>>>>>>> c75b52b121baee9151621703c6952b7a17960336
        conn.commit()

    def eliminar(self, sol_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM solicitudes WHERE sol_id = %s", (sol_id,))
        conn.commit()
<<<<<<< HEAD
=======


class SolicitudDAOPostgres:
    def guardar(self, solicitud_dto):
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO solicitudes (emp_id, jefe_id, sol_fecha_inicio, sol_fecha_fin, sol_motivo, sol_fecha_creacion)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                solicitud_dto.emp_id,
                solicitud_dto.jefe_id,
                solicitud_dto.sol_fecha_inicio,
                solicitud_dto.sol_fecha_fin,
                solicitud_dto.sol_motivo,
                solicitud_dto.sol_fecha_creacion
            ))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT sol_id, emp_id, jefe_id, sol_fecha_inicio, sol_fecha_fin, sol_motivo, sol_fecha_creacion
                FROM solicitudes
            """)
            rows = cursor.fetchall()
        return [SolicitudDTO(
            sol_id=row[0], emp_id=row[1], jefe_id=row[2],
            sol_fecha_inicio=row[3], sol_fecha_fin=row[4],
            sol_motivo=row[5], sol_fecha_creacion=row[6]
        ) for row in rows]

    def obtener_por_id(self, sol_id):
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT sol_id, emp_id, jefe_id, sol_fecha_inicio, sol_fecha_fin, sol_motivo, sol_fecha_creacion
                FROM solicitudes WHERE sol_id = %s
            """, (sol_id,))
            row = cursor.fetchone()
        if row:
            return SolicitudDTO(
                sol_id=row[0], emp_id=row[1], jefe_id=row[2],
                sol_fecha_inicio=row[3], sol_fecha_fin=row[4],
                sol_motivo=row[5], sol_fecha_creacion=row[6]
            )
        return None

    def actualizar(self, solicitud_dto):
        with conn.cursor() as cursor:
            sql = """
                UPDATE solicitudes
                SET emp_id = %s, jefe_id = %s, sol_fecha_inicio = %s,
                    sol_fecha_fin = %s, sol_motivo = %s, sol_fecha_creacion = %s
                WHERE sol_id = %s
            """
            cursor.execute(sql, (
                solicitud_dto.emp_id,
                solicitud_dto.jefe_id,
                solicitud_dto.sol_fecha_inicio,
                solicitud_dto.sol_fecha_fin,
                solicitud_dto.sol_motivo,
                solicitud_dto.sol_fecha_creacion,
                solicitud_dto.sol_id
            ))
        conn.commit()

    def eliminar(self, sol_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM solicitudes WHERE sol_id = %s", (sol_id,))
        conn.commit()
>>>>>>> c75b52b121baee9151621703c6952b7a17960336
