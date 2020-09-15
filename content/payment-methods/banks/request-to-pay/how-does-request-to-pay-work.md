---
title: "Request to Pay, How does it work?"
weight: 21
meta_title: "Request to Pay, how does it work? - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

## How does it work?

Request to Pay works in such a way that consumers are redirected to Deutsche Bank’s online banking platform, after authenticating themselves with the same credentials as when logging in to their online banking platform, a SEPA bank transfer is authorised directly from the consumer to the merchant via MultiSafepay. An authorised bank transfer can be settled instantly or after 24 hrs, depending on if the bank supports instant payments or not.

Request to Pay reduces cost and risk, enabling faster settlement, providing simplified reconciliation.

## Transaction Flow

The transaction flow shows the different ways a transaction can be processed. This differs per payment method.

* Order status      
The order status indicates the status of the order, such as _completed_, _pending_ or _rejected_. The order status is independent of the incoming or outgoing payment of the transaction.

* Transaction status       
The transaction status indicates the payment status of the transaction, such as _completed_, _pending_ or _rejected_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.

Request to Pay transactions received by MultiSafepay will be processed directly through Deutsche Bank. The following statuses are important when receiving an Request to Pay payment:

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | Consumer is redirected to the Deutsche Bank payment page  | 
| Uncleared   | Completed   | The payment has been authorised and successful. The consumer is redirected back to MultiSafepay   | 
| Completed   | Completed   |  Transaction is on credit notification. For banks that support instant SEPA credit transfers, the credit notifications can be immediate, otherwise this will be done within the next 24 hours.  | 
| Expired   | Expired    | The consumer does not complete the payment on the Deutsche Bank payment interface. | 
| Declined     | Declined     | Deutsche Bank or the consumer bank rejects the payment.  | 
| Void        | Void    | The consumer cancels the payment on the Deutsche Bank payment interface.   | 

## Refund flow

_Please note that refunds are processed by Deutsche Bank._

| Order Status                      | Transaction Status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Reserved       | Reserved    | A refund has been requested. | 
| Completed      | Completed   | Refund has been successfully processed.  | 
| Declined     | Declined   | Refund has been declined.      |               

The full API reference for Request to Pay can be found [here](https://docs.multisafepay.com/api/#directbanktransfer)

## Product Rules

Request to Pay has a number of product rules which are the following:

* Request to Pay supports Instant as well as Non-Instant SEPA bank transfers

* Online refunding is processed by Deutsche Bank themselves.

* Request to Pay can only process transactions in Euros (EUR)

* A minimum of 1 EUR and maximum of 15,000 EUR exist for Request to Pay transactions.
