---
title: "About SOFORT Banking"
breadcrumb_title: 'About SOFORT Banking'
weight: 10
meta_title: "About SOFORT Banking - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/SOFORT.svg'
aliases: 
    - /payment-methods/bancontact/what-is-sofort-banking/
---

SOFORT Banking is a payment method available in several European countries, and particularly popular in Germany. It integrates directly with the customer's bank like a direct bank transfer. The customer verifies the payment, which reduces the risks associated with traditional transfers. 

Once a payment is completed, the customer cannot reverse it and SOFORT Banking guarantees settlement.

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Bank  | |
| **API flow**  | `Direct`/`Redirect` | [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | Austria, Belgium, Germany, Italy, Spain, Switzerland, Poland  | |
| **Currencies**  | EUR {{< br >}} **Note:** British Pounds (GBP), Swiss Francs (CHF) and Polish Zloty (PLN) are **not** supported. | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payment-methods/banks/sofort-banking/user-guide/processing-refunds) | 
| **Recurring payments**  | Yes | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

- You can [adjust payment link lifetimes](/faq/api/adjusting-payment-link-lifetimes/).

- The minimum amount for SOFORT transactions is 0,10 EUR.

- Transactions must be processed in the supported countries or a 1024 error is returned on completion of payment.