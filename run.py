# need to allow module to import from requests
import requests

# this is how we set up our API
base_url = 'http://api.weatherapi.com/v1'
api_method = '/astronomy.json'
api_key = '9a58265ce66a444ab53202516240603'
city_name = 'Denver'

# & is how you separate query parameters 
request_url = f"{base_url}{api_method}?key={api_key}&q={city_name}"

print(request_url)

# this is how we make the request
res = requests.get(request_url)


# this is how we get the data from the request 

if res.ok:
    data = res.json()
    print(data)
    print(data['location']['name'])
    print(data['current']['temp_f'])
else:
    error = res.json()
    print(error['error']['message'])


