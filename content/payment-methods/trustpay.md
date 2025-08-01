---
title: TrustPay
category:
  uri: Payment methods
slug: trustpay
position: 18
privacy:
  view: public
parent:
  uri: banking-methods
---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/trustpay.svg" width="100" align="right" style={{ margin: "20px", maxHeight: "75px" }} />

<a href="https://www.trustpay.eu/" target="_blank" rel="noopener noreferrer">TrustPay</a><i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} /> is a bank payment method in the Czech Republic. Customers pay from their own online banking environment.<br /><br />Read how TrustPay can benefit your business on{" "}<a href="https://www.multisafepay.com/solutions/payment-methods/trustpay" target="_blank" rel="noopener noreferrer">multisafepay.com</a><i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />

| Supports                                                      | Details                                                                                                                                |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Austria, Czech Republic, Denmark, Estonia, Finland, Germany, Italy, Latvia, Netherlands, Norway, Poland, Spain, Sweden, United Kingdom |
| [Currencies](/docs/currencies/)                               | CZK, DKK, EUR, GBP, NOK, SEK                                                                                                           |
| [Chargebacks](/docs/chargebacks/)                             | No                                                                                                                                     |
| [Payment pages](/docs/payment-pages/)                         | Yes (current and deprecated versions)                                                                                                  |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial                                                                                                                  |
| [Second Chance](/docs/second-chance/)                         | Yes                                                                                                                                    |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/trustpay-payment-flow.svg" alt="TrustPay payment flow" style={{ display: "block", marginLeft: "auto", marginRight: "auto", maxWidth: "750px", width: "100%" }} />

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                          | Order status | Transaction status |
| ---------------------------------------------------- | ------------ | ------------------ |
| The customer has been redirected to their bank.      | Initialized  | Initialized        |
| MultiSafepay has collected payment.                  | Completed    | Completed          |
| The transaction was cancelled.                       | Void         | Cancelled          |
| The customer didn't complete payment within 10 days. | Expired      | Expired            |
| **Refunds:** Refund initiated.                       | Reserved     | Reserved           |
| **Refunds:** Refund complete.                        | Completed    | Completed          |

# Activation

1. Sign in to your{" "}

<a href="https://merchant.multisafepay.com" target="_blank" rel="noopener noreferrer">
  MultiSafepay dashboard
</a>

<i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.

2. To activate the payment method for:

* All websites, go to **Settings** > **Payment methods**.
* A specific website, go to **Websites**, and then click the relevant website.

3. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <a href="mailto:integration@multisafepay.com">[integration@multisafepay.com](mailto:integration@multisafepay.com)</a>

# Integration

### API

* See API reference – [Create order](/reference/createorder/) > Banking order.

<details id="example-requests">
  <summary>Example requests</summary>

  <br />

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **TrustPay redirect**.

  <div style={{ textAlign: "center" }}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{ width: "40%", height: "auto" }} />
  </div>
</details>

* Transactions expire after 10 days.

### Ready-made integrations

* TrustPay (redirect) is supported in most [ready-made integrations](/docs/our-integrations).
* Exceptions: Lightspeed, Shopify, Magento 1, OpenCart, OsCommerce, PWAs, Vue Storefront, Zen Cart.

### Testing

* You can't test TrustPay in your test MultiSafepay account.
* You can only make test payments in your live MultiSafepay account.

<br />

***

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)
