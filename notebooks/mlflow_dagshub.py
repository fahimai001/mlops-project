import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/fahimai001/mlops-project.mlflow')

dagshub.init(repo_owner='fahimai001', repo_name='mlops-project', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)