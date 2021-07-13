---
title: 'About Apple Pay'
breadcrumb_title: 'About Apple Pay'
weight: 10
meta_title: "About Apple Pay - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
aliases:
    - /payment-methods/wallet/applepay/apple-pay-what-is-it
---

Apple Pay is a leading global payment method that lets customers tokenize their payment details in a digital wallet. It supports Maestro, Mastercard, and Visa, and Dutch bank accounts. Customers can make both online and near-field communication (NFC) payments. An additional layer of security is provided by [3D Secure](/security-and-legal/payment-regulations/about-3d-secure/), which requires customers to verify their identity.

### Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Wallet  | |
| **API flow**  | `Redirect`| [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | Worldwide  | [More information](https://support.apple.com/en-us/HT207957) |
| **Currencies**  | Multiple | [More information](https://support.apple.com/en-us/HT207957) | 
| **Refunds**  | Full and partial  | [More information](/payments/methods/wallet/applepay/user-guide/processing-refunds/) | 
| **Recurring payments**  | No | [More information](/payments/about/recurring-payments/)  |
| **Chargebacks**  | Yes | [More information](/faq/chargebacks)  |

## Product rules

- You can [adjust payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes/).  

- Customers must use the Safari browser.  

- For most MultiSafepay plugins, if the customer uses an incompatible device, Apple Pay doesn't appear on the checkout page.  
    For our [OpenCart plugin](/payments/integrations/ecommerce-platforms/opencart/), Apple Pay does appear on the checkout page on incompatible devices, but throws an error when clicked and the payment button is disabled.   

- Apple Pay transactions are processed as credit card transactions and follow similar product rules, with the following exceptions:
    - An SSL secured connection (HTTPS) is required.
    - American Express is **not** supported.
