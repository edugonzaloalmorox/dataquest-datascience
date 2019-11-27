# Writing More Complex Queries

select Major, Unemployment_rate
from recent_grads
where Unemployment_rate <
    (select avg(Unemployment_rate)
     from recent_grads)
order by Unemployment_rate

