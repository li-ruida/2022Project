def removeTheComma(str):#去除逗号
    ans=''
    for tmpchar in str:
        if tmpchar != ',':
            ans+=tmpchar
    if ans[-1]=='+':
        ans=ans[0:-1]
    return ans

def removek(str):#去除k
    ans=''
    for tmpchar in str:
        if tmpchar != 'k':
            ans+=tmpchar
    ans=float(ans)*1000
    ans=int(ans)
    return ans

print(removeTheComma('5,000+'))