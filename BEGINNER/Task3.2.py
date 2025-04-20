# CHECKING IF CITY BELONGS TO A COUNTRY
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
Uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
city = input("Enter a city name: ").strip()   
#strip is used to remove any whitespace charaters in the

# Checking which country the city belongs to
if city in Australia:
    print(f"{city} is in Australia")  # f is used to format the string.
elif city in Uae:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print(f"Sorry, I don't recognize the city '{city}'")

#-----------------------OUTPUT-----------------------
#Enter a city name: Sydney
#Sydney is in Australia