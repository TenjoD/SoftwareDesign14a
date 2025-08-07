-- Crear base de datos (ejecutar en consola psql como superusuario)
CREATE DATABASE vacations_db;

-- Conectarse a la base de datos (dentro de psql)
-- \c productos_db

-- Crear tabla formularios

CREATE TABLE IF NOT EXISTS empleados (
    emp_id SERIAL PRIMARY KEY,
   emp_documento INT NOT NULL,
    emp_nombre VARCHAR(255) NOT NULL,
    emp_cargo VARCHAR(255),
    emp_area VARCHAR(255),
    emp_fecha_ingreso DATE NOT NULL,
    emp_dias_disponibles INT,
    jefe_id INT REFERENCES jefes(jefe_id)
);

CREATE TABLE IF NOT EXISTS jefes (
    jefe_id SERIAL PRIMARY KEY,
    jefe_nombre VARCHAR(255) NOT NULL,
    jefe_documento INT NOT NULL,
    jefe_correo VARCHAR(255),
    jefe_cargo VARCHAR(100),
    jefe_area VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS solicitudes (
    sol_id SERIAL PRIMARY KEY,
    emp_id INT REFERENCES empleados(emp_id),
    jefe_id INT REFERENCES jefes(jefe_id),
    sol_fecha_inicio DATE NOT NULL,
    sol_fecha_fin DATE NOT NULL,
    sol_motivo VARCHAR(255) NOT NULL,
    sol_fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE IF NOT EXISTS validaciones_jefe (
    val_jefe_id SERIAL PRIMARY KEY,
    sol_id INT REFERENCES solicitudes(sol_id),
    jefe_id INT REFERENCES jefes(jefe_id),
    estado VARCHAR(20) DEFAULT 'pendiente',  -- aprobado, rechazado, pendiente
    observaciones TEXT,
    fecha_validacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS validaciones_rrhh (
    val_rrhh_id SERIAL PRIMARY KEY,
    sol_id INT REFERENCES solicitudes(sol_id),
    estado VARCHAR(20) DEFAULT 'pendiente',  -- aprobado, rechazado, pendiente
    observaciones TEXT,
    fecha_validacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reportes (
    rep_id SERIAL PRIMARY KEY,
    emp_id INT REFERENCES empleados(emp_id),
    rep_estado_id INT REFERENCES estados(rep_estado_id) NOT NULL,
    rep_fecha_inicio DATE NOT NULL,
    rep_fecha_fin DATE NOT NULL,
    rep_fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);