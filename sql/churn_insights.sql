------- neurosight ai data analytics project ------




--------  Churn_Insight Querises ------>>>>>>>>>>>


----- Churn by tenure ------


SELECT 
CASE
WHEN tenure < 12 THEN '0-12 Months'
WHEN tenure < 24 THEN '12-24 Months'
WHEN tenure <48 THEN '24-48 Months'
ELSE  '48+ Months'
END AS tenure_group,

COUNT(*) AS customers,

SUM(CASE WHEN "Churn"='Yes'
THEN 1 ELSE 0 END) AS churned
FROM customers
GROUP BY tenure_group;




------- trying to find whether revenue is related to churn -----


SELECT 
"Churn",
AVG("MonthlyCharges") AS avg_monthly_charge
FROM customers 
GROUP BY "Churn";

----
SELECT 
"Churn",
AVG("TotalCharges") AS avg_total_charge
FROM customers
GROUP BY "Churn";
















