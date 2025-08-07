from modulos.aceptaciones.acceso_datos.aceptacion_dto import AceptacionDTO
from modulos.aceptaciones.acceso_datos.conexion import ConexionDB

conn = ConexionDB().obtener_conexion()

class AceptacionDAOMySQL:

    def listar_validaciones_por_jefe(self, jefe_id):
        with conn.cursor() as cursor:
            sql = """
                SELECT
                    vj.val_jefe_id, vj.sol_id, vj.jefe_id, vj.estado, vj.observaciones, vj.fecha_validacion,
                    e.emp_id, e.emp_nombre, e.emp_documento,
                    s.sol_fecha_inicio, s.sol_fecha_fin, s.sol_motivo
                FROM validaciones_jefe vj
                JOIN solicitudes s ON vj.sol_id = s.sol_id
                JOIN empleados e ON s.emp_id = e.emp_id
                WHERE vj.jefe_id = %s
                ORDER BY vj.fecha_validacion DESC
            """
            cursor.execute(sql, (jefe_id,))
            rows = cursor.fetchall()

        dtos = []
        for row in rows:
            dto = AceptacionDTO(val_jefe_id=row[0], sol_id=row[1], jefe_id=row[2], estado=row[3], observaciones=row[4], fecha_validacion=row[5], emp_id=row[6], emp_nombre=row[7],emp_documento=row[8], sol_fecha_inicio=row[9], sol_fecha_fin=row[10], sol_motivo=row[11])
            dtos.append(dto)
        return dtos

    def listar_validaciones_pendientes_por_jefe(self, jefe_id):
        with conn.cursor() as cursor:
            sql = """
                SELECT
                    vj.val_jefe_id, vj.sol_id, vj.jefe_id, vj.estado, vj.observaciones, vj.fecha_validacion,
                    e.emp_id, e.emp_nombre, e.emp_documento,
                    s.sol_fecha_inicio, s.sol_fecha_fin, s.sol_motivo
                FROM validaciones_jefe vj
                JOIN solicitudes s ON vj.sol_id = s.sol_id
                JOIN empleados e ON s.emp_id = e.emp_id
                WHERE vj.jefe_id = %s AND UPPER(TRIM(vj.estado)) = 'PENDIENTE'
                ORDER BY vj.fecha_validacion DESC
            """
            cursor.execute(sql, (jefe_id,))
            rows = cursor.fetchall()

        dtos = []
        for row in rows:
            dto = AceptacionDTO(val_jefe_id=row[0], sol_id=row[1], jefe_id=row[2], estado=row[3], observaciones=row[4], fecha_validacion=row[5], emp_id=row[6], emp_nombre=row[7],emp_documento=row[8], sol_fecha_inicio=row[9], sol_fecha_fin=row[10], sol_motivo=row[11])
            dtos.append(dto)
        return dtos

    def actualizar_estado_y_observaciones(self, val_jefe_id, nuevo_estado, observaciones):
        with conn.cursor() as cursor:
            sql = """
                UPDATE validaciones_jefe
                SET estado = %s,
                    observaciones = %s,
                    fecha_validacion = NOW()
                WHERE val_jefe_id = %s
            """
            cursor.execute(sql, (nuevo_estado, observaciones, val_jefe_id))
        conn.commit()

    def marcar_como_pendiente(self, val_jefe_id, observaciones="Cambio de fechas solicitado"):
        with conn.cursor() as cursor:
            sql = """
                UPDATE validaciones_jefe
                SET estado = 'PENDIENTE',
                    observaciones = %s,
                    fecha_validacion = NOW()
                WHERE val_jefe_id = %s
            """
            cursor.execute(sql, (observaciones, val_jefe_id))
        conn.commit()
