# Introduction

SELECT COUNT(Major) FROM recent_grads
WHERE ShareWomen < 0.5

# Finding a Column's Minimum and Maximum Values in SQL

SELECT MIN(Median)
from recent_grads
where Major_category='Engineering'