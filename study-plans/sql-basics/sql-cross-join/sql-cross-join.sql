-- Write your SQL query here
select s.segment_name, m.metric_name from segments s cross join metrics m order by s.segment_name, m.metric_name;