---
title: 'Betaal per Maand payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Betaal per Maand payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/betaal-per-maand/payment-flow/'
aliases: 
    - /payments/methods/billing-suite/betaalpermaand/payment-flow/
---

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant S as Santander
    participant Me as Merchant

    C->>Mu: Selects Betaal per Maand at checkout
    alt Redirect flow
    Mu->>C: Redirects customer briefly to payment page, <br> and then to Santander
    else Direct flow
    Mu->>C: Redirects customer to Santander
    end
    S->>Mu: Authorizes the payment
    Mu->>S: Captures the funds
    Me->>C: Ships the order and manually changes status to Shipped
    Note over Me,C: Manually change the order status to Shipped. 
    Me->>Mu: Provides track & trace code
    Mu->>S: Forwards track & trace code 
    S->>C: Sends invoice. Settlement is now guaranteed.
    C->>S: Selects payment period and method, and completes payment 
    S->>Mu: Transfers funds within 5 business days <br> of changing order status to Shipped
    Mu->>Me: Settles funds within 5 business days

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
| The customer has been redirected to Santander. {{< br >}} To cancel the transaction, email <support@multisafepay.com> | Initialized   | Initialized  |
| The customer has completed the pre-form and Santander is authorizing the transaction. | Uncleared | Initialized |
| Santander has authorized the transaction and the funds are awaiting capture. {{< br >}} You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| **Important:** {{< br >}} - [Manually change the order status to Shipped](/about-payments/pay-later-shipped-status/). {{< br >}} - [Send us the track-and-trace code](/payment-methods/betaal-per-maand/track-and-trace/). {{< br >}} You must ship to receive payment. | Shipped | Uncleared |
| MultiSafepay has collected payment. | Shipped    | Completed  |
| Santander declined the transaction. {{< br >}} They only provide the reason directly to the customer, for privacy and compliance reasons. | Declined   | Declined   |
| You cancelled the transaction before capture.   | Void   | Void   |
| The customer didn't complete payment or the funds weren't captured within 1&nbsp;day. | Expired | Expired  |

## Refund statuses

| Description   | Order status | Transaction status |
|----|----|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund is complete.  | Completed      | Completed   |

