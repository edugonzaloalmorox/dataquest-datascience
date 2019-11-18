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