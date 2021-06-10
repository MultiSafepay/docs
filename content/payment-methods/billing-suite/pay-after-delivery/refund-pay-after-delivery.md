---
title : "How to refund a Pay After Delivery transaction"
Weight: 23
meta_title: "Pay After Delivery, how to refund a transaction - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases: [/payment-methods/pay-after-delivery/refund-pay-after-delivery/]
---
## Request refund
Please follow these steps to refund a Pay After Delivery transaction:


#### Full order refund

1. Go to _transactions_ in the [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction overview_
3. With the search function you can find the transaction
4. Click on the transaction to open it
5. Select _refund complete order_
6. _Full refund_
7. _Save_.

**An amount will be refunded only if a payment is linked to the transaction. If no payment is linked to the transaction, only a credit on the invoice will take place. Credit the invoice to a zero amount means the customer will no longer receive a reminder of the invoice**


#### Partial refund by item or amount 
The order can be partially reimbursed in the checkout editor.  

1. Go to _transactions_ in the [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction overview_
3. With the search function you can find the transaction
4. Click on the transaction to open it
5. Select _refund order_
6. _Edit_
7. Choose the page(s) you want to deduct from the order
8. _Save_.

**The order shows the credited page with the deducted amount added to the checkout editor. A new payment link is generated and sent to the customer with the adjusted invoice.**

When you do not want to deduct an item but would like to submit an amount instead, follow these steps below to issue a partial refund:     

1. Select _refund order_
2. _edit_
3. Add the discount as a new page in the checkout editor - for example _-1 > discount > amount  > VAT_
4. Add the new order line to the order to deduct the amount given as a discount
5. _Save_.

**Example:**      

When the customer has not supplied a payment, the transaction can be cancelled by _refund completed order_, see further information in [full order refund](/payment-methods/billing-suite/pay-after-delivery/#request-refund) 

This way you credit the invoice to a zero amount and the customer will no longer receive a reminder of the order. 

1. Go to _transactions_ in the [MultiSafepay Control](https://merchant.multisafepay.com)
2. Select _transaction overview_
3. With the search function you can find the transaction
4. Click on the transaction to open it
5. Select _Complete own funds_ 
6. Submit a comment 
7. _Complete_ 
8. The funds will be deducted from your MultiSafepay balance
9. The invoice has been settled

In most ecommerce integrations you can also refund. See the corresponding [ecommerce integration FAQ](/integrations/ecommerce-integrations) for more information.

