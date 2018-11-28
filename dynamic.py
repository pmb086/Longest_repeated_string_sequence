from time import time
import sys
chars = []
def LRS(str, l1, l2):
    if l1 == 0 or l2 == 0:
        return 0
    elif str[l1-1] == str[l2-1] and l1 != l2:
        chars.append(str[l1-1])
        return LRS(str,l1-1, l2-1) + 1
    else:
        return max(LRS(str,l1,l2-1), LRS(str,l1-1,l2))
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
	out = LRS(str,l,l)
	#end = time()
	res = ""
	for i in chars:
		if i not in res:
			res+=i
	if res != "":
		print(res)
	else:
		print("String has no repeated characters")
	#print(out)
	#print(end-start)
else:
	print("Invalid Input")

