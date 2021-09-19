from json.decoder import JSONDecodeError
import urllib, json
from urllib import request,error

# http://climatedataapi.worldbank.org/climateweb/rest/v1/country/annualavg/tas/1980/1999/USA.json

def get_temperature(self, monannul, start, end, iso) -> str:
        """
        Get the temperature from the API.

        Returns the JSON of temperature statistics.
        """
        #This is converting a username into a UUID which is how Minecraft differentiates between players
        url = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/' + monannul + '/tas/' + start + end + iso + '.json'
        try:

            response = urllib.request.urlopen(url)
            json_results = response.read()
            try:
                r_obj = json.loads(json_results)
                uuid = r_obj['id']
                return uuid
            except JSONDecodeError:
                return "none"
        
        except urllib.error.HTTPError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e.code))
        
        except urllib.error.URLError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e))
            print("Perhaps you have no internet connection?")