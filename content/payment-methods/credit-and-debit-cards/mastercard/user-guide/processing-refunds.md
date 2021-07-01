---
title : "Processing refunds"
weight: 10
meta_title: "Mastercard - Processing refunds - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /payment-methods/credit-and-debit-cards/mastercard/refund-mastercard
---

{{< details title="Mastercard refund rules" >}}

- You cannot refund more than the amount of the original transaction.

- The maximum refund period is 180 days. After this period, we recommend processing refunds by bank transfer.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- The customer receives the refund in the bank account they originally paid from within the next business day.

- Depending on the customer's issuer, the amount may not appear directly on their card. We recommend that they contact the issuer. If they need an acquirer reference number (ARN), they can email the Support Team at <support@multisafepay.com> 

- If you process a partial refund on the same day, this is technically called a "reversal", but for simplicity is logged as a refund in your MultiSafepay account. On customer credit card statements, the transaction may either be adjusted to the new amount (partial reversal) _or_ not debited at all (full reversal).

{{< /details >}}

{{< details title="Refund statuses" >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund was successfully processed.  | Completed      | Completed   |
| The customer requested their bank to force reversal of funds. {{< br >}} See [About chargebacks](/faq/chargebacks/about-chargebacks/). | Chargeback | Completed   |

{{< /details >}}

## In your MultiSafepay account

{{< details title="Full refunds" >}}
  
To refund the full transaction, follow these steps:

1. Log in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Full refund**.
5. Click **Save**.

   The transaction is cancelled.

{{< /details >}}

{{< details title="Partial refunds" >}}

To refund part of the transaction in the checkout editor, follow these steps:

1. Log in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and click to open the **Transaction details** page.
4. Click **Refund order** > **Edit**.
5. Select the item(s) you want to deduct from the order.
6. Click **Save**.

   The transaction shows the credited item(s) with the deducted amount added to the transaction.
   A new payment link is generated and sent to the customer with the adjusted invoice.

{{< /details >}}

## Via our API
Make a POST `/orders/{order_id}/refunds` request. See API Reference – [Refund with shopping cart](/api/#refund-with-shopping-cart).

### In your backend
You can process refunds in the backend of most [ecommerce platforms](/integrations/ecommerce-integrations). For more information, see the User guide in the integration manaual for the relevant platform, e.g. Magento 2 – [Processing refunds](/integrations/ecommerce-integrations/magento2/faq/processing-refunds/).
