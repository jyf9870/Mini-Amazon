import psycopg2


def connect_db():
    # conn = psycopg2.connect(host="db", database="projectDB",
    #                         user="yc557", password="Oliver666", port="5432")
    conn = psycopg2.connect(host="127.0.0.1", database="projectDB",
    user="yc557", password="Oliver666", port="5432")
    return (conn, conn.cursor())


def execute_and_commit(sql, conn, cursor):
    cursor.execute(sql)
    conn.commit()
