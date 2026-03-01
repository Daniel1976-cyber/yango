-- =============================================
-- Base de datos para Tienda El Romero - Supabase
-- =============================================

-- Tabla de Categorías
CREATE TABLE categoria (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT DEFAULT ''
);

-- Tabla de Productos
CREATE TABLE producto (
    id SERIAL PRIMARY KEY,
    categoria_id INTEGER NOT NULL REFERENCES categoria(id) ON DELETE CASCADE,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    imagen VARCHAR(255) DEFAULT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT true
);

-- Tabla de Clientes
CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    direccion TEXT NOT NULL
);

-- Tabla de Pedidos
CREATE TABLE pedido (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL REFERENCES cliente(id) ON DELETE CASCADE,
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(20) DEFAULT 'pendiente' CHECK (estado IN ('pendiente', 'procesando', 'completado', 'cancelado')),
    total DECIMAL(10,2) DEFAULT 0
);

-- Tabla de Detalles de Pedido
CREATE TABLE detalle_pedido (
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER NOT NULL REFERENCES pedido(id) ON DELETE CASCADE,
    producto_id INTEGER NOT NULL REFERENCES producto(id) ON DELETE CASCADE,
    cantidad INTEGER NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL
);

-- =============================================
-- Índices para mejorar el rendimiento
-- =============================================
CREATE INDEX idx_producto_categoria ON producto(categoria_id);
CREATE INDEX idx_producto_activo ON producto(activo);
CREATE INDEX idx_pedido_cliente ON pedido(cliente_id);
CREATE INDEX idx_pedido_estado ON pedido(estado);
CREATE INDEX idx_detalle_pedido_pedido ON detalle_pedido(pedido_id);
CREATE INDEX idx_detalle_pedido_producto ON detalle_pedido(producto_id);

-- =============================================
-- Vistas útiles
-- =============================================
-- Vista de productos con nombre de categoría
CREATE VIEW vista_productos AS
SELECT 
    p.id,
    p.nombre,
    p.descripcion,
    p.precio,
    p.stock,
    p.imagen,
    p.fecha_creacion,
    p.activo,
    c.nombre AS categoria_nombre
FROM producto p
LEFT JOIN categoria c ON p.categoria_id = c.id;

-- Vista de pedidos con información del cliente
CREATE VIEW vista_pedidos AS
SELECT 
    ped.id,
    ped.fecha_pedido,
    ped.estado,
    ped.total,
    cl.nombre AS cliente_nombre,
    cl.email AS cliente_email
FROM pedido ped
LEFT JOIN cliente cl ON ped.cliente_id = cl.id;
