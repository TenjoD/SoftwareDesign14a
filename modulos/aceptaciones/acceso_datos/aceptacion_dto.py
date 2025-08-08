from datetime import datetime

class AceptacionDTO:
    def __init__(self, val_jefe_id=None, sol_id=None, jefe_id=None, estado="PENDIENTE", observaciones=None, fecha_validacion=None, emp_id=None, emp_nombre=None, emp_documento=None, sol_fecha_inicio=None, sol_fecha_fin=None, sol_motivo=None):
        self.val_jefe_id = val_jefe_id
        self.sol_id = sol_id
        self.jefe_id = jefe_id
        self.estado = estado
        self.observaciones = observaciones
        self.fecha_validacion = fecha_validacion or datetime.now()
        self.emp_id = emp_id
        self.emp_nombre = emp_nombre
        self.emp_documento = emp_documento
        self.sol_fecha_inicio = sol_fecha_inicio
        self.sol_fecha_fin = sol_fecha_fin
        self.sol_motivo = sol_motivo

    def __str__(self):
        return (
            f"AceptacionDTO(val_jefe_id={self.val_jefe_id}, sol_id={self.sol_id}, jefe_id={self.jefe_id}, "
            f"estado='{self.estado}', observaciones='{self.observaciones}', fecha_validacion={self.fecha_validacion}, "
            f"emp_nombre='{self.emp_nombre}', emp_documento={self.emp_documento}, "
            f"sol_fecha_inicio={self.sol_fecha_inicio}, sol_fecha_fin={self.sol_fecha_fin})"
        )
