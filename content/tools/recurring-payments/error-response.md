---
title : "Error as response"
weight: 56
meta_title: "Recurring Payments, Error as response - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
In some cases it may occur that an error is received as response on the recurring payment transaction request. In most cases this is a 1000 error.

### 1000 Error explained
Transaction not allowed. 

Payment method is disabled or not available. Contact our Integration Team at <integration@multisafepay.com> to validate and/or check the settings in your MultiSafepay Control. 

### Causes 
A 1000 error indicates that MultiSafepay does not allow the payment. The payment is blocked due to fraud or other settings set in your MultiSafepay Control.

**Fraud**\
In exceptional cases, the customer's data may have been added as fraud in our fraud filter system. This could be the address details or the bank account number linked to the recurring_id.

**Example:**\
If a bank account is blocked, credit card is marked as stolen or perhaps fraud has occurred on the address of the customer, the data will be stored in the fraud filter of MultiSafepay. This may result in declining the transaction on certain data. 

**Settings:**\
Another reason why a 1000 error may occur, may be because of certain settings that are set in your MultiSafepay Control that will not allow the payment to go through. Processing recurring payments needs to be approved and enabled by our Risk Team. 

**Example:**\
Enabling recurring payment will allow you to collect the amount of a customers bank account once every 24 hours. If the same recurring_id or customer data is used again within 24 hours, it will result in a 1000 error as response. 

**If any advice or assistance is needed, contact our Integration Team at <integration@multisafepay.com>.**











