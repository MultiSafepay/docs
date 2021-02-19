---
title: "How to refund a Betaal per Maand transaction"
weight: 23
meta_title: "Betaal per Maand, how to refund a transaction - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
aliases: [/payment-methods/betaalplan/refund-betaalplan/]
---
# Request refund
A Betaal per Maand transaction can be either fully or partially refunded in [MultiSafepay Control](https://merchant.multisafepay.com) 

In both cases, the amount will be refunded only if there is an initial payment linked to the transaction. Otherwise, only a credit on the invoice will take place.

## Full or partial transaction refund
Please follow these steps to refund a Betaal per Maand transaction:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction → transaction overview
3. Find the transaction through search
4. Open transaction
5. Select _refund_
6. Fill in the amount that you want to refund to the customer
7. Confirm the refund.

* The transaction status is now _initialized_. As long as the transaction status is marked as _initialized_, the refund can be cancelled. When the transaction status is marked as _completed_, the refund is processed correctly. The customer will receive the refund to the bank account number in which the transaction was originally paid to, within the next business day

* The amount is deducted from the transaction. The refund will always be linked to the original transaction

* In most plugins you can also refund. See the [Plugin FAQ](/integrations/plugins) for more information

* Once the refund is confirmed, there is no possibility to reverse the refund

* The initialized refund will be handed over to Santander who will handle the refund request. It is possible to initialize a refund at any time as there is no time limit on processing a refund.

> A refund will only be processed if the balance on your MultiSafepay Control is sufficient.


## Change order before shipment
If you want to change a Betaal per Maand order between acceptance of Santander and shipment by the Merchant, follow these steps:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _Transaction_ → _Transaction overview_
3. Locate the transaction and click on _Change order status_ under Order summary
4. Change the status of the initial order to _'Shipped'_ and add a Memo
5. Refund the required amount: the original or partial amount.
It is not possible to increase the amount of the initial order. If for some reason this is required, please contact your account manager.

