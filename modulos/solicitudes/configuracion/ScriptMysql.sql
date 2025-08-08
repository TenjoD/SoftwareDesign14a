-- Crear base de datos (funciona tanto para MySQL como PostgreSQL)
CREATE DATABASE IF NOT EXISTS vacations_db;

-- Usar la base de datos (MySQL)
USE vacations_db;

-- Crear tabla productos
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
    jefe_id INT REFERENCES empleados(jefe_id),
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
<<<<<<< HEAD
=======

CREATE TABLE IF NOT EXISTS validaciones_rrhh (
    val_rrhh_id SERIAL PRIMARY KEY,
    sol_id INT REFERENCES solicitudes(sol_id),
    estado VARCHAR(20) DEFAULT 'pendiente',  -- aprobado, rechazado, pendiente
    observaciones TEXT,
    fecha_validacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
>>>>>>> c75b52b121baee9151621703c6952b7a17960336
