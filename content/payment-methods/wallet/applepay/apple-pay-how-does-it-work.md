---
title: "Apple Pay, How it works"
weight: 21
meta_title: "Apple Pay, How it works - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

## How it works


Consumers input their credit card information into the Apple Pay app where it is digitized in the form of an encrypted token. Consumers can authorize payments by using either [Touch ID or Face ID](https://www.apple.com/apple-pay) on a payment terminal. The tokenized data is encrpyted and sent to MultiSafepay where it is then decrypted and forwarded to the relevant payment scheme. MultiSafepay supports the Visa, Mastercard and Maestro payment schemes for Apple Pay.

MultiSafepay authorizes and validates the payment as a standard credit card transaction. Therefore, transaction statuses remain the same as that of a credit card transaction. Read more about [standard credit card transactions](/payment-methods/credit-and-debit-cards) on our documentation page.

## Transaction Flow

The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

Apple Pay transactions received by MultiSafepay will be processed through our fraud filter. The following statuses are important when receiving an Apple Pay payment:

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated to initialize an Apple Pay payment, but no payment has yet been received.  | 
| Completed   | Completed   | A successful Apple Pay transaction has been received and the funds will be added to your MultiSafepay Control balance.   | 
| Uncleared   | Uncleared   |  Waiting for manual permission of the merchant to approve/disapprove the payment. [Read more on accepting uncleared credit card payments, how and why?](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction)  | 
| Declined    | Declined    | Rejected by the issuing bank. Read more about the reason why the transaction is declined in [what does this mean?](/faq/general/declined-status) | 
| Expired     | Expired     | An unfinished transaction will automatically expire after a predefined period.  | 
| Void        | Void    | Transaction has been cancelled.   | 

### Refund flow

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Reserved       | Reserved    | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 
| Chargeback     | Completed   | Forced reversal of funds initiated by customer’s bank (issuer). Only applicable to Direct Debit and credit card payments. Information on [how to proceed when receiving a chargeback](/faq/chargebacks/what-is-a-chargeback)         |               

Read more about Apple Pay on our [API reference](https://docs.multisafepay.com/api/#applepay) page.

## Product Rules

The product rules for Apple Pay remain similar to those of the product rules from credit card payments. This is due to the nature of the transaction being a typical credit card payment, although through the Apple Pay gateway:

* A SSL secured connection (HTTPS) is required for Apple Pay to be visible

* American Express is __not__ supported for Apple Pay payments

* Refunding more than the stated amount of the original transaction is __not__ possible for Apple Pay. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount) page

* Visa, Mastercard and Maestro (Apple Pay) transactions have a maximum refund period. All cards on Apple Pay records can be refunded within 180 days. After this period, it is advised to process the requested refund through a bank transfer

* The lifetime of a payment link can be adjusted. This might be beneficial for your inventory. The adjustment can be processed through the days or seconds active. Full documentation can be found on our [lifetime of a payment link](/faq/api/lifetime-of-a-payment-link) FAQ page

* Mastercard, Visa and Maestro (Apple Pay) can be processed in the following [currencies](/faq/general/which-currencies-are-supported-by-multisafepay) as standard currency
