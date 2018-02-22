import subprocess
command = 'DIR |MORE'
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()
print(process.returncode)
