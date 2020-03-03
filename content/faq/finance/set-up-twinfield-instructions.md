---
title : "How do I set-up my Twinfield platform?"
meta_title: "FAQ Finance - Twinfield - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: "."
---

In order to be able to import an accountant export from your MultiSafepay Control into your Twinfield account, you will need to provide an additional international bank account number (IBAN). However, bear in mind that this is just for Twinfield to be able to process this kind of operation and the account number can therefore be a "dummy" account. 

## How to "create" a dummy IBAN

1. Go to https://www.ibancalculator.com/bic_und_iban.html 
2. Navigate to the _Calculate an IBAN_ field
3. Select the Netherlands as country
4. Choose any option for a bank (e.g. ING Bank)
5. Fill in any 7 digits in the _Account number_ field
6. Click on calculate IBAN
7. A bank account number (IBAN) and BIC will be generated

## MultiSafepay Accountant Export

1. Navigate to _Reports_ --> _Accountant Export_ in your MultiSafepay Control
2. Select a range of dates from _Data Selection_
3. Select 'MT940' from the field _Report Type_
4. Select Twinfield from _Special Format_
5. Fill in the dummy IBAN number at _Bank Account / IBAN_
6. Fill in the BIC code in the _BIC_ field

## Twinfield Import Instructions

1. Log into your Twinfield account and select the _Cash & Banks_ section in the menu
2. Select _Cash & Banks_ one more time
3. Insert a new code in the _Code_ line, give it a e.g. name MSPAY and press _Next_
4. Fill in the required details as Account number, Account name, IBAN, BIC, General ledger account
5. Go back to the main _Cash & Banks_ section and select _Drag and drop bank statements or Browse_
6. Upload the MT940 statement generated in MultiSafepay Control