from flask import Flask

app=Flask(__name__)

@app.route("/members")
def members():
    return {"members": ["test 1", "test 2", "test 3"]}

if __name__ == "__main__":
    app.run(debug=True)