import socket
import json
from flask import Flask, request, send_from_directory, redirect, render_template, Markup
import os

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 5000))
host = "127.0.0.5"
port = 2345

@app.route("/site")
def site():
    path = request.args.get("path")
    resstr = ""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(bytes(path, 'utf-8'))
            resstr = ""
            while True:
                res = s.recv(1024)
                if (len(res) <= 0):
                    break
                resstr += res.decode("utf-8")
            s.close()
        if (resstr == "404"):
            return render_template("404s.html")
        elif (resstr == "500"):
            return render_template("500s.html")
        else:
            return resstr
    except ConnectionRefusedError as e:
        print(e)
        return render_template("503s.html")
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
