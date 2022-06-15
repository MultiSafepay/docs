---
title: 'Split Payments'
category: 6278c92bf4ad4a00361431b0
order: 900
hidden: false
slug: 'split-payments'
excerpt: 'Split funds between your partner/primary account and affiliated merchants.'
---
Split Payments lets you divide an incoming transaction amount between two or more MultiSafepay accounts. This feature is supported for all [account types](/create-account/) and affiliations, e.g.:

- Partner/primary accounts, e.g. for mixed baskets where customers buy products from multiple affiliated merchants in a single transaction on your marketplace
- Affiliated accounts, e.g. for franchises splitting 10% of all incoming transactions to the linked primary account

You can split payments by percentage, a fixed amount, or by both.

# Integration

See API recipe – [Split a payment](https://docs-api.multisafepay.com/recipes/split-a-payment).

Split Payments are not supported in our [ready-made integrations](/integrations/ready-made/).

# Refunds

You can process full and partial refunds, but only from the account that created the split payment. 

<details id="how-to-refund-split-payment">
<summary>How to refund a split payment</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and open the **Transaction details** page.
4. Click **Refund**.
5. Enter the amount you want to refund to the customer.
6. Click **Confirm refund**.  
    The [transaction status](/payments-statuses/) changes to **Initialized**.
7. [Cancel the refund](/refunds/).  

When the transaction status changes to **Completed**, the refund has been processed correctly. The customer receives the refund in the bank account the transaction was originally paid from the next business day.

</details>
<br>

> 📘 **More info**
> For more information or support, email <integration@multisafepay.com>