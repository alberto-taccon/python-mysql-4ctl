-- 1. Inserimento Modelli (Pool di elettronica reale)
INSERT INTO modelli_prodotto (cod_modello, nome, descrizione, categoria, prezzo_listino) VALUES
('IPH15P', 'iPhone 15 Pro', 'Smartphone Apple 128GB Titanio', 'Smartphone', 1239.00),
('SAM-S24', 'Samsung Galaxy S24', 'Smartphone Android 256GB', 'Smartphone', 929.00),
('MAC-M3', 'MacBook Air M3', 'Laptop 13 pollici 8GB RAM', 'Computer', 1349.00),
('IPAD-A6', 'iPad Air M2', 'Tablet 11 pollici Wi-Fi', 'Tablet', 719.00),
('SONY-WH', 'Sony WH-1000XM5', 'Cuffie Noise Cancelling', 'Audio', 349.00),
('LG-OLED', 'LG OLED C3 55"', 'TV Smart 4K 55 pollici', 'TV', 1199.00),
('PS5-SLM', 'PlayStation 5 Slim', 'Console con lettore disco', 'Gaming', 549.00),
('NIN-SWI', 'Nintendo Switch OLED', 'Console portatile', 'Gaming', 329.00),
('APP-W9', 'Apple Watch Series 9', 'Smartwatch 45mm GPS', 'Wearable', 459.00),
('BO-QC45', 'Bose QuietComfort', 'Cuffie Bluetooth', 'Audio', 269.00);

-- 2. Inserimento Clienti
INSERT INTO clienti (nome, cognome, data_nascita, email) VALUES
('Mario', 'Rossi', DATE '2000-10-10', 'mario.rossi@email.it'),
('Luca', 'Bianchi', DATE '1999-10-10', 'l.bianchi@gmail.com'),
('Elena', 'Verdi', DATE '1983-10-10', 'elena.verdi@outlook.com'),
('Giulia', 'Neri', DATE '1968-10-10', 'giulia.n@yahoo.it');

-- 3. Inserimento Prodotti (Pezzi fisici in magazzino con seriali casuali)
-- Creiamo più pezzi per lo stesso modello per simulare lo stock
INSERT INTO prodotti (id_modello, cod_seriale, data_arrivo, disponibilita) VALUES
(1, 'SER-IPH-001', '2023-10-10', 'N'), 
(1, 'SER-IPH-002', '2023-10-10', 'N'), 
(1, 'SER-IPH-003', '2024-01-15', 'S'),
(2, 'SER-SAM-999', '2023-11-20', 'N'), 
(3, 'SER-MAC-777', '2024-02-01', 'N'), 
(5, 'SER-SON-123', '2023-12-05', 'N'), 
(5, 'SER-SON-456', '2023-12-05', 'N'), 
(7, 'SER-PS5-000', '2024-03-10', 'S'),
(10, 'SER-BOS-555', '2024-01-20', 'N'),
(1, 'SN-IPH-A1', '2024-05-01', 'N'), 
(1, 'SN-IPH-A2', '2024-05-01', 'N'), 
(1, 'SN-IPH-A3', '2024-06-10', 'S'), 
(1, 'SN-IPH-A4', '2024-06-10', 'S'),
(2, 'SN-SAM-B1', '2024-04-12', 'N'), 
(2, 'SN-SAM-B2', '2024-04-12', 'N'),
(2, 'SN-SAM-B3', '2024-07-01', 'S'),
(3, 'SN-MAC-C1', '2024-01-20', 'N'), 
(3, 'SN-MAC-C2', '2024-01-20', 'N'),
(4, 'SN-PAD-D1', '2024-03-15', 'N'), 
(4, 'SN-PAD-D2', '2024-03-15', 'N'),
(5, 'SN-SON-E1', '2024-05-20', 'N'), 
(5, 'SN-SON-E2', '2024-05-20', 'N'),
(7, 'SN-PS5-F1', '2024-06-01', 'N'), 
(7, 'SN-PS5-F2', '2024-06-01', 'N'),
(7, 'SN-PS5-F3', '2024-06-01', 'N'),
(8, 'SN-NSW-G1', '2024-02-10', 'N'), 
(8, 'SN-NSW-G2', '2024-02-10', 'N'),
(9, 'SN-WAT-H1', '2024-05-15', 'N'), 
(9, 'SN-WAT-H2', '2024-05-15', 'N');

-- 4. Inserimento Ordini (Date casuali ultimo anno)
INSERT INTO ordini (id_cliente, data_ordine, prezzo_totale_pagato) VALUES
(1, '2023-11-15 10:30:00', 1588.00),
(2, '2024-02-14 16:45:00', 2278.00),
(3, '2024-03-01 09:15:00', 1198.00),
(1, '2024-05-10 11:00:00', 2168.00), 
(2, '2024-05-22 18:30:00', 349.00),  
(3, '2024-06-05 14:20:00', 1788.00), 
(4, '2024-06-12 09:45:00', 1239.00), 
(1, '2024-07-01 10:00:00', 549.00),  
(2, '2024-07-15 16:00:00', 1647.00), 
(4, '2024-07-20 12:30:00', 1068.00);

-- 5. Inserimento Dettagli Ordine (Colleghiamo i pezzi fisici agli ordini)
INSERT INTO dettagli_ordine (id_ordine, id_prodotto, prezzo_vendita_effettivo) VALUES
(1, 1, 1239.00),
(1, 6, 349.00),
(4, 17, 1349.00), 
(4, 14, 819.00), 
(5, 21, 349.00),
(6, 23, 549.00), 
(6, 10, 1239.00),
(7, 11, 1239.00),
(8, 24, 549.00),
(9, 25, 549.00), 
(9, 18, 549.00), 
(9, 19, 549.00),
(10, 26, 349.00),
(2, 2, 1239.00),
(3, 4, 929.00),
(3, 9, 269.00);

-- 6. Inserimento Garanzie (Solo per alcuni prodotti venduti)
INSERT INTO garanzie (id_prodotto, data_inizio, durata_mesi, stato_garanzia) VALUES
(1, '2023-11-15', 24, 'attiva'),
(2, '2024-02-14', 24, 'attiva'),
(4, '2024-03-01', 24, 'attiva'),
(6, '2023-11-15', 12, 'in assistenza');