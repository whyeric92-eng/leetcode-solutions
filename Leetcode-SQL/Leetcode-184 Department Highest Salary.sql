SELECT d.name AS Department, e.name AS Employee, e.salary AS salary
FROM Employee AS e
INNER JOIN Department AS d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN 
(SELECT e1.departmentId, Max(e1.salary)
FROM Employee AS e1
Group BY e1.departmentId);
--这种写法关键点就是在后面WHERE那个地方的用(departmentId,salary)去匹配对应的Employee的某一行

--推荐的写法:窗口函数
--内层:按部门分组(PARTITION BY),组内按工资降序排名(ORDER BY ... DESC),
--RANK()给每一行打名次,同分并列同名次,不合并行,所以并列最高工资的人都能保留
SELECT Department, Employee, salary AS Salary
FROM (
    SELECT d.name AS Department, e.name AS Employee, e.salary,
           RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
    FROM Employee AS e
    JOIN Department AS d ON e.departmentId = d.id
) AS ranked
--外层:WHERE不能直接用同层算出的rnk,所以把内层结果当成一张表(ranked)再过滤
WHERE rnk = 1;

-- 窗口函数(OVER):不会像GROUP BY一样把行压缩,每一行都保留,只是多加一列统计结果
-- PARTITION BY = 划分窗口范围(类似分组,但不合并行)
-- ORDER BY = 在窗口范围内排序
-- 常用搭配:RANK() / MAX() / MIN() OVER (PARTITION BY xxx ORDER BY xxx)
-- 例如求每个部门薪水最高的人:RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) = 1