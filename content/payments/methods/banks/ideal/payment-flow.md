---
title: "iDEAL payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "iDEAL payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/iDeal.svg'
url: '/payment-methods/ideal/payment-flow/'
aliases: 
    - /payment-methods/ideal/how-does-ideal-work/
    - /payments/methods/banks/ideal/payment-flow/
    - /payments/methods/banks/idealqr/payment-flow/
---
This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant CB as Customer's bank
    participant Me as Merchant

    alt Direct flow
    C->>Mu: Selects iDEAL and their bank at checkout
    Mu->>C: Redirects customer to their online banking environment
    else Redirect flow
    C->>Mu: Selects iDEAL (QR) at checkout
    Mu->>C: Redirects customer to payment page to select their bank, <br> and then to their online banking environment
    end
    C->>CB: Authenticates account/scans QR code and completes payment
    CB->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;   

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction via their bank. | Void   | Void/Cancelled   |
| iDEAL processing error. | Declined   | Declined   |
| The customer didn't complete payment within 1.5 hours. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |
| The refund is pending (banking only).  | Reserved | Reserved |
| The refund is complete. | Completed | Completed |

