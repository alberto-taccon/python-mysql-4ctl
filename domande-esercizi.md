
## Domande
- Qual è la differenza tra una query scritta direttamente nel codice e una query parametrizzata?
```text
In una query scritta da tastiera i dati sono specificati all'interno di essa, mentre in una parametrizzata i dati sono sempre specificati in essa, però non inseriti direttamente nella query ma vengono "passati" come variabili.
```

- Qual è il vantaggio di avere funzioni di supporto come esegui_select() ed esegui_dml()?
```text
Partendo dal presupposto che le due funzioni fanno cose diverse, si può dire che il vantaggio è quello di poter usare funzioni come esegui_dml() per svolgere più compiti, infatti questa viene richiamata in tutti e tre gli esempi(select, insert, delete). Per quanto riguarda esegui_select(), serve per rendere il codice più ordinato e riutizzabile.
```

- In che senso i tre file non sono alternative equivalenti, ma evoluzioni progressive dello stesso codice?
```text
I tre file non sono alternative equivalenti perchè non fanno la stessa cosa in modo diverso, sono tre esempi di livelli diversi partendo dal primo con query con dati hardcoded, nel secondo le query sono parametriche quindi i dati vengono passati come variabili, infine nel terzo c'è molto più ordine e il codice è strutturato in modo ottimale.
```


## Esercizi
Esercizi a partire dal **terzo file Python**.

### 1. Selezionare tutti i modelli di prodotto
Scrivere una funzione:

```python
def seleziona_tutti_modelli(connection):
    with connection.cursor() as cursor:
        query = "SELECT * FROM modelli_prodotto"
        cursor.execute(query)
        risultati = cursor.fetchall()
        return risultati
```
```text
(1, 'IPH15P', 'iPhone 15 Pro', 'Smartphone Apple 128GB Titanio', 'Smartphone', Decimal('1239.00'))
(2, 'SAM-S24', 'Samsung Galaxy S24', 'Smartphone Android 256GB', 'Smartphone', Decimal('929.00'))
(3, 'MAC-M3', 'MacBook Air M3', 'Laptop 13 pollici 8GB RAM', 'Computer', Decimal('1349.00'))
(4, 'IPAD-A6', 'iPad Air M2', 'Tablet 11 pollici Wi-Fi', 'Tablet', Decimal('719.00'))
(5, 'SONY-WH', 'Sony WH-1000XM5', 'Cuffie Noise Cancelling', 'Audio', Decimal('349.00'))
(6, 'LG-OLED', 'LG OLED C3 55"', 'TV Smart 4K 55 pollici', 'TV', Decimal('1199.00'))
(7, 'PS5-SLM', 'PlayStation 5 Slim', 'Console con lettore disco', 'Gaming', Decimal('549.00'))
(8, 'NIN-SWI', 'Nintendo Switch OLED', 'Console portatile', 'Gaming', Decimal('329.00'))
(9, 'APP-W9', 'Apple Watch Series 9', 'Smartwatch 45mm GPS', 'Wearable', Decimal('459.00'))
(10, 'BO-QC45', 'Bose QuietComfort', 'Cuffie Bluetooth', 'Audio', Decimal('269.00'))
(13, 'IPH16', 'iPhone 16', 'Smartphone Apple 256GB Nero', 'Smartphone', Decimal('979.00'))
```
La funzione deve restituire tutte le righe della tabella `modelli_prodotto`

---
### 2. Visualizzare gli acquisti di un utente a partire dalla sua email

Scrivere una funzione:

