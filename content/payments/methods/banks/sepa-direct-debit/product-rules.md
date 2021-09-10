---
title : "Product rules"
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "SEPA Direct Debit product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/directdebit-en.svg'
aliases: 
    - /payment-methods/sepa-direct-debit/what-is-sepa-direct-debit/
    - /payment-methods/direct-debit/what-is-direct-debit/
    - /payment-methods/banks/direct-debit/what-is-direct-debit/
    - /payments/methods/banks/sepa-direct-debit/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | SEPA region  | [More information](https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2020-01/EPC409-09%20EPC%20List%20of%20SEPA%20Scheme%20Countries%20v2.6%20-%20January%202020.pdf) |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | Yes | See below.  |
| **Payment flow**  | [Direct](/api/#sepa-direct-debit-direct) / {{< br >}} [Redirect](/api/#sepa-direct-debit-redirect) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | Yes | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | Doesn't apply | |
| **Adjust payment link lifetimes**  | No | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- You cannot refund more than the original transaction value.

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

{{< details title="Chargebacks" >}}

SEPA Direct Debit payments are not fully guaranteed. The customer can request a [chargeback](/payments/chargebacks/) within 56 days, or for unauthorized transactions (i.e. without verifiable consent from the customer) within 13 months. You cannot dispute chargebacks.

This process involves both your bank and the customer's bank and may cost up to 65 EUR. 

This makes SEPA Direct Debit unsuitable for normal retail businesses (e.g. clothing).

{{< /details >}}