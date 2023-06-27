-- https://leetcode.com/problems/employee-bonus/?envType=study-plan-v2&envId=top-sql-50

SELECT name, bonus FROM Employee
LEFT JOIN Bonus
ON Employee.empId = Bonus.empId
WHERE bonus IS NULL
OR bonus < 1000