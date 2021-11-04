ALTER TABLE movies
ADD lexemesTitle tsvsector;

UPDATE movies
SET lexemesTitle = to_tsvector(title);

UPDATE movies SET rank = ts_rank(lexemesTitle,plainto_tsquery(
(
SELECT title FROM movies WHERE url='the-godfather-part-iii'
)
));

CREATE TABLE recommendationsBasedOnTitleField AS
SELECT url, rank FROM movies WHERE rank > 0.05 ORDER BY rank DESC LIMIT 50;

\copy (SELECT * FROM recommendationsBasedOnTitleField) to '/home/pi/RSL/top50recommendationsBasedOnTitle.csv' WITH csv;
