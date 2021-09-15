---
title: 'Cartes Bancaires product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "Cartes Bancaires product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies"
layout: 'child'
logo: '/logo/Payment_methods/Cartes-Bancaire.svg'
url: '/payments/methods/cartes-bancaires/product-rules/'
aliases:
    - /payments/methods/credit-and-debit-cards/cartes-bancaires/user-guide/about-chargebacks/
    - /payments/methods/credit-and-debit-cards/cartes-bancaires/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | France  | |
| **Currencies**  | Multiple | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | Yes | [More information](/payments/chargebacks)  |
| **Payment flow**  | [Direct](/api/#create-a-direct-order) / [Redirect](/api/#create-a-redirect-order) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | Yes | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 1 hour | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- You cannot refund more than the amount of the original transaction.

- The maximum refund period is 180 days.

- MultiSafepay sends refunds to the issuer within 1 business day. 

- Whether or not the refund is visible to the customer depends on the issuer.

{{< /details >}}

{{< details title="Chargebacks" >}}

Cardholders who disagree with or do not recognise a transaction charged to their credit card can ask Cartes Bancaires to raise a dispute. Cartes Bancaires then notifies MultiSafepay and reclaims the transaction amount from you.

You are solely liable for paying for chargebacks

Cartes Bancaires gives cardholders the right to claim chargebacks for up to 180 days after the purchase.

For more information, see [Chargebacks](/payments/chargebacks).

{{< /details >}}

