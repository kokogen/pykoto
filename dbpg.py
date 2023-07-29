import psycopg2

with psycopg2.connect(database="asos",
                        host="localhost",
                        user="postgres",
                        password="pg123",
                        port="5432") as conn:

    with conn.cursor() as crs:
        crs.execute("select * from dds.dag;");
        rows = crs.fetchall()
        print(rows)