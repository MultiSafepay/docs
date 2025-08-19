---
title: Giropay (End-of-life)
category:
  uri: Payment methods
slug: giropay
position: 10
privacy:
  view: public
parent:
  uri: banking-methods
---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/giropay.svg" width="90" align="right" style={{ margin: "20px", maxHeight: "75px" }} />

<a href="https://www.giropay.de/" target="_blank">Giropay</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} /> is the leading inter-bank payment method in Germany, connecting all major German retail banks. Customers pay from their own online banking environment. <Glossary>Settlement</Glossary> is instant and guaranteed.

> ⚠️ Note:
>
> Giropay is end-of-life as of 01 July 2024. New activations are no longer possible.

Read how Giropay can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/giropay" target="_blank">multisafepay.com</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />

| Supports                                                      | Details                               |
| ------------------------------------------------------------- | ------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Germany                               |
| [Currencies](/docs/currencies/)                               | EUR                                   |
| [Chargebacks](/docs/chargebacks/)                             | No                                    |
| [Payment pages](/docs/payment-pages/)                         | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial                 |
| [Second Chance](/docs/second-chance/)                         | Yes                                   |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/giropay-payment-flow.svg" alt="Giropay payment flow" style={{ display: "block", marginLeft: "auto", marginRight: "auto", maxWidth: "750px", width: "100%" }} />

<br />

# Payment statuses

| The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds. | Description | Order status | Transaction status |
| :----------------------------------------------------------------------------------------------------------------------------------- | :---------- | :----------- | :----------------- |
| The customer has been redirected to their bank.                                                                                      | Initialized | Initialized  |                    |
| MultiSafepay has collected payment.                                                                                                  | Completed   | Completed    |                    |
| The customer cancelled the transaction.                                                                                              | Void        | Void         |                    |
| The customer didn't complete payment within 10 minutes.                                                                              | Expired     | Expired      |                    |
| **Refunds:** Refund initiated.                                                                                                       | Initialized | Initialized  |                    |
| **Refunds:** Refund complete.                                                                                                        | Completed   | Completed    |                    |

# Activation

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />. To activate the payment method for:<br />
   * All websites, go to **Settings** > **Payment methods**.
   * A specific website, go to **Websites**, and then click the relevant website.
2. Select the checkbox for the payment method, and then click **Save changes**.💬  **Support:** If the payment method isn't visible in your dashboard, email [support@multisafepay.com](mailto:support@multisafepay.com)

# Integration

### API

See API reference – [Create order](/reference/createorder/)   > Banking order.

<details id="example-requests">
  <summary>Example requests</summary>

  <br />

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Giropay redirect**.

  <div style={{ textAlign: "center" }}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{ width: "40%", height: "auto" }} />
  </div>
</details>

* Transactions don't expire.

### Ready-made integrations

Supported in all [ready-made integrations](/docs/our-integrations/) .

### Testing

To test Giropay payments, see Testing payment methods - [Banking methods](/docs/testing#banking-methods)  .\<br>

***

<br />

<blockquote className="callout callout_info">
  <h3 className="callout-heading">
    <span className="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>
    Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a>
  </p>
</blockquote>

<br />

[Top of page](#)
