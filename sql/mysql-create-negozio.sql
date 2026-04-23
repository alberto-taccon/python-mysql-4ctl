-- Tabella modelli (Catalogo)
CREATE TABLE modelli_prodotto (
    id_modello INT AUTO_INCREMENT PRIMARY KEY,
    cod_modello VARCHAR(50) NOT NULL UNIQUE, 
    nome VARCHAR(100) NOT NULL,
    descrizione VARCHAR(100) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    prezzo_listino DECIMAL(10, 2) NOT NULL,
    CONSTRAINT chk_prezzo_modello CHECK (prezzo_listino >= 0)
) ENGINE=InnoDB;

-- Tabella prodotti (Magazzino fisico)
CREATE TABLE prodotti (
    id_prodotto INT AUTO_INCREMENT PRIMARY KEY,
    id_modello INT NOT NULL,
    cod_seriale VARCHAR(50) NOT NULL UNIQUE,
    data_arrivo DATE NOT NULL,
    disponibilita CHAR(1) DEFAULT 'S',
    CONSTRAINT fk_prod_modello 
        FOREIGN KEY (id_modello) 
        REFERENCES modelli_prodotto(id_modello),
    CONSTRAINT chk_disp 
        CHECK (disponibilita IN ('S', 'N'))
) ENGINE=InnoDB;

-- Tabella Clienti
CREATE TABLE clienti (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cognome VARCHAR(50) NOT NULL,
    data_nascita DATE NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- Testata Ordine
CREATE TABLE ordini (
    id_ordine INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    data_ordine DATETIME DEFAULT CURRENT_TIMESTAMP,
    prezzo_totale_pagato DECIMAL(10, 2) NOT NULL,
    CONSTRAINT fk_ordini_clienti 
        FOREIGN KEY (id_cliente) 
        REFERENCES clienti(id_cliente)
) ENGINE=InnoDB;

-- Dettagli Ordine (una riga per ogni pezzo fisico)
CREATE TABLE dettagli_ordine (
    id_dettaglio INT AUTO_INCREMENT PRIMARY KEY,
    id_ordine INT NOT NULL,
    id_prodotto INT NOT NULL UNIQUE,
    prezzo_vendita_effettivo DECIMAL(10, 2) NOT NULL,
    CONSTRAINT fk_det_ordine 
        FOREIGN KEY (id_ordine) 
        REFERENCES ordini(id_ordine),
    CONSTRAINT fk_det_prodotto 
        FOREIGN KEY (id_prodotto) 
        REFERENCES prodotti(id_prodotto)
) ENGINE=InnoDB;

-- Garanzie
CREATE TABLE garanzie (
    id_garanzia INT AUTO_INCREMENT PRIMARY KEY,
    id_prodotto INT NOT NULL UNIQUE,
    data_inizio DATE NOT NULL,
    durata_mesi INT NOT NULL DEFAULT 24,
    stato_garanzia VARCHAR(20) NOT NULL,
    CONSTRAINT fk_gar_prod 
        FOREIGN KEY (id_prodotto) 
        REFERENCES prodotti(id_prodotto),
    CONSTRAINT chk_stati 
        CHECK (stato_garanzia IN ('attiva', 'scaduta', 'in assistenza'))
) ENGINE=InnoDB;