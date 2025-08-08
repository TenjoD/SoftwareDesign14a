from datetime import datetime
class ReporteDTO:
    def __init__(self, rep_id=None, emp_id=None, rep_estado_solicitud_id=None, rep_estado_jefe_id=None, rep_estado_rrhh_id=None, rep_fecha_inicio=None, rep_fecha_fin=None, rep_motivo="", rep_fecha_creacion=None):
        self.rep_id = rep_id
        self.emp_id = emp_id
        self.rep_estado_solicitud_id = rep_estado_solicitud_id
        self.rep_estado_jefe_id = rep_estado_jefe_id
        self.rep_estado_rrhh_id = rep_estado_rrhh_id
        self.rep_fecha_inicio = rep_fecha_inicio
        self.rep_fecha_fin =  rep_fecha_fin
        self.rep_fecha_creacion = rep_fecha_creacion or datetime.now()

    def __str__(self):
        return f"ReporteDTO(rep_id={{self.rep_id}}, emp_id='{{self.emp_id}}', rep_estado_solicitud_id='{{self.rep_estado_solicitud_id}}', rep_estado_jefe_id='{{self.rep_estado_jefe_id}}', rep_estado_rrhh_id='{{self.rep_estado_rrhh_id}}', rep_fecha_inicio={{self.rep_fecha_inicio}}, rep_fecha_fin='{{self.rep_fecha_fin}}, rep_fecha_creacion='{{self.rep_fecha_creacion}}')"
