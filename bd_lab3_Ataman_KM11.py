import pandas as pd
from sqlalchemy import create_engine

file_path = 'GlobalWeatherRepository.csv'

data = pd.read_csv(file_path)

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost/lab3"
engine = create_engine(DATABASE_URL)

table_name = 'weather'

data.to_sql(table_name, engine, if_exists='replace', index=False)

print(f"Дані з файлу '{file_path}' успішно перенесені в таблицю '{table_name}' успішно перенесені в таблицю.")
