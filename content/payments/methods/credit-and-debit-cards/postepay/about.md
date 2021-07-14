---
title: 'About Postepay'
breadcrumb_title: 'About Postepay'
weight: 10
meta_title: "About Postepay - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies"
layout: 'child'
read_more: '.'
aliases:
    - /payment-methods/branded-credit-cards/postepay/
    - /payment-methods/credit-and-debit-cards/branded-credit-cards/postepay/
---

Postepay is a popular Visa or Mastercard-branded credit card in Italy. An additional layer of security is provided by Verified by Visa or or MasterCard SecureCode (branded versions of [3D Secure](/security-and-legal/payment-regulations/about-3d-secure/)), which require cardholders to verify their identity.

### Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Credit card  | |
| **API flow**  | `Direct`/ {{< br >}} `Redirect`| [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | Italy  | |
| **Currencies**  | Multiple | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payments/refunds-and-chargebacks/refunds/) | 
| **Recurring payments**  | No | [More information](/payments/about/recurring-payments/)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

{{< details title="Postepay refund rules" >}}

- You cannot refund more than the amount of the original transaction.

- The maximum refund period is 180 days.

- MultiSafepay sends refunds to the issuer within 1 business day. 

- Whether or not the refund is visible to the customer depends on the issuer.

{{< /details >}}