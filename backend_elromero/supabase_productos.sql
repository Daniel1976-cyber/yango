-- Tabla simple de productos para Supabase
CREATE TABLE IF NOT EXISTS productos (
    id BIGINT PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio NUMERIC(10,2) NOT NULL,
    categoria TEXT,
    disponible BOOLEAN DEFAULT true,
    img TEXT,
    active BOOLEAN DEFAULT true
);

-- Índice para búsquedas por categoría
CREATE INDEX idx_productos_categoria ON productos(categoria);

-- Índice para productos activos
CREATE INDEX idx_productos_active ON productos(active);
