#adzuna api requires specific parameters to retrieve specific job
#listings such as api key api id and the search criteria
#

import json

import requests


def fetch_job_listings(app_id: str, app_key: str, search_query: str, location: str, country: str = 'us') -> dict:
    base_url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/1"
    parameters = {
        'app_id': app_id,
        'app_key': app_key,
        'what': search_query,
        'where': location,
        'content-type': 'application/json'
    }
    response = requests.get(base_url, params=parameters)
    return response.json()

def parse_response(response: dict):
    if 'results' in response:
        for job in response['results']:
            job_title = job.get('title', 'N/A')
            company = job.get('company', {}).get('display_name', 'N/A')
            location = job.get('location', {}).get('display_name', 'N/A')
            print(f"Job Title: {job_title}, Company: {company}, Location: {location}")
    else:
        print("No results found or an error occurred.")


# just a try to see the parameters
app_id = '<a0ff5860>'
app_key = '<b41cc7051c7cc0919b2559035475c370>'
search_query = 'Software Developer'
location = 'New York'


response_data = fetch_job_listings(app_id, app_key, search_query, location)
parse_response(response_data)
