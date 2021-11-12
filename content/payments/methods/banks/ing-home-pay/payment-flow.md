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

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant I as ING
    participant Me as Merchant

    C->>Mu: Selects ING Home'Pay at checkout
    Mu->>C: Connects to ING (direct/redirect)
    C->>I: Authenticates account and completes payment
    I->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Direct flow** | The customer is redirected to their online banking environment. | [API reference](/api/#ing-homepay---direct) |
| **Redirect flow** | The customer is redirected first to a [MultiSafepay payment page](/payment-pages/), and then to their online banking environment. | [API reference](/api/#ing-homepay---redirect) |

## Payment statuses

**Order status**: Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status**: Changes as the funds progress towards settlement in your MultiSafepay balance

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The transaction is complete.| Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment within 5 days and the transaction expired . | Expired | Expired |

**Note:** If the customer doesn't click the **Return to website** button, MultiSafepay doesn't receive an update and the transaction status remains **Initialized**.  
We import our bank statements daily and finalize all incoming payments.

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved | Reserved |
| The refund is complete. | Completed | Completed |

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).


