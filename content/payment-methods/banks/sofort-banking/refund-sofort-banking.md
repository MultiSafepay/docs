---
title: "How to refund an SOFORT Banking transaction?"
weight: 23
meta_title: "SOFORT Banking, how to refund a transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases: [/payment-methods/sofort-banking/refund-sofort-banking/]
---
## Request refund
Please follow these steps to refund a SOFORT Banking transaction:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction > transaction_
3. Find the transaction through search
4. Open transaction
5. Select _refund_
6. Fill in the amount that you want to refund to the customer
7. _Confirm_.

>_Please note that by default, MultiSafepay does not allow for you to refund more than the stated amount of the original transaction. Please refer to the [product rules](/payment-methods/banks/sofort-banking/#product-rules) for more information._

The transaction status is now _initialized_. As long as the transaction status is marked as _initialized_, the refund can be cancelled. When the transaction status is marked as _completed_, the refund is processed correctly. The customer will receive the refund to the bank account number in which the transaction was originally paid to, within the next business day.

A refund will only be processed if your balance on your MultiSafepay Control is positive.

In the event of a failed SOFORT Banking refund, please contact our support team at <support@multisafepay.com> to assist you.