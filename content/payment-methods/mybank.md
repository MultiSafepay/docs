---
title: MyBank
category:
  uri: Payment methods
slug: mybank
position: 14
privacy:
  view: public
parent:
  uri: banking-methods
---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/mybank.svg" width="100" align="right" style={{ margin: "20px", maxHeight: "75px" }} />

MyBank is a widely accepted inter-bank payment method that links most Italian retail banks.\
Customers pay in their own online banking environment. <Glossary>Settlement</Glossary> is instant and guaranteed.

| Supports                                                      | Details                    |
| ------------------------------------------------------------- | -------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Italy                      |
| [Currencies](/docs/currencies/)                               | EUR                        |
| [Chargebacks](/docs/chargebacks/)                             | No                         |
| [Payment pages](/docs/payment-pages/)                         | Yes (current version only) |
| [Payment components](/docs/payment-components/)               | Yes                        |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial      |
| [Second Chance](/docs/second-chance/)                         | Yes                        |

## Issuer fees

The customer's bank may apply their own fee to MyBank transactions (not influenced by MultiSafepay or MyBank).\
This can have a significant impact on transactions for small amounts (e.g., a 1 EUR transaction but with a 1.50 EUR issuer fee).

**💡 Tip:** Consider setting a minimum amount limit for MyBank transactions in your integration.

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/mybank-payment-flow.svg" alt="MyBank payment flow" style={{ display: "block", marginLeft: "auto", marginRight: "auto", maxWidth: "750px", width: "100%" }} />

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                                 | Order status | Transaction status |
| ----------------------------------------------------------- | ------------ | ------------------ |
| The customer has been redirected to their bank.             | Initialized  | Initialized        |
| MultiSafepay has collected payment.                         | Completed    | Completed          |
| The transaction was cancelled by you or the customer.       | Void         | Void               |
| The customer didn't complete payment within 1 hour.         | Expired      | Expired            |
| The customer didn't complete payment or there was an error. | Declined     | Declined           |
| **Refunds:** Refund initiated.                              | Reserved     | Reserved           |
| **Refunds:** Refund complete.                               | Completed    | Completed          |

# Activation

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank" rel="noopener noreferrer">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize: 12, color: "#8b929e" }} />.
2. To activate the payment method for:
   * All websites, go to **Settings** > **Payment methods**.
   * A specific website, go to **Websites**, and then click the relevant website.
3. Select the checkbox for the relevant payment method, and then click **Save changes**.

💬 **Support:** If the payment method isn't visible in your dashboard, email [support@multisafepay.com](mailto:support@multisafepay.com)

# Integration

### API

* See API reference – [Create order](/reference/createorder/) > Banking order.\
  In the `customer` object, set the `locale` to `IT`.

<details id="example-requests">
  <summary>Example requests</summary>

  <br />

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **MyBank direct/redirect**.

  <div style={{ textAlign: "center" }}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{ width: "40%", height: "auto" }} />
  </div>
</details>

* Transactions expire after 1 hour.

### Ready-made integrations

Coming soon in [our integrations](/docs/our-integrations/).

### Testing

To test MyBank payments, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).

***

<blockquote className="callout callout_info">
    <h3 className="callout-heading false">
        <span className="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)
