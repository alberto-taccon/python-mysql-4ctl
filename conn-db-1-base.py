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
# ESEMPIO SELECT BASE
# ==========================================================
"""
Esempio base di SELECT
"""
def esempio_select(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM clienti")
        risultati = cursor.fetchall()
        return risultati
    

# ==========================================================
# ESEMPIO INSERT BASE
# ==========================================================
"""
Esempio base di INSERT.
Anche qui i valori sono scritti direttamente nella query.
Funziona, ma non è il modo migliore se i dati cambiano.
"""
def esempio_insert(connection):
    with connection.cursor() as cursor:
        ris = cursor.execute(
            "INSERT INTO clienti (nome, cognome, data_nascita, email) "
            "VALUES ('Martino', 'Vallanzi', '1999-10-10', 'martino.valla@supermail.com')"
        )
    connection.commit()
    return ris


# ==========================================================
# ESEMPIO UPDATE BASE
# ==========================================================
"""
Esempio base di UPDATE.
I valori sono scritti direttamente nella query.
Funziona, ma non è il modo migliore se i dati cambiano.
"""
def esempio_update(connection):
    with connection.cursor() as cursor:
        ris = cursor.execute(
            "UPDATE clienti "
            "SET email = 'martino.vallanzi.nuova@supermail.com' "
            "WHERE email = 'martino.valla@supermail.com'"
        )
    connection.commit()
    return ris


# ==========================================================
# ESEMPIO DELETE BASE
# ==========================================================
"""
Esempio base di DELETE.
Il valore della condizione è scritto direttamente nella query.
Funziona, ma non è il modo migliore se i dati cambiano.
"""
def esempio_delete(connection):
    with connection.cursor() as cursor:
        ris = cursor.execute(
            "DELETE FROM clienti WHERE email = 'martino.vallanzi.nuova@supermail.com'"
        )
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
        # SELECT
        # ------------------------------
        risultati_base = esempio_select(conn)
        print("\nESEMPIO BASE - SELECT:")
        for riga in risultati_base:
            print(riga)

        # ------------------------------
        # DELETE
        # ------------------------------
        righe_eliminate_base = esempio_delete(conn)
        print(f"\nESEMPIO BASE - DELETE: righe eliminate = {righe_eliminate_base}")

        # ------------------------------
        # INSERT
        # ------------------------------
        righe_inserite_base = esempio_insert(conn)
        print(f"\nESEMPIO BASE - INSERT: righe inserite = {righe_inserite_base}")

        # ------------------------------
        # UPDATE
        # ------------------------------
        righe_aggiornate_base = esempio_update(conn)
        print(f"\nESEMPIO BASE - UPDATE: righe aggiornate = {righe_aggiornate_base}")

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