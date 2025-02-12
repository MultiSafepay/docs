---
title: 'Trustly'
category: 6298bd782d1cf4006032e765
order: 17
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'trustly'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/trustly.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.trustly.net/nl-NL" target="_blank">Trustly</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a quick, secure banking payment method that is available in 29 European countries. 
Customers pay from their own online banking environment.

Read how Trustly can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/trustly" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |  
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Austria, Czech Republic, Denmark, Estonia, Finland, Germany, Latvia, Lithuania, Netherlands, Norway, Poland, Portugal, Spain, Sweden, United Kingdom <br> <<glossary:Payouts>> are supported in all the above countries. See also countries that support [deposits](#deposits).  | 
| [Currencies](/docs/currencies/)  | EUR, GBP, SEK | 
| [Chargebacks](/docs/chargebacks/)  | No | 
| [Payment pages](/docs/payment-pages/) | Yes (current version only) |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial  |
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/trustly-payment-flow.svg" alt="Trustly payment flow" style="display: block;
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
| The customer cancelled the transaction at their bank. | Cancelled   | Cancelled   |
| The customer didn't complete payment within 2 days. | Expired | Expired |
| In rare cases, the transaction is marked as **uncleared**. <br> Trustly then informs MultiSafepay of the correct status, which may be **Completed**, **declined**, or **expired**. <br> **Uncleared** status automatically expires after 5 days. | Uncleared | Uncleared   |
| **Refunds:** Refund initiated. | Initialized | Initialized |
| **Refunds:** Refund complete. | Completed | Completed |
| Refund declined. | Declined | Declined |

# Activation 

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. To activate the payment method for:
- All websites, go to **Settings** > **Payment methods**.
- A specific website, go to **Websites**, and then click the relevant website.
4. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <support@multisafepay.com>

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > Banking order.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Trustly redirect**.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- Transactions expire after 2 hours.

### Ready-made integrations
- Trustly (direct) is supported in most [ready-made integrations](/docs/our-integrations/).
- Exceptions: OsCommerce, PWAs, Vue Storefront, and Zen Cart.

### Testing
To test Trustly payments, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).
<br>

---
# User guide

## Deposits

Deposits are only supported in certain countries.

<details id="countries-that-support-deposits">
<summary>See all countries that support deposits</summary>
<br>

- Austria
- Denmark
- Estonia
- Finland
- Germany
- Latvia
- Lithuania
- Netherlands
- Norway
- Spain
- Sweden
- UK

</details>
---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
