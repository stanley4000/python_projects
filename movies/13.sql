/*  list the names of all people who starred in a movie in which Kevin Bacon also starred.
    Your query should output a table with a single column for the name of each person.
    There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958.
    Kevin Bacon himself should not be included in the resulting list.
*/
SELECT people.name FROM stars
JOIN movies ON movies.id = stars.movie_id
JOIN people ON people.id = stars.person_id
WHERE movies.id IN 
(SELECT movies.id FROM people
JOIN stars on stars.person_id = people.id
JOIN movies ON movies.id = stars.movie_id
WHERE people.name = 'Kevin Bacon' AND people.birth = 1958)
AND people.name != 'Kevin Bacon';