```python
def seleziona_acquisti_cliente(connection, email):
    with connection.cursor() as cursor:
        query = "SELECT clienti.nome, clienti.cognome, clienti.email, ordini.id_ordine, ordini.data_ordine, prodotti.cod_seriale, modelli_prodotto.nome, modelli_prodotto.categoria, dettagli_ordine.prezzo_vendita_effettivo from clienti, dettagli_ordine, modelli_prodotto, ordini, prodotti where clienti.email=%s and clienti.id_cliente = ordini.id_cliente and dettagli_ordine.id_prodotto = prodotti.id_prodotto and ordini.id_ordine = dettagli_ordine.id_ordine and prodotti.id_modello = modelli_prodotto.id_modello"
        cursor.execute(query)
        risultati = cursor.fetchall()
        return risultati
```
```text
('Mario', 'Rossi', 'mario.rossi@email.it', 1, datetime.datetime(2023, 11, 15, 10, 30), 'SER-IPH-001', 'iPhone 15 Pro', 'Smartphone', Decimal('1239.00'))
('Mario', 'Rossi', 'mario.rossi@email.it', 1, datetime.datetime(2023, 11, 15, 10, 30), 'SER-SON-123', 'Sony WH-1000XM5', 'Audio', Decimal('349.00'))
('Mario', 'Rossi', 'mario.rossi@email.it', 4, datetime.datetime(2024, 5, 10, 11, 0), 'SN-MAC-C1', 'MacBook Air M3', 'Computer', Decimal('1349.00'))
('Mario', 'Rossi', 'mario.rossi@email.it', 4, datetime.datetime(2024, 5, 10, 11, 0), 'SN-SAM-B1', 'Samsung Galaxy S24', 'Smartphone', Decimal('819.00'))
('Mario', 'Rossi', 'mario.rossi@email.it', 8, datetime.datetime(2024, 7, 1, 10, 0), 'SN-PS5-F2', 'PlayStation 5 Slim', 'Gaming', Decimal('549.00'))
```
La query deve restituire almeno i seguenti campi:

* nome
* cognome
* email
* id_ordine
* data_ordine
* cod_seriale
* nome del modello
* categoria
* prezzo_vendita_effettivo
---

### 3. Contare quanti prodotti di un modello sono presenti a magazzino
Scrivere una funzione:

```python
def conta_prodotti_modello(connection, cod_modello):
    with connection.cursor() as cursor:
        query = "select modelli_prodotto.nome, COUNT(modelli_prodotto.id_modello) quantità from modelli_prodotto, prodotti where modelli_prodotto.cod_modello = %s and modelli_prodotto.id_modello = prodotti.id_modello and prodotti.disponibilita='S' group by modelli_prodotto.id_modello"
        cursor.execute(query)
        risultati = cursor.fetchall()
        return risultati
```
```text
('iPhone 15 Pro', 3)
```
La funzione deve restituire il numero di prodotti presenti a magazzino associati a un determinato modello, identificato tramite il campo cod_modello.

---

### 4. Inserire un nuovo modello di prodotto
Scrivere una funzione:

* la query l'ho già provata (🐐)

```python

def inserisci_modello(connection, cod_modello, nome, descrizione, categoria, prezzo_listino):
    with connection.cursor() as cursor:
        query = """
            INSERT INTO modelli_prodotto (cod_modello, nome, descrizione, categoria, prezzo_listino) VALUES (%s, %s, %s, %s, %s) 
        """
        ris = cursor.execute(query, (cod_modello, nome, descrizione, categoria, prezzo_listino))
        connection.commit()
        return ris

```
```text
Righe inserite: 1
```
La funzione deve permettere di inserire un nuovo modello di prodotto

---

### 5. Aggiornare il prezzo di listino di un modello
Scrivere una funzione:

```python
def aggiorna_prezzo_modello(connection, cod_modello, nuovo_prezzo):
    with connection.cursor() as cursor:
        query = "UPDATE modelli_prodotto set prezzo_listino = %s where cod_modello = %s;"
        ris = cursor.execute(query, (nuovo_prezzo, cod_modello))
    connection.commit()
    return ris
```
```text
Righe aggiornate: 1

* avevo dubbi sul come si inseriscono i parametri nella query, ho chiesto a chatgpt e mi ha spiegato che nella prima parte non conta nulla, è importante l'ordine in cui le metto in cursor.execute()
```
La funzione deve permettere di modificare il prezzo di listino di un modello di prodotto, a partire dal suo codice

## Indicazioni operative

Per scegliere la funzione di supporto corretta:
- usare `esegui_select(...)` per le query `SELECT`;
- usare `esegui_dml(...)` per le query `INSERT`, `UPDATE` e `DELETE`.

Testare la funzione all'interno del main() e stampare a video il risultato
