---
title : "Processing refunds"
meta_title: "Pay After Delivery - Processing refunds - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
weight: 1
---

You cannot refund more than the amount of the original transaction.

There is no time limit on refunding successful transactions once shipped, so long as the receiving bank can process the refund.

### In MultiSafepay Control

You can process 3 types of refund: full, partial, and discounts.

Refunds can only be processed for payments linked to transactions. If no payment is linked to the transaction, the customer receives credit on their invoice instead. To stop sending reminders to the customer, credit the invoice for a zero amount. 

If the customer hasn't paid, you can cancel the transaction by performing a full refund.

{{< details title="Full refunds" >}}
  
To refund the full transaction, follow these steps:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Full refund**.
5. Click **Save**.

   The transaction is cancelled.

{{< /details >}}

{{< details title="Partial refunds" >}}

To refund part of the transaction in the checkout editor, follow these steps:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Edit**.
5. Select the item(s) you want to deduct from the order.
6. Click **Save**.

   The transaction shows the credited item(s) with the deducted amount added to the transaction.
   A new payment link is generated and sent to the customer with the adjusted invoice.

{{< /details >}}

{{< details title="Discounts" >}}

Discounts are processed as a **negative amount** instead of a **negative quantity**. This method of adding discounts only applies to successful transactions. 

For how to add discounts **before** the transaction request is submitted to MultiSafepay, see API Reference - [Discount](/api/#discount).

Instead of deleting an item in the checkout editor, you may want to add a discount. Follow these steps:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Edit**.
5. Add the discount as a new page in the checkout editor.  
    Example: quantity (1) > discount (item or name) > amount (as negative) > VAT
6. To deduct the amount of the discount, add a new line to the order.
7. Click **Save**.

   The discount is added to the transaction. 
   A new payment link is generated and sent to the customer with the adjusted invoice.

{{< /details >}}

### In your backend

You can process refunds in the backend of most MultiSafepay [ecommerce integrations](/integrations/ecommerce-integrations). For more information, see the User guide of the relevant integration.

