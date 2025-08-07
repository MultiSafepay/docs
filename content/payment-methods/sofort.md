---
title: Sofort (Deprecated)
category:
  uri: Payment methods
slug: sofort
position: 16
privacy:
  view: public
parent:
  uri: banking-methods
---
> ⚠️ **Note:**
>
> Sofort is no longer available as a standalone payment method due to its acquisition by Klarna.\
> Existing integrations will be kept intact, but it cannot be activated for new merchants.
> For alternative banking methods, see <a href="https://docs.multisafepay.com/docs/banking-methods" target="_blank">our overview</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.

<br />

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/logo/Payment_methods/Klarna-Sofort.svg" width="100" align="right" style={{ margin: "15px", maxHeight: "75px" }} />

<a href="https://www.klarna.com/pay-now/" target="_blank">Sofort</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} /> is a banking payment method by Klarna. It integrates with the customer's bank like a <Glossary>direct</Glossary> bank transfer. The customer verifies the payment, which reduces the risks associated with traditional transfers.\
<br />
Once payment is completed, the customer cannot reverse it, and Sofort guarantees <Glossary>settlement</Glossary>.

Read how Sofort can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/sofort" target="_blank">multisafepay.com</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />

| Supports                                                      | Details                                                                                                                                                                                                          |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Amount limit**                                              | Minimum amount: 0,10 EUR <br /> See also [Amount limits and processing times](#amount-limits-and-processing-times) below.                                                                                        |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Austria, Belgium, France, Germany, Italy, Poland, Spain, Switzerland, UK <br /> ❗ Transactions processed in non-supported countries return a [1024 error](/docs/troubleshooting#error-1024-transaction-refused). |
| [Currencies](/docs/currencies/)                               | EUR                                                                                                                                                                                                              |
| [Chargebacks](/docs/chargebacks/)                             | No                                                                                                                                                                                                               |
| [Payment components](/docs/payment-components/)               | Yes                                                                                                                                                                                                              |
| [Payment pages](/docs/payment-pages/)                         | Yes (current version only)                                                                                                                                                                                       |
| [Recurring payments](/docs/recurring-payments/)               | Yes                                                                                                                                                                                                              |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial                                                                                                                                                                                            |
| [Second Chance](/docs/second-chance/)                         | Yes                                                                                                                                                                                                              |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/sofort-payment-flow.svg" alt="Sofort payment flow" style={{ display: "block", marginLeft: "auto", marginRight: "auto", maxWidth: "750px", width: "100%" }} />

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                                                                                                                                                                                                                      | Order status | Transaction status |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | ------------------ |
| The customer has been redirected to their bank.                                                                                                                                                                                                  | Initialized  | Initialized        |
| The customer's bank has authorized the transaction and is transferring the funds. This may take up to 3 business days for all amounts. <br /> **Do not ship yet!** MultiSafepay assumes no responsibility if you ship and the transaction fails. | Uncleared    | Uncleared          |
| MultiSafepay has collected payment.                                                                                                                                                                                                              | Completed    | Completed          |
| The customer cancelled the transaction via Sofort.                                                                                                                                                                                               | Void         | Void/Cancelled     |
| The customer didn't complete payment within 1 day.                                                                                                                                                                                               | Expired      | Expired            |
| **Refunds:** Refund initiated.                                                                                                                                                                                                                   | Reserved     | Reserved           |
| **Refunds:** Refund complete.                                                                                                                                                                                                                    | Completed    | Completed          |

### Amount limits and processing times

Amounts **less than** 100 EUR are transferred immediately.\
Amounts **over** 100 EUR require approval from Sofort and can take a few days to change to **Completed**.

To speed up Sofort payments, you can increase your limit above 100 EUR. First, consider how much risk is acceptable to your business in case Sofort declines a payment.

To adjust your Sofort limit, email [sales@multisafepay.com](mailto:sales@multisafepay.com).

# Activation

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.
2. To activate the payment method for:
   * All websites, go to **Settings** > **Payment methods**.
   * A specific website, go to **Websites**, and then click the relevant website.
3. Select the checkbox for the payment method, and then click **Save changes**.

💬 **Support:** If the payment method isn't visible in your dashboard, email [support@multisafepay.com](mailto:support@multisafepay.com)

# Integration

### API

* See API reference – [Create order](/reference/createorder/) > Banking order.

  <details id="example-requests">
    <summary>Example requests</summary>

    <br />

    For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Sofort direct/redirect**.

    <div style={{ textAlign: "center" }}>
      <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{ width: "40%", height: "auto" }} />
    </div>
  </details>

* Transactions expire after 1 day.

### Ready-made integrations

Supported in all [ready-made integrations](/docs/our-integrations/).

### Testing

To test Sofort payments, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).<br />

***

<blockquote className="callout callout_info">
  <h3 className="callout-heading">
    <span className="callout-icon">💬</span> Support
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)