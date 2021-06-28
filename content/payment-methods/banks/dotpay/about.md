---
title: "About Dotpay"
breadcrumb_title: 'About Dotpay'
weight: 10
meta_title: "About Dotpay - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/Dotpay.svg'
aliases: [/payment-methods/dotpay/dotpay-what-is-it/]
---

Dotpay is an inter-bank payment method that links all major Polish retail banks. Customers pay from their own online banking environment.

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Bank  | |
| **API flow**  | `Redirect` | [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | Poland  | |
| **Currencies**  | EUR, PLN | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payment-methods/banks/dotpay/user-guide/processing-refunds) | 
| **Recurring payments**  | No | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

- You can [adjust payment link lifetimes](/faq/api/adjusting-payment-link-lifetimes/).

- You must provide the customer's first and last name to finalize payment, since the customer cannot enter them on the payment page. Otherwise the transaction is automatically rejected. 