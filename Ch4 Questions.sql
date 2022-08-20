-- 4.1: Which of the payment IDs would be returned by the following filter conditions?
-- customer_id <> 5 AND (amount > 8 OR date(payment_date) = '2005-08-23')

-- First payment, 8.99, and seventh payment. First payment is above 8, seventh fits the 
-- date criteria. Both have customer_id of four and match one condition of the second logic
-- statement.

-- 4.2 Which of the payment IDs would be returned by the following filter conditions?
-- customer_id = 5 AND NOT (amount > 6 OR date(payment_date) = '2005-06-19')

-- Customer_id must be 5 and either amount less than six or payment different than June 19.
-- All of customer_id = 5 except for 114 and 109. 114 is on June 19, 109's amount is 6.99.

-- 4.3: Find amounts of 1.98, 7.98, 9.98

select * from payment
where amount in ('1.98', '2.98', '9.98');

-- Two payments.

-- 4.4: Query with all customers whose last name has A in second, W anywhere after

SELECT customer_id, first_name, last_name from customer
where last_name like '_A%W%';