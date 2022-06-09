---
title: 'WeChat Pay'
weight: 240
meta_title: "Payment methods - WeChat Pay - MultiSafepay Docs"
layout: 'single'
logo: '/logo/Payment_methods/wechat.svg' 
short_description: 'Accept WeChat Pay payments via QR codes'
url: '/payment-methods/wechat-pay/'
aliases:
    - /payments/methods/wallet/wechatpay/
    - /payments/methods/wechatpay/product-rules/
    - /payment-methods/wechatpay/product-rules/
    - /payment-methods/wechatpay/overview/
    - /payment-methods/wechat-pay/overview/
    - /payments/methods/wallet/wechatpay/payment-flow/
    - /payment-methods/wechat-pay/payment-flow/
    - /payments/methods/wallet/wechatpay/integration-and-testing/
    - /payment-methods/wechat-pay/integration-testing/
    - /payments/methods/wallet/wechatpay/activation/
    - /payment-methods/wechat-pay/activation/
---

[WeChat Pay](https://pay.weixin.qq.com/index.php/public/wechatpay) is a leading global payment method that lets Chinese customers link their credit card or bank account to a digital wallet. It&nbsp;supports online and QR payments.

[See how WeChat Pay can benefit your business!](https://www.multisafepay.com/solutions/payment-methods/wechat-pay)

## Overview

|   |   |  
|---|---|
| **Countries**  | Worldwide  | 
| **Currencies**  | EUR {{< br >}} To request support for more currencies, email <sales@multisafepay.com> | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial](/refunds/#full-and-partial-refunds) | 
| **Transactions expire after**  | 2 hours | 

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant W as WeChat Pay
    participant Me as Merchant

    C->>Mu: Selects WeChat Pay at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page <br> with WeChat QR code
    else Direct flow
    Mu->>C: Displays WeChat QR code
    end
    C->>W: Scans code with WeChat app to complete payment 
    W->>Mu: Transfers funds 
    Mu->>Me: Settles funds

{{< /mermaid >}}
&nbsp;   

<details id="payment-statuses">

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payment-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| A QR code has been generated. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the payment. | Void   | Void   |
| The customer didn't complete payment within 2 hours. | Expired | Expired |
| **Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete.  | Completed | Completed |

{{< /details >}}

## Activation and integration

| | |
|---|---|
| **Activation** | [Apply to MultiSafepay](/payments/activating-payment-methods/#apply-to-multisafepay) |
| **Checkout options** | [Payment pages](/payment-pages/) ([current version](/payment-pages/activation/) only) |
| **Testing** | [Test payment details](/testing/test-payment-details/#wallets) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order <br> Examples > WeChat Pay direct/redirect |
| **Ready-made integrations** | Supported in our [PrestaShop 1.7 plugin](/prestashop-1-7/). |

### Displaying QR codes

To display WeChat Pay QR codes, you can use:

- Redirect orders to [payment pages](/payment-pages/), where the QR code is displayed under **Payment methods**.

- Direct orders, retrieve the `qr_url`, and render the QR code in your system to display it to the customer.
