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

In your MultiSafepay Control > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

|                       | Flow      | Order status | Transaction status |
|--------------------------------|-----------|---|-----------------------------------------------------------------------------------------|
| 1. | The customer initiates a transaction |    |   |
|  | The transaction is successful. | Completed  | Initialized  |
| 2. | MultiSafepay sends a capture to E-invoicing. | Shipped | Initialized |
| 3. | E-invoicing confirms the transaction. | | |
| 4. | Ship the order. | | |
| 5. | E-invoicing sends the customer an invoice. |     |   |
| 6. | MultiSafepay receives the funds and adds them to your MultiSafepay balance.| | |

See also:

- [Viewing transactions](/payment-methods/billing-suite/e-invoicing/user-guide/viewing-transactions/)
- [Batching transactions for subscriptions](/payment-methods/billing-suite/e-invoicing/user-guide/batching-transactions/)

## Other statuses

| Description | Order status | Transaction status |
|---|---|---|
| E-invoicing rejected the transaction. | Declined | Declined |
| The transaction was not completed and it expired. | Expired | Expired |
| The transaction has been cancelled. | Void | Cancelled |

## Refund statuses

For how to process refunds, see [Processing refunds](/payment-methods/billing-suite/e-invoicing/faq/processing-refunds/).

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund has been successfully processed.  | Completed | Completed |