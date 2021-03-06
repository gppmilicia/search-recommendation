SET group_concat_max_len=102400;

SELECT * FROM (SELECT "tag_id", "product_name", "users"
               UNION ALL
               SELECT tag_id, product_name, group_concat(DISTINCT user_id ORDER BY user_id SEPARATOR " ") as users
               FROM signals
               GROUP BY tag_id, product_name) as export
INTO OUTFILE '/var/lib/mysql-files/extract_data.csv'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';