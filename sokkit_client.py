import socket
import xmltodict
import json
import sys

pathf = sys.argv[1]
inint = str(sys.argv[2]).split("-")
HOST = "127.0.0."+inint[0]
PORT = int(inint[1])
print(PORT)
try:
    with open(pathf+"manifest.xml", "r") as xmlf:
        data = json.loads(json.dumps(xmltodict.parse(xmlf.read())))
except OSError as e:
    print("No manifest.xml file in folder.")
    raise SystemExit

dict_keys = list(data.keys())
mdict_keys = list(data["manifest"].keys())
req_keys = ['manifest','pages','all']
for r in req_keys:
    if (not r in dict_keys and not r in mdict_keys):
        print("Missing required key %s"%(r,))
        raise SystemExit
d = data["manifest"]
path = d["all"]["path"]
while True:
     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            resstr = ""
            while resstr == "":
                res = conn.recv(1024)
                if (len(res) <= 0):
                    break
                resstr += res.decode("utf-8")
            if (not resstr in path):
                conn.sendall(b"404")
                conn.shutdown(socket.SHUT_RDWR) 
                conn.close()
            else:
                try:
                    fn = ""
                    for dv in d["pages"]["page"]:
                        if (dv["path"] == resstr):
                            fn = dv["filename"]
                    with open(pathf+fn) as f:
                        conn.sendall(bytes(f.read(), 'utf-8'))
                        conn.shutdown(socket.SHUT_RDWR) 
                        conn.close()
                except KeyError as e:
                    print("Missing manifest.xml key %s in page %s"%(e[0], resstr))
                    conn.sendall(b"500")
                    conn.shutdown(socket.SHUT_RDWR) 
                    conn.close()
            
            
                
