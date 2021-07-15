---
title: 'About Cartes Bancaires'
breadcrumb_title: 'About Cartes Bancaires'
weight: 10
meta_title: "About Cartes Bancaires - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies"
layout: 'child'
logo: '/logo/Payment_methods/Cartes-Bancaire.svg'
aliases:
    - /payments/methods/credit-and-debit-cards/cartes-bancaires/user-guide/about-chargebacks/
---

Cartes Bancaires is a popular Visa-branded credit card in France. An additional layer of security is provided by Verified by Visa (Visa's version of [3D Secure](/security-and-legal/payment-regulations/about-3d-secure/)), which requires cardholders to verify their identity.

### Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Credit card  | |
| **API flow**  | `Direct`/ {{< br >}} `Redirect`| [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | France  | |
| **Currencies**  | Multiple | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payments/refunds-and-chargebacks/refunds/) | 
| **Recurring payments**  | Yes | [More information](/payments/about/recurring-payments/)  |
| **Chargebacks**  | Yes | [More information](/payments/refunds-and-chargebacks/chargebacks)  |

## Product rules

{{< details title="Refunds" >}}

- You cannot refund more than the amount of the original transaction.

- The maximum refund period is 180 days.

- MultiSafepay sends refunds to the issuer within 1 business day. 

- Whether or not the refund is visible to the customer depends on the issuer.

{{< /details >}}

{{< details title="Chargebacks" >}}

Cardholders who disagree with or do not recognise a transaction charged to their credit card can ask Cartes Bancaires to raise a dispute. Cartes Bancaires then notifies MultiSafepay and reclaims the transaction amount from you.

You are solely liable for paying for chargebacks

Cartes Bancaires gives cardholders the right to claim chargebacks for up to 180 days after the purchase.

For more information, see [Chargebacks](/payments/refunds-and-chargebacks/chargebacks).

{{< /details >}}

