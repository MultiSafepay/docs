---
title : "About SEPA Direct Debit"
breadcrumb_title: 'About SEPA Direct Debit'
weight: 10
meta_title: "About SEPA Direct Debit - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/directdebit-en.svg'
aliases: 
    - /payment-methods/sepa-direct-debit/what-is-sepa-direct-debit/
    - /payment-methods/direct-debit/what-is-direct-debit/
    - /payment-methods/banks/direct-debit/what-is-direct-debit/
---

SEPA Direct Debit is a European payment method where customers authorize automatic one-off or recurring debits directly from their bank account. It is available in 36 countries and supports SOFORT Banking and iDEAL.

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Bank  | |
| **API flow**  | `Direct`/ {{< br >}} `Redirect` | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | SEPA region  | [More information](https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2020-01/EPC409-09%20EPC%20List%20of%20SEPA%20Scheme%20Countries%20v2.6%20-%20January%202020.pdf) |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payments/refunds-and-chargebacks/refunds/) | 
| **Recurring payments**  | Yes | [More information](/payments/about/recurring-payments/)  |
| **Chargebacks**  | Yes | [More information](/faq/chargebacks)  |

## Product rules

You cannot [adjust payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes/).

{{< details title="SEPA Direct Debit refund rules" >}}

- You cannot refund more than the original transaction value.

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

## Chargebacks
SEPA Direct Debit payments are not fully guaranteed. The customer can request a [chargeback](/faq/chargebacks/) within 56 days, or for unauthorized transactions (i.e. without verifiable consent from the customer) within 13 months. You cannot dispute chargebacks.

This process involves both your bank and the customer's bank and may cost up to 65 EUR. 

This makes SEPA Direct Debit unsuitable for normal retail businesses (e.g. clothing).