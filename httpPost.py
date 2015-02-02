import json
import urllib
import urllib2

url = "http://104.236.95.188/user/create"

data = {
	'name': 'admin',
	'email': 'admin@gmail.com',
	'password': 'admin',
	'mobile': '88949'
}

headers = {'Content-Type': 'application/json'}

d = urllib.urlencode(data)
da = json.dumps(data)

req = urllib2.Request(url, da, headers)
response = urllib2.urlopen(req)
page = response.read()
print page