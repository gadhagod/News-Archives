SELECT n._id, models.a.description, models.a.link, models.a.title
FROM commons.NewsArchives n, 
UNNEST (n.articles AS a) AS models
WHERE lower(models.a.description) LIKE lower(concat('%', :keyword, '%'))