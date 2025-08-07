
from modulos.reportes.acesso_datos.reporte_dto import ReporteDTO
from modulos.reportes.acesso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()
class ReporteDAOMySQL:
    def guardar(self, reporte_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO reportes (emp_id, rep_estado_solicitud_id, rep_estado_jefe_id, rep_estado_rrhh_id, rep_fecha_inicio, rep_fecha_fin, rep_fecha_creacion) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (reporte_dto.emp_id, reporte_dto.rep_estado_solicitud_id, reporte_dto.rep_estado_jefe_id, reporte_dto.rep_estado_rrhh_id, reporte_dto.rep_fecha_inicio, reporte_dto.rep_fecha_fin, reporte_dto.rep_fecha_creacion))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT rep_id, emp_id, rep_estado_solicitud_id, rep_estado_jefe_id, rep_estado_rrhh_id, rep_fecha_inicio, rep_fecha_fin, rep_fecha_creacion FROM reportes")
            rows = cursor.fetchall()
        return [ReporteDTO(rep_id=row[0], emp_id=row[1], rep_estado_solicitud_id=row[2], rep_estado_jefe_id=row[3], rep_estado_rrhh_id=row[4], rep_fecha_inicio=row[5], rep_fecha_fin=row[6], rep_fecha_creacion=row[7]) for row in rows]

    def obtener_por_id(self, rep_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT rep_id, emp_id, rep_estado_solicitud_id, rep_estado_jefe_id, rep_estado_rrhh_id, rep_fecha_inicio, rep_fecha_fin, rep_fecha_creacion FROM reportes WHERE rep_id = %s", (rep_id,))
            row = cursor.fetchone()
        if row:
            return ReporteDTO(rep_id=row[0], emp_id=row[1], rep_estado_solicitud_id=row[2], rep_estado_jefe_id=row[3], rep_estado_rrhh_id=row[4], rep_fecha_inicio=row[5], rep_fecha_fin=row[6], rep_fecha_creacion=row[7])
        return None

    def actualizar(self, reporte_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE reportes SET emp_id = %s, rep_estado_solicitud_id = %s, rep_estado_jefe_id = %s, rep_estado_rrhh_id = %s, rep_fecha_inicio = %s, rep_fecha_fin = %s, rep_fecha_creacion = %s WHERE rep_id = %s"
            cursor.execute(sql, (reporte_dto.emp_id, reporte_dto.rep_estado_solicitud_id, reporte_dto.rep_estado_jefe_id, reporte_dto.rep_estado_rrhh_id, reporte_dto.rep_fecha_inicio, reporte_dto.rep_fecha_fin, reporte_dto.rep_fecha_creacion, reporte_dto.rep_id))
        conn.commit()

    def eliminar(self, rep_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM reportes WHERE rep_id = %s", (rep_id,))
        conn.commit()

class ReporteDAOPostgres:
    def guardar(self, reporte_dto):
        with conn.cursor() as cursor:
            sql = "INSERT INTO reportes (emp_id, rep_estado_solicitud_id, rep_estado_jefe_id, rep_estado_rrhh_id, rep_fecha_inicio, rep_fecha_fin, rep_fecha_creacion) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (reporte_dto.emp_id, reporte_dto.rep_estado_solicitud_id, reporte_dto.rep_estado_jefe_id, reporte_dto.rep_estado_rrhh_id, reporte_dto.rep_fecha_inicio, reporte_dto.rep_fecha_fin, reporte_dto.rep_fecha_creacion))
        conn.commit()

    def obtener_todos(self):
        with conn.cursor() as cursor:
            cursor.execute("SELECT rep_id, emp_id, rep_estado_solicitud_id, rep_estado_jefe_id, rep_estado_rrhh_id, rep_fecha_inicio, rep_fecha_fin, rep_fecha_creacion FROM reportes")
            rows = cursor.fetchall()
        return [ReporteDTO(rep_id=row[0], emp_id=row[1], rep_estado_solicitud_id=row[2], rep_estado_jefe_id=row[3], rep_estado_rrhh_id=row[4], rep_fecha_inicio=row[5], rep_fecha_fin=row[6], rep_fecha_creacion=row[7]) for row in rows]

    def obtener_por_id(self, rep_id):
        with conn.cursor() as cursor:
            cursor.execute("SELECT rep_id, emp_id, rep_estado_solicitud_id, rep_estado_jefe_id, rep_estado_rrhh_id, rep_fecha_inicio, rep_fecha_fin, rep_fecha_creacion FROM reportes WHERE rep_id = %s", (rep_id,))
            row = cursor.fetchone()
        if row:
            return ReporteDTO(rep_id=row[0], emp_id=row[1], rep_estado_solicitud_id=row[2], rep_estado_jefe_id=row[3], rep_estado_rrhh_id=row[4], rep_fecha_inicio=row[5], rep_fecha_fin=row[6], rep_fecha_creacion=row[7])
        return None

    def actualizar(self, reporte_dto):
        with conn.cursor() as cursor:
            sql = "UPDATE reportes SET emp_id = %s, rep_estado_solicitud_id = %s, rep_estado_jefe_id = %s, rep_estado_rrhh_id = %s, rep_fecha_inicio = %s, rep_fecha_fin = %s, rep_fecha_creacion = %s WHERE rep_id = %s"
            cursor.execute(sql, (reporte_dto.emp_id, reporte_dto.rep_estado_solicitud_id, reporte_dto.rep_estado_jefe_id, reporte_dto.rep_estado_rrhh_id, reporte_dto.rep_fecha_inicio, reporte_dto.rep_fecha_fin, reporte_dto.rep_fecha_creacion, reporte_dto.rep_id))
        conn.commit()

    def eliminar(self, rep_id):
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM reportes WHERE rep_id = %s", (rep_id,))
        conn.commit()
