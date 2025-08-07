---
title: Belfius
category:
  uri: Payment methods
slug: belfius
position: 4
privacy:
  view: public
parent:
  uri: banking-methods
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/belfius.svg" width="100" alt="Belfius logo" style={{ margin: "20px", maxHeight: "75px", float: "right" }} />

<a href="https://www.belfius.be/common/EN/fw/language.html" target="_blank" rel="noopener noreferrer">Belfius</a><i className="fa fa-external-link" style={{ fontSize: 12, color: '#8b929e' }} /> is a popular online banking payment method for Belfius bank customers in Belgium.\
<p>Read how Belfius can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/belfius" target="_blank" rel="noopener noreferrer">multisafepay.com</a><i className="fa fa-external-link" style={{ fontSize: 12, color: '#8b929e' }} /></p>

| Supports                                                      | Details                                                           |
| ------------------------------------------------------------- | ----------------------------------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Belgium                                                           |
| [Currencies](/docs/currencies/)                               | EUR                                                               |
| [Chargebacks](/docs/chargebacks/)                             | No                                                                |
| [Payment pages](/docs/payment-pages/)                         | Yes (current version only)                                        |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial (1 business day after payment is completed) |
| [Second Chance](/docs/second-chance/)                         | Yes                                                               |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/belfius-payment-flow.svg" alt="Belfius payment flow" style={{ display: "block", marginLeft: "auto", marginRight: "auto", maxWidth: "750px", width: "100%" }} />

**⚠️ Note:** MultiSafepay doesn’t automatically receive the customer's IBAN when a transaction is completed, but we import our bank statements daily. All incoming payments are then completed.

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                         | Order status | Transaction status |
| --------------------------------------------------- | ------------ | ------------------ |
| The customer has been redirected to Belfius.        | Initialized  | Initialized        |
| MultiSafepay has collected payment.                 | Completed    | Completed          |
| You cancelled the transaction.                      | Void         | Void/Cancelled     |
| The customer didn't complete payment within 5 days. | Expired      | Expired            |
| **Refunds:** Refund initiated.                      | Reserved     | Reserved           |
| **Refunds:** Refund complete.                       | Completed    | Completed          |

**⚠️ Note:** If the customer doesn’t click the **Return to website** button, MultiSafepay doesn’t receive an update and the <Glossary>transaction status</Glossary> remains **Initialized**. We import our bank statements daily and finalize all incoming payments.

# Activation

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank" rel="noopener noreferrer">MultiSafepay dashboard</a>{" "}\
   <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.
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

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Belfius direct/redirect**.

  <div style={{ textAlign: "center" }}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{ width: "40%", height: "auto" }} />
  </div>
</details>

* Transactions expire after 5 days.

### Ready-made integrations

* Supported in most [ready-made integrations](/docs/our-integrations/).
* Exceptions: OsCommerce and ZenCart.

### Testing

To test Belfius payments, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).<br />

***

<blockquote className="callout callout_info">
    <h3 className="callout-heading false">
        <span className="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)
