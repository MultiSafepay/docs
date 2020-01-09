---
title : "How to test Recurring Payments?"
weight: 55
meta_title: "Recurring Payments, how to test them? - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
To test recurring payments on your staging environment, email our Integration Team at <integration@multisafepay.com> with the request to enable it in your 
[MultiSafepay Test Control](https://testmerchant.multisafepay.com/).


##### SEPA Direct Debit

MultiSafepay provides a test platform for SEPA Direct Debit transactions. By entering a test IBAN you will be able to simulate the outcome of the transaction.

| **IBAN** | **Status** | **Description** |
---|---|---
NL87ABNA0000000001 | Initialized/Completed | Transaction is Initialized (after 2 minutes it is Completed)
NL87ABNA0000000002 | Initialized/Declined | Transaction is Initialized (after 2 minutes it is Declined)
NL87ABNA0000000003 | Initialized/Uncleared/Completed | Transaction is Initialized ( after 2 minutes it is Uncleared, and 1 minute later it is Completed)
NL87ABNA0000000004 | Initialized/Uncleared/Declined | Transaction is Initialized ( after 2 minutes it is Uncleared, and 1 minute later it is Declined)
