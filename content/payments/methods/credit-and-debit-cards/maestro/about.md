---
title: 'About Maestro'
breadcrumb_title: 'About Maestro'
weight: 10
meta_title: "About Maestro - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
aliases:
    - /payment-methods/maestro/what-is-maestro/
---

Maestro is a debit card service owned by Mastercard. It is accepted across Europe and in many other countries, and is especially popular in Belgium. An additional layer of security is provided by mandatory [3D Secure](/security-and-legal/payment-regulations/about-3d-secure/) authentication, which requires cardholders to verify their identity.

### Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Debit card  | |
| **API flow**  | `Direct`/ {{< br >}} `Redirect`| [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | Worldwide  | |
| **Currencies**  | Multiple | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payments/refunds-and-chargebacks/refunds/) | 
| **Recurring payments**  | Yes | [More information](/payments/about/recurring-payments/)  |
| **Chargebacks**  | Yes | [More information](/faq/chargebacks) |

## Product rules

You can [adjust payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes/).

{{< details title="Maestro refund rules" >}}

- You cannot refund more than the amount of the original transaction.

- The maximum refund period is 180 days. After this period, we recommend processing refunds by bank transfer.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- The customer receives the refund in the bank account they originally paid from within the next business day.

- Depending on the customer's issuer, the amount may not appear directly on their card. We recommend that they contact the issuer. If they need an acquirer reference number (ARN), they can email the Support Team at <support@multisafepay.com> 

{{< /details >}}
