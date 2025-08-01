---
title: 'WeChat Pay'
category: 6298bd782d1cf4006032e765
order: 10
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'wechat-pay'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/wechatpay.svg" width="110" align="right" style={{ margin: "20px", maxHeight: "75px" }} />

<a href="https://pay.weixin.qq.com/index.php/public/wechatpay" target="_blank">WeChat Pay</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} /> is a leading global payment method that lets Chinese customers link their card or bank account to a digital wallet. It supports online and QR payments for **B2C only** (B2B is **not** supported).

Read how WeChat Pay can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/wechat-pay" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />

| Supports                                                      | Details                                                                                                     |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Worldwide                                                                                                   |
| [Currencies](/docs/currencies/)                               | EUR – To request support for more currencies, email [sales@multisafepay.com](mailto:sales@multisafepay.com) |
| [Chargebacks](/docs/chargebacks/)                             | No                                                                                                          |
| [Payment pages](/docs/payment-pages/)                         | Yes (current version only)                                                                                  |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial                                                                                       |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/wechatpay-payment-flow.svg" alt="WeChat Pay payment flow" style={{ display: "block", marginLeft: "auto", marginRight: "auto", maxWidth: "750px", width: "100%" }} />

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                          | Order status | Transaction status |
| ---------------------------------------------------- | ------------ | ------------------ |
| A QR code has been generated.                        | Initialized  | Initialized        |
| MultiSafepay has collected payment.                  | Completed    | Completed          |
| The customer cancelled the payment.                  | Void         | Void               |
| The customer didn't complete payment within 2 hours. | Expired      | Expired            |
| **Refunds:** Refund initiated.                       | Reserved     | Reserved           |
| **Refunds:** Refund complete.                        | Completed    | Completed          |

# Activation

1. Email a request to [sales@multisafepay.com](mailto:sales@multisafepay.com)
2. We check your eligibility and if approved, activate the payment method for your account.
3. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.
4. To activate the payment method for:

* All websites, go to **Settings** > **Payment methods**.
* A specific website, go to **Websites**, and then click the relevant website.

5. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email [support@multisafepay.com](mailto:support@multisafepay.com)

# Integration

### API

* See API reference – [Create order](/reference/createorder/) > Wallet order.

  <details id="example-requests">
    <summary>Example requests</summary>

    <br />

    For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **WeChat Pay direct/redirect**.

    <div style={{ textAlign: "center" }}>
      <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{ width: "40%", height: "auto" }} />
    </div>
  </details>

* Transactions expire after 2 hours.

* For <Glossary>direct</Glossary> orders, retrieve the `qr_url`, and render the QR code in your system to display it to the customer.

* For <Glossary>redirect</Glossary> orders, the QR code displays on the [payment page](/docs/payment-pages/) under **Payment methods**.

### Ready-made integrations

Supported in our [PrestaShop plugin](/docs/prestashop/).

### Testing

To test WeChat Pay payments, see Testing payment methods - [Wallets](/docs/testing#wallets).

<br />

***

<blockquote class="callout callout_info">
  <h3 class="callout-heading false">
    <span class="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)