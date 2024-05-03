-- 코드를 작성해주세요
SELECT  ED.ID,
        ED.GENOTYPE,
        PED.GENOTYPE AS PARENT_GENOTYPE
FROM    ECOLI_DATA AS ED LEFT JOIN ECOLI_DATA AS PED ON ED.PARENT_ID = PED.ID
WHERE   ED.GENOTYPE & PED.GENOTYPE = PED.GENOTYPE
ORDER BY ED.ID