---
title: "CBC payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "CBC payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/cbc.svg'
aliases: 
    - /payment-methods/cbc/how-does-cbc-work/
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of settlement in your MultiSafepay balance

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer initiates a transaction and is redirected to a MultiSafepay PayV2 payment page. | Initialized | Initialized |
| 2. | The customer authenticates their account and completes the payment. {{< br >}} **Note:** If the customer doesn’t click the **Return to website** button, MultiSafepay doesn’t receive an update and the transaction status remains **Initialized**. We import our bank statements daily and all incoming payments are then finalized. | | |
| 3. | The transaction is successful.  |  |  |
| 4. | MultiSafepay collects the funds and adds them to your MultiSafepay balance.| Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the predetermined period. | Expired | Expired |

## Refund statuses

 Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund has been successfully processed. | Completed | Completed |





