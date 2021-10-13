---
title: "EPS product rules"
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "EPS product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/bancepsontact.svg'
url: '/payment-methods/eps/product-rules/'
aliases: 
    - /payment-methods/eps/what-is-eps/
    - /payments/methods/banks/eps/about/
    - /payments/methods/eps/product-rules/
---

|   |   |   |
|---|---|---|
| **Countries**  | Austria  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Payment flow**  | [Redirect](/api/#eps) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | Doesn't apply | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}
- [Full and partial refunds](/payments/refunds/) are supported.

- You cannot refund more than the original transaction value.

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}