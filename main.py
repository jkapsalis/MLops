from AdzunaClient.client import fetch_job_listings, parse_response


def main():
    # Users input
    print("Welcome to the Job Search App!")
    app_id = '<YOUR_APP_ID>'
    app_key = '<YOUR_APP_KEY>'
    search_query = input("Enter the job title you are looking for: ")
    location = input("Enter the location: ")

    try:
        #   i   call here the  fetch_job_listings
        response_data = fetch_job_listings(app_id, app_key, search_query, location)

        # print the response of the data
        parse_response(response_data)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
