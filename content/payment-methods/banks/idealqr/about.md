---
title : "About iDEAL QR"
breadcrumb_title: 'About iDEAL QR'
weight: 10
meta_title: "About iDEAL QR - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/iDeal_QR.svg' 
aliases: 
    - /payment-methods/idealqr/what-is-idealqr/
---

iDEAL QR is an additional service offered by the Dutch payment method [iDEAL](/payment-methods/banks/ideal).
 
Customers pay by using their smartphone to scan a QR code, on paper or on screen. This lets you bring offline payments online. 

**Note:** Most Dutch banks have their own QR code on their payment page, but this is not the same as iDEAL QR.

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Bank  | |
| **API flow**  | `Redirect` | [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | The Netherlands  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payment-methods/banks/idealqr/user-guide/processing-refunds) | 
| **Recurring payments**  | No | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

- The lifetime of iDEAL QR payment links is 30 days by default. You can [adjust payment link lifetimes](/faq/api/adjusting-payment-link-lifetimes/).

- To set the payment amount using the `min_amount` and `max_amount` parameters in the payment request, see API Reference&nbsp;–&nbsp;[iDEAL QR](/api/#ideal-qr).

- You can use the same iDEAL QR code more than once.

- You can generate more than one payment link for a single order ID. Subsequent transactions each have a unique order ID.