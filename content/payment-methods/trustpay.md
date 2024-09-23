---
title: 'TrustPay'
category: 6298bd782d1cf4006032e765
order: 17
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'trustpay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/trustpay.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.trustpay.eu/" target="_blank">TrustPay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a bank payment method in the Czech Republic. Customers pay from their own online banking environment.

Read how TrustPay can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/trustpay" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details | 
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Austria, Czech Republic, Denmark, Estonia, Finland, Germany, Italy, Latvia, Netherlands, Norway, Poland, Spain, Sweden, United Kingdom  | 
| [Currencies](/docs/currencies/)  | CZK, DKK, EUR, GBP, NOK, SEK | 
| [Chargebacks](/docs/chargebacks/)  | No  | 
| [Payment pages](/docs/payment-pages/) | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial  |
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/trustpay-payment-flow.svg" alt="TrustPay payment flow" style="display: block;
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
| The transaction was cancelled. | Void   | Cancelled   |
| The customer didn't complete payment within 10 days. | Expired | Expired |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete. | Completed | Completed |

# Activation 

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. To activate the payment method for:
- All sites, go to **Settings** > **Payment methods**.
- A specific site, go to **Sites**, and then click the relevant site.
3. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > Banking order.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **TrustPay redirect**.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- Transactions expire after 10 days.

### Ready-made integrations
- TrustPay (redirect) is supported in most [ready-made integrations](/docs/our-integrations).
- Exceptions: Lightspeed, Shopify, Magento 1, OpenCart, OsCommerce, PWAs, Vue Storefront, Zen Cart.

### Testing
- You can't test TrustPay in your test MultiSafepay account. 
- You can only make test payments in your live MultiSafepay account.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
