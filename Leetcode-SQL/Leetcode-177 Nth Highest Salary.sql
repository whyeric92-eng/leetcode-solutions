CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N - 1;
  RETURN (
      -- Write your MySQL query statement below 
        SELECT DISTINCT salary 
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET M 
      -- 这个地方不可以直接写N-1 因为OFFSET后面只能接SET的变量或者具体的数字
  );
END