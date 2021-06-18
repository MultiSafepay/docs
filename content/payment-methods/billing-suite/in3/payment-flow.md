---
title: 'in3 payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "in3 payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish and status change descriptions"
layout: 'child'
logo: '/svgs/in3.svg'
---

The table below shows a successful in3 payment flow from start to finish.  

In your MultiSafepay Control > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

### Payment flow

|                       | Flow      | Order status | Transaction status |
|--------------------------------|-----------|---|-----------------------------------------------------------------------------------------|
| 1. | The customer initiates a transaction, is redirected to in3, and enters their details. | Initialized   | Initialized  |
| 2. | in3 authorizes the payment. |   |   |
| 3. | The customer has 5 minutes to pay the first installment, or the transaction is cancelled. {{< br >}} The first installment is required to create the order. | Uncleared  | Initialized  |
| 4. | The customer pays the first installment. {{< br >}} Settlement is now guaranteed. | Completed  | Uncleared  |
| 5. | Ship the order. | | |
| 6. | MultiSafepay adds the funds to your MultiSafepay balance (within 15 days of the first installment). | Completed | Completed |
| 7. | The customer has 30 days to pay the second installment. |  | |
| 8. | The customer has 60 days to pay the third installment. |  | |


### Unsuccessful statuses
You can cancel payments before the funds are captured. After the funds are captured you can only process a refund.

| Description                      | Order status      | Transaction status |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| in3 has declined the payment. No order was created.    | Declined   | Declined   |
| The payment was cancelled or abandoned. | Void    | Void    |

### Refund statuses

For how to process refunds, see [Processing refunds](/payment-methods/billing-suite/in3/faq/processing-refunds).

| Description                      | Order status      | Transaction status |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| in3 has successfully processed a full or partial refund. | Completed    | Completed   |
| in3 has declined a full or partial refund request.  | Declined      | Declined   |
