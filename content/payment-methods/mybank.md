---
title: 'MyBank'
category: 6298bd782d1cf4006032e765
order: 12
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'mybank'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/mybank.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

MyBank is a widely accepted inter-bank payment method that links most Italian retail banks. 
Customers pay in their own online banking environment. <<glossary:Settlement>> is instant and guaranteed.

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Italy  | 
| [Currencies](/docs/currencies/)  | EUR | 
| [Chargebacks](/docs/chargebacks/)  | No | 
| [Payment pages](/docs/payment-pages/) | Yes (current version only) |
| [Payment components](/docs/payment-components/) | Yes |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial |
| [Second Chance](/docs/second-chance/) | Yes |

## Issuer fees

The customer's bank may apply their own fee to MyBank transactions (not influenced by MultiSafepay or MyBank). This can have a significant impact on transactions for small amounts, e.g. 1 EUR transaction, but a 1,50 EUR issuer fee.

&nbsp; **💡 Tip!** Consider setting a minimum amount limit for MyBank transactions in your integration.

# Payment flow
This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/mybank-payment-flow.svg" alt="MyBank payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment.| Completed | Completed |
| The transaction was cancelled by you or the customer. | Void   | Void   |
| The customer didn't complete payment within 1 hour. | Expired | Expired |
| The customer didn't complete payment or there was an error. | Declined | Declined |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete. | Completed | Completed |

# Activation 

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. To activate the payment method for:
- All sites, go to **Settings** > **Payment methods**.
- A specific site, go to **Sites**, and then click the relevant site.
3. Select the checkbox for the relevant payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <support@multisafepay.com>

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > Banking order. In the `customer` object, set the `locale` to `IT`.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **MyBank direct/redirect**.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- Transactions expire after 1 hour.

### Ready-made integrations
Coming soon in [our integrations](/docs/our-integrations/).

### Testing
To test MyBank payments, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)