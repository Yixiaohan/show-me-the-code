import os

for i in range(25):
    if(i < 9):
        s = 'No.000' + str(i+1)
    else:
        s = 'No.00' + str(i+1)
    os.system("mkdir -p %s" %s)
