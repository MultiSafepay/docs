---
title: 'About Dankort'
breadcrumb_title: 'About Dankort'
weight: 10
meta_title: "About Dankort - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies"
layout: 'child'
read_more: '.'
aliases:
    - /payment-methods/branded-credit-cards/dankort-what-is-it/
    - /payment-methods/credit-and-debit-cards/branded-credit-cards/dankort-what-is-it/
    - /payment-methods/credit-and-debit-cards/dankort-what-is-it/
    - /payments/methods/credit-and-debit-cards/dankort/user-guide/about-chargebacks/
---

Dankort is a popular Visa-branded credit card in Denmark. An additional layer of security is provided by Verified by Visa (Visa's version of [3D Secure](/security-and-legal/payment-regulations/about-3d-secure/)), which requires cardholders to verify their identity.

### Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Credit card  | |
| **API flow**  | `Direct`/ {{< br >}} `Redirect`| [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | Denmark  | |
| **Currencies**  | Multiple | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payments/refunds/) | 
| **Recurring Payments**  | Yes | [More information](/payments/features/recurring-payments/)  |
| **Chargebacks**  | Yes | [More information](/payments/chargebacks) |

## Product rules

{{< details title="Refunds" >}}

- You cannot refund more than the amount of the original transaction.

- The maximum refund period is 180 days.

- MultiSafepay sends refunds to the issuer within 1 business day. 

- Whether or not the refund is visible to the customer depends on the issuer.

{{< /details >}}

{{< details title="Chargebacks" >}}

Cardholders who disagree with or do not recognise a transaction charged to their credit card can ask Dankort to raise a dispute. Dankort then notifies MultiSafepay and reclaims the transaction amount from you.

You are solely liable for paying for chargebacks.

Dankort gives cardholders the right to claim chargebacks for up to 180 days after the purchase.

For more information, see [Chargebacks](/payments/chargebacks).

{{< /details >}}