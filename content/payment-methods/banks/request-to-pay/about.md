---
title: "About Request to Pay"
breadcrumb_title: 'About Request to Pay'
weight: 10
meta_title: "About Request to Pay - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/RTP.svg'
aliases: 
    - /payment-methods/bancontact/what-is-request-to-pay/
---

Request to Pay is a Deutsche Bank payment method, previously known as Direct Bank Transfer, based on the PSD2 Open Banking API. Customers are redirected to Deutsche Bank online banking, authenticate themselves, and authorize a secure SEPA transfer. 

Settlement is instant (if supported) or within 24 hours. The funds are transferred directly to your business bank account, instead of your MultiSafepay balance, which simplifies reconciliation.

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Bank  | |
| **API flow**  | `Direct`/ {{< br >}} `Redirect` | [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | Germany  | More countries will follow as more banks migrate to PSD2 APIs. |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payment-methods/banks/request-to-pay/user-guide/processing-refunds) | 
| **Recurring payments**  | No | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

- Request to Pay supports both instant and non-instant SEPA bank transfers.
- A minimum amount of 1 EUR and maximum of 15,000 EUR applies.