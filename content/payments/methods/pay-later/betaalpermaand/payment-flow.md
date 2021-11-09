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

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant S as Santander
    participant Me as Merchant

    C->>Mu: Selects Betaal per Maand at checkout
    Mu->>C: Connects to Santander <br> (direct/redirect)
    S->>Mu: Authorizes the payment
    Mu->>S: Captures the funds
    Me->>C: Ships the order
    Note over Me,C: Manually change the order status to Shipped. 
    Me->>Mu: Provides track & trace code
    Mu->>S: Forwards track & trace code 
    S->>C: Sends invoice 
    Note over S,C: Settlement is now guaranteed!
    C->>S: Selects payment period and method, and completes payment 
    S->>Mu: Transfers funds within 5 business days <br> of order status changing to Shipped
    Mu->>Me: Settles funds within 5 business days

{{< /mermaid >}}
&nbsp;  
|  |  |  |
|---|---|---|
| **Direct flow** | The customer is redirected straight to Santander. | [API reference](/api/#santander-betaal-per-maand---direct) |
| **Redirect flow** | The customer is briefly redirected to a [MultiSafepay payment page](/payment-pages/) and then to Santander. | [API reference](/api/#/api/#santander-betaal-per-maand---redirect) |

## Payment statuses

**Order status**: Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status**: Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. {{< br >}} To cancel the transaction at this point, email <support@multisafepay.com> | Uncleared   | Initialized  |
| Betaal per Maand is authorizing the payment. | Uncleared   | Uncleared  |
| MultiSafepay has sent a capture to Betaal per Maand. {{< br >}} The transaction appears in both your MultiSafepay account and your [backend](/getting-started/glossary/#backend) via the [notification URL](/developer/api/notification-url/). {{< br >}} You can no longer cancel. You can only refund. | Completed  | Uncleared  |
| Ship the order. {{< br >}} You **must**: {{< br >}} - Ship the order to receive payment. {{< br >}} - [Change the order status to Shipped](/payments/methods/billing-suite/betaalpermaand/user-guide/changing-order-status-to-shipped/). {{< br >}} - [Provide the track-and-trace code](/payments/methods/billing-suite/betaalpermaand/faq/providing-track-and-trace/) to MultiSafepay. | Shipped | Uncleared |
| The transaction is complete. | Shipped    | Completed  |
| Betaal per Maand has declined the payment. Betaal per Maand only provides the reason directly to the customer, for privacy and compliance reasons. | Declined   | Declined   |
| The payment was cancelled.   | Void   | Cancelled   |
| The customer did not complete payment and the transaction expired. | Expired | Expired  |

## Refund statuses

| Description   | Order status | Transaction status |
|----|----|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund is complete.  | Completed      | Completed   |

