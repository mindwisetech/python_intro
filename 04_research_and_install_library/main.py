import requests

def main():
    url = "https://api.github.com"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises error for bad status
        data = response.json()

        print("GitHub API info:")
        print(f"Current user URL: {data['current_user_url']}")
        print(f"Repository URL: {data['repository_url']}")
        print(f"Search URL: {data['user_search_url']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
