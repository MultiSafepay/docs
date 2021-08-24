---
title: 'About GooglePay'
breadcrumb_title: 'About GooglePay'
weight: 10
meta_title: "About GooglePay - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
---


### Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Wallet  | |
| **API flow**  | `redirect` and `direct` | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | Worldwide | [More information](https://support.google.com/pay/answer/9023773?hl=en#zippy=%2Cpay-online-or-in-apps) |
| **Currencies**  | Multiple | | 
| **Refunds**  | Full and partial  | [More information](/payments/refunds/) | 
| **Recurring payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Chargebacks**  | Yes | [More information](/faq/chargebacks)  |

## Product rules

- You can [adjust payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes/).  

- Customers must use the Safari browser.  

- For most MultiSafepay plugins, if the customer uses an incompatible device, Apple Pay doesn't appear on the checkout page.  
    For our [OpenCart plugin](/payments/integrations/ecommerce-platforms/opencart/), Apple Pay does appear on the checkout page on incompatible devices, but throws an error when clicked and the payment button is disabled.   

- Apple Pay transactions are processed as credit card transactions and follow similar product rules, with the following exceptions:
    - An SSL secured connection (HTTPS) is required.
    - American Express is **not** supported.

{{< details title="Refunds" >}}

- You cannot refund more than original amount.

- The maximum refund period for Maestro, Mastercard, and Visa transactions is 180 days. After this, we recommend processing refunds by bank transfer.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- The customer receives the refund in their Apple Pay account and it appears on their credit card statement within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com>

{{< /details >}}
