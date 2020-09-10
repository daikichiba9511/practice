import sys
import subprocess
from typing import List, Union

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
        print(process.stderr.decode("utf-8"))
        raise ValueError(" === failed, so revise command ===")
        

def settings_on_colab():
    run_command(["pip3", "install", "mlflow", "--quiet"])
    print("mlflow is installed")
    run_command(["pip3", "install", "pyngrok", "--quiet"])
    print("pyngrok installed")
    print(" === install is finished ===")