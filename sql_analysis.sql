--total tickets

select count(*) as total_tickets from dbo.tickets

--Most common issue

select issue_type,count(*)as total from dbo.tickets
group by issue_type
order by total desc

--Average resolution time

select avg(resolution_time) as Avg_resolution_time from dbo.tickets

--tickets by priority

select priority,count(priority) from dbo.tickets
group by priority

--Monthly trend

select month(created_date) as Month, count(*) as Total from dbo.tickets
group by month(created_date)
order by total desc

