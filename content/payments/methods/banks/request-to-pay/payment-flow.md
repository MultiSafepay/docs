---
title: "Request to Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Request to Pay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/RTP.svg'
url: '/payment-methods/request-to-pay/payment-flow/'
aliases: 
    - /payment-methods/bancontact/how-does-request-to-pay-work/
    - /payments/methods/banks/request-to-pay/payment-flow/
---

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant D as Deutsche Bank
    participant Me as Merchant

    C->>Mu: Selects Request to Pay at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page to select their bank, <br> then to online banking
    else Direct flow
    Mu->>C: Redirects customer to online banking
    end
    C->>D: Authenticates account and authorizes SEPA bank transfer
    D->>Mu: Transfers funds (within 24 hours, <br> if Instant SEPA not supported)
    Mu->>Me: Settles funds
    
{{< /mermaid >}}
&nbsp;  

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Payments | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Deutsche Bank. | Initialized | Initialized |
| Deutsche Bank has authorized the transaction and is transfering the funds. | Completed  | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Deutsche Bank declined the transaction. | Declined | Declined   |
| The customer cancelled the transaction at Deutsche Bank. | Void | Void |
| The customer didn't complete payment within 1 hour. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |
| Refund declined. | Declined | Declined |



        


