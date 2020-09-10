import sys
import subprocess
from typing import List, Union
import mlflow

from pyngrok import ngrok
from pathlib import Path

Job = Union[List[str], str]

def run_command(job: Job):
    """run command line.

    Arguments
    --------------
        job: command line 

    Example
    ----------
        $ls -a -G ~/hoge/hoge/

        =>
        path = "~/hoge/hoge"
        job = ["ls", "-a", "-G", path]
        run_commnand(job)
    """
    process = subprocess.run(
        job, 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # if process is failed, process.returncode != 0
    if process.returncode != 0:
        raise ValueError(f" === {process.stderr.decode('utf-8')} , so revise command ===")

class MLflowServer:
    """MLFlow server wrapper class for Colab
    
    Arguments
    --------------
        exp_path: the path in which you want to save outcomes of experiments

    Examples
    --------
    [1] %cd "path/to/experiments"

    [2] import set_mlflowserver
        set_mlflowserver.settings_on_colab()
    
    [3] from mlflowserver import MLflowServer

    [4] mlflowserver = MLflowServer("./") # ./  is the path in which you want to save the outcome

    [5] NGROK_AUTH_TOKEN = "<your ngrok auth token>"
        mlflowserver.run(NGROK_AUTH_TOKEN)
    """
    def __init__(self, exp_path: str):
        self.exp_path = Path(exp_path)
        self.artifact_path = self.exp_path / "mlruns"

        if not self.artifact_path.exists():
            self.artifact_path.mkdir()
            print(" === making artifact dir is completed ===")


    def cp_mlflow_from_drive(self, artifact_path):
        """copy mlflow directory into current directory 
        """
        mlflowdir_copy_job = ["cp", "-R", "-U", self.artifact_path, "./"]
        run_command(mlflowdir_copy_job)
        print(f" === copied mlflow dirs from {self.artifact_path} === ")

    def run(self, ngrok_access_token):

        # self.cp_mlflow_from_drive(self.artifact_path)

        # run tracking UI in the background
        get_ipython().system_raw(
            "mlflow ui --port 5000 &"
        )# run tracking UI in the background

        # Terminate open tunnels if exist
        ngrok.kill()

        # Setting the authtoken (optional)
        # Get your authtoken from https://dashboard.ngrok.com/auth
        ngrok.set_auth_token(ngrok_access_token)

        # Open an HTTPs tunnel on port 5000 for http://localhost:5000
        public_url = ngrok.connect(port="5000", proto="http", options={"bind_tls": True})
        print("MLflow Tracking UI:", public_url)

    def end(self):
        # self.save()
        # Terminate open tunnels if exist
        ngrok.kill()
        print(" === server is finished ===")

    def save(self):
        mlflowdir_copy_job = ["cp", "-R", "./mlruns", self.artifact_path]
        run_command(mlflowdir_copy_job)
        print(f" save mlflow dir into {self.artifact_path}")
