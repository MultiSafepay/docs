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
| 1. | The customer initiates a transaction. | |  |
| 2. | MultiSafepay generates a window for the customer to log in to Edenred. |   |  |
| 3. | The customer enters their Edenred username, password and pin number.| | |
| 4. | The customer authorizes MultiSafepay to access their Edenred account.| | |
| 5. | Edenred confirms successful authentication and that enough funds are available. | | |
| 6. | Edenred transfers funds to the merchant and notifies MultiSafepay. | Completed | Completed |


