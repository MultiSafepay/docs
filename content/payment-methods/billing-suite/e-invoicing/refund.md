---
title : "How to refund E-Invoicing transaction"
weight: 23
meta_title: "E-Invoicing, how to refund a transaction - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
aliases: [/payment-methods/e-invoicing/refund/]
---
## Refund
There are 3 ways to refund a E-Invoicing order in your [MultiSafepay Control](https://merchant.multisafepay.com)

In all three cases of a refund, only an amount will be refunded if a payment is linked to the transaction.
If no payment is linked to the transaction, only a credit on the invoice will take place.

### Full refund order
The order can be fully reimbursed by the refund option. Please follow these steps:

1. Go to _transactions_ in the [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction overview_
3. With the search function you can find the transaction
4. Click on the transaction to open it
5. Select _refund order_
6. _Full refund_
7. _Save_.

The order is _cancelled_.

### Partial refund
The Transaction can be partially refunded in the checkout editor. Please follow these steps:

1. Go to _transactions_ in the [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction overview_
3. With the search function you can find the transaction
4. Click on the transaction to open it
5. Select _refund order_
6. Choose _Edit_
7. Choose the page(s) you want to deduct from the order
8. _Save_.

The transaction shows the credited page with the deducted amount added to the transaction.
A new payment link is generated and sent to the customer with the adjusted invoice.

### Add a discount 
Instead of deleting a page in the checkout editor you may want to add a discount. Please follow these steps:

1. Go to _transactions_ in the [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction overview_
3. With the search function you can find the transaction
4. Click on the transaction to open it
5. Select _refund order_
6. Choose _edit_
7. Add the discount as a new page in the checkout editor
For example _-1 → discount → amount  → VAT_
8. Add the new order line to the order to deduct the amount given as a discount
9. _Save_.

The discount is added to the transaction.
A new payment link is generated and sent to the customer with the adjusted invoice.

In most plugins you can also refund. See the [Plugin FAQ](/integrations/plugins) for more information.
