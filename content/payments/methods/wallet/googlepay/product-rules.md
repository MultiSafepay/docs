---
title: 'Google Pay product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "Product rules - Google Pay - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
noindex: '.'
---

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide | [More information](https://support.google.com/pay/answer/9023773?hl=en#zippy=%2Cpay-online-or-in-apps) |
| **Currencies**  | Multiple | | 
| **Chargebacks**  | Yes | [More information](/faq/chargebacks)  |
| **Payment flow**  | [Direct](/api/#google-pay---direct) / [Redirect](/api/#google-pay---redirect) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 1 hour | |
| **Adjust payment link lifetimes** | Yes | [More information](/developer/api/adjusting-payment-link-lifetimes/) |

**Note:** Google Pay transactions are processed as credit card transactions and follow similar product rules.

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- You cannot refund more than original amount.

- The maximum refund period for Maestro, Mastercard, and Visa transactions is 180 days. After this, we recommend processing refunds by bank transfer.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- The customer receives the refund in their Google Pay account and it appears on their credit card statement within the next business day.

{{< /details >}}
