from os import system
import subprocess
def g():
    a = subprocess.Popen("bundle update", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ls = a.stdout.readlines()
    ln = ls[-1]
    l1 = ls[-2]
    print(ln)
    if ln[0:14] == 'Make sure that':
        return ln.split('`')[1]
    elif l1[0:14] == 'Make sure that':
        return l1.split('`')[1]
    else:
        return False

def h():
    while True:
        a = g()
        if a:
            print(a)
            subprocess.Popen(a, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        else:
            return "success"
    
