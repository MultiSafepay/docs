---
title: "ING Home Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "ING Home Pay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/ING_Homepay.svg'
url: '/payment-methods/ing-home-pay/payment-flow/'
aliases: 
    - /payment-methods/ing-home-pay/how-does-ing-home-pay-work/
    - /payments/methods/banks/ing-home-pay/payment-flow/
---


The table below shows a successful payment flow from start to finish.  

{{< details title="Order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer selects ING Home'Pay at checkout and is redirected to a [MultiSafepay payment page](/payment-pages/activation/). | Initialized | Initialized |
| 2. | The customer authenticates their account and completes the payment. {{< br >}} **Note:** If the customer doesn't click the **Return to website** button, MultiSafepay doesn't receive an update and the transaction status remains **Initialized**. We import our bank statements daily and all incoming payments are then finalized. | | |
| 3. | MultiSafepay collects the funds and settles them in your MultiSafepay balance.| Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the 5-day period. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund has been successfully processed. | Completed | Completed |




