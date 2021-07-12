---
title: 'Split payments'
weight: 80
layout: 'single'
meta_title: "Split payments - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
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
Split payments lets you spread a transaction amount over several MultiSafepay accounts, e.g. to charge a fee for using your platform to other parties. Customers can also pay for products and services from several webshops in a single transaction. 

You can split payments based on percentage, fixed amount, or a combination of the two. 

## Processing split payments
Split payments are not supported in our [ecommerce integrations](/integrations/ecommerce-integrations) by default. You can add it as a custom feature via our API. See API Reference – [Split payments](/api/#split-payments).

You can select to split by a "fixed" amount, a "percentage", or a combination of both. The amount for "fixed" payments is in cents and matches the currency the transaction was paid in. This data is stored in `var3`. Any value you provide for `var3` is overwritten.

{{< details title="Prerequisites" >}}

- Two active MultiSafepay accounts  
- Access to the code that creates the JSON request

{{< /details >}}

{{< details title="Add an affiliate object" >}}

To process split payments, add an `affiliate` object:

```shell
"affiliate": {
   "split_payments": [
        {
            "merchant": 987654321,
            "fixed": 123,
            "description": "Fixed fee"
        },
        {
            "merchant": 987654321,
            "percentage": 12.3,
            "description": "Relative fee"
        }
    ]
}
```
{{< /details >}}

## Refunding split payments
You can only refund split payments (in full or in part) from the account that originally received the funds and split them to another account.

{{< details title="Example" >}}

Account A receives a payment of 80 EUR of which 10 EUR is split to account B. The customer receives a refund of 50 EUR from account A. 

{{< /details >}}

To refund a split payment, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Search for the transaction and open the **Transaction details** page.
4. Click **Refund**.
5. Enter the amount you want to refund to the customer.
6. Click **Confirm refund**.  

The transaction status changes to **Initialized**, and you can [cancel the refund](/tools/multisafepay-control/processing-refunds/).  

When the transaction status changes to **Completed**, the refund has been processed correctly. The customer receives the refund in the bank account the transaction was originally paid from the next business day.

For refunding more than the original amount, see [Processing refunds](/tools/multisafepay-control/processing-refunds/).



