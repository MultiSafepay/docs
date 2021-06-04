---
title: "How to refund a CBC transaction"
weight: 23
meta_title: "CBC, how to refund a transaction - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---
## Request refund
Please follow these steps to refund a CBC transaction:

1. Select _transaction > transaction overview in your [MultiSafepay Control](https://merchant.multisafepay.com)_
2. Find the transaction through search
3. Open transaction
4. Select _refund_
5. Fill in the amount that you want to refund to the customer
6. _Confirm the refund_.

>_Please note that by default, MultiSafepay does not allow for you to refund more than the stated amount of the original transaction._

The transaction status is now _initialized_. As long as the transaction status is marked as _initialized_, the refund can be cancelled. When the transaction status is marked as _completed_, the refund is processed correctly. The customer will receive the refund to the bank account number in which the transaction was originally paid to, within the next business day.

>_A refund will only be processed if your balance on your MultiSafepay Control is sufficient_.

We do not automatically receive the IBAN when a transaction is completed. However, we import our bank statements daily and all incoming payments which have not been completed yet will then be completed. Refunds can therefore be done after 1 business day.

If a CBC refund fails, email the Support Team at <support@multisafepay.com>
