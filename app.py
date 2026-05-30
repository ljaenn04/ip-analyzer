from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_ip_info(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}")
        return r.json()
    except:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    info = None
    ip = ""
    if request.method == "POST":
        ip = request.form.get("ip")
        info = get_ip_info(ip)
    return render_template("index.html", info=info, ip=ip)

if __name__ == "__main__":
    app.run(debug=True)