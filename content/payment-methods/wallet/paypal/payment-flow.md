---
title: "PayPal payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "PayPal payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
aliases: 
    - /payment-methods/paypal/how-does-paypal-work
---

The table below shows a successful transaction flow from start to finish. 

**Note:** MultiSafepay does not collect funds for PayPal.

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction. | Initialized | Initialized |
| 2. | PayPal generates a payment link. |   |  |
| 3. | The customer completes the payment. | | |
| 4. | The transaction is successful, and PayPal adds the funds to your PayPal business account. | Completed | Initialized |
| 5. | Orders cannot be shipped while the transaction status is **Initialized**. To ship the order, set the transaction status to **Completed**. | Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The payment was made in a currency that is not enabled in your PayPal business account. Enable the currency for the order status to change to completed. {{< br >}} You can only decline or authorize **Uncleared** transactions in your PayPal account. | Uncleared | Initialized |
| PayPal has declined the transaction. | Declined | Declined   |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the predetermined period. | Expired | Expired |

For refund statuses, see [Processing refunds](/payment-methods/wallet/paypal/user-guide/processing-refunds/).




