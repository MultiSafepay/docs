---
title: 'E-invoicing payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "E-invoicing payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
---

The table below shows a successful E-invoicing payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction. |    |   |
| 2. | E-invoicing authorizes the payment. | Completed  | Initialized  |
| 3. | Once authorized, MultiSafepay sends a capture to E-invoicing. |  |  |
| 4. | Ship the order. | Shipped | Initialized |
| 5. | E-invoicing invoices the customer. |     |   |
| 6. | The customer completes the payment. |     |   |
| 7. | E-invoicing settles the funds with MultiSafepay. |     |   |
| 8. | MultiSafepay adds the funds to your MultiSafepay balance.| | |

See also:

- [Viewing transactions](/payment-methods/billing-suite/e-invoicing/user-guide/viewing-transactions/)
- [Batching transactions for subscriptions](/payment-methods/billing-suite/e-invoicing/user-guide/batching-transactions/)

## Unsuccessful statuses
You can cancel payments before the funds are captured. After the funds are captured you can only process a refund.

| Description | Order status | Transaction status |
|---|---|---|
| E-invoicing has declined the payment. | Declined | Declined |
| The payment has been cancelled. | Void | Cancelled |
| The payment was not completed and it expired. | Expired | Expired |

For refund statuses, see [Processing refunds](/payment-methods/billing-suite/e-invoicing/user-guide/processing-refunds/).

