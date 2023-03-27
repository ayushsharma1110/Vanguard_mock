import pandas

from sqlalchemy import create_engine


# DF creation for UserTransactionDetails.csv
df = pandas.read_csv("UserTransactionsDetails.csv")
df = df.fillna(0)
df = df.drop_duplicates()
df = df.dropna()
print(df.values)

print(df)


# Df connection
my_conn=create_engine('mysql+mysqldb://root:1234@localhost/mock')

df.to_sql(con=my_conn, name='usertransactiondetails', if_exists='append', index=False)

print ('Data has been Exported')