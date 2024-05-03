-- 코드를 작성해주세요
SELECT ID, FISH_NAME, LENGTH
FROM FISH_INFO I
JOIN FISH_NAME_INFO N USING(FISH_TYPE)

WHERE FISH_TYPE IN (
    SELECT FISH_TYPE
    FROM FISH_INFO
    GROUP BY FISH_TYPE
    HAVING LENGTH = MAX(LENGTH)
)
ORDER BY ID