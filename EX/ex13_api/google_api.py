"""
EX13 - API.

This program creates a single playlist based on array of YouTube playlists in Google Spreadsheet.

"""


import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_links_from_spreadsheet(id: str, token_file_name: str) -> list:
    """
    Return a list of strings from the first column of a Google Spreadsheet with the given ID.

    Example input with https://docs.google.com/spreadsheets/d/1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M
        get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json')

    Returns
        ['https://www.youtube.com/playlist?list=PLPszdKAlKCXUhU3r25SOFgBxwCEr-JHVS', ... and so on]

    :param id: spreadsheet id to fetch strings from
    :param token_file_name: the name of the file where access token is fetched from
    :return: list full url-s to YouTube playlist resources
    """
    # For auth.
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    # User credentials are stored in specified which will be generated automatically after first authorisation.
    # Initially there are no credentials.
    credentials = None
    if os.path.exists(token_file_name):
        credentials = Credentials.from_authorized_user_file(token_file_name, scopes)
    # If there are no (valid) user credentials available, user must log in.
    if not credentials or not credentials.valid:
        # If the access token is expired and can be refreshed, refresh.
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            # Otherwise prompt user to log in.
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes)
            credentials = flow.run_local_server(port=0)
            # Save the user credentials for the next time into specified file.
            with open(token_file_name, "w") as token:
                token.write(credentials.to_json())
    try:
        # Establish connection with sheets API version 4 using application credentials.
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()
        # Fetch the cell values from the A column, first sheet of the spreadsheet defined using its id.
        result = sheets.values().get(spreadsheetId=id, range="Sheet1!A:A").execute()
        values = result.get("values", [])

        if not values:
            print("No content found.")
            return []
        # Since every row is a list with one value itself, unpack them.
        values = [f"https://www.youtube.com/playlist?list={value[0]}" for value in values]
        return values

    except HttpError as err:
        print(err)


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """
    Return a list of links to songs in the YouTube playlist with the given address.

    Example input
        get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                'ThisIsNotARealKey_____ThisIsNotARealKey')

    Returns
        ['https://youtube.com/watch?v=r_It_X7v-1E', 'https://youtube.com/watch?v=U4ogK0MIzqk', ... and so on]

    :param link:
    :param developer_key:
    :return:
    """
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    list_of_links = []
    # For getting results from all pages not only from the first.
    next_page_token = ""

    # Create something similar like "do while loop" is in JavaScript.
    # For that create a loop which looks like infinite, but break it conditionally from the inside.
    while True:
        # The following part of the code runs at least once.
        playlist_id = link.lstrip("https://www.youtube.com/playlist?list=")
        youtube = build(api_service_name, api_version, developerKey=developer_key)
        request = youtube.playlistItems().list(part="contentDetails", playlistId=playlist_id, pageToken=next_page_token)
        response = request.execute()
        for item in response["items"]:
            list_of_links.append(f"https://www.youtube.com/watch?v={item['contentDetails']['videoId']}")
        # Check whether the response has a next page token to use.
        if "nextPageToken" in response:
            next_page_token = response["nextPageToken"]
        # If there is no next page set the token empty. This is important for breaking the loop.
        else:
            next_page_token = ""
        # If there is no next pae break the loop.
        if not next_page_token:
            break
    return list_of_links


if __name__ == "__main__":
    import json

    key = ""
    spreadsheet_id = ""
    spreadsheet_data = []
    final_links = []

    # Not committing my credentials so loading them in from files.
    with open("api_key.json", "r") as api_key:
        key += json.load(api_key)["key"]
    with open("spreadsheet.txt", "r") as spreadsheet:
        for line in spreadsheet:
            spreadsheet_data.append(line.strip())
    spreadsheet_id = spreadsheet_data[0]

    # First load list of playlists from spreadsheet.
    list_of_playlists = get_links_from_spreadsheet(spreadsheet_id, "token.json")
    # Printing them out just for testing purposes.
    print(list_of_playlists)
    # Then extract the video links from each playlist.
    for playlist in list_of_playlists:
        final_links.extend(get_links_from_playlist(playlist, key))
    # Then print out the list of videos.
    print(final_links)
