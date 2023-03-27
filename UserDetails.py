import pandas as pd

from sqlalchemy import create_engine


# df creation for UserDetails.csv
def df():
    df = pd.read_csv("UserDetails.csv")
    df = df.drop_duplicates()
    df = df.drop(['Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8'], axis=1)
    df = df.dropna()


print(df)


# Function for df connection
def conn(df):
    my_conn = create_engine('mysql+mysqldb://root:1234@localhost/mock')

    df.to_sql(con=my_conn, name='Userdetails', if_exists='append', index=False)


