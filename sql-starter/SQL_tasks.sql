SELECT FirstName, LastName, Title
From employees;

SELECT FirstName, LastName, Title
From employees
WHERE City="Seattle";

SELECT FirstName, LastName, Title
From employees
WHERE City="London";

SELECT FirstName
FROM employees
WHERE Title LIKE "%Sales%";

SELECT FirstName
FROM employees
WHERE Title LIKE "%Sales%" AND TitleOfCourtesy IN ("Ms.", "Mrs.");

SELECT FirstName, BirthDate
FROM employees
ORDER BY BirthDate ASC
LIMIT 5; 

SELECT FirstName
FROM employees
ORDER BY HireDate 
LIMIT 5;

SELECT FirstName
FROM employees
WHERE ReportsTo IS NULL;

SELECT a.FirstName, a.LastName, b.FirstName, b.LastName
FROM employees AS a
JOIN employees AS b
WHERE  a.ReportsTo=b.EmployeeID

SELECT COUNT(FirstName)
FROM employees
WHERE TitleOfCourtesy IN ("Ms.", "Mrs.");

SELECT COUNT(FirstName)
FROM employees
WHERE TitleOfCourtesy NOT IN ("Ms.", "Mrs.");

SELECT City, COUNT(City)
FROM employees
GROUP BY City;

SELECT o.OrderID, e.EmployeeID
FROM orders AS o
JOIN employees AS e
WHERE o.EmployeeID=e.EmployeeID;

SELECT o.OrderID, s.CompanyName
FROM orders AS o
JOIN shippers AS s
WHERE o.ShipVia = s.ShipperID;

SELECT ShipCountry,COUNT(ShipCountry)
FROM orders 
GROUP BY ShipCountry;

SELECT orders.EmployeeID, COUNT(orders.EmployeeID)
FROM orders 
JOIN employees
GROUP BY orders.EmployeeID
ORDER BY COUNT( orders.EmployeeID) DESC
LIMIT 1;

SELECT orders.CustomerID, COUNT(orders.CustomerID)
FROM orders
JOIN customers
GROUP BY orders.CustomerID
ORDER BY COUNT(orders.CustomerID) DESC
LIMIT 1;

SELECT orders.OrderID, employees.FirstName, customers.ContactName
FROM orders
JOIN employees
ON orders.EmployeeID = employees.EmployeeID 
JOIN customers
ON orders.CustomerID = customers.CustomerID;

SELECT customers.ContactName, shippers.CompanyName
FROM orders
JOIN customers
ON orders.CustomerID = customers.CustomerID
JOIN shippers
ON orders.ShipVia = shippers.ShipperID;

 

