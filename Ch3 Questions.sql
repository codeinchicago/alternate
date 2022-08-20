-- 3.1: Actor ID, first name, last name for all actors. Sort by last name and then by first name

SELECT actor_id, first_name, last_name
FROM actor
ORDER BY last_name;

SELECT actor_id, first_name, last_name
FROM actor
ORDER BY first_name;

-- 3.2: Get actor id, first name, last name, for actors
-- with last name of "Williams" or "Davis"

SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name = 'Williams' or last_name = 'Davis';

-- 3.3: id of customers from Jul 5, 2005. Distinct customer ID.

SELECT DISTINCT customer_id from rental
where date(rental_date) = '2005-07-05';

-- 3.4: Fill in the blanks question.