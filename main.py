import pandas as pd
import psycopg2


def check_if_data_exists(file):
    poke_json = pd.read_json(file)

    if poke_json.empty:
        raise Exception("No data")
    poke_csv = poke_json.to_csv("poke.csv", index=False)
    return poke_csv


def set_unique_id(poke_csv):
    poke_df = pd.read_csv(poke_csv)
    poke_df.sort_values(by=['id'], inplace=True)
    poke_df.drop('id', axis=1, inplace=True)
    if poke_df['id'].is_unique:
        return poke_df
    raise Exception("id is not unique.")

# depois criar features em poke_df


def database_connection():
    conn = psycopg2.connect(
        database="",
        user="",
        password="",
        host="",
        port=""
    )

    conn.autocommit = True
    cursor = conn.cursor()
    sql = '''CREATE database mydb''';
    cursor.execute(sql)
