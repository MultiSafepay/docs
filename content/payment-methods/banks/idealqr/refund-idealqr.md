---
title : "How do I refund iDEAL QR transactions"
weight: 23
meta_title: "iDEAL QR, how to refund a transaction - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---
## Request refund
You can refund iDEAL QR transactions either in [MultiSafepay Control](https://merchant.multisafepay.com) or through our [API](/api/#ref_create_refund)

Please follow these steps to refund a iDEAL QR transaction:

1. Login into your [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction -> transaction overview_
3. Find the transaction through search
4. Open transaction
5. Select _refund_
6. Fill in the amount that you want to refund to the customer  
7. Confirm the refund.

>_Please note that by default, MultiSafepay does not allow for you to refund more than the stated amount of the original transaction. Please refer to the [product rules](/payment-methods/banks/idealqr/#product-rules) for more information._

The transaction status is now _initialized_. As long as the transaction status is marked as _initialized_, the refund can be cancelled. When the transaction status is marked as _completed_, the refund is processed correctly. The customer will receive the refund to the bank account number in which the transaction was originally paid to, within the next business day

>_A refund will only be processed if your balance on your MultiSafepay Control is sufficient_.

In the event of a failed iDEAL QR refund, please contact our support team at <support@multisafepay.com> to assist you.