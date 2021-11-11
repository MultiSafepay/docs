---
title: "WeChat Pay payment flow"
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "WeChat Pay payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
url: '/payment-methods/wechat-pay/payment-flow/'
aliases:
    - /payments/methods/wallet/wechatpay/payment-flow/
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant W as WeChat Pay
    participant Me as Merchant

    C->>Mu: Selects WeChat Pay at checkout
    Mu->>C: Connects to WeChat Pay and generates QR code (direct/redirect)
    C->>W: Scans code with WeChat app to complete payment 
    W->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;  

|  |  |  |
|---|---|---|
| **Direct flow** | The customer selects WeChat Pay at checkout and MultiSafepay displays a WeChat QR code. | [API reference](/api/#wechat-pay---direct) |
| **Redirect flow** | The customer is redirected to a [MultiSafepay payment page](/payment-pages/) containing a WeChat QR code. | [API reference](/api/#wechat-pay---redirect) |   

## Payment statuses

**Order status**: Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status**: Changes as the funds progress towards settlement in your MultiSafepay balance

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The transaction is complete. | Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment within 2&nbsp;hours and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund is complete.  | Completed      | Completed   |

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

