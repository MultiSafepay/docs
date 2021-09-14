---
title: 'Product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "Apple Pay product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
url: '/payments/methods/apple-pay/product-rules/'
aliases:
    - /payments/methods/wallet/applepay/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide  | [More information](https://support.apple.com/en-us/HT207957) |
| **Currencies**  | Multiple | [More information](https://support.apple.com/en-us/HT207957) | 
| **Chargebacks**  | Yes | [More information](/payments/chargebacks/)  |
| **Payment flow**  | [Direct](/api/#apple-pay-direct) / [Redirect](/api/#apple-pay-redirect) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 1 hour | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- You cannot refund more than original amount.

- The maximum refund period for Maestro, Mastercard, and Visa transactions is 180 days. After this, we recommend processing refunds by bank transfer.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- The customer receives the refund in their Apple Pay account and it appears on their credit card statement within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com>

{{< /details >}}

- Customers must use the Safari browser.  

- For most MultiSafepay plugins, if the customer uses an incompatible device, Apple Pay doesn't appear on the checkout page.  
    For our [OpenCart plugin](/payments/integrations/ecommerce-platforms/opencart/), Apple Pay does appear on the checkout page on incompatible devices, but throws an error when clicked and the payment button is disabled.   

- Apple Pay transactions are processed as [credit card transactions](/payments/methods/credit-and-debit-cards/) and follow similar product rules, with the following exceptions:
    - An SSL secured connection (HTTPS) is required.
    - American Express is **not** supported.