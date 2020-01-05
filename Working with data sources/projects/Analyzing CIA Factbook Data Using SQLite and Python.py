import sqlite3
import pandas as pd
conn = sqlite3.connect("factbook.db")
cursor = conn.cursor() 


# Exploring the data

q = "SELECT * FROM sqlite_master WHERE type='table';"
pd.read_sql_query(q, conn)

q2 = "SELECT * FROM facts limit 5"
pd.read_sql_query(q2, conn)


## Summary statistics

q3 = '''select min(population), 
       max(population),
        min(population_growth),
        max(population_growth)
from facts'''

pd.read_sql_query(q3, conn)

q4 = '''
select countries
from facts
where population == (select max(population) from facts)
'''

pd.read_sql_query(q4, conn)


q5 = '''
select countries
from facts
where population == (select min(population) from facts)
'''

pd.read_sql_query(q5, conn)


import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)


q6 = '''select population, population_growth, birth_rate, death_rate
from facts
where population != (select max(population) from facts)
and  population != (select min(population) from facts) 
'''

pd.read_sql_query(q6, conn).hist()


