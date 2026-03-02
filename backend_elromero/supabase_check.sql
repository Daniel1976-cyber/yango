-- SQL para ver estructura y datos de la tabla productos
-- Ejecuta esto en el SQL Editor de Supabase

-- Ver todas las tablas
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';

-- Ver datos de la tabla productos
SELECT * FROM productos;

-- Ver estructura de la tabla productos
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'productos';
