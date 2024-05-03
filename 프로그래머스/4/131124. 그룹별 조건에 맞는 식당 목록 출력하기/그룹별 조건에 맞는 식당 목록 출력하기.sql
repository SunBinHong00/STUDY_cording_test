SELECT P.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM (SELECT *, COUNT(MEMBER_ID) OVER(PARTITION BY MEMBER_ID) AS COUNT_REVIEW
      FROM REST_REVIEW) AS R
JOIN MEMBER_PROFILE AS P
ON R.MEMBER_ID = P.MEMBER_ID
WHERE COUNT_REVIEW = (
    SELECT COUNT(MEMBER_ID) OVER(PARTITION BY MEMBER_ID) AS C
    FROM REST_REVIEW
    ORDER BY C DESC
    LIMIT 1)
ORDER BY REVIEW_DATE, REVIEW_TEXT;
