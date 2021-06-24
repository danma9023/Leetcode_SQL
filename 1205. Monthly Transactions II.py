# 1205. Monthly Transactions II
# Medium

# 79

# 250

# Add to List

# Share
# SQL Schema
# Table: Transactions

# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | id             | int     |
# | country        | varchar |
# | state          | enum    |
# | amount         | int     |
# | trans_date     | date    |
# +----------------+---------+
# id is the primary key of this table.
# The table has information about incoming transactions.
# The state column is an enum of type ["approved", "declined"].
# Table: Chargebacks

# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | trans_id       | int     |
# | trans_date     | date    |
# +----------------+---------+
# Chargebacks contains basic information regarding incoming chargebacks from some transactions placed in Transactions table.
# trans_id is a foreign key to the id column of Transactions table.
# Each chargeback corresponds to a transaction made previously even if they were not approved.
 

# Write an SQL query to find for each month and country: the number of approved transactions and their total amount, the number of chargebacks, and their total amount.

# Note: In your query, given the month and country, ignore rows with all zeros.

# The query result format is in the following example:

 

# Transactions table:
# +-----+---------+----------+--------+------------+
# | id  | country | state    | amount | trans_date |
# +-----+---------+----------+--------+------------+
# | 101 | US      | approved | 1000   | 2019-05-18 |
# | 102 | US      | declined | 2000   | 2019-05-19 |
# | 103 | US      | approved | 3000   | 2019-06-10 |
# | 104 | US      | declined | 4000   | 2019-06-13 |
# | 105 | US      | approved | 5000   | 2019-06-15 |
# +-----+---------+----------+--------+------------+

# Chargebacks table:
# +----------+------------+
# | trans_id | trans_date |
# +----------+------------+
# | 102      | 2019-05-29 |
# | 101      | 2019-06-30 |
# | 105      | 2019-09-18 |
# +----------+------------+

# Result table:
# +---------+---------+----------------+-----------------+------------------+-------------------+
# | month   | country | approved_count | approved_amount | chargeback_count | chargeback_amount |
# +---------+---------+----------------+-----------------+------------------+-------------------+
# | 2019-05 | US      | 1              | 1000            | 1                | 2000              |
# | 2019-06 | US      | 2              | 8000            | 1                | 1000              |
# | 2019-09 | US      | 0              | 0               | 1                | 5000              |
# +---------+---------+----------------+-----------------+------------------+-------------------+

select  t1.month as month, 
        t1.country,
        sum(case when type = 'approved' then 1 else 0 end) as approved_count,
        sum(case when type = 'approved' then t1.amount else 0 end) as approved_amount,
        sum(if(type = 'chargeback', 1, 0)) as chargeback_count,
        sum(if(type = 'chargeback', t1.amount, 0)) as chargeback_amount
        
from 
(        
(select date_format (t.trans_date, '%Y-%m') as month,
t.country, t.amount, 'approved' as type from Transactions t
where t.state='approved')

union all

(select  date_format(c.trans_date, '%Y-%m') as month,
t.country, t.amount, 'chargeback' as type from Transactions t join 
Chargebacks c
on c.trans_id = t.id
) 
)t1

group by t1.month, t1.country
