---
title: "Second Chance, How it works"
weight: 61
meta_title: "Second Chance, How it works - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
When a customer initiates a payment, but does not finish it for any reason, MultiSafepay will send a Second Chance reminder email. Included in these emails, there is a payment link that will allow the customer to finalize the payment. The first Second Chance email is sent after **1 hour** and the second after **24 hours** after the initial transaction was started.

_**A Second Chance email can be sent as long as the email address of the customer is included in the transaction request.**_

## When is the Second Chance email excluded?

**Transaction status**         
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

The Second Chance email cannot be activated and/or sent to the customer when the transaction status of the original transaction states:

1. _Pending_
2. _Uncleared_
3. _Completed_.

**Excluded payment methods**      
Certain payments methods have a different flow and, as a result, the Second Chance email cannot be activated and/or sent to the customers. Below, you can find a list of all the exceptions:

1. [Klarna](/payment-methods/klarna/)
2. [Afterpay](/payment-methods/afterpay/)
3. [Betaalplan](/payment-methods/betaalplan/)
4. [Pay After Delivery](/payment-methods/pay-after-delivery/)
5. [Bank transfer](/payment-methods/bank-transfer/)
6. [Direct Debit](/payment-methods/direct-debit/).


## Altering the Second Chance configuration
At the moment you can not change the Second Chance email in the settings. The Second Chance email can only be either enabled or disabled. When enabled, the Second Chance will be sent twice within 24 hours and this cannot be adjusted (after 1 hour and after 24 hours).

The Second Chance email can be personalised through an email template. More information on how to personalize a Second Chance email is available in [Personalize the Second Chance email](/tools/second-chance/how-to-personalize-the-second-chance-e-mail/).


### External plugins 
When enabled, the Second Chance email can have a negative result if, for example, you use an external warehouse system. A simple cron may resolve a conflict between the Second Chance email and a warehouse system. However, it is not a stable solution in all situations. 

**Example:**        
When an order is cancelled in the webshop, an order can still be paid by Second Chance. This can be done within 30 days or within <i>days_active</i> / <i>second_active</i>. If an order is paid, we will reopen the order within the webshop. A warehouse system may already release the reservation on the order upon receiving a _cancelled_ status, or, in some cases, consider the _cancelled_ status to be permanent. As result, it may be, that the order is no longer available in stock. 

**The Second Chance email is also likely to cause an issue in combination with running an ERP system.** 

### How long is a Second Chance active?
The payment link added in the Second Chance email has the same lifetime as the original payment request and is by default 30 days. 


### Days and seconds active
When enabled, the Second Chance email will be sent once after 1 hour and once after 24 hours. This cannot be adjusted at this time. It is, however, possible to influence the life of the payment link by changing the parameters <i>days_active</i> and <i>second_active</i>. 

**Example 1:**      
When the days_active is set to 2, the payment link will automatically expire after the two days. The customer will not be able to complete the payment after the expired period. This ensures that the stock is reversed after the payment link expires.

**Example 2:**    
When the seconds_active is set within 84600 seconds (equivalent of 24 hours), the payment link supplied in the second Second Chance email will no longer be valid. The second Second Chance email is sent regardless and this cannot be changed. 

**When a payment link is set to expire within 24 hours and the Second Chance is enabled, the customer will receive an expired payment link in the Second Chance email.** 

More information on <i>days_active</i> and <i>second_active</i> is available on our FAQ page, [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link/).


<br>
