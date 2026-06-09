import pandas as pd 


def calculate_kpis(df):

    total_customers = len(df)


    churned_customers = (
        df["Churn"] == "Yes"
    ).sum()
    

    active_customers = (
        df["Churn"] == "No"
    ).sum()
    

    Churn_rate = round(
        churned_customers / 
        total_customers * 100, 2
    )



    return {
        "total_customers": total_customers,
        "churned_customers": churned_customers,
        "active_customers": active_customers,
        "Churn_rate": Churn_rate
}


##### contract analysis #####

def contract_analysis(df):

    contract_table = pd.crosstab(
        df["Contract"],
        df["Churn"]
    )

    contract_table["Churn_rate"] = round(
        contract_table["Yes"] / 
        (contract_table["Yes"] + contract_table["No"]) * 100, 2
    )   
    
    return contract_table



def tech_support_analysis(df):

    tech_support_table = pd.crosstab(
        df["TechSupport"],
        df["Churn"]
    )

    tech_support_table["Churn_rate"] = round(
        tech_support_table["Yes"] / 
        (tech_support_table["Yes"] + tech_support_table["No"]) * 100, 2
    )   
    
    return tech_support_table



def online_security_analysis(df):

    online_security_table = pd.crosstab(
        df["OnlineSecurity"],
        df["Churn"]
    )

    online_security_table["Churn_rate"] = round(
        online_security_table["Yes"] / 
        (online_security_table["Yes"] + online_security_table["No"]) * 100, 2
    )   
    
    return online_security_table

