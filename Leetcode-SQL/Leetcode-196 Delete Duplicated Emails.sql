-- 经典错误写法: 不能在 DELETE/UPDATE 的子查询里直接引用你正在删除/更新的那张表。
DELETE FROM Person AS p1
WHERE (
    p1.id NOT IN 
    (SELECT min(p2.id)
    FROM Person AS p2
    GROUP BY p2.email)
);

-- 解法1
DELETE FROM Person AS p1
WHERE p1.id NOT IN ( 
    SELECT id FROM 
    (SELECT min(p2.id) AS id
    FROM Person AS p2
    GROUP BY p2.email)
    AS temp
);
-- 解决方法: SELECT id FROM (...) AS temp 这一层。MySQL 优化器就认为你读的是一个临时结果集,不是原表了

-- 解法2: 自连接 直观
DELETE p1 FROM Person p1
JOIN Person p2
  ON p1.email = p2.email AND p1.id > p2.id;

-- 解法3: 窗口函数 (值得学习)
DELETE FROM Person
WHERE id IN (
    SELECT id FROM (
        SELECT id,
               ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
        FROM Person
    ) AS ranked
    WHERE rn > 1
);