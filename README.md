# BitcoinBalanceCheck

**What is the script about?**

The script allows to check the Bitcoin balance of one or more addresses at a specific time. It let you check the current balance or the balance at one time in the past. 

**How it works?**

```python bitcoincheck3.py <mandatory: path to address file> <optional: date in form of DD-MM-YYYY>```

for example: 
```python bitcoincheck3.py address.txt 01-01-2016```

It gives the balance on 1st January 2016 of all addresses listed in address.txt file
The result looks like
![Result of balance check](http://i.imgur.com/iY7EoPL.png)

If you do not provide a date then the current balance is given back.

The repository contains two versions: 
- bitcoincheck2.py is compatible up to Python 2.7
- bitcoincheck3.py is compatible with Python 3.6 and 3.7 (it may be compatible with previous Python 3 versions)

*Note for developers: The script uses the API from blockcypher.com. If too many requests are made in a short time, the API of blockcypher.com sends timeout errors. Therefore a wait of one second was built in between the requests.*

