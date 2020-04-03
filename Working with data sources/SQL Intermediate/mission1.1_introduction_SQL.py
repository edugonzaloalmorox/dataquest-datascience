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






