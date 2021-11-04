ALTER TABLE movies
ADD lexemesStarring tsvsector;

UPDATE movies
SET lexemesStarring = to_tsvector(Starring);

UPDATE movies SET rank = ts_rank(lexemesStarring,plainto_tsquery(
(
SELECT Starring FROM movies WHERE url='the-godfather-part-iii'
)
));

CREATE TABLE recommendationsBasedOnStarringField AS
SELECT url, rank FROM movies WHERE rank > 0.05 ORDER BY rank DESC LIMIT 50;

\copy (SELECT * FROM recommendationsBasedOnStarringField) to '/home/pi/RSL/top50recommendationsBasedOnStarring.csv' WITH csv;
