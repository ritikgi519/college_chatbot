from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from chatbot import chatbot_response

app = Flask(__name__)
app.secret_key = "srms_secret_key"   # needed for login session

# ---- Login Page ----
@app.route("/login", methods=["GET", "POST"])
def login():
    print("Login route accessed", request.method)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(f"Received credentials - Username: {username}, Password: {password}")
        session["user"] = username
        print("Login successful")
        return redirect(url_for("home"))
    else:
        return render_template("login.html")

      


# ---- Chatbot Home ----
@app.route("/")
def home():
    # only allow after login
    if "user" in session:
        return render_template("index.html")
    return redirect(url_for("login"))


# ---- Chatbot API ----
@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.json.get("message")
    response = chatbot_response(user_msg)
    return jsonify({"reply": response})


# ---- Logout ----
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
