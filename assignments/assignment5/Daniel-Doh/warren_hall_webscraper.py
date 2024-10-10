from bs4 import BeautifulSoup
import requests


def print_warren_hall_smoothies():
    '''
    Web scrapes a list of warren hall smoothies at Warren Hall
    '''
    response = requests.get('https://www.bu.edu/dining/location/warren/#menu')
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        all_smoothies = soup.find_all(
            "h3", class_="nutrition-title",  string=lambda text: "Smoothie" in text)
        for smoothie in all_smoothies:
            print(smoothie.text[0:-15])
    else:
        print("Failed to fetch the page:", response.status_code)


print_warren_hall_smoothies()
