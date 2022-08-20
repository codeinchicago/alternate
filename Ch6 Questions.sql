select 'CUST' typ, c.first_name, c.last_name
from customer c
UNION ALL
select 'ACTR' typ, a.first_name, a.last_name
from actor a;