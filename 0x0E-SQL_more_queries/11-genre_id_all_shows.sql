-- Lists all shows contained in the database hbtn_0d_tvshows.
-- SELECT is used to retrieve rows selected from one or more tables.
SELECT tvs.title, tvsg.genre_id
FROM tv_shows AS tvs
-- LEFT JOIN: Table "tv_shows" is set to depend on table "tv_shows_genres".
LEFT JOIN tv_show_genres AS tvsg
ON tvs.id=tvsg.show_id
ORDER BY tvs.title, tvsg.genre_id ASC;
