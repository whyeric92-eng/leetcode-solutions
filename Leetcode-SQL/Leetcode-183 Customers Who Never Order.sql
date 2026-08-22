SELECT name AS Customers
FROM Customers
WHERE id NOT IN (SELECT o.customerId FROM Orders AS o);
-- 用NOT IN来"跟一组值比较" !=用来跟一个值比较