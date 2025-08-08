from datetime import datetime
<<<<<<< HEAD
=======

>>>>>>> c75b52b121baee9151621703c6952b7a17960336
class SolicitudDTO:
    def __init__(self, sol_id=None, emp_id=None, jefe_id=None, sol_fecha_inicio=None, sol_fecha_fin=None, sol_motivo="", sol_fecha_creacion=None):
        self.sol_id = sol_id
        self.emp_id = emp_id
        self.jefe_id = jefe_id
        self.sol_fecha_inicio = sol_fecha_inicio
<<<<<<< HEAD
        self.sol_fecha_fin =  sol_fecha_fin
        self.sol_motivo = sol_motivo
        sol_fecha_creacion = sol_fecha_creacion or datetime.now()

    def __str__(self):
        return f"SolicitudDTO(sol_id={{self.sol_id}}, emp_id='{{self.emp_id}}', jefe_id='{{self.jefe_id}}',sol_fecha_inicio={{self.sol_fecha_inicio}}, sol_fecha_fin='{{self.sol_fecha_fin}}, sol_motivo='{{self.sol_motivo}}, sol_fecha_creacion='{{sol_fecha_creacion}}')"
=======
        self.sol_fecha_fin = sol_fecha_fin
        self.sol_motivo = sol_motivo
        self.sol_fecha_creacion = sol_fecha_creacion or datetime.now()

    def __str__(self):
        return (
            f"SolicitudDTO(sol_id={self.sol_id}, emp_id={self.emp_id}, jefe_id={self.jefe_id}, "
            f"sol_fecha_inicio={self.sol_fecha_inicio}, sol_fecha_fin={self.sol_fecha_fin}, "
            f"sol_motivo='{self.sol_motivo}', sol_fecha_creacion={self.sol_fecha_creacion})"
        )
>>>>>>> c75b52b121baee9151621703c6952b7a17960336
