# Attività: collegamento tra Python e database MySQL (phpmyadmin)

## Obiettivo
L'attività ha lo scopo di mostrare come un programma Python possa collegarsi a un database MySQL ed eseguire query SQL.

---

## 1. Creazione della tabella e inserimento dei dati iniziali

Eseguire gli script seguenti su phpmyadmin:

```text
mysql-create-negozio.sql
```

```text
mysql-insert-negozio.sql
```

Questi script creano e popolano le tabelle del negozio che abbiamo già utilizzato le volte scorse

---

## 2. Apertura del tunnel SSH

Aprire un terminale ed eseguire il seguente comando:

```bash
ssh -N -L 3307:localhost:3306 [nome_utente_database]@lab.alberghetti.cloud
```
Sostituire con il proprio nome utente phpmyadmin e quando richiesto, inserire la password.

Il terminale deve rimanere aperto durante l'esecuzione dei file Python.

---

## 3. Configurazione dei file Python

Prima di eseguire i file Python, modificare nel codice i parametri di connessione al database:

- utente;
- password;
- nome del database.

Host e porta devono rimanere coerenti con il tunnel SSH (quindi non fare niente)

```python
"host": "127.0.0.1"
"port": 3307
```

---

## 4. Esecuzione dei file Python

Eseguire i tre file Python forniti.

I tre file **non rappresentano tre alternative equivalenti**, ma tre **evoluzioni progressive dello stesso codice**.

- Il primo file mostra una versione base, con query scritte direttamente nel codice.
- Il secondo file introduce le query parametrizzate.
- Il terzo file presenta una struttura più ordinata, con funzioni di supporto e funzioni dedicate alle operazioni sul database.


## Problemi comuni

### Errore di connessione
Verificare:
- che il tunnel SSH sia aperto;
- che host e porta siano corretti;
- che utente, password e nome database siano corretti.

### Errore durante l'`INSERT`
E' un errore del dominio del database e non dell'applicazione.
Verificare che non esista già un record con la stessa email, poiché il campo `email` è definito `UNIQUE`.

### `UPDATE` o `DELETE` con 0 righe coinvolte
E' un errore del dominio del database e non dell'applicazione.
Questo significa che nessuna riga soddisfa la condizione indicata nella query.
