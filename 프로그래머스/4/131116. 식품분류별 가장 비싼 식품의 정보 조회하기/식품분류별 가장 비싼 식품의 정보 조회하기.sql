# 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회
SELECT A.CATEGORY, A.MAX_PRICE, A.PRODUCT_NAME
FROM (SELECT CATEGORY, PRICE,
      MAX(PRICE) OVER (PARTITION BY CATEGORY) MAX_PRICE, PRODUCT_NAME
      FROM FOOD_PRODUCT
      WHERE CATEGORY IN ('과자', '국', '김치', '식용유')) A
WHERE A.MAX_PRICE = A.PRICE
ORDER BY A.MAX_PRICE DESC;

