---
title: 'WeChat Pay'
category: 6298bd782d1cf4006032e765
order: 508
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'wechat-pay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/wechat.svg" width="110" align="right" style="margin: 20px; max-height: 75px"/>

[WeChat Pay](https://pay.weixin.qq.com/index.php/public/wechatpay) is a leading global payment method that lets Chinese customers link their credit card or bank account to a digital wallet. It supports online and QR payments.

Read how WeChat Pay can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/wechat-pay)

| Overview | Details | 
|---|---|
| **Chargebacks**  | No |
| **Countries**  | Worldwide  | 
| **Currencies**  | EUR – To request support for more currencies, email <sales@multisafepay.com> | 
| **Expiration**  | Transactions expire after 2 hours. |  
| **Payment pages** | [Yes](/payment-pages/) (current version only) |
| **Refunds** | [Yes](/refunds/): Full and partial | 

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

- **Order status:** Changes as the customer's order with you progresses towards shipment 
- **Transaction status:** Changes as the funds progress towards settlement in your account balance

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| A QR code has been generated. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the payment. | Void   | Void   |
| The customer didn't complete payment within 2 hours. | Expired | Expired |

</details>

<details id="refund-statuses">
<summary>Refund statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| Refund initiated. | Reserved | Reserved |
| Refund complete.  | Completed | Completed |

</details>

# Activation 

First apply to MultiSafepay, and then activate in your dashboard.

<details id="how-to-activate-wechat-pay"> 
<summary>How to activate WeChat Pay</summary>
<br>

1. Email a request to <risk@multisafepay.com> 
2. We check your eligibilty and if approved, activate the payment method for your account. 
3. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
4. Go to **Settings**. 
5. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
6. Select the checkbox for the relevant payment method, and then click **Save changes**.

> 💬  Support
> If the payment method isn't visible in your dashboard, email <integration@multisafepay.com> 

</details>

# Integration

| Integration | Details |
|---|---|
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Wallet order <br> Examples > WeChat Pay direct/redirect <br> - For direct orders, retrieve the `qr_url`, and render the QR code in your system to display it to the customer. <br> - For redirect orders to [payment pages](/payment-pages/), the QR code displays under **Payment methods**.  |
| **Ready-made integrations** | Supported in our [PrestaShop 1.7 plugin](/prestashop/). |
<br>

> ℹ️ Testing
> To test WeChat Pay payments, see [Testing](/testing/#wallets).
<br>

---

> 💬  Support
> Email <support@multisafepay.com>
[Top of page](#)
