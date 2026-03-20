from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Compose with ENV is running 🚀"

@app.route("/db")
def db_test():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT")
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f"Database version: {db_version}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)