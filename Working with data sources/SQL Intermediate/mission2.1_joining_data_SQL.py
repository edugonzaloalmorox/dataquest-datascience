# Introducing joins

Join the tables on the values where facts.id and cities.facts_id are equal

```select * from facts
inner join cities on cities.facts_id = facts.id 
limit 10
````

# Understanding inner joins 

Joins cities to facts using an INNER JOIN.
 - Uses aliases for table names.
Includes, in order:
 - All columns from cities.
 - The name column from facts aliased to country_name.

 `````select c.*, f.name as country_name from facts f
inner join cities c on c.facts_id = f.id
limit 5
````

# Practicing inner joins

select f.name as country, c.name as capital_city from cities c
inner join facts f on f.id = c.facts_id
where c.capital = 1 -- this is a var that indicates capital if = 1

# Left joins

select f.name as country, f.population
from facts as f
left join cities c on c.facts_id = f.id
where c.name is null 

# Finding the most populous cities 

select c.name as capital_city
        , f.name as country
        , c.population
from cities as c
left join facts f on f.id = c.facts_id
where capital = 1
order by 3 desc
limit 10

# Combining joins and subqueries

select c.name as capital_city,
       f.name as country,
       c.population
from facts as f
inner join (
    select * from cities 
    where capital = 1
    and population >  10000000
) as c on c.facts_id = f.id
order by c.population desc

# Challenge: Complex Query with Joins and Subqueries

SELECT
    f.name country,
    c.urban_pop,
    f.population total_pop,
    (c.urban_pop / CAST(f.population AS FLOAT)) urban_pct
FROM facts f
INNER JOIN (
            SELECT
                facts_id,
                SUM(population) urban_pop
            FROM cities
            GROUP BY 1
           ) c ON c.facts_id = f.id
           WHERE urban_pct > 0.5
           ORDER BY urban_pct ASC










