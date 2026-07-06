-- Write your SQL query here
select a.username, COALESCE(b.username, 'organic') as referrer_name from user_referrals as a left join user_referrals b on a.referred_by=b.id order by a.username;