import pymysql
from datetime import date

# Configurazione della connessione al database
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "4CTL_tacco.a.201208",
    "password": "forzamilan22522",
    "database": "4CTL_tacco.a.201208", # lo stesso del NOME_UTENTE
    "port": 3307,
    "cursorclass": pymysql.cursors.Cursor,
    "connect_timeout": 5,
}


def get_connection():
    """
    Crea e restituisce una connessione al database.
    """
    return pymysql.connect(**DB_CONFIG)

def esegui_select(connection, query, params):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        risultati = cursor.fetchall()
        return risultati

def esegui_dml(connection, query, params):
    with connection.cursor() as cursor:
        righe_coinvolte = cursor.execute(query, params)
    connection.commit()
    return righe_coinvolte

def seleziona_tutti_modelli(connection):
    with connection.cursor() as cursor:
        query = "SELECT * FROM modelli_prodotto"
        return esegui_select(connection, query, ())

def seleziona_acquisti_cliente(connection, email):
    with connection.cursor() as cursor:
        query = "SELECT clienti.nome, clienti.cognome, clienti.email, ordini.id_ordine, ordini.data_ordine, prodotti.cod_seriale, modelli_prodotto.nome, modelli_prodotto.categoria, dettagli_ordine.prezzo_vendita_effettivo from clienti, dettagli_ordine, modelli_prodotto, ordini, prodotti where clienti.email=%s and clienti.id_cliente = ordini.id_cliente and dettagli_ordine.id_prodotto = prodotti.id_prodotto and ordini.id_ordine = dettagli_ordine.id_ordine and prodotti.id_modello = modelli_prodotto.id_modello"
        params = (email)
        return esegui_select(connection, query, params)

def conta_prodotti_modello(connection, cod_modello):
    with connection.cursor() as cursor:
        query = "select modelli_prodotto.nome, COUNT(modelli_prodotto.id_modello) quantità from modelli_prodotto, prodotti where modelli_prodotto.cod_modello = %s and modelli_prodotto.id_modello = prodotti.id_modello and prodotti.disponibilita='S' group by modelli_prodotto.id_modello"
        params = (cod_modello)
        return esegui_select(connection, query, params)

def inserisci_modello(connection, cod_modello, nome, descrizione, categoria, prezzo_listino):
    with connection.cursor() as cursor:
        query = "INSERT INTO modelli_prodotto (cod_modello, nome, descrizione, categoria, prezzo_listino) VALUES (%s, %s, %s, %s, %s)"
        params=  (cod_modello, nome, descrizione, categoria, prezzo_listino)
        return esegui_dml(connection, query, params)
    
def aggiorna_prezzo_modello(connection, cod_modello, nuovo_prezzo):
    with connection.cursor() as cursor:
        query = "UPDATE modelli_prodotto set prezzo_listino = %s where cod_modello = %s;"
        params = (nuovo_prezzo, cod_modello)
        return esegui_dml(connection, query, params)
    
# ==========================================================
# PROGRAMMA PRINCIPALE
# ==========================================================

def main():
    conn = None

    try:
        conn = get_connection()
        print("Connessione riuscita.")
        
        # es 1
        print("\nSelezionare tutti i modelli di prodotto")
        modelli = seleziona_tutti_modelli(conn)
        for riga in modelli:
            print(riga)
    
        # es 2
        print("\nVisualizzare gli acquisti di un utente a partire dalla sua email")
        email = "mario.rossi@email.it"
        acquisti = seleziona_acquisti_cliente(conn, email)
        for riga in acquisti:
            print(riga)
        # es 3
        print("\nContare quanti prodotti di un modello sono presenti a magazzino")
        cod_modello = "IPH15P"
        quantità = conta_prodotti_modello(conn, cod_modello)
        for riga in quantità:
            print(riga)
        
        # es 4
        print("\nInserire un nuovo modello di prodotto")
        cod_modello = "IPH16"
        nome = "iPhone 16"
        descrizione = "Smartphone Apple 256GB Nero"
        categoria = "Smartphone"
        prezzo_listino = 979.00
        righe_inserite = inserisci_modello(
            conn, 
            cod_modello, 
            nome, 
            descrizione, 
            categoria, 
            prezzo_listino
        )
        print(f"Righe inserite: {righe_inserite}")
        
        # es 5
        print("\nAggiornare il prezzo di listino di un modello")
        cod_modello = "IPH16"
        nuovo_prezzo = 980.00
        righe_aggiornate = aggiorna_prezzo_modello(conn, cod_modello, nuovo_prezzo)
        print(f"Righe aggiornate: {righe_aggiornate}")

    except pymysql.MySQLError as exc:
        if conn:
            conn.rollback()
        print(f"Errore database: {exc}")

    finally:
        if conn:
            conn.close()
            print("\nConnessione chiusa.")


if __name__ == "__main__":
    main()