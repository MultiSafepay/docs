---
title: Trustly
category:
  uri: Payment methods
slug: trustly
position: 17
privacy:
  view: public
parent:
  uri: banking-methods
---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/trustly.svg" width="100" align="right" style={{ margin: '20px', maxHeight: '75px' }} />

<a href="https://www.trustly.net/nl-NL" target="_blank" rel="noopener noreferrer">Trustly</a><i className="fa fa-external-link" style={{ fontSize: '12px', color: '#8b929e' }} /> is a quick, secure banking payment method that is available in 29 European countries. Customers pay from their own online banking environment.<br /><br />Read how Trustly can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/trustly" target="_blank" rel="noopener noreferrer">multisafepay.com</a><i className="fa fa-external-link" style={{ fontSize: '12px', color: '#8b929e' }} />

| Supports                                                      | Details                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Austria, Czech Republic, Denmark, Estonia, Finland, Germany, Latvia, Lithuania, Netherlands, Norway, Poland, Portugal, Spain, Sweden, United Kingdom <br /> <Glossary>Payouts</Glossary> are supported in all the above countries. See also countries that support [deposits](#deposits). |
| [Currencies](/docs/currencies/)                               | EUR, GBP, SEK                                                                                                                                                                                                                                                                             |
| [Chargebacks](/docs/chargebacks/)                             | No                                                                                                                                                                                                                                                                                        |
| [Payment pages](/docs/payment-pages/)                         | Yes (current version only)                                                                                                                                                                                                                                                                |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial                                                                                                                                                                                                                                                                     |
| [Second Chance](/docs/second-chance/)                         | Yes                                                                                                                                                                                                                                                                                       |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/trustly-payment-flow.svg" alt="Trustly payment flow" style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto', maxWidth: '750px', width: '100%' }} />

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                                                                                                                                                                                                                          | Order status | Transaction status |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------ |
| The customer has been redirected to their bank.                                                                                                                                                                                                      | Initialized  | Initialized        |
| MultiSafepay has collected payment.                                                                                                                                                                                                                  | Completed    | Completed          |
| The customer cancelled the transaction at their bank.                                                                                                                                                                                                | Cancelled    | Cancelled          |
| The customer didn't complete payment within 2 days.                                                                                                                                                                                                  | Expired      | Expired            |
| In rare cases, the transaction is marked as **uncleared**. <br /> Trustly then informs MultiSafepay of the correct status, which may be **Completed**, **declined**, or **expired**. <br /> **Uncleared** status automatically expires after 5 days. | Uncleared    | Uncleared          |
| **Refunds:** Refund initiated.                                                                                                                                                                                                                       | Initialized  | Initialized        |
| **Refunds:** Refund complete.                                                                                                                                                                                                                        | Completed    | Completed          |
| Refund declined.                                                                                                                                                                                                                                     | Declined     | Declined           |

# Activation

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank" rel="noopener noreferrer">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize: '12px', color: '#8b929e' }} />.
2. To activate the payment method for:

* All websites, go to **Settings** > **Payment methods**.
* A specific website, go to **Websites**, and then click the relevant website.

4. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email [support@multisafepay.com](mailto:support@multisafepay.com)

# Integration

### API

* See API reference – [Create order](/reference/createorder/) > Banking order.

  <details id="example-requests">
    <summary>Example requests</summary>

    <br />

    For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Trustly redirect**.

    <div style={{ textAlign: 'center' }}>
      <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{ width: '40%', height: 'auto' }} />
    </div>
  </details>

* Transactions expire after 2 hours.

### Ready-made integrations

* Trustly (direct) is supported in most [ready-made integrations](/docs/our-integrations/).
* Exceptions: OsCommerce, PWAs, Vue Storefront, and Zen Cart.

### Testing

To test Trustly payments, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).\ <br />

***

# User guide

## Deposits

Deposits are only supported in certain countries.

<details id="countries-that-support-deposits">
  <summary>See all countries that support deposits</summary>

  <br />

  * Austria
  * Denmark
  * Estonia
  * Finland
  * Germany
  * Latvia
  * Lithuania
  * Netherlands
  * Norway
  * Spain
  * Sweden
  * UK
</details>

<blockquote className="callout callout_info">
  <h3 className="callout-heading">
    <span className="callout-icon">💬</span> Support
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)
