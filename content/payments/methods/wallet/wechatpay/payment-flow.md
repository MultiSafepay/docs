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

The table below shows a successful transaction flow from start to finish. 

{{< details title="Order and transaction statuses" >}}

- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|   | Flow | Order status | Transaction status |
|---|---|---|---|
| 1. | The customer selects WeChat at checkout. | Initialized | Initialized |
| 2. | MultiSafepay generates a payment link with a QR code. |   |  |
| 3. | The customer scans the QR code with the WeChat app and completes payment. | | |
| 4. | MultiSafepay collects the funds and settles them in your MultiSafepay balance. | Completed | Completed |

## Unsuccessful statuses

| Description | Order status | Transaction status |
|---|---|---|
| The transaction has been cancelled. | Void   | Cancelled   |
| The customer didn't complete the payment and the transaction expired after the 2-hour period. | Expired | Expired |

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund was successfully processed.  | Completed      | Completed   |



