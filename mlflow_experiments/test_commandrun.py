import sys
import subprocess


def main():
    # permission
    subprocess.run(["chmod", "755", "test.sh"])

    # run command line
    process = subprocess.run(
        "./test.sh",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    print(process.stdout.decode("utf-8"))
    
if __name__ == '__main__':
    main()