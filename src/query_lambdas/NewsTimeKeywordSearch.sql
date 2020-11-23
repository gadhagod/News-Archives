SELECT n._id, models.a.description, models.a.link, models.a.title
FROM commons.NewsArchives n, 
UNNEST (n.articles AS a) AS models
WHERE lower(models.a.title) LIKE lower(concat('%', :keyword, '%')) AND n._id LIKE concat(:time, '%')
ORDER BY n._id DESC
LIMIT :limit_count