---
title: 'About V Pay'
breadcrumb_title: 'About V Pay'
weight: 10
meta_title: "About V Pay - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
aliases:
    - /payment-methods/vpay/what-is-vpay/
    - /payments/methods/credit-and-debit-cards/vpay/user-guide/about-chargebacks/
---

V Pay is a debit card service owned by Visa. It is accepted across Europe. An additional layer of security is provided by mandatory [3D Secure](/security-and-legal/payment-regulations/about-3d-secure/) authentication, which requires cardholders to verify their identity.

### Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Debit card  | |
| **API flow**  | `Direct`/ {{< br >}} `Redirect`| [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | Worldwide  | |
| **Currencies**  | Multiple | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payments/refunds-and-chargebacks/refunds/) | 
| **Recurring payments**  | No | [More information](/payments/about/recurring-payments/)  |
| **Chargebacks**  | Yes | [More information](/payments/refunds-and-chargebacks/chargebacks) |

## Product rules

You can [adjust payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes/).

{{< details title="Refunds" >}}

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

For more information, see [Chargebacks](/payments/refunds-and-chargebacks/chargebacks).

{{< /details >}}