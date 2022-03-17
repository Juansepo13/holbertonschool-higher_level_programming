-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- SELECT statement with clauses.
SELECT tg.name FROM tv_genres  AS tg JOIN tv_show_genres tn ON tg.id=tn.genre_id JOIN tv_shows AS ts ON tn.show_id=ts.id WHERE ts.title="Dexter" ORDER BY tg.name ASC;
