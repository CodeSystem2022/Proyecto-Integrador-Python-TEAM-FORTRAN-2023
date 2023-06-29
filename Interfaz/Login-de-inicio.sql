   CREATE TABLE usuarios (
        id SERIAL PRIMARY KEY,
        usuario VARCHAR(50) NOT NULL,
        contraseña VARCHAR(50) NOT NULL,
        correo_electronico VARCHAR(100) NOT NULL
    );