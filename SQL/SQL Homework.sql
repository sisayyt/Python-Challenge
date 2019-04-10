

USE Sakila;
-- 1a. Display the first and last names of all actors from the table actor.
SELECT First_name, Last_name
FROM actor

-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.

SELECT  Upper (CONCAT (First_name, '  ',  Last_name)) Actor_Name
FROM actor

-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, 
"Joe." What is one query would you use to obtain this information?
SELECT actor_id, first_name, last_name
FROM actor_info
WHERE first_name = 'Joe'

-- 2b. Find all actors whose last name contain the letters GEN:
SELECT last_name
FROM actor
WHERE last_name like "%GEN%"

-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
SELECT First_name, Last_name
FROM actor
WHERE last_name like "%LI%"
ORDER BY last_name

-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:

SELECT Country_id, Country
FROM country
WhERE country IN ('Afghanistan', 'Bangladesh', 'China');

-- 3a. You want to keep a description of each actor. You don't think you will be performing queries on a description, 
-- so create a column in the table actor named description and use the data type BLOB (Make sure to research the type BLOB, 
-- as the difference between it and VARCHAR are significant).

ALTER TABLE  actor
ADD COLUMN  description blob (255);
SET SQL_SAFE_UPDATES = 0;



-- 3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the description column.
ALTER table actor 
DROP Column description;

-- 4a. List the last names of actors, as well as how many actors have that last name.
SELECT last_name, COUNT(*) 'Count'
FROM actor
GROUP BY last_name;

-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
SELECT last_name, Count(*) 'Count'
FROM actor
GROUP BY last_name;
HAVING COUNT > 2;

-- 4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
UPDATE actor
SET last_name = 'GROUCHO WILLIAMS'
WHERE last_name = "HARPO WILLIAMS"

-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO.
SET SQL_SAFE_UPDATES = 0;
UPDATE actor
SET first_name = "GROUCHO"
WHERE first_name = "HARPO"

-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?
DESCRIBE sakila.address;

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:

SELECT  s.First_Name, s. Last_Name, a.Address
FROM staff s
INNER JOIN address a ON
s.address_id = a.address_id

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
SELECT s.staff_id, s.first_name, s.last_name, Sum(p.amount) Amount
FROM staff s
INNER JOIN payment p ON p.staff_id = s.staff_id
WHERE payment_date BETWEEN '2005/08/01' AND '2005/08/31'
GROUP BY Staff_ID

 -- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
SELECT f.title Film_Title,  COUNT(a.actor_id) Number_of_Actors
FROM film f
INNER JOIN film_actor a on
f.film_id = a.film_id
GROUP BY a.actor_id
                
-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?
    
SELECT title, COUNT(inventory_id)
FROM film f
INNER JOIN inventory i 
ON f.film_id = i.film_id
WHERE title = "Hunchback Impossible";

-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
SELECT first_name, last_name, SUM(amount) Total_Payment
FROM Customer
INNER JOIN Payment
ON customer.customer_id = payment.customer_id
GROUP BY payment.customer_id
ORDER BY last_name  ASC

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
 
SELECT title
FROM film WHERE title 
LIKE 'K%' OR title LIKE 'Q%'
AND title IN 
(
SELECT name
FROM language
WhERE language_id = 1
);


-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.
        
SELECT first_name, last_name
FROM  actor
WHERE actor_id IN
     (SELECT actor_id
      FROM film_actor
	WHERE film_id in
		(SELECT film_id
		FROM film
		WHERE title = 'Alone Trip'));

-- 7c. You want to run an email marketing campaign in Canada, for which you 
-- will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.

SELECT country, last_name, first_name, email
FROM country c
LEFT JOIN customer cu
ON c.country_id = cu.customer_id
WHERE country = 'Canada';


-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. 
-- Identify all movies categorized as family films.

SELECT title, category
FROM film_list
WHERE category = 'Family';

-- 7e. Display the most frequently rented movies in descending order.

SELECT inventory.film_id, film_text.title, count(rental.inventory_id) Frequently_rented
FROM inventory 
INNER JOIN rental ON
inventory.inventory_id = rental.inventory_id
INNER JOIN film_text on
inventory.film_id = film_text.film_id
GROUP BY rental.inventory_id
ORDER BY COUNT(rental.inventory_id) DESC;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
SELECT s.store_id, SUM(amount) as Revenue
FROM store s
INNER JOIN staff st ON
s.store_id = st.store_id
INNER JOIN payment p ON
p.staff_id = st.staff_id
GROUP BY s.store_id
ORDER BY SUM(amount);

-- 7g. Write a query to display for each store its store ID, city, and country.

SELECT s.store_id, c.city, co.country
FROM country co
INNER JOIN city c ON
c.country_id = co.country_id
INNER JOIN address a ON
c.city_id = a.city_id
INNER JOIN store s ON
a.address_id = s.address_id

-- 7h. List the top five genres in gross revenue in descending order. 
--(Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)


SELECT Name, sum(p.amount) Revenue
FROM  rental r
INNER JOIN payment p ON
p.rental_id = r.rental_id
INNER JOIN inventory i ON
i.inventory_id = r.inventory_id
INNER JOIN film_category ca ON
ca.film_id = i.film_id
INNER JOIN category c ON
c.category_id = ca.category_id
GROUP BY name
ORDER BY sum(amount) ASC

-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.

CREATE VIEW top_five_grossing_genres AS

SELECT Name, sum(p.amount) Revenue
FROM rental r
INNER JOIN payment p on
p.rental_id = r.rental_id
INNER JOIN inventory i on
i.inventory_id = r.inventory_id
INNER JOIN film_category ca on
ca.film_id = i.film_id
INNER JOIN category c on
c.category_id = ca.category_id
GROUP BY name
LIMIT 5;

-- 8b. How would you display the view that you created in 8a?
SELECT * FROM top_five_grossing_genres;

-- 8c. You find that you no longer need the view top_five_genres. 
-- Write a query to delete it.

DROP VIEW top_five_grossing_genres;