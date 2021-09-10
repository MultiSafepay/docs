---
title: "Product rules"
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "TrustPay product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
aliases: 
    - /payment-methods/trustpay/trustpay-what-is-it/
    - /payments/methods/banks/trustpay/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | Czech Republic  | |
| **Currencies**  | CZK | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Recurring Payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Payment flow**  | [Redirect](/api/#trustpay) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Transactions expire after**  | 10 days | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- You can refund more than the original transaction value. See [Processing refunds](/tools/multisafepay-control/processing-refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}
