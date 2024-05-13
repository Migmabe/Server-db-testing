from flask import Flask, jsonify, request
import db_nav


# ----------LIST TO DICT CONVERTER----------#

def to_dict(list_item):
    dict_ = {}
    k = 1
    for _ in list_item:
        dict_[f"user{k}"] = _
        k += 1
    return dict_

# -----------END--------------------#

app = Flask(__name__)

# Declare db
DB = db_nav.CRUD()


# This route redirects the user to the resource that returns filtered data from either database
# depending on the db selection
@app.route(
    '/<string:database>/<string:search_parameter>')  # example http://127.0.0.1:5001/users/username?value=miguelin
def user_locator(database, search_parameter):
    flask_query = request.args.get("value")
    # Now handle the request by selecting the search method
    if database == "users":
        if search_parameter == "username":
            entry = DB.read(database, username=flask_query)  # all returns a list with all the hits
            json_object = jsonify(user={
                "name": entry.name,
                "username": entry.username,
                "accountType": entry.accountType
            })
            return json_object
        elif search_parameter == "name":
            entry = DB.read(database, name=flask_query).all()
            json_object = jsonify(to_dict(entry))
            return json_object


if __name__ == "__main__":
    app.run(debug=True, port=5001)
