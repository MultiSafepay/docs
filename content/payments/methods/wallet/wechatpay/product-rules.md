---
title: 'Product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "WeChat Pay product rules - MultiSafepay Docs"
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
url: '/payment-methods/wechatpay/product-rules/'
aliases:
    - /payments/methods/wechatpay/product-rules/
---

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide  | |
| **Currencies**  | EUR | | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Payment flow**  | [Direct](/api/#wechat-pay---direct) / [Redirect](/api/#wechat-pay---redirect) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 2 hours | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com>

{{< /details >}}

- To request support for more currencies, email your account manager at <sales@multisafepay.com>
