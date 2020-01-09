---
title : "How do I set-up my Exact Online platform?"
meta_title: "FAQ Finance - Exact Online - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: "."
---

In order to be able to import an accountant export from your MultiSafepay Control into your Exact Online account, you will need to provide an additional international bank account number (IBAN). However, bear in mind that this is just for Exact to be able to process this kind of operation and the account number can therefore be a "dummy" account. 

## How to "create" a dummy IBAN

1. Go to https://www.ibancalculator.com/bic_und_iban.html 
2. Navigate to the _Calculate an IBAN_ field
2. Select the Netherlands as country
3. Choose any option for a bank (e.g. ING Bank)
4. Fill in any 7 digits in the _Account number_ field
5. Click on calculate IBAN
6. A bank account number (IBAN) and BIC will be generated

## How do I process the bank account number in my Exact Online platform?

1. Go to bank accounts in your Exact Online platform
2. Click new
3. Select payment service provider as type
4. Enter the full international bank account number
5. Synchronize by selecting the ING bank
6. Click save

You have created a bank account. All transactions linked to this bank account number can now be registered.

Exact Online and Exact Globe can both perfectly import and match our MT940 report if:

- your accounting package supports the processing of MT940 files _(bank statements)_.
- the order numbering that appears in the exported accountant files (eg 200160526), also appears in the correct invoice fields in your accounting platform.
- the customer's name and the order amounts that appear in the exported accountant files correspond to those in your accounting platform,

_Exact Basic / Standard package does not support the MT940 import function, at least Exact Advanced version is required to import an MT940 report_.

_Lightspeed users must require Lightspeed to perform an adjustment to make sure the order number appears in the correct field in Exact for it to be matched with our MT940_.
