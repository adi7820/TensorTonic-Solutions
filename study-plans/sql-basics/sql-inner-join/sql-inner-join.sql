-- Write your SQL query here
select e.name, e.salary, d.dept_name from employees as e inner join departments as d on e.dept_id=d.id order by name;