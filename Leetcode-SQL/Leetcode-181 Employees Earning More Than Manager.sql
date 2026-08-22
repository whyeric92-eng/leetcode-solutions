SELECT e1.name AS Employee
FROM Employee AS e1
WHERE e1.salary > 
    (SELECT e2.salary 
     FROM Employee AS e2
     WHERE e2.id = e1.managerId);
--关联子查询复杂度都接近O(N2)了，不好

--用join 自连接(self-join)
SELECT e1.name AS Employee
FROM Employee AS e1
INNER JOIN Employee AS e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;