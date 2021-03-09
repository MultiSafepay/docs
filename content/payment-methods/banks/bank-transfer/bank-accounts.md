---
title : "MultiSafepay local bank accounts for Bank transfers"
weight: 24
meta_title: "Bank transfer - Local bank accounts - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
aliases: [/payment-methods/bank-transfer/bank-accounts/]
---
## MultiSafepay local bank accounts for bank transfers

MultiSafepay has a local bank account available for European bank transfer used by customers. As a result, the customer can process the bank transfer in a familiar and faster way through a national bank account.

MultiSafepay offers national bank accounts for bank transfers of the following countries in their local currencies:

* Austria (EUR)
* Belgium (EUR)
* Czech Republic (CZK)   
* France (EUR)  
* Germany (EUR)
* Great Britain (GBP)
* Hungary (HUF)
* Italy (EUR)
* Netherlands (EUR)
* Poland (PLN)
* Portugal (EUR)
* Spain (EUR)

The cost for an international bank transfer and currency conversion will no longer be deducted from the customer's bank account.
The customer will pay the regular national fees charged by the customer's bank.

Please keep in mind that USD (Dollar) is not supported due to the very high transaction and conversion costs for the customer. 

## Email notifications

If you prefer to send payment instructions to the customer yourself, set the *disable_send_email* parameter to _false_ in the corresponding API call. In this case, MultiSafepay does not send the customer an email notification.
For more information please see our API documentation regarding [Bank transfer](https://docs.multisafepay.com/api/#direct-bank-transfer)

