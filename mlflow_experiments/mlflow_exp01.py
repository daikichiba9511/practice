import os
import mlflow
import tempfile

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

SEED = 42
# np.random.seed(SEED)

# settigs to connect tracking server
mlflow.set_tracking_uri("http://0.0.0.0:5000")
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://0.0.0.0:9000"
os.environ["AWS_ACCESS_KEY_ID"] = "minio-access-key"
os.environ["AWS_SECRET_ACCESS_KEY"] = "minio-secret-key"

@dataclass(frozen=True)
class Data:
    X_train: np.ndarray
    y_train: np.ndarray
    X_test: np.ndarray
    y_test: np.ndarray
    
def make_datasets() -> Data:
    """ Create Datasets for experiments
    
    Returns
    -------
        data: immutable class.
    """
    N = 200
    X = np.linspace(-3, 3, N)
    y = np.sin(X) + 0.2 * X + 0.3 * np.random.randn(N)
    X_train, X_test, y_train, y_test = train_test_split(
        X.reshape(-1, 1), y, test_size=0.3, random_state=SEED
    )
    data = Data(X_train, y_train, X_test, y_test)
    return data

def plot_results(
    model, data: Data, score, filename=None
    ):
    """ plot train data and test data and prediceted results.
    
    Arguments
    ---------
        model: ML model which has attr (predcit)
        data: sample data contains train data and test data.
        score: 
        filename: if not None, this one is filename when save results
    
    """
    plt.clf()
    fig = plt.figure()
    plt.scatter(data.X_test, data.y_test, label="test_data", edgecolor="k", facecolor="w")
    plt.scatter(data.X_train, data.y_train, label="Other training data", facecolor="r")

    plt.title("predicted results")
    plt.xlabel("$x$")
    plt.ylabel("$y$")

    x = np.reshape(np.arange(-3, 3, 0.01), (-1, 1))
    plt.scatter(np.sort(data.X_test), model.predict(np.sort(data.X_test)), label=f"model ($R^2 = {score:.3f}$)", color="b")
    plt.grid()
    plt.legend()
    plt.show()

    if filename is not None:
        fig.savefig(filename)
    plt.close()

def main():
    # set experiment name
    mlflow.set_experiment("tutorial00")

    # To send artifact, make directory for saving dataset at once
    temp_dir = tempfile.TemporaryDirectory()

    # make dataset
    data = make_datasets()

    # save data
    np.savetxt(os.path.join(temp_dir.name, "X_train.csv"), data.X_train, delimiter=',')
    np.savetxt(os.path.join(temp_dir.name, "y_train.csv"), data.y_train, delimiter=',')
    np.savetxt(os.path.join(temp_dir.name, "X_test.csv"), data.X_test, delimiter=',')
    np.savetxt(os.path.join(temp_dir.name, "y_test.csv"), data.y_test, delimiter=',')


    # run start: runID is published here
    # runID is experiments number to specify each ones
    for C in {0.01, 1, 10, 100}:
        print(f"========= train starts with C = {C} ============")
        with mlflow.start_run(run_name="Search C", nested=True):

            mlflow.log_artifacts(temp_dir.name, artifact_path="dataset")

            model = SVR(kernel="rbf", C=C, epsilon=0.1, gamma="auto").fit(data.X_train, data.y_train)

            mlflow.set_tag("algolithm", "SVR")

            mlflow.log_param("C", C)

            score = model.score(data.X_test, data.y_test)
            print(f"Score : {score:.3f}")
            mlflow.log_metric("R2 Score", score)

            # save model
            mlflow.sklearn.log_model(model, "model", serialization_format="cloudpickle")

            # log an artifact (output file)
            # by specify "w", we can write results as string in output.txt
            with tempfile.TemporaryDirectory() as tmp:
                filename = os.path.join(tmp, "predict_results.png")
                plot_results(model, data, score, filename=filename)
                # record outcomes
                mlflow.log_artifact(filename, artifact_path="results")
        mlflow.end_run()

if __name__ == '__main__':
    main()
    