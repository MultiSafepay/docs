---
title: 'Dotpay'
category: 6298bd782d1cf4006032e765
order: 8
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'dotpay'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/dotpay.svg" width="100" align="right" style={{ margin: "20px", maxHeight: "75px" }} />

<a href="https://www.dotpay.pl/en" target="_blank" rel="noopener noreferrer">Dotpay</a> <i className="fa fa-external-link" style={{ fontSize: 12, color: "#8b929e" }} /> is an inter-bank payment method that links all major Polish retail banks. Customers pay from their own online banking environment.

Read how Dotpay can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/dotpay" target="_blank" rel="noopener noreferrer">multisafepay.com</a> <i className="fa fa-external-link" style={{ fontSize: 12, color: "#8b929e" }} />

| Supports                                                      | Details                               |
| ------------------------------------------------------------- | ------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Poland                                |
| [Currencies](/docs/currencies/)                               | EUR, PLN                              |
| [Chargebacks](/docs/chargebacks/)                             | No                                    |
| [Payment pages](/docs/payment-pages/)                         | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial                 |
| [Second Chance](/docs/second-chance/)                         | Yes                                   |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/dotpay-payment-flow.svg" alt="Dotpay payment flow" style={{ display: "block", marginLeft: "auto", marginRight: "auto", maxWidth: "750px", width: "100%" }} />

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                         | Order status | Transaction status |
| --------------------------------------------------- | ------------ | ------------------ |
| The customer has been redirected to their bank.     | Initialized  | Initialized        |
| MultiSafepay has collected payment.                 | Completed    | Completed          |
| The customer didn't complete payment within 3 days. | Expired      | Expired            |
| **Refunds:** Refund initiated.                      | Reserved     | Reserved           |
| **Refunds:** Refund complete.                       | Completed    | Completed          |

# Activation

1. Email a request to [sales@multisafepay.com](mailto:sales@multisafepay.com).\
   We check your eligibility and, if approved, activate the payment method for your account.
2. Once approved, sign in to your <a href="https://merchant.multisafepay.com" target="_blank" rel="noopener noreferrer">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize: 12, color: "#8b929e" }} />.
3. To activate the payment method for:
   * All websites, go to **Settings** > **Payment methods**.
   * A specific website, go to **Websites**, and then click the relevant website.
4. Select the checkbox for the payment method, and then click **Save changes**.

💬 **Support:** If the payment method isn't visible in your dashboard, email [integration@multisafepay.com](mailto:integration@multisafepay.com)

# Integration

### API

* See API reference – [Create order](/reference/createorder/) > Banking order.

<details id="example-requests">
  <summary>Example requests</summary>

  <br />

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Dotpay redirect**.

  <div style={{ textAlign: "center" }}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{ width: "40%", height: "auto" }} />
  </div>
</details>

**⚠️ Note:** **Direct** API requests are not supported for Dotpay.

* Transactions expire after 3 days.

### Ready-made integrations

Supported in all [ready-made integrations](/docs/our-integrations/).

### Testing

To test Dotpay payments, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).

***

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)