import pandas as pd
import psycopg2


def check_if_data_exists(file):
    poke_json = pd.read_json(file)
    if poke_json.empty:
        raise Exception("No data")
    poke_json.to_csv("poke.csv", index=False)
    poke_csv = pd.read_csv("poke.csv")
    return poke_csv


def set_unique_id(poke_csv):
    poke_csv.to_csv('first_poke.csv', sep=',', index=False, encoding='utf-8')
    poke_df = pd.read_csv('first_poke.csv')
    poke_df['id'] = poke_df.reset_index().index
    poke_df.sort_values(by=['id'], inplace=True)
    if poke_df['id'].is_unique:
        return poke_df
    else:
        raise Exception("id is not unique.")

# depois criar features em poke_df


def database_connection(poke_df):
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS pokemon")
    sql_query = """
    CREATE TABLE IF NOT EXISTS pokemon(
        id INT PRIMARY KEY NOT NULL,
        name VARCHAR(50) NOT NULL,
        fst_type VARCHAR(50) NOT NULL,
        snd_type VARCHAR(50),
        total INT NOT NULL,
        hp INT NOT NULL,
        attack INT NOT NULL,
        defense INT NOT NULL,
        sp_atk INT NOT NULL,
        sp_def INT NOT NULL,
        speed INT NOT NULL

    )
    """
    cursor.execute(sql_query)
    poke_df.to_csv('final_poke.csv', sep=',', index=False, encoding='utf-8')
    with open('final_poke.csv') as csv_poke:
        next(csv_poke)
        cursor.copy_from(csv_poke, "pokemon", sep=",")


a = check_if_data_exists('pokemon.json')
b = set_unique_id(a)
database_connection(b)
