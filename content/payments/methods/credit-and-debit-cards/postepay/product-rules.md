---
title: 'Product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "Postepay product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies"
layout: 'child'
read_more: '.'
url: '/payments/methods/postepay/product-rules/'
aliases:
    - /payment-methods/branded-credit-cards/postepay/
    - /payment-methods/credit-and-debit-cards/branded-credit-cards/postepay/
    - /payments/methods/credit-and-debit-cards/postepay/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | Italy  | |
| **Currencies**  | Multiple | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Payment flow**  | [Direct](/api/#create-a-direct-order) / [Redirect](/api/#create-a-redirect-order) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 1 hour | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- You cannot refund more than the amount of the original transaction.

- The maximum refund period is 180 days.

- MultiSafepay sends refunds to the issuer within 1 business day. 

- Whether or not the refund is visible to the customer depends on the issuer.

{{< /details >}}