import os
from pathlib import Path
import time
import subprocess
import sys
import sys
external_module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app'))

# Add the external module directory to the Python path
sys.path.append(external_module_path)


# system path
print("Systmen Path:", sys.path)


# Get the current working directory
current_directory = os.getcwd()

# Print the current working directory
print("Current Working Directory:", current_directory)
# Get a list of files in the current directory
files_in_directory = os.listdir(current_directory)

# Print the list of files
print("Files in the current directory:")
for file in files_in_directory:
    print(file)


# from app.app.profiles.models import UserProfile
# subprocess.run(["pip", "install", "requests"])

import requests

# API_URL=f"http://app:8000/api/recommendations/calculate_similarity/2/"
BASE_API_URL = "http://app:8000/api/recommendations/calculate_similarity/"

def fetch_and_process_data():
    try:
    
        # user_ids_to_process = UserProfile.objects.filter(similarity_calculation_done=False).values_list('user_id', flat=True)
        user_ids_to_process=[3]
        print("++++++++++user_id_to_process+++++++++++++++++++",user_ids_to_process)
        for user_id in user_ids_to_process:
            # Construct the API URL with the current user ID
            api_url = f"{BASE_API_URL}{user_id}/"

            # Call your API
            print("+++++++++++++before call++++++++++++++++")
            response = requests.get(api_url)

            # Check the HTTP status code
            if response.status_code == 200:
                # Process the response data (add your logic here)
                data = response.json()
                print(data)
            else:
                print(f"++++++++Error: Unexpected status code {response.status_code}")


    except requests.ConnectionError as e:
        print(f"Error: Unable to connect to the API. {e}")
    except requests.RequestException as e:
        print(f"Error: Request failed. {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred. {e}")

if __name__ == "__main__":
    while True:
        print("+++++++++++++++++++++++++++++++++SERVICE CALL HAPPEN++++++++++++++++++++++++++++++++++++++")
        fetch_and_process_data()
        time.sleep(5)  # Sleep for 1 hour (adjust as needed)
