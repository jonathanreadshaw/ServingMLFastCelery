from fastapi import FastAPI
from fastapi.responses import JSONResponse
from celery.result import AsyncResult

from celery_task_app.tasks import predict_churn_single
from models import Customer, Task, Prediction

app = FastAPI()


@app.post('/churn/predict', response_model=Task, status_code=202)
async def churn(customer: Customer):
    """Create celery prediction task. Return task_id to client in order to retrieve result"""
    task_id = predict_churn_single.delay(dict(customer))
    return {'task_id': str(task_id), 'status': 'Processing'}


@app.get('/churn/result/{task_id}', response_model=Prediction, status_code=200,
         responses={202: {'model': Task, 'description': 'Accepted: Not Ready'}})
async def churn_result(task_id):
    """Fetch result for given task_id"""
    task = AsyncResult(task_id)
    if not task.ready():
        print(app.url_path_for('churn'))
        return JSONResponse(status_code=202, content={'task_id': str(task_id), 'status': 'Processing'})
    result = task.get()
    return {'task_id': task_id, 'status': 'Success', 'probability': str(result)}

