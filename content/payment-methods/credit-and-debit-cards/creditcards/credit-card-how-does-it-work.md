---
title: "Credit Cards, How do they work?"
weight: 21
meta_title: "Credit cards, how do they work? - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
## How it works
In order to pay with Mastercard, Visa or American Express the customer needs to fill in their card number, CVC-code and expiry date to release a payment. When the 3D Secure is enabled on the credit card, the customer needs to provide an authentic code on the next page to finalize the payment. The 3D secure insures that the customer is the rightful account holder.

As payment processor, MultiSafepay is an [acquirer](/faq/getting-started/glossary/#acquirer) itself for Visa and Mastercard.

### "Visa, Mastercard and American Express" transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

Credit card transactions received by MultiSafepay will be processed through our fraud filter. The following statuses are important when receiving a credit card payment:

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful credit card  transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Uncleared   | Uncleared   |  Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction/)  | 
| Declined    | Declined    | Transaction has been rejected. [read more on credit card status 'declined'. What does this mean?](/payment-methods/creditcards/creditcard-status-declined-what-does-this-mean-/) | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 


#### Transaction flow when processing on own MID 
> When using an own MID (MerchantID) from American Express, the funds are not processed by MultiSafepay. Instead, the funds will be added to your own balance at American Express.


| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Uncleared   | Initialized | Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction/)  | 
| Completed   | Initialized | A successful credit card  transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 


#### Refund flow

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Reserved       | Reserved    | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 
| Chargeback     | Completed   | Forced reversal of funds initiated by customer’s bank (issuer). Only applicable to SEPA Direct Debit and credit card payments. Information on [how to proceed when receiving a chargeback](/payment-methods/creditcards/what-is-a-chargeback/)         |               

The full API reference for credit cards can be found [here](/api/#credit-cards)

### Product rules
Some rules may apply to certain payment methods. For credit cards, the following rules apply:

* Refunding more than the stated amount of the original transaction is NOT possible for credit cards. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount/) page

* Visa, Mastercard and American Express transactions have a maximum refund period. All cards can be refunded within 180 days. After this period, it is advised to process the requested refund through a bank transfer

* The lifetime of a payment link can be adjusted. This might be beneficial for your inventory. The adjustment can be processed through the days or seconds active. Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link/) FAQ page

* Mastercard, Visa and American Express can be processed in the following [currencies](/faq/general/which-currencies-are-supported-by-multisafepay/) as standard currency 


    If a different currency is desired, contact our support department for the possibilities. Submit your request at <support@multisafepay.com>
