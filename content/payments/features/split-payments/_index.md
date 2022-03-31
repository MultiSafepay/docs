---
title: 'Split Payments'
weight: 20
layout: 'single'
meta_title: "Split Payments - MultiSafepay Docs"
logo: '/svgs/Split payments.svg'
short_description: 'Split funds between your partner/primary account and affiliated merchants.'
url: '/features/split-payments/'
aliases:
    - /tools/split-payments/about-split-payments/
    - /tools/split-payments/what-is-split-payments
    - /tools/split-payments/processing-split-payments/
    - /tools/split-payments/how-do-i-get-split-payments
    - /tools/split-payments/refunding-split-payments/
    - /tools/split-payments/how-do-i-refund-split-payment-orders
    - /payments/features/split-payments/
---

Split Payments lets you divide an incoming transaction amount between two or more MultiSafepay accounts. This feature is supported for all [account types](/account/account-types/) and affiliations, e.g.:

- Partner/primary accounts, e.g. for mixed baskets where customers buy products from multiple affiliated merchants in a single transaction on your marketplace
- Affiliated accounts, e.g. for franchises splitting 10% of all incoming transactions to the linked primary account

You can split payments by percentage, a fixed amount, or by both.

## Integration

To split a payment, see API reference – [Create order](https://api-docs.multisafepay.com/reference/createorder).

## Refunds
You can process full and partial refunds, but only from the account that created the split payment. 

To refund a split payment, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and open the **Transaction details** page.
4. Click **Refund**.
5. Enter the amount you want to refund to the customer.
6. Click **Confirm refund**.  

The [transaction status](/about-payments/multisafepay-statuses/) changes to **Initialized**, and you can [cancel the refund](/refunds/about/#cancelling-refunds).  

When the transaction status changes to **Completed**, the refund has been processed correctly. The customer receives the refund in the bank account the transaction was originally paid from the next business day.

To refund more than the original amount, see [Refunds](/refunds/).

**Note:** Split Payments are not supported in our [ready-made integrations](/integrations/ready-made/).

