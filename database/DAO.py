from database.DB_connect import DBConnect
from model.state import State
from model.sighting import Sighting


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def ge_all_years():
        cnx = DBConnect.get_connection()
        result = []

        cursor = cnx.cursor()
        query = """select distinct YEAR(s.datetime) 
                       from sighting s
                       
                       """
        cursor.execute(query)
        for row in cursor:
            result.append(row[0])

        cursor.close()
        cnx.close()

        return result

    @staticmethod
    def ge_all_states(anno: int):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT st.*
                       FROM sighting sig, state st 
                       WHERE sig.state=st.id AND YEAR(sig.datetime)=%s
                       ORDER BY Name ASC"""
            cursor.execute(query, (anno,))

        for row in cursor:
            result.append(
                State(row["id"],
                      row["Name"],
                      row["Capital"],
                      row["Lat"],
                      row["Lng"],
                      row["Area"],
                      row["Population"],
                      row["Neighbors"]))

        cursor.close()
        cnx.close()

        return result

    @staticmethod
    def get_all_states():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * 
                    from state s"""
            cursor.execute(query)

            for row in cursor:
                result.append(
                    State(row["id"],
                          row["Name"],
                          row["Capital"],
                          row["Lat"],
                          row["Lng"],
                          row["Area"],
                          row["Population"],
                          row["Neighbors"]))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_sightings():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * 
                    from sighting s 
                    order by `datetime` asc """
            cursor.execute(query)

            for row in cursor:
                result.append(Sighting(**row))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_nodes(a,c):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * 
                        from sighting s 
                        where year(s.datetime)=%s and s.state=%s
                        order by `datetime` asc """
            cursor.execute(query, (a, c,))

            for row in cursor:
                result.append(Sighting(**row))
            cursor.close()
            cnx.close()
        return result


    #arco fra due avvistamenti esiste se e solo se tali avvistamenti hanno la stessa
    # Forma (colonna “shape” del db) e sono avvenuti ad una distanza inferiore a 100km.
    # Per calcolare la distanza in km tra due avvistamenti
    # utilizzare il metodo distance_HV già fornito nella classe Sighting.

