---
title: "Product rules"
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "SOFORT Banking product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/SOFORT.svg'
url: '/payments/methods/sofort-banking/product-rules/'
aliases: 
    - /payment-methods/bancontact/what-is-sofort-banking/
    - /payments/methods/banks/sofort-banking/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | Austria, Belgium, Germany, Italy, Spain, Switzerland, Poland  | |
| **Currencies**  | EUR {{< br >}} **Note:** British Pounds (GBP), Swiss Francs (CHF) and Polish Zloty (PLN) are **not** supported. | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Payment flow**  | [Direct](/api/#sofort-direct) / [Redirect](/api/#sofort-redirect) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | Yes | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 1 day | |
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


- The minimum amount for SOFORT transactions is 0,10 EUR.

- Transactions must be processed in the supported countries or a 1024 error is returned on completion of payment.