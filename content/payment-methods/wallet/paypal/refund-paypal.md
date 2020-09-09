---
title : "How to refund a PayPal transaction"
weight: 23
meta_title: "PayPal, how to refund a transaction - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---
## Request refund
The refund of a PayPal transaction can be processed from within your [MultiSafepay Control](https://merchant.multisafepay.com)

Please follow these steps:

1. Select _Transactions -> Transaction overview_
2. Find the transaction through search
3. Open the transaction
4. Select _refund_
5. Fill in the amount that you are going to refund to the customer
6. _Confirm_.

>_Please note that by default, MultiSafepay does not allow for you to refund more than the stated amount of the original transaction. Please refer to the [product rules](/payment-methods/paypal/#product-rules) for more information._

* The transaction status is now _initialized_. As long as the transaction status is marked as _initialized_, the refund can be cancelled. When the transaction status is marked as _completed_, the refund is processed correctly. The customer will receive the refund to the bank account number in which the transaction was originally paid to, within the next business day

* PayPal transactions can be refunded within 60 days

* A refund will only be processed if your PayPal balance is sufficient. Otherwise, PayPal will proceed with issuing an [eCheck](https://www.paypal.com/us/smarthelp/article/what-is-an-echeck-faq1082) You will need to make sure that PayPal is authorized to withdraw funds from a linked bank account when a refund is requested and your balance is insufficient, in order to avoid a potential cancellation on PayPal's side. As a merchant, you will need to take care of these settings yourself, from within your PayPal account. Failing to do so can result in a cancelled refund and follow-up complaints and escalation from your customers. For any questions related to this topic, we strongly encourage you to reach out to PayPal's support. 
