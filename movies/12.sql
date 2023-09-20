/*  list the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred.
    Your query should output a table with a single column for the title of each movie.
    You may assume that there is only one person in the database with the name Bradley Cooper.
    You may assume that there is only one person in the database with the name Jennifer Lawrence.
*/
SELECT movies.title
FROM people
JOIN stars ON stars.person_id = people.id
JOIN movies ON movies.id = stars.movie_id
WHERE people.name = 'Bradley Cooper' AND movies.title IN 
(SELECT movies.title FROM people
JOIN stars ON stars.person_id = people.id
JOIN movies ON movies.id = stars.movie_id
WHERE people.name = 'Jennifer Lawrence');



