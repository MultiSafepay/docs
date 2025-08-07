---
title: Request to Pay (End-of-life)
category:
  uri: Payment methods
slug: request-to-pay
position: 15
privacy:
  view: public
parent:
  uri: banking-methods
---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/RTP.svg" width="60" align="right" alt="Request to Pay" style={{ margin: "20px", maxHeight: "75px" }} />

Request to Pay is a Deutsche Bank payment method based on the PSD2 Open Banking API. Customers are redirected to Deutsche Bank online banking to authenticate themselves, and authorize a secure SEPA transfer. <Glossary>Settlement</Glossary> is instant (if supported) or within 24 hours.

The funds are transferred directly to your business bank account, instead of your account balance, which simplifies reconciliation.

Read how Request to Pay can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/request-to-pay" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }}></i> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />

> ⚠️ Availability\
> Request to Pay is end-of-life and is no longer available.

| Supports                                                      | Details                                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Amount limits**                                             | Minimum amount: 1 EUR, maximum amount: 15,000 EUR                        |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Germany – More countries will follow as more banks migrate to PSD2 APIs. |
| [Currencies](/docs/currencies/)                               | EUR                                                                      |
| [Chargebacks](/docs/chargebacks/)                             | No                                                                       |
| [Payment pages](/docs/payment-pages/)                         | Yes (current version only)                                               |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial <br /> All refunds are processed by Deutsche Bank. |
| [Second Chance](/docs/second-chance/)                         | Yes                                                                      |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/request-to-pay-payment-flow.svg" alt="Request to Pay payment flow" style={{ display: "block", marginLeft: "auto", marginRight: "auto", maxWidth: "750px", width: "100%" }} />

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                                                 | Order status | Transaction status |
| --------------------------------------------------------------------------- | ------------ | ------------------ |
| The customer has been redirected to Deutsche Bank.                          | Initialized  | Initialized        |
| Deutsche Bank has authorized the transaction and is transferring the funds. | Completed    | Uncleared          |
| MultiSafepay has collected payment.                                         | Completed    | Completed          |
| Deutsche Bank declined the transaction.                                     | Declined     | Declined           |
| The customer cancelled the transaction at Deutsche Bank.                    | Void         | Void               |
| The customer didn't complete payment within 1 hour.                         | Expired      | Expired            |
| **Refunds:** Refund initiated.                                              | Reserved     | Reserved           |
| **Refunds:** Refund complete.                                               | Completed    | Completed          |
| Refund declined.                                                            | Declined     | Declined           |

# Activation

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }}></i> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.
2. To activate the payment method for:
   * All websites, go to **Settings** > **Payment methods**.
   * A specific website, go to **Websites**, and then click the relevant website.
3. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email [integration@multisafepay.com](mailto:integration@multisafepay.com)

# Integration

### API

* See API reference – [Create order](/reference/createorder/) > Banking order.

<details id="example-requests">
  <summary>Example requests</summary>

  <br />

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Request to Pay direct/redirect**.

  <div style={{ textAlign: "center" }}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{ width: "40%", height: "auto" }} />
  </div>
</details>

* Transactions expire after 1 hour.

### Ready-made integrations

**Not** supported in our [ready-made integrations](/docs/our-integrations/).

### Testing

You can't test Request to Pay in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account.

***

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)