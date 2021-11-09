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

## How it works

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

{{< details title="Direct vs redirect">}}

[Direct flow](/api/#wechat-pay---direct)  
The customer selects WeChat Pay at checkout and MultiSafepay displays a WeChat QR code.  

[Redirect flow](/api/#wechat-pay---redirect)  
The customer is redirected to a [MultiSafepay payment page](/payment-pages/) containing a WeChat QR code. 

{{< /details>}}

## Payment statuses

{{< details title="Order and transaction statuses" >}}
For each payment in your MultiSafepay account, there are two statuses that change as payment progresses:

**Order status**  
The progression of the customer's order with you, independent of the payment

**Transaction status**  
The progression towards settling the funds in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. | Initialized | Initialized |
| The transaction is complete. | Completed | Completed |
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete payment within 2 hours and the transaction expired. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund is complete.  | Completed      | Completed   |



