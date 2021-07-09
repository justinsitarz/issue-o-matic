import requests
import json
import base64
from requests.auth import HTTPBasicAuth


site = '<your site name here>'
url = 'https://{}.atlassian.net/rest/api/3/issue'.format(site)

user = '<your user email address here>'
token = '<your api token here' # generate one here: https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/
b_auth = base64.b64encode(bytes('{}:{}'.format(user, token), 'utf-8'))
auth = b_auth.decode('utf-8')
number_of_issues = 100

headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Basic {}'.format(auth)}


for x in range(number_of_issues):
	body = {"fields":{"summary":"My summary","issuetype":{"name": "Task"},"project":{"key":"OP8"}}}
	res = requests.post(url, data=json.dumps(body), headers=headers)
	print(res.json())
