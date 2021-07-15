---
title : "About iDEAL QR"
breadcrumb_title: 'About iDEAL QR'
weight: 10
meta_title: "About iDEAL QR - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/iDeal_QR.svg' 
aliases: 
    - /payment-methods/idealqr/what-is-idealqr/
---

iDEAL QR is an additional service offered by the Dutch payment method [iDEAL](/payments/methods/banks/ideal).
 
Customers pay by using their smartphone to scan a QR code, on paper or on screen. This lets you bring offline payments online. 

**Note:** Most Dutch banks have their own QR code on their payment page, but this is not the same as iDEAL QR.

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Bank  | |
| **API flow**  | `Redirect` | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | The Netherlands  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payments/refunds-and-chargebacks/refunds/) | 
| **Recurring payments**  | No | [More information](/payments/about/recurring-payments/)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

- The lifetime of iDEAL QR payment links is 30 days by default. You can [adjust payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes/).

- To set the payment amount using the `min_amount` and `max_amount` parameters in the payment request, see API Reference&nbsp;–&nbsp;[iDEAL QR](/api/#ideal-qr).

- You can use the same iDEAL QR code more than once.

- You can generate more than one payment link for a single order ID. Subsequent transactions each have a unique order ID.

{{< details title="Refunds" >}}

- You can refund more than the original transaction value. See [Processing refunds](/tools/multisafepay-control/processing-refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Refunds can only be processed for payments linked to transactions. If no payment is linked to the transaction, the customer receives credit on their invoice instead.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}