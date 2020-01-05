 # Previewing a table using select

select * from recent_grads limit 10


# Filtering Rows using WHERE 

select major, ShareWomen from recent_grads
where ShareWomen <= 0.5

# Expressing multiple filter criteria with AND

select major, Major_category, median, ShareWomen from recent_grads
where ShareWomen >= 0.5 and Median > 50000


# Returning one of several conditions with OR
select Major, Median,  Unemployed from recent_grads
where Median >= 10000 OR Unemployed <= 1000 
limit 20

# Grouping Operators With Parentheses
select Major, Major_category, ShareWomen, Unemployment_rate from recent_grads
where (Major_category = 'Engineering') and (ShareWomen > 0.5 or Unemployment_rate <0.051)

# Ordering results using order by

select Major, ShareWomen, Unemployment_rate from recent_grads
where  ShareWomen >0.3 and Unemployment_rate <0.1
order by ShareWomen desc

# Practice writing a Query

`Write a query that returns the Engineering or Physical Sciences majors in ascending order of unemployment rates`

select Major_category, Major, Unemployment_rate from recent_grads
where Major_category IN ('Engineering','Physical Sciences') 
order by Unemployment_rate asc
