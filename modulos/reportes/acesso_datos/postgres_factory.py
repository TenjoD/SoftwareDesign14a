from modulos.reportes.acesso_datos.reporte_dao import ReporteDAOPostgres
from modulos.reportes.acesso_datos.dao_factory import ReporteDAOFactory

class PostgresReporteDAOFactory(ReporteDAOFactory):
    def crear_dao(self):
        return ReporteDAOPostgres()