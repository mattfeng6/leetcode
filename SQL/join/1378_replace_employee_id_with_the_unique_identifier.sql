-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/?envType=study-plan-v2&envId=top-sql-50

SELECT eu.unique_id, e.name
FROM Employees as e
LEFT JOIN EmployeeUNI as eu
ON e.id = eu.id