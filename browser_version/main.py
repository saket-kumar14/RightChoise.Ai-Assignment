import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
def get_user():
    try:
        url =  "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)
        users = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching: {e}")
        return []

    user_details = [{
        "id": user["id"],
        "name": user["name"],
        "username": user["username"],
        "email": user["email"],
        "city": user["address"]["city"]
        } 
        for user in users
        if user["address"]["city"].startswith("S")
        ]

    return render_template('index.html', users=user_details)


if __name__ == "__main__":
    # get_user()
    app.run(debug=True)