import requests

def fetch_random_user_freeqpi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch data from FreeAPI")
    
def main():
    try:
        username, country = fetch_random_user_freeqpi()
        print(f"Random User from FreeAPI:\nUsername: {username}\nCountry: {country}")
    except Exception as e:
        print(f"Error: {e}")
    

if __name__ == "__main__":
    main()