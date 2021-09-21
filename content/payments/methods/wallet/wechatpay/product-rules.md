---
title: 'Product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "WeChat Pay product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
url: '/payments/methods/wechatpay/product-rules/'
---

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide  | |
| **Currencies**  | EUR | | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Payment flow**  | [Direct](/api/#wechat-pay---direct) / [Redirect](/api/#wechat-pay---redirect) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 2 hours | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- You can refund more than the original amount. See [Processing refunds](/tools/multisafepay-control/processing-refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com>

{{< /details >}}

- To request support for more currencies, email your account manager at <sales@multisafepay.com>

- Currency conversion is processed in EUR only.
