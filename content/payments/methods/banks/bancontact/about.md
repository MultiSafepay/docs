---
title: "About Bancontact"
breadcrumb_title: 'About Bancontact'
weight: 10
meta_title: "About Bancontact - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/bancontact.svg'
aliases: 
    - /payment-methods/bancontact/what-is-bancontact/
---

Bancontact is a leading Belgian payment method that supports online, mobile app, and POS payments. Bancontact is a household name and supported by over 80% of Belgian webshops. It was formerly known as Mister Cash.

Once a payment is completed, the customer cannot reverse it and Bancontact guarantees settlement.

Non-mobile payments always use [3D Secure](/faq/general/glossary/#3d-secure) 1.0 verification.

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Bank  | |
| **API flow**  | `Redirect` | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | Belgium  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payments/refunds-and-chargebacks/refunds/) | 
| **Recurring payments**  | Yes | [More information](/payments/about/recurring-payments/)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

You can [adjust payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes/).

{{< details title="Refunds" >}}
- You can refund more than the original transaction value. See [Processing refunds](/tools/multisafepay-control/processing-refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}



