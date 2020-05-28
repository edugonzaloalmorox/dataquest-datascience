# Joining three tables

SELECT 
# rename variables with the new names (asked in the exercise)
t.track_id
, t.name as track_name
, mt.name as track_type
, il.unit_price
, il.quantity
FROM invoice_line il
# use old var names for joining
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
where il.invoice_id = 4


# Joining more than three tables (add an additional column)

SELECT 
t.track_id
, t.name as track_name
, a.name as artist_name # new variable
, mt.name as track_type
, il.unit_price
, il.quantity
FROM invoice_line il
INNER JOIN track t ON t.track_id = il.track_id
INNER JOIN media_type mt ON mt.media_type_id = t.media_type_id
INNER JOIN album ab on ab.album_id = t.album_id
INNER JOIN artist a on a.artist_id = ab.artist_id
where il.invoice_id = 4


# Combining Multiple joins with Subqueries
# Tip: build the subquery first 



select 
final.title album, 
final.name artist, 
count(*) tracks_purchased
from invoice_line 
inner join 
(select ar.name,
       al.title,
       tr.track_id
from artist ar 
inner join track tr on tr.album_id = al.album_id
inner join album al on al.artist_id = ar.artist_id) final
on final.track_id = invoice_line.track_id
group by 1, 2
order by 3 desc
limit 5

# Recursive joins
# || " " || for concatenating two variables and leave a space between them

select e1.first_name || " " || e1.last_name employee_name,
       e1.title as employee_title, 
       e2.first_name || " " || e2.last_name supervisor_name,
       e2.title as supervisor_title       
from employee as e1
left join employee e2 on e1.reports_to = e2.employee_id
order by 1


# Pattern matching

select
first_name, 
last_name, 
phone
from customer
where first_name like '%Belle%'


#Generating  columns with the case statement

select 
   c.first_name || " " || c.last_name customer_name,
   COUNT(i.invoice_id) number_of_purchases,
   SUM(i.total) total_spent, 
   CASE
    when sum(i.total)  < 40 then 'small spender'
    when sum(i.total) > 100 then 'big spender'
    else "regular"
    end 
    as customer_category
from invoice i
inner join customer c on i.customer_id = c.customer_id
group by 1 
order by 1












