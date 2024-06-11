import json
import os
import modules as md
import atlassian.errors
import requests
from requests.auth import HTTPBasicAuth
from atlassian import Confluence
import urllib3
from html import escape


def update_confluence(template):
    # Global variable to use across function.
    global page_id
    page_id = str()

    # Disable API error warnings.
    urllib3.disable_warnings()

    # Confluence API user and token from Windows environments.
    username = os.getenv('WIKI_USER')
    token = os.getenv('CONFLUENCE_TOKEN')

    # Read config yaml file.
    data = md.readYaml('config.yaml')

    # Establish connection to confluence using user and token.
    confluence = Confluence(url="https://organisation.atlassian.net/wiki/", username=username, password=token,
                            verify_ssl=False, cloud=True)

    # Convert confluence template to confluence body data.
    string = '{}'.format(template)

    # Generate new confluence page.
    confluence_page_id = confluence.create_page(space='CONFLUENCE_SPACE', parent_id='PARENT_ID', body='',
                                                title='[XXX_{}] functional validation'.format(data['airline']))

    # Attach images to confluence.
    images_to_upload = os.listdir('Images')
    os.chdir('Images')
    for image in images_to_upload:
        confluence.attach_file(image, page_id=confluence_page_id['id'])

    # Update report
    confluence.update_page(page_id=confluence_page_id['id'], body=string, parent_id="PARENT_ID",
                           title='[Imperva_{}] functional validation'.format(data['airline']))

    print("Report updated https://Organisation.atlassian.net/wiki/spaces/SPACE/pages/{}".format(confluence_page_id['id']))

    # url_1 = "https://organisation.atlassian.net/wiki/api/v2/pages/"
    #
    # auth = HTTPBasicAuth(username=username, password=token)
    # headers = {"Accept": "application/json", "Content-Type": "application/json"}
    #
    # payload = (
    #     json.dumps({"spaceId": "spaceid", "title": "XXX test", "parentId": "parentid"})
    # )

    # response = confluence.get_page_by_id(page_id="pageid", expand="body.storage")
    # print(response)
    # response = requests.request(verify=False,
    #                             method="GET",
    #                             url=url_2,
    #                             headers=headers,
    #                             #data=payload,
    #                             auth=auth
    #                             )
