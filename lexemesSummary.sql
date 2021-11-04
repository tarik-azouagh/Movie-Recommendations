ALTER TABLE movies
ADD lexemesSummary tsvsector;

ALTER TABLE movies
ADD rank float4;

UPDATE movies
SET lexemesSummary = to_tsvector(Summary);

UPDATE movies SET rank = ts_rank(lexemesSummary,plainto_tsquery(
(
SELECT Summary FROM movies WHERE url='the-godfather-part-iii'
)
));

CREATE TABLE recommendationsBasedOnSummaryField3 AS
SELECT url, rank FROM movies WHERE rank > 0.05 ORDER BY rank DESC LIMIT 50;

\copy (SELECT * FROM recommendationsBasedOnSummaryField3) to '/home/pi/RSL/top50recommendationsBasedOnSummary.csv' WITH csv;
