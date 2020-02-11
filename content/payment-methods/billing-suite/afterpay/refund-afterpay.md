---
title: "How to refund an AfterPay transaction"
weight: 23
meta_title: "Afterpay, how to refund a transaction - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---

# Request a refund 

There are 3 ways to refund an AfterPay transaction in [MultiSafepay Control](https://merchant.multisafepay.com)

In all three cases of a refund, an amount will be refunded only if a payment is linked to the transaction. If no payment is linked to the transaction, only a credit on the invoice will take place.

## Full refund
The transaction can be fully refunded through the refund option.

1. Go to _transactions_ in [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction overview_
3. With the search function you can find the transaction
4. Click on the transaction to open it
5. Select _refund order_
6. _Full refund_
7. _Save_.

The transaction is cancelled.

## Partial refund
The Transaction can be partially refunded in the checkout editor. Please follow these steps:

1. Go to _transactions_ in [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction overview_
3. With the search function you can find the transaction
4. Click on the transaction to open it
5. Select _refund order_
6. Choose _Edit_
7. Choose the item(s) you want to deduct from the order
8. _Save_.

The transaction shows the credited item(s) with the deducted amount added to the transaction.
A new payment link is generated and sent to the customer with the adjusted invoice.

## Add a discount
Instead of deleting an item in the checkout editor you may want to add a discount. Please follow these steps:

1. Go to _transactions_ in the [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction overview_
3. With the search function you can find the transaction
4. Click on the transaction to open it
5. Select _refund order_
6. Choose _edit_
7. Add the discount as a new page in the checkout editor. _For example, -1 -> discount -> amount -> VAT_
8. Add the new order line to the order to deduct the amount given as a discount
9. _Save_.

The discount is added to the transaction.
A new payment link is generated and sent to the customer with the adjusted invoice.

In most plugins you can also refund. See the corresponding [plugin FAQ](/integrations/plugins/) for more information.


