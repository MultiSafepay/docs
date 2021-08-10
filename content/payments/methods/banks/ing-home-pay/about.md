---
title: "About ING Home Pay"
breadcrumb_title: 'About ING Home Pay'
weight: 10
meta_title: "About ING Home'Pay - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/ING_Homepay.svg'
aliases: 
    - /payment-methods/ing-home-pay/what-is-ing-home-pay/
---

ING Home'Pay is an online payment method for ING customers in Belgium. Customers are redirected to their ING banking environment to complete payment.

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Bank  | |
| **API flow**  | `Redirect` | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | Belgium  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payments/refunds/) | 
| **Recurring payments**  | No | [More information](/payments/features/recurring-payments/)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

You can [adjust payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes/).

{{< details title="Refunds" >}}

- MultiSafepay doesn't automatically receive the IBAN when a transaction is completed, but we import our bank statements daily. All incoming payments are then completed. You can process refunds after 1 business day.

- You can refund more than the original transaction value. See [Processing refunds](/tools/multisafepay-control/processing-refunds/).

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

- If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}
