-- n 6.sql, write a SQL query to determine the average rating of all movies released in 2012.
-- Your query should output a table with a single column and a single row (plus optional header) containing the average rating.

SELECT ROUND (AVG(rating), 2) FROM ratings JOIN movies ON movies.id = ratings.movie_id WHERE year = 2012;
