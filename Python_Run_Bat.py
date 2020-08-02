import subprocess
p = subprocess.Popen("cmd.exe /c" + "test.bat abc", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

curline = p.stdout.readline()
while(curline != b''):
    print(curline)
    curline = p.stdout.readline()

p.wait()
print(p.returncode)