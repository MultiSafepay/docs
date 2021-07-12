---
title : "Processing refunds"
meta_title: "Bancontact QR - Processing refunds - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
weight: 10
aliases: 
    - /payment-methods/bancontact/refund-bancontact-qr/
---
{{< details title="Bancontact QR refund rules" >}}
- You can refund more than the original transaction value. See [Processing refunds](/tools/multisafepay-control/processing-refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

{{< details title="Refund statuses" >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund has been successfully processed. | Completed | Completed |

{{< /details >}}

## In your MultiSafepay account

{{< details title="Full refunds" >}}
  
To refund the full transaction, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Full refund**.
5. Click **Save**.

   The transaction is cancelled.

{{< /details >}}

{{< details title="Partial refunds" >}}

To refund part of the transaction in the checkout editor, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Edit**.
5. Select the item(s) you want to deduct from the order.
6. Click **Save**.

   The transaction shows the credited item(s) with the deducted amount added to the transaction.
   A new payment link is generated and sent to the customer with the adjusted invoice.

{{< /details >}}

## In your backend

You can process refunds in the backend of most [ecommerce platforms](/integrations/ecommerce-integrations). For more information, see the User guide in the integration manual for the relevant platform, e.g. Magento 2 – [Processing refunds](/integrations/ecommerce-integrations/magento2/faq/processing-refunds/). 
