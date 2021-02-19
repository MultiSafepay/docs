---
title: "How to refund a Klarna transaction"
weight: 23
meta_title: "Klarna, how to refund a transaction - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
aliases: [/payment-methods/klarna/refund-klarna/]
---
# Request a refund 

There are 3 ways to refund a Klarna transaction in your [MultiSafepay Control](https://merchant.multisafepay.com) account.

In all three cases of a refund, an amount will be refunded only if a payment is linked to the transaction. If no payment is linked to the transaction, only a credit on the invoice will take place.

## Full refund
The transaction can be fully refunded through the refund option:

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

{{< alert-notice >}} Submitting a discount with the payment method Klarna is processed on a __negative amount__ instead of on a __negative quantity__. This method of adding a discount only applies to a successfully placed Klarna transaction. More information about how to add a discount before the transaction request is submitted to MultiSafepay is available on our [API Documentation page](/api/#discount) {{< /alert-notice >}}


1. Go to _transactions_ in the [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction overview_
3. With the search function you can find the transaction
4. Click on the transaction to open it
5. Select _refund order_
6. Choose _edit_
7. Add the discount as a new page in the checkout editor.\
_**For example, quantity (1) → discount (item or name) → amount (as negative)→ VAT**_
8. Add the new order line to the order to deduct the amount given as a discount
9. _Save_.

The discount is added to the transaction. A new payment link is generated and sent to the customer with the adjusted invoice.

In most plugins you can also refund. See the corresponding [plugin FAQ](/integrations/plugins) for more information.



_Pay-after-delivery methods allow customers to pay only for items they keep from an order. This means that sometimes the complete customer journey also consists of a product return process. In the event of the return process taking too long to verify, the collection period can be paused for 2 to 4 weeks by placing it on hold. This can only be done via <verkoop@klarna.com> or +31 208082853_
