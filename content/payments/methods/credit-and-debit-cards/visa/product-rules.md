---
title: 'Visa product rules'
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "Visa product  - MultiSafepay Docs"
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
url: '/payments/methods/visa/product-rules/'
aliases:
    - /payment-methods/credit-and-debit-cards/visa/what-is-visa
    - /payment-methods/credit-and-debit-cards/visa/what-is-a-chargeback
    - /payments/methods/credit-and-debit-cards/visa/user-guide/about-chargebacks/
    - /payments/methods/credit-and-debit-cards/visa/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | Worldwide  | |
| **Currencies**  | Multiple | [More information](/faq/general/supported-currencies)  | 
| **Chargebacks**  | Yes | See below.  |
| **Payment flow**  | [Redirect](/api/#visa) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring payments**  | Yes | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 1 hour | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |


{{< details title="Refunds" >}}

- [Full and partial refunds](/payments/refunds/) are supported.

- You cannot refund more than the amount of the original transaction.

- The maximum refund period is 180 days. After this period, we recommend processing refunds by bank transfer.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- The customer receives the refund in the bank account they originally paid from within the next business day.

- Depending on the customer's issuer, the amount may not appear directly on their card. We recommend that they contact the issuer. If they need an [acquirer reference number (ARN)](/credit-and-debit-cards/glossary/#acquirer-reference-number-arn), they can email the Support Team at <support@multisafepay.com> 

- If you process a partial refund on the same day, this is technically called a "reversal", but for simplicity is logged as a refund in your MultiSafepay account. On customer credit card statements, the transaction may either be adjusted to the new amount (partial reversal) _or_ not debited at all (full reversal).

{{< /details >}}

{{< details title="Chargebacks" >}}

Cardholders who disagree with or do not recognise a transaction charged to their credit card can ask Visa to raise a dispute. Visa then notifies MultiSafepay and reclaims the transaction amount from you. 

You are solely liable for paying chargebacks.

Visa gives cardholders the right to claim chargebacks for up to 180 days after the purchase.

For more information, see [Chargebacks](/payments/chargebacks).

To help reduce chargebacks, see [Your logo in online banking](/payments/methods/credit-and-debit-cards/user-guide/your-logo-online-banking).

{{< /details >}}