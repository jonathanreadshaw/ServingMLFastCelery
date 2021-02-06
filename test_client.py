import requests
from time import sleep

test_body = {
    "Customer_Age": 45,
    "Gender": "M",
    "Dependent_count": 3,
    "Education_Level": "High School",
    "Marital_Status": "Married",
    "Income_Category": "$60K - $80K",
    "Card_Category": "Blue",
    "Months_on_book": 39,
    "Total_Relationship_Count": 5,
    "Months_Inactive_12_mon": 1,
    "Contacts_Count_12_mon": 3,
    "Credit_Limit": 12691,
    "Total_Revolving_Bal": 777,
    "Avg_Open_To_Buy": 11914,
    "Total_Amt_Chng_Q4_Q1": 1.335,
    "Total_Trans_Amt": 1144,
    "Total_Trans_Ct": 42,
    "Total_Ct_Chng_Q4_Q1": 1.625,
    "Avg_Utilization_Ratio": 0.061
}


def dummy_task(data, poll_interval=5, max_attempts=5):
    base_uri = r'http://127.0.0.1:8000'
    predict_task_uri = base_uri + '/churn/predict'
    task = requests.post(predict_task_uri, json=data)
    task_id = task.json()['task_id']
    predict_result_uri = base_uri + '/churn/result/' + task_id
    attempts = 0
    result = None
    while attempts < max_attempts:
        attempts += 1
        result_response = requests.get(predict_result_uri)
        if result_response.status_code == 200:
            result = result_response.json()['probability']
            break
        sleep(poll_interval)
    return result


if __name__ == '__main__':
    prediction = dummy_task(test_body)
    print(prediction)
