-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- SELECT is used to retrieve rows selected from one or more tables.
SELECT tvs.title, tvsg.genre_id
FROM tv_shows AS tvs
-- JOIN clause link data between tables based on values of common columns.
JOIN tv_show_genres AS tvsg
WHERE tvs.id=tvsg.show_id
ORDER BY tvs.title, tvsg.genre_id ASC;
