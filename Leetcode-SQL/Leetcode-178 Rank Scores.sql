--  Write your MySQL query statement below
SELECT s.score,
    (SELECT COUNT(DISTINCT s2.score)
    FROM Scores AS s2 WHERE s2.score >= s.score) AS 'rank'
    -- 这个rank的写法很巧妙 通过查询大于等于自己的distinct的score来确认rank
FROM Scores AS s
ORDER BY s.score DESC