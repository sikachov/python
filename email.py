import sys

def test1(dom):
    if (len(dom)>2) and (len(dom)<257):
        if ('.' in dom):
            for i in dom:
                if i not in correct:
                    return False
            return True
        else:
            return False
    else:
        return True


def test2(site):
    correct.append('"')
    correct.append(',')
    correct.append(':')
    correct.append('!')
    if len(site)<129:
        for i in site:
            if i not in correct:
                return False
        return True
    else:
        return False


def test3(dom):
    first,second=dom.split('.')
    if (first[0]=='-') or (first[len(first)-1]=='-') or (second[0]=='-') or (second[len(second)-1]=='-'):
        return False
    else:
        return True


def test4(site):
    count=site.count('"')
    if count%2==0:
        return True
    else:
        return False

def search(char,string):
    length=len(string)
    a=[]
    for i in xrange(length):
        if string[i]==char:
            a.append(i)
    return a

def test5(site):
    b=search('.',site)
    i=0
    j=0
    for i in xrange(len(b)-1):
        if b[i+1]-b[i]==1:
            return False
    return True
def test6(site):
    f=site.split('"')
    if ('!' in f[0]) or (':' in f[0]) or (',' in f[0]):
        return False
    else:
        if ('!' in f[len(f)-1]) or (':' in f[len(f)-1]) or (',' in f[len(f)-1]):
            return False
        else:
            return True


correct=['q','w','e','r','t','y','u','i','o','p',
         'a','s','d','f','g','h','j','k','l',
         'z','x','c','v','b','n','m',
         '1','2','3','4','5','6','7','8','9','0','-','_','.']
mail=raw_input("E-mail: ")
if mail.find('@')<0:
    print 'Incorrect'
    sys.exit()

name,domain=mail.split('@')

if (test1(domain)==test2(name)==test3(domain)==test4(name)==test5(name)==test6(name)==True):
    print 'Correct'
else:
    print 'Incorrect'
