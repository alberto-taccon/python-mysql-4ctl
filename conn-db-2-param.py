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


# ==========================================================
# ESEMPIO SELECT PARAMETRICO
# ==========================================================

"""
Esempio di SELECT parametrizzata.
I valori sono separati dalla query e passati con execute(..., (parametri)).
"""
def esempio_select_parametrico(connection, id_cliente, nome):
    with connection.cursor() as cursor:
        query = "SELECT * FROM clienti WHERE id_cliente = %s AND nome = %s"
        cursor.execute(query, (id_cliente, nome))
        risultati = cursor.fetchall()
        return risultati


# ==========================================================
# ESEMPIO INSERT PARAMETRICO
# ==========================================================

"""
Esempio di INSERT parametrizzato.
I valori sono separati dalla query e passati con execute(..., (parametri)).
"""
def esempio_insert_parametrico(connection, nome, cognome, data_nascita, email):
    with connection.cursor() as cursor:
        query = """
            INSERT INTO clienti (nome, cognome, data_nascita, email)
            VALUES (%s, %s, %s, %s)
        """
        ris = cursor.execute(query, (nome, cognome, data_nascita, email))
        connection.commit()
        return ris


# ==========================================================
# ESEMPIO UPDATE PARAMETRICO
# ==========================================================

"""
Esempio di UPDATE parametrizzato.
I valori sono separati dalla query e passati con execute(..., (parametri)).
"""
def esempio_update_parametrico(connection, nuova_email, email_attuale):
    with connection.cursor() as cursor:
        query = "UPDATE clienti SET email = %s WHERE email = %s"
        ris = cursor.execute(query, (nuova_email, email_attuale))
    connection.commit()
    return ris


# ==========================================================
# ESEMPIO DELETE PARAMETRICO
# ==========================================================

"""
Esempio di DELETE parametrizzato.
Il valore della clausola WHERE è separato dalla query.
"""
def esempio_delete_parametrico(connection, email):
    with connection.cursor() as cursor:
        query = "DELETE FROM clienti WHERE email = %s"
        ris = cursor.execute(query, (email,))
    connection.commit()
    return ris


# ==========================================================
# PROGRAMMA PRINCIPALE
# ==========================================================

def main():
    conn = None

    try:
        conn = get_connection()
        print("Connessione riuscita.")

        # ------------------------------
        # SELECT parametrica
        # ------------------------------
        # Parametri
        id_cliente_select = 3
        nome_select = "Elena"

        # Chiamata funzione
        risultati_param = esempio_select_parametrico(
            conn,
            id_cliente_select,
            nome_select
        )
        print("\nESEMPIO PARAMETRICO - SELECT:")
        for riga in risultati_param:
            print(riga)

        # ------------------------------
        # DELETE parametrico
        # ------------------------------
        # Parametri
        email_delete = "davide.moretti.nuova@supermail.com"

        # Chiamata funzione
        righe_eliminate_param = esempio_delete_parametrico(
            conn,
            email_delete
        )
        print(f"\nESEMPIO PARAMETRICO - DELETE: righe eliminate = {righe_eliminate_param}")

        # ------------------------------
        # INSERT parametrico
        # ------------------------------
        # Parametri
        nome_insert = "Davide"
        cognome_insert = "Moretti"
        data_nascita_insert = date(1997, 11, 4)
        email_insert = "davide.moretti@supermail.com"

        # Chiamata funzione
        righe_inserite_param = esempio_insert_parametrico(
            conn,
            nome_insert,
            cognome_insert,
            data_nascita_insert,
            email_insert
        )
        print(f"\nESEMPIO PARAMETRICO - INSERT: righe inserite = {righe_inserite_param}")

        # ------------------------------
        # UPDATE parametrico
        # ------------------------------
        # Parametri
        nuova_email_update = "davide.moretti.nuova@supermail.com"
        email_attuale_update = "davide.moretti@supermail.com"

        # Chiamata funzione
        righe_aggiornate_param = esempio_update_parametrico(
            conn,
            nuova_email_update,
            email_attuale_update
        )
        print(f"\nESEMPIO PARAMETRICO - UPDATE: righe aggiornate = {righe_aggiornate_param}")

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