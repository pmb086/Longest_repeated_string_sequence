from time import time
import sys
def LRS(str): 
    m = len(str) 
    lrs = [[0 for i in range(m+1)] for j in range(m+1)] 
      
    for i in range(1, m + 1): 
        for j in range(1, m + 1): 
            if (str[i-1] == str[j-1] and i != j): 
                lrs[i][j] = 1 + lrs[i-1][j-1] 
            else: 
                lrs[i][j] = max(lrs[i][j-1], lrs[i-1][j]) 
    out = '' 
    i, j = m, m 
    while (i > 0 and j > 0): 
        if (lrs[i][j] == lrs[i-1][j-1] + 1): 
            out = out + str[i-1] 
            i = i - 1
            j = j - 1
        elif (lrs[i][j] == lrs[i-1][j]): 
            i = i - 1
        else: 
            j = j - 1      
    return out[::-1] 

if sys.argv[1] == '':
	str =''
else:
	str = sys.argv[1]
	l = len(str);
	int = ''.join(i for i in str if i.isdigit())
if str == "":
	print("Invalid Input")
elif int == '' and str.isalpha():
	#start = time()
	out = LRS(str)
	#end = time()
	if out != "":
		print(out)
	else:
		print("String has no repeated characters")
	#print(end-start)
else:
	print("Invalid Input")
