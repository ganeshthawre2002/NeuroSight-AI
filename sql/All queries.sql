------- neurosight ai data analytics project ------


------ KPI ----- Queries --------->>>>>>


SELECT COUNT (*)
FROM customers;

----- Total cutomers -----

SELECT COUNT(*) AS total_customers 
FROM customers;



------ Churned Customers ------

SELECT COUNT(*) as churned_customers
FROM customers
WHERE "Churn" = 'Yes';


------- Churn Rate ------


SELECT ROUND(
100.0* SUM(CASE WHEN "Churn" = 'Yes' THEN 1 ELSE 0 END) /
COUNT (*),2) AS churn_rate
FROM customers;



-------- Average monthly revenue ------


SELECT 
AVG("MonthlyCharges")
AS avg_monthly_charge
FROM customers;



-------- avarage customer tenure ------


SELECT
ROUND(AVG(tenure),2)
AS avg_tenure
FROM customers;



-------- bussiness quetions ---->>>>>>>
-------- which contract hs highest churn -----


SELECT 
"Contract",
COUNT(*) AS customers,
SUM(
CASE WHEN "Churn"='Yes'
THEN 1 ELSE 0 END )
AS churned
FROM customers 
GROUP BY "Contract";



-------- which payment mothod has highest churn ---------


SELECT 
"PaymentMethod",
COUNT(*) AS customers,
SUM(
CASE WHEN "Churn" ='Yes'
THEN 1 ELSE 0 END)
AS churned
FROM customers
GROUP BY "PaymentMethod"
ORDER BY churned DESC;





------- churn rate as per contract type  ------ 

SELECT 
"Contract",
COUNT(*) AS customers,
SUM(
CASE WHEN"Churn" ='Yes'
THEN 1 ELSE 0 END )
AS churned,
ROUND(100.0 * SUM(
CASE WHEN "Churn"='Yes'
THEN 1 ELSE 0 END)/
COUNT(*),2)
AS churn_rate
FROM customers
GROUP BY "Contract";




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











