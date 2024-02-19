import time

word=input("Enter word:-")
temp=""
for j in range(0,len(word),1):
    for i in range(97,123,1):
        if(chr(i)!=word[j]):
            time.sleep(0.05)
            print(temp,end="")
            print(chr(i))
        elif(chr(i)==word[j]):
                temp+=word[j]
                break
print(word)