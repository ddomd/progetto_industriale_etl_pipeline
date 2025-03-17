import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from pandas import DataFrame

load_dotenv()

engine = create_engine(os.getenv("CONN_STRING"))


def bulk_insert(table_name: str, dataframe: DataFrame, schema="public"):
    try:
        dataframe.to_sql(
            name=table_name,
            con=engine,
            if_exists="append",
            index=False,
            schema=schema,
            chunksize=1000,
        )
        print(f"- Successfully inserted {len(dataframe)} rows into {table_name}")
    except Exception as e:
        print(f"- Error inserting data into {table_name}: {str(e)}")


def truncate_table(table_name: str, schema="public"):
    try:
        sql = text(f"TRUNCATE TABLE {schema}.{table_name}")

        with engine.begin() as conn:
            conn.execute(sql)

        print(f"- Successfully truncated table {schema}.{table_name}")

    except Exception as e:
        print(f"- Error truncating table {schema}.{table_name}: {str(e)}")


def upsert_dataframe(table_name: str, dataframe: DataFrame, schema="public"):
    columns = ", ".join(dataframe.columns)
    placeholders = ", ".join([f":{col}" for col in dataframe.columns])
    update_set = ", ".join(
        [f"{col} = EXCLUDED.{col}" for col in dataframe.columns if col != "id"]
    )

    query = text(
        f"""
        INSERT INTO {schema}.{table_name} ({columns})
        VALUES ({placeholders})
        ON CONFLICT (id) DO UPDATE SET {update_set}
    """
    )

    records = dataframe.to_dict("records")

    with engine.begin() as conn:
        conn.execute(query, records)
