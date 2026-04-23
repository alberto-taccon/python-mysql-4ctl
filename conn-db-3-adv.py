import pymysql
from datetime import date

# Configurazione della connessione al database
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "NOME_UTENTE_DATABASE",
    "password": "PASSWORD_DATABASE",
    "database": "4CTL",
    "port": 3307,
    "cursorclass": pymysql.cursors.Cursor,
    "connect_timeout": 5,
}


def get_connection():
    """
    Crea e restituisce una connessione al database.
    """
    return pymysql.connect(**DB_CONFIG)


# ==========================================================
# FUNZIONI DI SUPPORTO
# ==========================================================
"""
Esegue una query SELECT e restituisce tutte le righe trovate.
params serve quando la query contiene dei placeholder %s, se non ci sono params passare ()
"""
def esegui_select(connection, query, params):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        risultati = cursor.fetchall()
        return risultati


"""
Esegue una query DML (INSERT, UPDATE, DELETE).
Restituisce il numero di righe coinvolte.
"""
def esegui_dml(connection, query, params):
    with connection.cursor() as cursor:
        righe_coinvolte = cursor.execute(query, params)
    connection.commit()
    return righe_coinvolte


# ==========================================================
# FUNZIONI DATABASE
# ==========================================================
"""
Restituisce tutti i clienti e sfrutta la funzione esegui_select
"""
def seleziona_tutti_clienti(connection):
    query = "SELECT * FROM clienti"
    return esegui_select(connection, query, ())


"""
Restituisce i clienti che rispettano id e nome.
"""
def seleziona_cliente(connection, id_cliente, nome):
    query = "SELECT * FROM clienti WHERE id_cliente = %s AND nome = %s"
    params = (id_cliente, nome)
    return esegui_select(connection, query, params)


"""
Inserisce un nuovo cliente.
"""
def inserisci_cliente(connection, nome, cognome, data_nascita, email):
    query = "INSERT INTO clienti (nome, cognome, data_nascita, email) VALUES (%s, %s, %s, %s)"
    params = (nome, cognome, data_nascita, email)
    return esegui_dml(connection, query, params)


"""
Aggiorna l'email di un cliente data la sua email attuale.
"""
def aggiorna_email_cliente(connection, email_attuale, nuova_email):
    query = "UPDATE clienti SET email = %s WHERE email = %s"
    params = (nuova_email, email_attuale)
    return esegui_dml(connection, query, params)


"""
Elimina un cliente data la sua email.
"""
def elimina_cliente(connection, email):
    query = "DELETE FROM clienti WHERE email = %s"
    params = (email,)
    return esegui_dml(connection, query, params)


# ==========================================================
# PROGRAMMA PRINCIPALE
# ==========================================================

def main():
    conn = None

    try:
        conn = get_connection()
        print("Connessione riuscita.")

        print("\nFUNZIONI:")

        clienti = seleziona_tutti_clienti(conn)
        print("Tutti i clienti:")
        for riga in clienti:
            print(riga)

        clienti_filtrati = seleziona_cliente(conn, 3, "Elena")
        print("\nClienti filtrati:")
        for riga in clienti_filtrati:
            print(riga)

        righe_delete = elimina_cliente(conn, "sara.conti.nuova@supermail.com")
        print(f"\nEliminazione con funzione applicativa: righe eliminate = {righe_delete}")

        nuove_righe = inserisci_cliente(
            conn,
            "Sara",
            "Conti",
            date(2000, 9, 21),
            "sara.conti@supermail.com"
        )
        print(f"Inserimento con funzione applicativa: righe inserite = {nuove_righe}")

        righe_update = aggiorna_email_cliente(
            conn,
            "sara.conti@supermail.com",
            "sara.conti.nuova@supermail.com"
        )
        print(f"Aggiornamento con funzione applicativa: righe aggiornate = {righe_update}")

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