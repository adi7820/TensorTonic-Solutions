-- Write your SQL query here
select name, salary from employees where department in ('Engineering', 'Marketing') and salary > 70000;