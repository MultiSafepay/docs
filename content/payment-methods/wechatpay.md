---
title: 'WeChat Pay'
category: 6298bd782d1cf4006032e765
order: 508
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'wechat-pay'
---
[WeChat Pay](https://pay.weixin.qq.com/index.php/public/wechatpay) is a leading global payment method that lets Chinese customers link their credit card or bank account to a digital wallet. It supports online and QR payments.

See how WeChat Pay can [benefit your business](https://www.multisafepay.com/solutions/payment-methods/wechat-pay).

# Overview

|   |   |  
|---|---|
| **Countries**  | Worldwide  | 
| **Currencies**  | EUR – To request support for more currencies, email <sales@multisafepay.com> | 
| **Chargebacks**  | No | 
| **Refunds** | [Full and partial](/refunds/) | 
| **Transactions expire after**  | 2 hours | 

# Payment flow

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

# Payment statuses

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payment-statuses/).

| Description | Order status | Transaction status |
|---|---|---|
| **Payments** | | |
| A QR code has been generated. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the payment. | Void   | Void   |
| The customer didn't complete payment within 2 hours. | Expired | Expired |
| **Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete.  | Completed | Completed |

</details>

# Activation and integration

| | |
|---|---|
| **Activation** | [Apply to MultiSafepay](/payment-methods/#apply-to-multisafepay) |
| **Checkout options** | [Payment pages](/payment-pages/) (current version only) |
| **Testing** | [Test payment details](/testing/#wallets) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order <br> Examples > WeChat Pay direct/redirect |
| **Ready-made integrations** | Supported in our [PrestaShop 1.7 plugin](/prestashop/). |
<br>

---

# User guide

## QR codes

<details id="how-to-display-qr-codes">
<summary>How to display QR codes</summary>
<br>

To display WeChat Pay QR codes, you can use:

- Redirect orders to [payment pages](/payment-pages/), where the QR code is displayed under **Payment methods**.
- Direct orders, retrieve the `qr_url`, and render the QR code in your system to display it to the customer.
</details>
<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>