---
title: "American Express, How does it work?"
weight: 21
meta_title: "American Express, how does it work? - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
---
## How it works
>American Express payments are processed as credit card payments. Email requests to enable credit card payments in your MultiSafepay Control to your account manager at <sales@multisafepay.com>

### Transaction flow
The transaction flow shows the different ways an American Express transaction can be processed.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

American Express transactions received by MultiSafepay will be processed through our fraud filter. The following statuses are important when receiving a credit card payment:

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Completed   | Completed   | A successful American Express transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Uncleared   | Uncleared   |  Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction)  | 
| Declined    | Declined    | Rejected by the issuing bank. Read more about the reason why the transaction is declined in [what does this mean?](/faq/general/declined-status) | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 
| 

### Transaction flow when processing on own MID 
> When using an own MID (MerchantID) from American Express, the funds are not processed by MultiSafepay. Instead, the funds will be added to your own balance at American Express.


| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet.  | 
| Uncleared   | Initialized | Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction)  | 
| Completed   | Initialized | A successful credit card  transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 


### Refund flow

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Reserved       | Reserved    | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 
| Chargeback     | Completed   | Forced reversal of funds initiated by customer’s bank (issuer). Only applicable to SEPA Direct Debit and credit card payments. Information on [how to proceed when receiving a chargeback](/faq/chargebacks/what-is-a-chargeback)         |     

The full API reference for American Express can be found [here](/api/#credit-cards)

### Product rules
Some rules may apply to certain payment methods. For American Express, the following rules apply:

* Refunding more than the stated amount of the original transaction is NOT possible for American Express. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount) page

* American Express transactions have a maximum refund period of 180 days. After this period, it is advised to process the requested refund through a bank transfer

* The lifetime of a payment link can be adjusted. This might be beneficial for your inventory. The adjustment can be processed through the days or seconds active. Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link) FAQ page.

* If you refund the transaction (partially) on the same day this is called a reversal. To keep things easy manageable in your reporting, this is logged as a refund. However, your customers might experience otherwise: the transaction in their overview will be adjusted to the new amount (partial reversal) of the order __or__ is not debited at all (full reversal).


    If a different currency is desired, contact our support department for the possibilities. Email your request to <support@multisafepay.com>
