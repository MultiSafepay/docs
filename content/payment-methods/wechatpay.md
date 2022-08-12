---
title: 'WeChat Pay'
category: 6298bd782d1cf4006032e765
order: 508
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'wechat-pay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/wechat.svg" width="110" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://pay.weixin.qq.com/index.php/public/wechatpay" target="_blank">WeChat Pay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a leading global payment method that lets Chinese customers link their credit card or bank account to a digital wallet. It supports online and QR payments.

Read how WeChat Pay can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/wechat-pay" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details | 
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Worldwide  | 
| [Currencies](/docs/currencies/)  | EUR – To request support for more currencies, email <sales@multisafepay.com> | 
| [Chargebacks](/docs/chargebacks/)  | No |
| [Payment pages](/docs/payment-pages/) | Yes (current version only) |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial | 

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/wechatpay-payment-flow.svg" alt="WeChat Pay payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| A QR code has been generated. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the payment. | Void   | Void   |
| The customer didn't complete payment within 2 hours. | Expired | Expired |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete.  | Completed | Completed |

# Activation 

First apply to MultiSafepay, and then activate in your dashboard.

<details id="how-to-activate-wechat-pay"> 
<summary>How to activate WeChat Pay</summary>
<br>

1. Email a request to <risk@multisafepay.com> 
2. We check your eligibilty and if approved, activate the payment method for your account. 
3. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
4. Go to **Settings**. 
5. To activate the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
6. Select the checkbox for the payment method, and then click **Save changes**.

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>


</details>

# Integration

### API
- [Create order](/reference/createorder/) > Wallet order. 
- Examples > WeChat Pay direct/redirect.
- Transactions expire after 2 hours.
- For direct orders, retrieve the `qr_url`, and render the QR code in your system to display it to the customer.
- For redirect orders to [payment pages](/docs/payment-pages/), the QR code displays under **Payment methods**.

### Ready-made integrations
Supported in our [PrestaShop 1.7 plugin](/docs/prestashop-1-7/).

### Testing
To test WeChat Pay payments, see [Testing](/docs/testing#wallets).

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
