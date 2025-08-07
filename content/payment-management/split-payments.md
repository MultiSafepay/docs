---
title: Split payments
category:
  uri: Payment management
slug: split-payments
position: 6
privacy:
  view: public
---
Split Payments lets you divide an incoming transaction amount between two or more MultiSafepay accounts.

# How it works

This feature is supported for all [account types](/docs/create-account/) and affiliations, e.g.:

* Partner/primary accounts, e.g. for mixed baskets where customers buy products from multiple affiliated merchants in a single transaction on your marketplace
* Affiliated accounts, e.g. for franchises splitting 10% of all incoming transactions to the linked primary account

You can split payments by percentage, a fixed amount, or by both.

# Activation

The Split Payments feature is available by default for all MultiSafepay accounts.

# Integration

See Recipes – <a href="https://docs.multisafepay.com/recipes/split-a-payment" target="_blank">Split a payment</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i> !<a href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" target="_blank"></a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i>.

Split Payments are not supported in our [ready-made integrations](/docs/our-integrations/).

***

# User guide

## Refunds

You can process full and partial refunds, but only from the account that created the split payment.

<details id="how-to-refund-split-payment">
  <summary>How to refund a split payment</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i> !<a href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" target="_blank">external link icon</a> <i className="fa fa-external-link" style={{ fontSize:'12px', color:'#8b929e' }}></i>.
  2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
  3. On the **Transaction details** page, click **Refund**.
  4. Enter the amount you want to refund to the customer, and then click **Confirm refund**.\
     The <Glossary>transaction status</Glossary> changes to **Initialized**.
  5. [Cancel the refund](/docs/refund-payments/).

  When the transaction status changes to **Completed**, the refund has been processed correctly. The customer receives the refund in the bank account the transaction was originally paid from the next business day.
</details>

<br />

***

<blockquote className="callout callout_info">
    <h3 className="callout-heading false">
        <span className="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)