import subprocess

command = "poetry run python -m private_gpt"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
output, error = process.communicate()

if error:
    print(f"Error: {error.decode()}")
else:
    print(f"Output: {output.decode()}")