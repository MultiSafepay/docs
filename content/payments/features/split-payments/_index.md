---
title: 'Split payments'
weight: 40
layout: 'single'
meta_title: "Split payments - MultiSafepay Docs"
logo: '/svgs/Split payments.svg'
short_description: 'Split funds to different bank accounts based on percentage or fixed amount.'
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
Split payments lets you divide a transaction amount between [partner](/account/account-types/) or [affiliate](/account/account-types/) accounts, e.g. as a fee for using your platform.

You can split payments by percentage, a fixed amount, or by both. 

See API reference – [Split payments orders](/api/#split-payments-orders).

## Refunding split payments
You can only refund split payments (in full or in part) from the account that originally received the funds and then split them to other accounts. 

To refund a split payment, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and open the **Transaction details** page.
4. Click **Refund**.
5. Enter the amount you want to refund to the customer.
6. Click **Confirm refund**.  

The [transaction status](/payments/multisafepay-statuses/) changes to **Initialized**, and you can [cancel the refund](/tools/multisafepay-control/processing-refunds/).  

When the transaction status changes to **Completed**, the refund has been processed correctly. The customer receives the refund in the bank account the transaction was originally paid from the next business day.

To refund more than the original amount, see [Refunds](/payments/refunds/).

**Note:** Split payments are not supported in our [ecommerce integrations](/integrations/ecommerce-integrations).

