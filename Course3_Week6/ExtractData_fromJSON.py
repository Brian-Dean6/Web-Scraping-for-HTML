import json
import urllib.request
import ssl 

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
ssl._create_default_https_context = ssl._create_default_https_context = ssl._create_unverified_context

url = "https://py4e-data.dr-chuck.net/comments_1824171.json"  # Replace with the actual URL containing the JSON data

try:
    # Fetch JSON data from the URL
    with urllib.request.urlopen(url) as response:
        data = response.read().decode()

    # Load JSON data
    json_data = json.loads(data)

    # Extract the "count" values as a list
    count_values = [item['count'] for item in json_data['comments']]

    # Calculate the sum of "count" values
    sum_of_counts = sum(count_values)

    print('Sum of "count" values:', sum_of_counts)

except urllib.error.URLError as e:
    print(f"Error fetching data from the URL: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON data: {e}")
