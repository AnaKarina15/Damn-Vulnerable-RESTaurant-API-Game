import subprocess


def get_disk_usage(parameters: str):
    allowed = ["-h", "-a", "-T"] # parameters

    args = parameters.split()
    for a in args:
        if a not in allowed:
            raise Exception("Invalid parameter")

    command = ["df"] + args

    try:
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )
        usage = result.stdout.strip().decode()
    except:
        raise Exception("An unexpected error was observed")

    return usage
