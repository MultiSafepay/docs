---
title : "Product rules"
breadcrumb_title: 'Product rules'
weight: 10
meta_title: "iDEAL QR product rules - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/iDeal_QR.svg' 
url: '/payments/methods/ideal-qr/product-rules/'
aliases: 
    - /payment-methods/idealqr/what-is-idealqr/
    - /payments/methods/banks/idealqr/about/
---

|   |   |   |
|---|---|---|
| **Countries**  | The Netherlands  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Chargebacks**  | No | [More information](/payments/chargebacks/)  |
| **Payment flow**  | [Redirect](/api/#ideal-qr) | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Recurring Payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Transactions expire after**  | 1.5 hours | |
| **Adjust payment link lifetimes**  | Yes | [More information](/api/#adjust-payment-link-lifetimes)  |

{{< details title="Refunds" >}}
- [Full and partial refunds](/payments/refunds/) are supported.

- You can refund more than the original transaction value. See [Processing refunds](/tools/multisafepay-control/processing-refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Refunds can only be processed for payments linked to transactions. If no payment is linked to the transaction, the customer receives credit on their invoice instead.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}

- To set the payment amount using the `min_amount` and `max_amount` parameters in the payment request, see API reference&nbsp;–&nbsp;[iDEAL QR](/api/#ideal-qr).

- You can use the same iDEAL QR code more than once.

- You can generate more than one payment link for a single order ID. Subsequent transactions each have a unique order ID.