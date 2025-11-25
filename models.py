  -- Tabla: evento
  CREATE TABLE `evento` (
    `id_evento` INT NOT NULL AUTO_INCREMENT,
    `nombre_evento` VARCHAR(255) NOT NULL,
    `descripcion` TEXT,
    `fecha_inicio` DATETIME NOT NULL,
    `fecha_fin` DATETIME NOT NULL,
    `ubicacion` VARCHAR(255) NOT NULL,
    `tipo_evento` VARCHAR(50) NOT NULL,
    `capacidad_maxima` INT NOT NULL,
    `costo_entrada` DECIMAL(10,2) NOT NULL,
    `organizador` VARCHAR(100) NOT NULL,
    `estado_evento` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`id_evento`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
  -- Tabla: participante
  CREATE TABLE `participante` (
    `id_participante` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(100) NOT NULL,
    `apellido` VARCHAR(100) NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `telefono` VARCHAR(20),
    `fecha_registro` DATETIME NOT NULL,
    `tipo_participante` VARCHAR(50) NOT NULL,
    `empresa` VARCHAR(100),
    `pais` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`id_participante`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
  -- Tabla: ticket
  CREATE TABLE `ticket` (
    `id_ticket` INT NOT NULL AUTO_INCREMENT,
    `id_evento` INT NOT NULL,
    `id_participante` INT NOT NULL,
    `fecha_compra` DATETIME NOT NULL,
    `precio_pagado` DECIMAL(10,2) NOT NULL,
    `tipo_ticket` VARCHAR(50) NOT NULL,
    `estado_ticket` VARCHAR(50) NOT NULL,
    `metodo_pago` VARCHAR(50) NOT NULL,
    `codigo_qr` VARCHAR(255),
    PRIMARY KEY (`id_ticket`),
    INDEX `idx_ticket_evento` (`id_evento`),
    INDEX `idx_ticket_participante` (`id_participante`),
    CONSTRAINT `fk_ticket_evento` FOREIGN KEY (`id_evento`) REFERENCES `evento` (`id_evento`) ON DELETE CASCADE,
    CONSTRAINT `fk_ticket_participante` FOREIGN KEY (`id_participante`) REFERENCES `participante` (`id_participante`) ON DELETE CASCADE
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
  -- Tabla: agenda_evento
  CREATE TABLE `agenda_evento` (
    `id_sesion` INT NOT NULL AUTO_INCREMENT,
    `id_evento` INT NOT NULL,
    `nombre_sesion` VARCHAR(255) NOT NULL,
    `descripcion_sesion` TEXT,
    `hora_inicio` TIME NOT NULL,
    `hora_fin` TIME NOT NULL,
    `orador` VARCHAR(100),
    `sala` VARCHAR(50),
    `tema` VARCHAR(100),
    PRIMARY KEY (`id_sesion`),
    INDEX `idx_agenda_evento_evento` (`id_evento`),
    CONSTRAINT `fk_agenda_evento_evento` FOREIGN KEY (`id_evento`) REFERENCES `evento` (`id_evento`) ON DELETE CASCADE
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
  -- Tabla: patrocinador
  CREATE TABLE `patrocinador` (
    `id_patrocinador` INT NOT NULL AUTO_INCREMENT,
    `nombre_patrocinador` VARCHAR(100) NOT NULL,
    `nivel_patrocinio` VARCHAR(50),
    `contacto_persona` VARCHAR(100),
    `email_contacto` VARCHAR(100),
    `telefono_contacto` VARCHAR(20),
    `sitio_web` VARCHAR(255),
    `monto_patrocinio` DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    PRIMARY KEY (`id_patrocinador`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
  -- Tabla: evento_patrocinador
  CREATE TABLE `evento_patrocinador` (
    `id_evento_patrocinador` INT NOT NULL AUTO_INCREMENT,
    `id_evento` INT NOT NULL,
    `id_patrocinador` INT NOT NULL,
    `fecha_inicio_acuerdo` DATE NOT NULL,
    `fecha_fin_acuerdo` DATE NOT NULL,
    `monto_acordado` DECIMAL(10,2) NOT NULL,
    `tipo_beneficio` TEXT,
    PRIMARY KEY (`id_evento_patrocinador`),
    INDEX `idx_evpat_evento` (`id_evento`),
    INDEX `idx_evpat_patrocinador` (`id_patrocinador`),
    CONSTRAINT `fk_evpat_evento` FOREIGN KEY (`id_evento`) REFERENCES `evento` (`id_evento`) ON DELETE CASCADE,
    CONSTRAINT `fk_evpat_patrocinador` FOREIGN KEY (`id_patrocinador`) REFERENCES `patrocinador` (`id_patrocinador`) ON DELETE CASCADE
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
  -- Tabla: feedback_evento
  CREATE TABLE `feedback_evento` (
    `id_feedback` INT NOT NULL AUTO_INCREMENT,
    `id_evento` INT NOT NULL,
    `id_participante` INT NOT NULL,
    `fecha_feedback` DATETIME NOT NULL,
    `calificacion_general` INT NOT NULL,
    `comentarios_adicionales` TEXT,
    `sugerencias` TEXT,
    `calificacion_oradores` DECIMAL(4,2),
    PRIMARY KEY (`id_feedback`),
    INDEX `idx_feedback_evento` (`id_evento`),
    INDEX `idx_feedback_participante` (`id_participante`),
    CONSTRAINT `fk_feedback_evento` FOREIGN KEY (`id_evento`) REFERENCES `evento` (`id_evento`) ON DELETE CASCADE,
    CONSTRAINT `fk_feedback_participante` FOREIGN KEY (`id_participante`) REFERENCES `participante` (`id_participante`) ON DELETE CASCADE
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
  
