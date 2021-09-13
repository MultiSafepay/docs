---
title: "Product rules"
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "Trustly product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/trustly.svg'
url: '/payments/methods/trustly/product-rules/'
aliases: 
    - /payment-methods/trustly/what-is-trustly/
    - /payments/methods/banks/trustly/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, United Kingdom  | |
| **Currencies**  | EUR, GBP, SEK | [More information](/faq/general/supported-currencies) | 
| **Payment flow**  | [Redirect](/api/#trustly) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Transactions expire after**  | 2 hours | |
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
