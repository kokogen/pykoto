from sqlalchemy import create_engine, text
from sqlalchemy import MetaData, Table

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

metadata_obj = MetaData()

stmt = text("select id, body from tb1 where id > :c")
with engine.connect() as conn:
    conn.execute(text("create table tb1 (id int primary key, body varchar(100) not null)"))

    # conn.execute(
    #     text("insert into tb1 (id, body) values(:id, :body)"),
    #     [{"id": 1, "body": "First thing"},{"id": 2, "body": "Second thing"},{"id": 3, "body": "Pipito"}]
    # )
    # result = conn.execute(stmt, {"c" : 2})
    # for id, body in result:
    #     print(f"{id}:\t{body}")
    # conn.commit()

    conn.commit()

    some_tbl = Table("tb1", metadata_obj, autoload_with=engine)


    print(type(some_tbl))