from modulos.reportes.acesso_datos.reporte_dao import ReporteDAOMySQL
from modulos.reportes.acesso_datos.dao_factory import ReporteDAOFactory

class MySQLReporteDAOFactory(ReporteDAOFactory):
    def crear_dao(self):
        return ReporteDAOMySQL()