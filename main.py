from flask import Flask, jsonify
import db_nav
import requests


# Declare db
DB = db_nav.CRUD()


@app.route('/test')
def test():
    entry = DB.read(["user", "systemlogon"], username="miguelin")
    return jsonify(name=entry.name)


if __name__ == "__main__":
    print("running")
    app.run(debug=True, port=5001)
