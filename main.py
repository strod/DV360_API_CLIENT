from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import discovery
import json

scopes = [
    'https://www.googleapis.com/auth/display-video', 
    'https://www.googleapis.com/auth/dfatrafficking', 
    'https://www.googleapis.com/auth/doubleclickbidmanager'
]
client_secret_path = "./OAuth/client_secret_rt.json"

ADVERTISER_ID = '586578177'  #@param {type:"string"}
CREATIVE_ID = '472341983'

# For use with legacy DBM API
SDF_VERSION = '5.3'  #@param {type:"string"}

# For use with DV360 API
SDF_VERSION_DV360 = 'SDF_VERSION_5_3'  #@param {type:"string"}



if __name__ == "__main__":

    # Set up a flow object to create the credentials using the
    # client secrets file and OAuth scopes.
    credentials = InstalledAppFlow.from_client_secrets_file(
        client_secret_path, 
        scopes).run_local_server()

    # Build the discovery document URL.
    discovery_url = f'https://displayvideo.googleapis.com/$discovery/rest?version=v2'

    # Build the API service.
    service = discovery.build(
        'displayvideo',
        'v2',
        discoveryServiceUrl=discovery_url,
        credentials=credentials)

    # Build advertisers.list request.
    request = service.advertisers().creatives().list(
        advertiserId=ADVERTISER_ID, orderBy="createTime desc")

    # Execute request.
    response = request.execute()

    # Print response.
    with open("response.json", "w") as file:
        json.dump(response, file, indent=4)
    
    # Get the media file
    # resourceName = response['name']
    # media_request = service.media().download_media(resourceName=resourceName)
    # media_response = media_request.execute()

    # with open("media_response.json", "w") as file:
    #     json.dump(media_response, file, indent=4)

    # if len(response['advertisers']) > 0:
    #     for advertiser in response['advertisers']:
    #         print(f'ID: {advertiser["advertiserId"]} Display Name: {advertiser["displayName"]}')
    # else:
    #     print('No advertisers found.')