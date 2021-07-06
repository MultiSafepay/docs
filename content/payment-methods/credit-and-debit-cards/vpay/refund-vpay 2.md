---
title: "How to refund a V Pay transaction"
weight: 23
meta_title: "V Pay, how to refund a transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
---
## Request refund
The refund of a transaction with the payment method V Pay can be processed from within your [MultiSafepay Control](https://merchant.multisafepay.com)

Please follow these steps:

1. Select _Transactions > Transaction overview_
2. Find the transaction through search
3. Open the transaction
4. Select _refund_
5. Fill in the amount that you are going to refund to the customer
6. _Confirm_.

* Refunding more than the stated amount of the original transaction is NOT possible with V Pay. More information is available on our [refund more than original amount](/faq/finance/refund-more-than-original-amount) page

* The transaction status is now _initialized_. As long as the transaction status is marked as _initialized_, the refund can be cancelled. When the transaction status is marked as _completed_, the refund is processed correctly. The customer will receive the refund to the bank account number in which the transaction was originally paid to, within the next business day.

> A refund will be processed the next business day. However, depending an the issuer, it is possible that the amount is not shown directly on the card. If this is the case, we recommend contacting the issuer of your credit card. If an ARN is needed, the support department is able to provide one. 

A refund will only be processed if your balance on your MultiSafepay Control is positive.
