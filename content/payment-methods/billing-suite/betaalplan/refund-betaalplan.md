---
title: "How to refund a Betaalplan transaction"
weight: 23
meta_title: "Betaalplan, how to refund a transaction - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
# Request refund
A Betaalplan transaction can be either fully or partially refunded in [MultiSafepay Control](https://merchant.multisafepay.com). 

In both cases, the amount will be refunded only if there is an initial payment linked to the transaction. Otherwise, only a credit on the invoice will take place.

## Full or partial transaction refund
Please follow these steps to refund a Betaalplan transaction:

1. Login into your [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction -> transaction overview
3. Find the transaction through search
4. Open transaction
5. Select _refund_
6. Fill in the amount that you want to refund to the customer
7. Confirm the refund.

* The transaction status is now _initialized_. As long as the transaction status is marked as _initialized_, the refund can be cancelled. When the transaction status is marked as _completed_, the refund is processed correctly. The customer will receive the refund to the bank account number in which the transaction was originally paid to, within the next business day

* The amount is deducted from the transaction. The refund will always be linked to the original transaction

* In most plugins you can also refund. See the [Plugin FAQ](/integrations/) for more information

* Once the refund is confirmed, there is no possibility to reverse the refund

> A refund will only be processed if the balance on your MultiSafepay Control is sufficient.

<br>
