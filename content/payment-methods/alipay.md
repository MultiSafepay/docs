---
title: Alipay
category:
  uri: Payment methods
slug: alipay
position: 0
privacy:
  view: public
parent:
  uri: wallets
---
> ⚠️ Action required
>
> Alipay will soon deprecate. We recommend migrating to [Alipay+](/docs/alipay-plus/) as soon as possible.

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/alipay.svg" width="100" align="right" style={{ margin: "20px", maxHeight: "75px" }} />

<a href="https://global.alipay.com/platform/site/ihome" target="_blank">Alipay</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} /> is a leading global payment method that lets Chinese customers link their card or bank account to a digital wallet. It supports online, QR, and contactless <Glossary>POS</Glossary> payments, as well as international money transfers.

For Chinese customers, Alipay accounts are verified and linked to their Chinese bank account. Since 2021, non-Chinese customers can also pay with Alipay using the Tour Pass.

Read how Alipay can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/alipay" target="_blank">multisafepay.com</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />

| Supports                                                      | Details                                    |
| ------------------------------------------------------------- | ------------------------------------------ |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Worldwide                                  |
| [Currencies](/docs/currencies/)                               | EUR, USD (currency conversion in EUR only) |
| [Chargebacks](/docs/chargebacks/)                             | No                                         |
| [Discounts](/docs/discounts/)                                 | Yes                                        |
| [Payment pages](/docs/payment-pages/)                         | Yes (current version only)                 |
| [Refunds](/docs/refund-payments/)                             | Yes: Full, partial, and API refunds        |
| [Second Chance](/docs/second-chance/)                         | Yes                                        |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/alipay-payment-flow.svg" alt="Alipay payment flow" style={{ display: "block", marginLeft: "auto", marginRight: "auto", maxWidth: "750px", width: "100%" }} />

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                                               | Order status | Transaction status |
| ------------------------------------------------------------------------- | ------------ | ------------------ |
| The customer has been redirected to Alipay.                               | Initialized  | Initialized        |
| MultiSafepay has collected payment.                                       | Completed    | Completed          |
| The customer didn't complete payment within 5 hours, or it was cancelled. | Expired      | Expired            |
| **Refunds:** Refund initiated.                                            | Reserved     | Reserved           |
| **Refunds:** Refund complete.                                             | Completed    | Completed          |

# Activation

1. Email a request to [sales@multisafepay.com](mailto:sales@multisafepay.com)\
   We check your eligibility and if approved, activate the payment method for your account.
2. Once approved, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.
3. To activate the payment method for:

* All sites, go to **Settings** > **Payment methods**.
* A specific website, go to **Websites**, and then click the relevant website.

4. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email [integration@multisafepay.com](mailto:integration@multisafepay.com)

# Integration

### API

* See API reference – [Create order](/reference/createorder/) > Wallet order.

  <details id="example-requests">
    <summary>Example requests</summary>

    <br />

    For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Alipay(+) direct/redirect**. Set `gateway` to `ALIPAY`, and `type` to `direct` or `redirect`.

    <div style={{ textAlign: "center" }}>
      <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{ width: "40%", height: "auto" }} />
    </div>
  </details>

* Transactions expire after 5 hours.

### Ready-made integrations

* Supported in all [ready-made integrations](/docs/our-integrations/) (direct).
* Exceptions: PrestaShop 1.6, OsCommerce, and Zen Cart.

### Testing

To test Alipay payments, see Testing payment methods - [Wallets](/docs/testing#wallets). <br />

***

<blockquote className="callout callout_info">
  <h3 className="callout-heading false">
    <span className="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)