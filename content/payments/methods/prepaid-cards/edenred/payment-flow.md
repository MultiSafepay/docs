---
title: "Edenred payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Edenred payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer selects Edenred at checkout. | |  |
| 2. | The customer is redirected and signs in to Edenred with their username, password, and PIN. {{< br >}} They authorize MultiSafepay to access their Edenred account. |   |  |
| 3. | Edenred confirms successful authentication and that enough funds are available on the voucher. | | |
| 4. | Edenred transfers the funds to the merchant and notifies MultiSafepay. | Completed | Completed |


