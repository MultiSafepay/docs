---
title: "Alipay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Alipay payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
aliases: 
    - /payment-methods/wallet/alipay/alipay-how-does-it-work
---

The table below shows a successful transaction flow from start to finish. 

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction. | Initialized | Initialized |
| 2. | MultiSafepay generates a payment link. |   |  |
| 3. | The customer completes the payment. | | |
| 4. | The transaction is successful. |  |  |
| 5. | Alipay settles the funds with MultiSafepay. | Completed | Completed |
| 6. | MultiSafepay adds the funds to your MultiSafepay balance. |  |  |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| Alipay has declined the transaction. | Declined | Declined   |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the predetermined period. | Expired | Expired |

For refund statuses, see [Processing refunds](/payment-methods/wallet/alipay/user-guide/processing-refunds/).



