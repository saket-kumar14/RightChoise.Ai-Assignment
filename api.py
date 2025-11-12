import requests

def get_user():
    try:
        url =  "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)
        users = response.json()
    except requests.exceptions.RequestException as e:
        print("Error while fetching:{e}")
        return []

    user_details = [{
        "name": user["name"],
        "username": user["username"],
        "email": user["email"],
        "city": user["address"]["city"]
        } 
        for user in users
        if user["address"]["city"].startswith("S")
        ]

    # print(user_details)
    if user_details:
        for i,user in enumerate(user_details, start=1):
            print(f"User {i}:")
            print(f" Name:{user['name']}")
            print(f" Username:{user['username']}")
            print(f" Email:{user['email']}")
            print(f" City:{user['city']}")
            print("------------------------")
    else:
        print("No users found")

get_user()