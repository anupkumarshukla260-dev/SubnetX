from flask import Flask, render_template, request
import subprocess
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():

    ip = request.form.get("ip", "")
    cidr = request.form.get("cidr", "")

    # Run your original Python file
    result = subprocess.run(
        [sys.executable, "subnet.py"],
        input=f"{ip}\n{cidr}\n",
        capture_output=True,
        text=True
    )

    output = result.stdout

    if result.returncode != 0:
        output = "Error: " + result.stderr

    return render_template(
        "index.html",
        result=output,
        ip=ip,
        cidr=cidr
    )


if __name__ == "__main__":
    app.run(debug=True)