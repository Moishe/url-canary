import hashlib
import requests
import time

path = 'https://www.epa.gov/climatechange/climate-change-basic-information'

print "This script will exit with a code of 1 if the page at %s changes." % path

previous_hash = None
while True:
    response = requests.get(path)
    if response.status_code != 200:
        print "Error: "
        print response
        exit(1)

    response_hash = hashlib.sha224(response.text.encode('utf-8')).hexdigest()

    if previous_hash:
        if response_hash != previous_hash:
            print "Hash changed."
            exit(1)
    else:
        previous_hash = response_hash

    time.sleep(60)
