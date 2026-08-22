SELECT w1.id
FROM Weather AS w1
JOIN Weather AS w2 
ON w1.recordDate = w2.recordDate + INTERVAL 1 DAY
-- 标准date前后一天的写法 
AND w1.temperature > w2.temperature;