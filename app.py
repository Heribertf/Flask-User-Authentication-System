from flask import Flask, render_template, request, redirect, flash, session
import bcrypt
import pyodbc
import secrets
from db_connection import get_db_connection

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route("/")
def index():
    if "user" in session:
        return redirect("/home")
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT PasswordHash FROM Users WHERE Username = ?", (username,))
            user = cursor.fetchone()

            if user:
                stored_password_hash = user[0]
                if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
                    session["user"] = username
                    return redirect("/home")
                else:
                    flash("Invalid password.", "danger")
            else:
                flash("Username not found.", "danger")
        except Exception as e:
            flash(f"An error occurred: {e}", "danger")
        finally:
            cursor.close()
            conn.close()

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


            cursor.execute(
                "INSERT INTO Users (Username, PasswordHash) VALUES (?, ?)",
                (username, password_hash)
            )
            conn.commit()
            flash("Registration successful! Please log in.", "success")
            return redirect("/login")
        except pyodbc.IntegrityError:
            flash("Error: Username already exists.", "danger")
        except Exception as e:
            flash(f"An error occurred: {e}", "danger")
        finally:
            cursor.close()
            conn.close()

    return render_template("register.html")

@app.route("/home")
def home():
    if "user" not in session:
        return redirect("/")
    return render_template("home.html", username=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully.", "info")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
