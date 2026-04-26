#--------------------------------------------------------------------------------------------
# This script concerns the content from Chapter 17 in Python Crash Course about Working with APIs
# APIs are application programming interfaces that request specific information from a website
# and do something with that information (like a visualization)
# This is helpful when you want to use current data to generate a visualization and ensure it's
# always up to date!
#----------------------------------------------------------------------------------------
# Import the requests library to make HTTP requests
import requests

# The URL of a public API that returns random cat facts in JSON format
url = "https://catfact.ninja/fact"

# Send a GET request to the API
response = requests.get(url)

# Convert the response JSON into a Python dictionary
data = response.json()

# Extract the 'fact' field from the dictionary
fact = data["fact"]

# Print the cat fact to the screen
print("Random Cat Fact:")
print(fact)
