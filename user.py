import requests

def get_user():
    try:
        url =  "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)
        users = response.json()

        user_details = []
        for user in users:
            if user["address"]["city"].startswith("S"):
                user_details.append({
                    "id": user["id"],
                    "name": user["name"],
                    "username": user["username"],
                    "email": user["email"],
                    "city": user["address"]["city"]
                })
        return user_details
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching:{e}")
        return []
    
if __name__ == "__main__":
    users = get_user()

    if users:
        for user in users:
            print(f"User {user['id']}:")
            print(f" Name: {user['name']}")
            print(f" Username: {user['username']}")
            print(f" Email: {user['email']}")
            print(f" City: {user['city']}")
            print("------------------------")
    else:
        print("No users found in cities starting with 'S'.")
