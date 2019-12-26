# Writing More Complex Queries

select Major, Unemployment_rate
from recent_grads
where Unemployment_rate <
    (select avg(Unemployment_rate)
     from recent_grads)
order by Unemployment_rate


SELECT CAST(COUNT(*) as float)/CAST((SELECT COUNT(*) from recent_grads) as float) proportion_abv_avg 
from recent_grads
WHERE ShareWomen > 
(SELECT AVG(ShareWomen) from recent_grads)

select Major, Major_category
from recent_grads
where Major_category in 
(select Major_category from recent_grads
group by Major_category
order by sum(Total) DESC
limit 5)

# Avg ratio
select AVG(cast(Sample_size as float) / cast(Total as float)) as avg_ratio
from recent_grads
