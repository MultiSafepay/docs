---
title: Belfius
category:
  uri: Payment methods
slug: belfius
position: 5
privacy:
  view: public
parent:
  uri: banking-methods
---
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Bizum.svg/122px-Bizum.svg.png" width="100" align="right" style={{ margin: "20px", maxHeight: "75px" }} />

<a href="https://bizum.es/" target="_blank">Bizum</a><i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} /> is a mobile payment system in Spain that enables users to make instant transfers through their banking app, providing a quick and secure way to conduct payments.

| Supports                                                      | Details                                                                                                                                                                                                  |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Spain                                                                                                                                                                                                    |
| [Currencies](/docs/currencies/)                               | EUR                                                                                                                                                                                                      |
| [Chargebacks](/docs/chargebacks/)                             | No                                                                                                                                                                                                       |
| [Payment pages](/docs/payment-pages/)                         | Yes                                                                                                                                                                                                      |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial<br />**⚠️Note:** Bizum does not support more than one refund per transaction. Once a partial refund has been processed, no further refunds can be issued for the same transaction. |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/diagrams/svg/bizum-payment-flow.svg" alt="Bizum payment flow" style={{ display: "block", marginLeft: "auto", marginRight: "auto", maxWidth: "750px", width: "100%" }} />

***

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                                                                      | Order status | Transaction status |
| ------------------------------------------------------------------------------------------------ | ------------ | ------------------ |
| The customer has initiated a transaction and gets redirected to Bizum. You can no longer cancel. | Initialized  | Initialized        |
| The customer has completed the authentication.                                                   | Completed    | Initialized        |
| The customer didn't complete payment within 30 minutes.                                          | Expired      | Expired            |
| The authentication failed.                                                                       | Declined     | Declined           |
| **Refunds:** Refund complete.                                                                    | Completed    | Initialized        |
| **Refunds:** Refund declined.                                                                    | Declined     | Declined           |

***

# Activation

1. Request merchant registration at your local bank, and follow guidelines provided by them (for example agreements).
2. Provide MultiSafepay with your **FUC** (Merchant Identification Code), **CSB**, and **Terminal**.
3. We confirm activation.
4. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.
5. To activate the payment method for:

* All websites, go to **Settings** > **Payment methods**.
* A specific website, go to **Websites**, and then click the relevant website.
* Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email [support@multisafepay.com](mailto:integration@multisafepay.com)

# Integration

## API

See API reference – [Create order](/reference/createorder/) > Banking order.

<details id="example-requests">
  <summary>Example requests</summary>

  <br />

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Bizum direct/redirect**.

  Set `gateway` to `BIZUM`, and `type` to `direct` or `redirect`.

  <div style={{ textAlign: "center" }}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{ width: "40%", height: "auto" }} />
  </div>
</details>

* Transactions expire after 30 minutes.

## Ready made solutions

Bizum is supported in most <a href="https://docs.multisafepay.com/docs/our-integrations" target="_blank">ready-made integrations</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.

* Exceptions:
  * Craft Commerce
  * Odoo
  * OsCommerce
  * Zen Cart

## Testing

To test Bizum payments, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).

# User guides

## Amount limits

* Minimum order amount:  0.50 EUR
* Maximum order amount: 1,000 EUR
* Maximum amount per day: 2,000 EUR
* Maximum amount per month: 5,000 EUR

## Cancellation

You can no longer cancel a transaction after the status changes to **Initialized**.

## Refunds

You can process full and partial refunds in your dashboard.

<blockquote class="callout callout_info">
  <h3 class="callout-heading false">
    <span class="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)
