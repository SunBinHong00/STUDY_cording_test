-- 코드를 입력하세요
with recursive RC as (
    select 0 as HOUR
    union all
    select HOUR+1 from rc where HOUR<23
)

SELECT HOUR,  COUNT(B.ANIMAL_TYPE) AS COUNT
FROM RC A
LEFT JOIN ANIMAL_OUTS B ON A.HOUR = HOUR(B.DATETIME)
GROUP BY A.HOUR
ORDER BY HOUR

# SELECT *
# FROM ANIMAL_OUTS 