SELECT visited_on,
       amount,
       ROUND(amount / 7, 2) AS average_amount
FROM (
    SELECT c1.visited_on,
           SUM(c2.amount) AS amount
    FROM (SELECT DISTINCT visited_on FROM Customer) c1
    JOIN Customer c2
      ON c2.visited_on BETWEEN DATE_SUB(c1.visited_on, INTERVAL 6 DAY) AND c1.visited_on
    GROUP BY c1.visited_on
) t
WHERE visited_on >= (SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) FROM Customer)
ORDER BY visited_on;