def removeTheComma(str):#去除逗号
    ans=''
    for tmpchar in str:
        if tmpchar != ',':
            ans+=tmpchar
    return ans

def removek(str):#去除k
    ans=''
    for tmpchar in str:
        if tmpchar != 'k':
            ans+=tmpchar
    ans=float(ans)*1000
    ans=int(ans)
    return ans

