# CHACKING THE CITIES AND THEIR COUNTRIES.
city_country= {                      # Dictionary of cities and their countries
    "mumbai": "India",
    "chennai": "India",
    "delhi": "India",
    "new york": "USA",
    "los angeles": "USA",
    "chicago": "USA",
    "london": "UK",
    "manchester": "UK",
    "paris": "France",
    "lyon": "France",
}
city1 = input("Enter the first city: ").strip().lower()    #strip is used to remove any whitespace charaters.
city2 = input("Enter the second city: ").strip().lower()   #lower is used to covert the string to lowercase.

if city1 in city_country and city2 in city_country:   #checking if both cities are in the dictionary.
    country1 = city_country[city1]                    #getting the country of the first city.
    country2 = city_country[city2]                    #getting the country of the second city.

    if country1 == country2:                          #checking if both cities are in the same country.
        print(f"Both cities are in {country1}.")
    else:
        print(f"{city1.title()} is in {country1} and {city2.title()} is in {country2}.")    
        #title is used to convert the first character of each word to uppercase.
else:
    print("One or both cities are not in the database.")     # cities are not in dictionary.

#--------------------------------OUTPUT-----------------------
#Enter the first city: DELHI
#Enter the second city: LONDON
#Delhi is in India and London is in UK.