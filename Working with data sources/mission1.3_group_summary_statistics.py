# Calculating group level summary statistics 

SELECT SUM(Employed) 
FROM recent_grads 
GROUP BY Major_category

# Using group by

select Major_category, 
       AVG(Employed)/AVG(Total) as share_employed
from recent_grads
group by Major_category

# Using having

select Major_category, 
       AVG(Low_wage_jobs)/AVG(Total) as share_low_wage
from recent_grads
group by Major_category 
having share_low_wage > 0.1

# Using Round

SELECT ROUND(ShareWomen, 4), # it does not create a new variable, only rounds it
       Major_category
FROM recent_grads
LIMIT 10

# Nesting functions

SELECT Major_category,
       ROUND(AVG(College_jobs)/AVG(Total), 3) as share_degree_jobs
FROM recent_grads
GROUP BY Major_category
HAVING share_degree_jobs < .3

# Casting

select Major_category, 
CAST(SUM(Women) as Float)/ CAST(SUM(Total) as Float) as SW
from recent_grads
group by Major_category
order by SW








