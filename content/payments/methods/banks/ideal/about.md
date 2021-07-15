---
title: "About iDEAL"
breadcrumb_title: 'About iDEAL'
weight: 10
meta_title: "About iDEAL - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Key information, supported countries and currencies, product rules"
layout: 'child'
logo: '/logo/Payment_methods/iDeal.svg'
aliases: 
    - /payment-methods/ideal/what-is-ideal/
---
iDEAL is an inter-bank payment method that links all major Dutch retail banks. It is the leading payment method in the Netherlands, comprising around 60% of all online transactions.

Customers pay via a mobile banking app or in their own online banking environment. Once a payment is completed, the customer cannot reverse it and iDEAL guarantees settlement.

To increase transparency for customers, the name of your website appears on the iDEAL payment page and "Your-website-name by MultiSafepay" on the customer's bank statement. 

## Summary

|   |   |   |
|---|---|---|
| **Payment type**   | Bank  | |
| **API flow**  | `Direct`/`Redirect` | [More information](/developer/api/difference-between-direct-and-redirect) |
| **Countries**  | The Netherlands  | |
| **Currencies**  | EUR | [More information](/faq/general/supported-currencies) | 
| **Refunds**  | Full and partial  | [More information](/payments/refunds-and-chargebacks/refunds/) | 
| **Recurring payments**  | Yes | [More information](/payments/about/recurring-payments/)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

## Product rules

You can [adjust payment link lifetimes](/developer/api/adjusting-payment-link-lifetimes/).

{{< details title="Refunds" >}}
- You cannot refund more than the amount of the original transaction.

- There is no time limit on refunding successful transactions, so long as the receiving bank can process the refund.

- Refunds are only processed if there are enough funds in your MultiSafepay balance.

- Refunds can only be processed for payments linked to transactions. If no payment is linked to the transaction, the customer receives credit on their invoice instead.

- While the transaction status is **Initialized**, you can cancel the refund. Once the status changes to **Completed**, the refund has been processed. 

- The customer receives the refund in the bank account they originally paid from within the next business day.

If a refund fails, email the Support Team at <support@multisafepay.com> 

{{< /details >}}