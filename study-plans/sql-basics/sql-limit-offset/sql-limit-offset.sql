-- Write your SQL query here
select product, revenue, sale_date from sales order by revenue desc, sale_date asc limit 3 OFFSET 1