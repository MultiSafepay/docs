---
title: 'E-Invoicing payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "E-Invoicing payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/e-invoicing/payment-flow/'
aliases:
    - /payments/methods/billing-suite/e-invoicing/payment-flow/
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}
For each payment in your MultiSafepay account, there are two statuses that change as payment progresses:

**Order status:** The progression of the customer's order with you, independent of the payment  
**Transaction status:** The progression towards settling the funds in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer selects E-Invoicing at checkout. | Initialized   | Initialized  |
| 2. | E-Invoicing authorizes the payment. | Completed  | Initialized  |
| 3. | Once authorized, MultiSafepay sends a capture to E-Invoicing. |  |  |
| 4. | Ship the order. {{< br >}} You **must**: {{< br >}} - Ship the order to receive payment. {{< br >}} - [Change the order status to Shipped](/payments/methods/billing-suite/e-invoicing/user-guide/changing-order-status-to-shipped/). | Shipped | Initialized |
| 6. | E-Invoicing invoices the customer. |     |   |
| 7. | The customer completes payment. |     |   |
| 8. | MultiSafepay collects the funds and settles them in your MultiSafepay balance. | Completed    | Completed  |

See also:

- [Viewing transactions](/payments/methods/billing-suite/e-invoicing/user-guide/viewing-transactions/)
- [Batching transactions for subscriptions](/payments/methods/billing-suite/e-invoicing/user-guide/batching-transactions/)

## Unsuccessful statuses
You can cancel payments before the funds are captured. After the funds are captured, you can only process a refund.

| Description | Order status | Transaction status |
|---|---|---|
| E-Invoicing has declined the payment. | Declined | Declined |
| The payment has been cancelled. | Void | Cancelled |
| The payment was not completed and it expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund has been successfully processed.  | Completed | Completed |

