四个最基础的关键字
SELECT + FROM：要哪些列，从哪张表拿
SELECT * FROM orders;
* 是"所有列"。
只要订单号和数量：
SELECT so, qty FROM orders;

WHERE：筛选行，就是你很熟的 if
SELECT * FROM orders WHERE qty >= 10;
读作"从 orders 里选出所有列，但只要 qty 大于等于 10 的那些行"。这和你 big_orders 函数里 if qty >= min_qty 是同一件事，只是换了一种语言写。

ORDER BY：排序
SELECT * FROM orders ORDER BY qty DESC;
DESC 是从大到小，ASC（默认）是从小到大。

GROUP BY + SUM：这个你一眼就能认出来
SELECT company, SUM(qty) FROM orders GROUP BY company;

DISTINCT:去重
SELECT DISTINCT 列名 FROM ...

AS：起个"别名
SELECT 原来的列名 AS 新名字 FROM ...

LIMIT:查询结果的前 n 行
LIMIT 1 就是"只要最高的那一行"。

OFFSET n:跳过前 n 行，从第 n+1 行开始算。
OFFEST 1 就是跳过前 1 行，从第 2 行开始算。

