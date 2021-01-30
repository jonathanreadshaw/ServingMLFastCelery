from pydantic import BaseModel


class Customer(BaseModel):
    """ Features for customer churn prediction """
    Customer_Age: int
    Gender: str
    Dependent_count: int
    Education_Level: str
    Marital_Status: str
    Income_Category: str
    Card_Category: str
    Months_on_book: int
    Total_Relationship_Count: int
    Months_Inactive_12_mon: int
    Contacts_Count_12_mon: int
    Credit_Limit: float
    Total_Revolving_Bal: int
    Avg_Open_To_Buy: float
    Total_Amt_Chng_Q4_Q1: float
    Total_Trans_Amt: int
    Total_Trans_Ct: int
    Total_Ct_Chng_Q4_Q1: float
    Avg_Utilization_Ratio: float


class Task(BaseModel):
    """ Celery task representation """
    task_id: str
    status: str


class Prediction(BaseModel):
    """ Prediction task result """
    task_id: str
    status: str
    probability: float
