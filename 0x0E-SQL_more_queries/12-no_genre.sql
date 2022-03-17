-- Lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- SELECT statement retrieves rows selected from one or more tables.
SELECT ts.title, tg.genre_id
FROM tv_shows AS ts
-- FROM clause lists the tables and any joins in "tv_shows".
LEFT JOIN tv_show_genres AS tg
-- ON clause, separates the join terms from the filtering terms.
ON ts.id=tg.show_id
-- WHERE clause filters out the results.
WHERE tg.genre_id IS NULL
ORDER BY ts.title, tg.genre_id ASC;
