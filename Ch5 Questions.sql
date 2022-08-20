-- Example of aliases being useful. film_actor and actor tables queried twice.
-- Goal is to find films in which both actors appeared.

select f.title
FROM film f
join film_actor fa1
ON f.film_id = fa1.film_id
join actor a1
on fa1.actor_id = a1.actor_id
join film_actor fa2
on f.film_id = fa2.film_id
join actor a2
on fa2.actor_id = a2.actor_id
where (a1.first_name = 'CATE' AND a1.last_name = 'MCQUEEN')
AND (a2.first_name = 'CUBA' and a2.last_name = 'BIRCH');

-- 5.1: 
SELECT c.first_name, c.last_name, a.address, ct.city
FROM customer c
JOIN address a
ON c.address_id = a.address_id
JOIN city ct
-- Need to make the city ids match.
ON a.city_id = ct.city_id
WHERE a.district = 'California';

-- 5.2: Return the title of every film in which an actor with the first name JOHN appeared.
select * from film_actor;

-- Getting all actors named John.
select actor_id, first_name, last_name from actor
where first_name = 'JOHN';

-- Getting name of films in which actor_id = 192.
select f.title from film f
JOIN film_actor fa
ON fa.film_id = f.film_id
where fa.actor_id = '192';

-- 5.3: Return all addresses in the same city.
select a.address, a2.address, a.city_id from address a
join address a2
where a.city_id = a2.city_id and a.address and a.address != a2.address;