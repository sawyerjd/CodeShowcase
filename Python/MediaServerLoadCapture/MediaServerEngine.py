import requests, json, datetime, time, csv
from requests.auth import HTTPDigestAuth
#import json, datetime, time, csv

keyName = 'avgAverageLoad'
fileName = 'capture'
server = 'ServerName'
port = '8102'

# Function that sends the GET request to the server and
# returns the JSON response decoded in utf-8
def get_request(param,username,password):

    response = requests.get('http://' + server + ':' + port + '/api/v1/server/' + param,auth=HTTPDigestAuth(username, password), verify=True)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

# Create the CSV file and add the header row
with open(fileName + '.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['time', 'load'])
    csvfile.close()

# Every 10 seconds, get parameter of interest and append the value and time to a CSV file
while True:

    # Call get-request function and pass in parameter of interest and creds
    data = get_request('enginestatus', 'apiusername', 'apipassword')

    # Get current time in H:M:S format
    currentDateTime = datetime.datetime.now()
    capTime = currentDateTime.strftime('%H:%M:%S')

    # Open CSV file and write time and parameter value
    with open(fileName + '.csv', 'a+', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([capTime, data[keyName]])
        csvfile.close()

    # Also print the parameter value to terminal
    print(data[keyName])

    time.sleep(5)
