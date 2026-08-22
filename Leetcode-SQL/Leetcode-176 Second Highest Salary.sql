-- # Write your MySQL query statement below
SELECT 
    (SELECT DISTINCT salary 
     FROM Employee ORDER BY salary DESC 
     LIMIT 1 OFFSET 1) as SecondHighestSalar;
-- 这样SELECT ...(子查询) as Name 如果子查询没查到的话就是返回Null 