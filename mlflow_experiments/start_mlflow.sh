#!/bin/sh

mlflow server \
    --backend-store-uri "postgresql://mlflowuser:mlflowpassword@postgresql:3306/mlflowdb" \
    --default-artifact-root "s3://default/" --host 0.0.0.0 --port 5000