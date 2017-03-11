# BitcoinBalanceCheck

**What is the script about?**

The script allows to check the Bitcoin balance of one or more addresses at a specific time. It let you check the current balance or the balance at one time in the past.

**How it works?**

```python bitcoin.py <mandatory: path to address file> <optional: date in form of DD-MM-YYYY>```

for example: 
```python bitcoin.py address.txt 01-01-2016```

It gives the balance on 1st January 2016 of all addresses listed in address.txt file

If you do not provide a date then the current balance is given back.

