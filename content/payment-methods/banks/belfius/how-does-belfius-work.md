---
title: "Belfius, How does it work?"
weight: 21
meta_title: "Belfius, how does it work? - Multisafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
## How does it work?
Belfius is similar to other online banking payment methods.<br>

A customer chooses to pay with Belfius, authenticates their account, and confirms the payment.

>_Belfius payments can only be processed on our new payment page starting with [PayV2](/tools/payment-pages/what-is-payv2/)._


### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized  | Initialized  | A payment link has been generated, but no payment has been received yet.   |
| Completed   | Completed   | A successful Belfius transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 

#### Refund flow 

| Order Status                      | Transactoin Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Reserved       | Reserved    | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 

The full API reference for Belfius can be found [here](/api/#belfius).

Please note that successful Belfius payments that are not finalized by pressing the return to shop button will not be updated on our end, resulting in the transaction status NOT changing from _initialized_. However, we import our bank statements daily and all incoming payments which have not yet been completed will then be finalized.


### Product rules
Some rules may apply to certain payment methods. For Belfius, the following rules apply:

* Refunding more than the stated amount of the original transaction is possible with Belfius. More information available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount/) page

* Successful Belfius transactions have no expiring date regarding refunding, as long as the receiving bank is able to process the refund

* Payments done through Belfius are processed in [Euros (EUR)](/faq/general/which-currencies-are-supported-by-multisafepay/)

* The lifetime of a payment link can be adjusted. This might be beneficial for your inventory. The adjustment can be processed through the days or seconds active.   
Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link/) FAQ page.<br>







