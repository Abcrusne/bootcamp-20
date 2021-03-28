-- In 12.sql, write a SQL query to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.
-- Your query should output a table with a single column for the title of each movie.
-- You may assume that there is only one person in the database with the name Johnny Depp.
-- You may assume that there is only one person in the database with the name Helena Bonham Carter.

SELECT title FROM people JOIN stars ON people.id = stars.person_id  JOIN movies ON movies.id = stars.movie_id WHERE name = "Johnny Depp" AND movie_id IN (SELECT movie_id FROM people JOIN stars ON people.id = stars.person_id WHERE name = "Helena Bonham Carter");