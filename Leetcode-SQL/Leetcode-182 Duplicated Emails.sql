-- Write your MySQL query statement below
SELECT email
FROM Person 
GROUP BY email
HAVING COUNT(email)>1;
-- 这个要注意的是WHERE里面不可以跟聚合函数 需要配合GROUP BY 和 HAVING 使用