SELECT DISTINCT l1.num as ConsecutiveNums
FROM Logs AS l1
INNER JOIN Logs AS l2 ON l1.id = l2.id-1
INNER JOIN Logs AS l3 ON l1.id = l3.id-2
WHERE l1.num = l2.num AND l1.num = l3.num;
-- 这个写法很巧妙 相当于是选Logs的3行出来拼接在一起比较