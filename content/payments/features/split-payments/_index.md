---
title: 'Split Payments'
weight: 60
layout: 'single'
meta_title: "Split Payments - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
logo: '/svgs/Split payments.svg'
short_description: 'Split funds to different bank accounts based on percentage or fixed amount.'
aliases:
    - /tools/split-payments/about-split-payments/
    - /tools/split-payments/what-is-split-payments
    - /tools/split-payments/processing-split-payments/
    - /tools/split-payments/how-do-i-get-split-payments
    - /tools/split-payments/refunding-split-payments/
    - /tools/split-payments/how-do-i-refund-split-payment-orders
---
Split Payments is a MultiSafepay solution that lets:  

- Merchants or [partners](/account/account-types/) divide a transaction amount between several MultiSafepay accounts, e.g. to charge [affiliates](/account/account-types/) a fee for using your platform
- Customers pay for products and services from multiple webshops in a single transaction

You can split payments by a percentage, a fixed amount, or a combination of the two. 

## Activating split payments
Split Payments are not supported in our [ecommerce integrations](/integrations/ecommerce-integrations) by default. You can add them to your `POST /orders` request via our API. See API reference – [Split Payments](/api/#split-payments).

### Prerequisites

- Two active MultiSafepay accounts  
- Access to the code that creates JSON requests

## Refunding split payments
You can only refund split payments (in full or in part) from the account that originally received the funds and split them to other accounts.

For example, account A receives a payment of 80 EUR of which 10 EUR is split to account B. The customer receives a refund of 50 EUR from account A. 

To refund a split payment, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and open the **Transaction details** page.
4. Click **Refund**.
5. Enter the amount you want to refund to the customer.
6. Click **Confirm refund**.  

The [transaction status](/payments/multisafepay-statuses/) changes to **Initialized**, and you can [cancel the refund](/tools/multisafepay-control/processing-refunds/).  

When the transaction status changes to **Completed**, the refund has been processed correctly. The customer receives the refund in the bank account the transaction was originally paid from the next business day.

To refund more than the original amount, see [Processing refunds](/tools/multisafepay-control/processing-refunds/).



