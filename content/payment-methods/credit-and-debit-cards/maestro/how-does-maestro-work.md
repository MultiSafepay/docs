---
title: "Maestro, How does it work?"
weight: 21
meta_title: "Maestro, how does it work? - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---
## How it works
Maestro payments are processed as a credit card payment. Therefore, credit card payments must be enabled within your MultiSafepay Control to process a Maestro payment. Submit your request to enable credit cards (Visa, Mastercard and Maestro) to your account manager or contact us at <sales@multisafepay.com>

A Maestro payment is always validated with the 3D secure code. 3D secure verification is deemed mandatory by Maestro.

### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

Maestro (debit card) transactions received by MultiSafepay will be processed through our fraud filter. The following statuses are important when receiving a Maestro payment:

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet. | 
| Completed   | Completed   | A successful Maestro transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Uncleared   | Uncleared   |  Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction/)
| Declined    | Declined    | Transaction has been rejected. [read more on credit card status 'declined'. What does this mean?](/faq/general/declined-status/) | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 
| 


#### Refund flow 

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Reserved       | Reserved    | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 
| Chargeback     | Completed   | Forced reversal of funds initiated by customer’s bank (issuer). Only applicable to SEPA Direct Debit and credit card payments. Important information on [how to proceed when receiving a chargeback](/faq/chargebacks/what-is-a-chargeback/)              |


The full API reference for Maestro and credit cards can be found [here](/api/#credit-cards)

### Product rules
Some rules may apply to certain payment methods. For Maestro, the following rules apply:

* Refunding more than the stated amount of the original transaction is NOT possible for Maestro. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount/) page

* Maestro transactions have a maximum refund period of 180 days. After this period, it is advised to process the requested refund through a bank transfer

* The lifetime of a payment link can be adjusted. This might be beneficial for your inventory. The adjustment can be processed through the days or seconds active. Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link/) FAQ page.


* Payments done through Maestro are processed in [Euros (EUR)](/faq/general/which-currencies-are-supported-by-multisafepay/)
