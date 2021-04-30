---
title: "Apple Pay, How it works"
weight: 21
meta_title: "Apple Pay, How it works - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

## How it works

1. The customer enters their credit card information into the Apple Pay app where it is stored as an encrypted token. 
2. The customer authorizes the payment on an iOS device using either [Touch ID or Face ID](https://www.apple.com/apple-pay). 
3. The tokenized data is encrypted and sent to MultiSafepay.
4. MultiSafepay decrypts the data and forwards it to the relevant payment scheme. Supported payment schemes for Apple Pay: Visa, Mastercard, and Maestro.
5. MultiSafepay authorizes and validates the payment as a [standard credit card transaction](/payment-methods/credit-and-debit-cards), using the same transaction statuses.

## Transaction flow

The transaction flow is the different ways an Apple Pay transaction can be processed:

- Order status: The status of the customer's order, e.g. **Completed**, **Pending**, **Rejected**. Independent of the incoming or outgoing payment for the transaction.

- Transaction status: The status of the payment for the transaction, e.g. **Completed**, **Pending**, or **Rejected**. Once the transaction status is **Completed**, the amount of the transaction is added to your MultiSafepay balance.

## Fraud filter

All Apple Pay transactions pass through our fraud filter and may receive one of the following statuses:

| Order status                      | Transaction status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Initialized | Initialized | A payment link has been generated to initialize an Apple Pay payment, but no payment has yet been received.  | 
| Completed   | Completed   | A successful Apple Pay payment has been received and the funds will be added to your MultiSafepay balance.   | 
| Uncleared   | Uncleared   |  Waiting for manual permission from the merchant to accept or decline the payment. For more information, see [Accepting uncleared credit card payments](/faq/risk-and-fraud/how-to-accept-an-uncleared-transaction).  | 
| Declined    | Declined    | Rejected by the issuing bank. For more information, see [Declined status](/faq/general/declined-status). | 
| Expired     | Expired     | A transaction for which no payment is received automatically expires after a fixed period.  | 
| Void        | Void    | The transaction has been cancelled.   | 

### Refund flow

| Order status                      | Transaction status      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| Reserved       | Reserved    | The customer has requested a refund. | 
| Completed      | Completed   | The refund has been successfully processed.  | 
| Chargeback     | Completed   | The issuing bank initiated a forced reversal of funds. Only applicable to direct debit and credit card payments. For more information, see [About chargebacks](/faq/chargebacks/about-chargebacks)         |               

For information about using Apple Pay via our API, see API - [Apple Pay](/api/#applepay) page.

## Product rules

Apple Pay transactions are like credit card transactions and follow similar product rules, except for these specific differences:

- An SSL secured connection (HTTPS) is required.

- American Express is **not** supported.

- It is **not** possible to refund more than the amount of the original transaction. For more information, see [Refunding more than original transaction value](/faq/finance/refunding-more-than-original-transaction-value).

- Visa, Mastercard and Maestro transactions have a maximum refund period of 180 days. After this period, we recommend processing refunds by bank transfer.

- You can adjust the lifetime of payment links using the through the days_active or seconds_active parameters. For more information, see [Lifetime of a payment link](/faq/api/lifetime-of-a-payment-link).

* You can process transactions in [these standard currencies](/faq/general/currencies-supported).

- Customers must use the Safari browser.
