# The software is released under MIT License.
#
# Copyright 2017 github.com/ptrk01
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software # without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to # permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A #PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF #CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import urllib
import json
import time
import datetime
import sys
import os.path

if len(sys.argv) < 2:
    sys.exit("ERROR: Please provide a file with addresses")
elif len(sys.argv) > 3:
    sys.exit("ERROR: Invalid input arguments")

file = sys.argv[1]
if os.path.isfile(file) is False:
    sys.exit("ERROR: File does not exist")

date = "31-12-9999"
if len(sys.argv) == 3:
    date = sys.argv[2]
    
try:
    datetime.datetime.strptime(date, '%d-%m-%Y')
except ValueError:
    sys.exit("ERROR: Incorrect data format, should be DD-MM-YYYY")

addresses = [line.rstrip('\n') for line in open(file)]

print "Calculation is running . . ."

fixDate = time.mktime(datetime.datetime.strptime(date, "%d-%m-%Y").timetuple())
url = "https://api.blockcypher.com/v1/btc/main/addrs/"
balances = {}

for address in addresses:
    time.sleep(1)
    balances[address] = 0
    lastDate = 0
    result = json.load(urllib.urlopen(url + address))
    try:
        transactions = result["txrefs"]
    except KeyError:
        print result
    for i in range(len(transactions)):
        ts = time.strptime(transactions[i]["confirmed"][:19], "%Y-%m-%dT%H:%M:%S")
        txDate = time.mktime(datetime.datetime.strptime(time.strftime("%m-%d-%Y", ts), "%m-%d-%Y").timetuple())

	if txDate < fixDate and lastDate < transactions[i]["confirmed"]:
       		balances[address] = transactions[i]["ref_balance"]
                lastDate = transactions[i]["confirmed"]

totalBalance = 0    
for k, v in balances.iteritems():
    totalBalance += v
    print "%s %f" % (k, v/100000000.0)

if date <> "31-12-9999":
	print "Total balance on %s was %f Bitcoin" % (date, totalBalance/100000000.0)
else:
	print "Total current balance is %f Bitcoin" % (totalBalance/100000000.0)