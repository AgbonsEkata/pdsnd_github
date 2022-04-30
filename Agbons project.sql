/*Q1 - How many rented movies were returned late, early, and on time?
#Query: */

WITH t1 AS (SELECT *,
                   DATE_PART ('day', return_date - rental_date) AS Date_difference
            FROM rental),

t2 AS (SELECT rental_duration,
              date_difference,
              CASE
              WHEN rental_duration > date_difference THEN 'Returned Early'
              WHEN rental_duration = date_difference THEN 'Returned On Time'
              ELSE 'Returned Late'
              END AS Return_status
      FROM film f
      JOIN inventory I
        USING(film_id)
      JOIN t1
        USING (inventory_id))
SELECT
  return_status,
  COUNT(*) AS total_no_of_films
FROM t2
GROUP BY 1
ORDER BY 2 DESC;


/* Q2 - What are the top and least rented (in-demand) genres, and what are their total sales?”
#Query */
SELECT
  t1.genre,
  t1.total_rent_demand,
  t2.total_sales
FROM (SELECT
             C.name AS Genre,
             COUNT(cu.customer_id) AS total_rent_demand
      FROM category c
      JOIN film_category FC
        ON c.category_id = FC.category_id
      JOIN film f
        USING (film_id)
      JOIN inventory I
        USING (film_id)
      JOIN rental r
        USING (inventory_id)
      JOIN customer cu
        USING (customer_id)
      GROUP BY 1
      ORDER BY 2) t1
JOIN
(SELECT
  c.name AS Genre,
  SUM(p.amount) AS Total_sales
FROM category c
JOIN film_category FC
  USING (category_id)
JOIN film f
  USING (film_id)
JOIN inventory I
  USING (film_id)
JOIN rental r
  USING (inventory_id)
JOIN payment p
  USING (rental_id)
GROUP BY 1
ORDER BY 2 DESC) t2
  ON t1.genre = t2.genre;


/*Q3 - How many distinct users have rented each genre?
#Query: */
SELECT
  c.name AS Genre,
  COUNT(Distinct cu.customer_id) AS Rent_demand
FROM category c
JOIN film_category FC
  USING (category_id)
JOIN film f
  USING (film_id)
JOIN inventory I
  USING(film_id)
JOIN rental r
  USING (inventory_id)
JOIN customer cu
  USING(customer_id)
GROUP BY 1
ORDER BY 2 desc;



/*Q4 - Provide a table with the family-friendly film categories. Each of the quartiles, and the corresponding count of movies within each combination of film category for each corresponding rental duration category.
Query: */
SELECT
  category_name,
  quartiles,
  COUNT(category_name) AS Category_count
FROM (SELECT
  c.name category_name,
  NTILE(4) OVER (ORDER BY f.rental_duration) AS quartiles
FROM film f
JOIN film_category fc
  ON f.film_id = fc.film_id
JOIN category c
  ON c.category_id = fc.category_id
WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')) t1
GROUP BY 1,
         2
ORDER BY 1, 2;
