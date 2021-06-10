---
title: "V Pay, How does it work?"
weight: 21
meta_title: "V Pay, how does it work? - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
---
## How it works
V Pay payments are processed as a credit card payment. Therefore, credit card payments must be enabled within your MultiSafepay Control to process a V Pay payment. Submit your request to enable credit cards (Visa, Mastercard and Maestro) to your account manager or contact us at <sales@multisafepay.com>

A V Pay payment is always validated with the [3D Secure](/faq/general/glossary/#3d-secure) code. 3D Secure verification is deemed mandatory by V Pay.

V Pay payments are processed through the VISA gateway when Visa is activated as a payment method in your MultiSafepay Control.

### Transaction flow
The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

V Pay (debit card) transactions received by MultiSafepay will be processed through our fraud filter. The following statuses are important when receiving a V Pay payment:

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated, but no payment has been received yet. | 
| Completed   | Completed   | A successful V Pay transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Uncleared   | Uncleared   |  Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction)
| Declined    | Declined    | Rejected by the issuing bank. Read more about the reason why the transaction is declined in [what does this mean?](/faq/general/declined-status) | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Cancelled    | Transaction has been cancelled.   | 
| 


#### Refund flow 

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Reserved       | Reserved    | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 
| Chargeback     | Completed   | Forced reversal of funds initiated by customer’s bank (issuer). Only applicable to SEPA Direct Debit and credit card payments. Important information on [how to proceed when receiving a chargeback](/faq/chargebacks/what-is-a-chargeback)              |


The full API reference for V Pay and credit cards can be found [here](/api/#credit-cards)

### Product rules
Some rules may apply to certain payment methods. For V Pay, the following rules apply:

* Refunding more than the stated amount of the original transaction is NOT possible for V Pay. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount) page

* V Pay transactions have a maximum refund period of 180 days. After this period, it is advised to process the requested refund through a bank transfer

* The lifetime of a payment link can be adjusted. This might be beneficial for your inventory. The adjustment can be processed through the days or seconds active. Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link) FAQ page.

* Payments done through V Pay are processed in [Euros (EUR)](/faq/general/which-currencies-are-supported-by-multisafepay)
