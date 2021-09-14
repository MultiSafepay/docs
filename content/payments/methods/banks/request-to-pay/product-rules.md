---
title: "Product rules"
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "Request to Pay product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/RTP.svg'
url: '/payments/methods/request-to-pay/product-rules/'
aliases: 
    - /payment-methods/bancontact/what-is-request-to-pay/
    - /payments/methods/banks/request-to-pay/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | Germany  | More countries will follow as more banks migrate to PSD2 APIs. |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Payment flow**  | [Direct](/api/#request-to-pay-direct) / [Redirect](/api/#request-to-pay-redirect) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 1 hour | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- All refunds are processed by Deutsche Bank.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

- Request to Pay supports both instant and non-instant SEPA bank transfers.
- A minimum amount of 1 EUR and maximum of 15,000 EUR applies.