---
title: 'Split payments'
category: 6278c92bf4ad4a00361431b0
order: 6
hidden: false
slug: 'split-payments'
---
Split Payments lets you divide an incoming transaction amount between two or more MultiSafepay accounts. 

# How it works

This feature is supported for all [account types](/docs/create-account/) and affiliations, e.g.:

- Partner/primary accounts, e.g. for mixed baskets where customers buy products from multiple affiliated merchants in a single transaction on your marketplace
- Affiliated accounts, e.g. for franchises splitting 10% of all incoming transactions to the linked primary account

You can split payments by percentage, a fixed amount, or by both.

# Activation
None.

# Integration

See Recipes – <a href="https://docs.multisafepay.com/recipes/split-a-payment" target="_blank">Split a payment</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.


Split Payments are not supported in our [ready-made integrations](/docs/our-integrations/).
<br>

---

# User guide

## Refunds

You can process full and partial refunds, but only from the account that created the split payment. 

<details id="how-to-refund-split-payment">
<summary>How to refund a split payment</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
3. On the **Transaction details** page, click **Refund**.
4. Enter the amount you want to refund to the customer, and then click **Confirm refund**.  
    The <<glossary:transaction status>> changes to **Initialized**.
5. [Cancel the refund](/docs/refund-payments/).  


When the transaction status changes to **Completed**, the refund has been processed correctly. The customer receives the refund in the bank account the transaction was originally paid from the next business day.

</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
