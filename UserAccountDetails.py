import pandas

from sqlalchemy import create_engine

# df creation for UserAccountDetails.csv

df1 = pandas.read_csv("UserAccountDetails.csv")
df1 = df1.drop_duplicates()
df1 = df1.fillna({'AccountBalance':'0'})
df1 = df1.dropna()
print(df1.values)
print(len(df1))

# def conn(df1):
my_conn = create_engine('mysql+mysqldb://root:1234@localhost/mock')

df1.to_sql(con=my_conn, name='Useraccountdetails', if_exists='append', index=False)