---
title : "How do I set-up my Exact Online platform?"
meta_title: "FAQ Finance - Exact Online - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: "."
---

In order to be able to import an accountant export from your MultiSafepay Control into your Exact Online account, you will need to provide an additional international bank account number (IBAN). However, bear in mind that this is just for Exact to be able to process this kind of operation and the account number can therefore be a "dummy" account. 

## How to create a dummy IBAN

1. Go to https://www.ibancalculator.com/bic_und_iban.html 
2. Navigate to the _Calculate an IBAN_ field
3. Select the Netherlands as country
4. Choose any option for a bank (e.g. ING Bank)
5. Fill in any 7 digits in the _Account number_ field
6. Click on calculate IBAN
7. A bank account number (IBAN) and BIC will be generated

## How to process a dummy IBAN in Exact Online platform

1. Navigate to _Financial -> Banking & Cash -> Bank accounts -> Overview_
2. Click _New_
3. Enter the dummy IBAN created before
4. Click _Save_

You have created a bank account. All transactions linked to this bank account number can now be registered.

## How to export MT940 files from MultiSafepay Control

1. Navigate to _Reports –> Accountant Export_ in your MultiSafepay Control
2. Select a range of dates from _Data Selection_
3. Select ‘MT940’ from the field _Report Type_
4. Click _Advanced options_
5. Fill in the dummy IBAN number at _Bank Account / IBAN_
6. Fill in the BIC code in the _BIC_ field

## Exact Online Import Instructions

1. Log into your Exact Online account and go to _Financial -> Banking & Cash -> Statements -> Import_
2. Click _Choose File_ and select the MT940 file you want to upload
3. Click _Import_


Exact Online and Exact Globe can both perfectly import and match our MT940 report if:

- your accounting package supports the processing of MT940 files _(bank statements)_.
- the order numbering that appears in the exported accountant files (eg 200160526), also appears in the correct invoice fields in your accounting platform.
- the customer's name and the order amounts that appear in the exported accountant files correspond to those in your accounting platform,

_Exact Basic / Standard package does not support the MT940 import function, at least Exact Advanced version is required to import an MT940 report_.

_Lightspeed users must require Lightspeed to perform an adjustment to make sure the order number appears in the correct field in Exact for it to be matched with our MT940_.
