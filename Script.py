import requests
from bs4 import BeautifulSoup

# URL of the Election Commission of India results page
url = "https://results.eci.gov.in/PcResultGenJune2024/partywiseleadresultState-544.htm"

# Send a GET request to the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Extract data about BJP's seat count
    # Using the appropriate HTML identifiers from the actual website
    bjp_seats = soup.find('td', text='Bharatiya Janata Party').find_next_sibling('td').text.strip()

    # Extract other required data similarly by identifying the appropriate HTML elements and attributes
    inc_seats = soup.find('td', text='Indian National Congress').find_next_sibling('td').text.strip()
    sp_seats = soup.find('td', text='Samajwadi Party').find_next_sibling('td').text.strip()
    tmc_seats = soup.find('td', text='All India Trinamool Congress').find_next_sibling('td').text.strip()
    dmk_seats = soup.find('td', text='Dravida Munnetra Kazhagam').find_next_sibling('td').text.strip()

    # Print the extracted data
    print(f"BJP Seats: {bjp_seats}")
    print(f"INC Seats: {inc_seats}")
    print(f"SP Seats: {sp_seats}")
    print(f"TMC Seats: {tmc_seats}")
    print(f"DMK Seats: {dmk_seats}")

else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
