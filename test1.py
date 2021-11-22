import re

result=[]
pattern = r"hostname \S*"
i=1
k=0
l=1
while 1:
    try:
        file = open("S%d.txt" %i,"r")
    
    except FileNotFoundError :
        while k < len(result):
            while l < len(result):
                if result[l] == result[k]:
                    print('Error. Find swithes with identical hostnames.')
                    exit(1)
                l=l+1
            k=k+1
            l=k+1
        if len(result)==0:
            print('Error. Dont find files with configuration of switches.')
            exit(0)
        print('Test is successfull!')
        exit(0)


    match=re.search(pattern, file.read())
    result.append(match[0])
    file.close()
    i=i+1
