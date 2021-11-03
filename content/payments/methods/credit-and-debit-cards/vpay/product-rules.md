---
title: 'V Pay product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "V Pay product rules - MultiSafepay Docs"
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
url: '/payments/methods/vpay/product-rules/'
aliases:
    - /payment-methods/vpay/what-is-vpay/
    - /payments/methods/credit-and-debit-cards/vpay/user-guide/about-chargebacks/
---

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide  | |
| **Currencies**  | Multiple | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | Yes | See below. |
| **Payment flow**  | [Redirect](/api/#visa) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 1 hour | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- You cannot refund more than the amount of the original transaction.

- The maximum refund period is 180 days. After this period, we recommend processing refunds by bank transfer.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- The customer receives the refund in the bank account they originally paid from within the next business day.

{{< /details >}}

{{< details title="Chargebacks" >}}

Cardholders who disagree with or do not recognise a transaction charged to their credit card can ask V Pay to raise a dispute. V Pay then notifies MultiSafepay and reclaims the transaction amount from you.

You are solely liable for paying for chargebacks.

V Pay gives cardholders the right to claim chargebacks for up to 180 days after the purchase.

For more information, see [Chargebacks](/payments/chargebacks).

{{< /details >}}