---
title: 'Trustly'
category: 6298bd782d1cf4006032e765
order: 115
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'trustly'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Trustly.svg" width="60" align="right" style="margin: 20px; max-height: 75px"/>

[Trustly](https://www.trustly.net/nl-NL) is a quick, secure banking payment method that is available in 29 European countries. 
Customers pay from their own online banking environment.

Read how Trustly can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/trustly)

| Supports | Details |  
|---|---|
| **Countries**  | Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, United Kingdom  | 
| **Currencies**  | EUR, GBP, SEK | 
| [Chargebacks](/docs/chargebacks/)  | No | 
| [Payment pages](/docs/payment-pages/) | Yes (current version only) |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial  |
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/trustly-payment-flow.svg" alt="Trustly payment flow" style="display: block;
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

You can enable Trustly yourself in your dashboard.

<details id="how-to-activate-trustly"> 
<summary>How to activate Trustly</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings**. 
3. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
4. Select the checkbox for the relevant payment method, and then click **Save changes**.

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>


</details>

# Integration

### API
- [Create order](/reference/createorder/) > Banking order.
- Examples > Trustly redirect.
- Transactions expire after 2 hours.

### Ready-made integrations
- Trustly (direct) is supported in most [ready-made integrations](/docs/our-integrations/).
- Exceptions: Lightspeed, Shopify, OsCommerce, PWAs, Vue Storefront, Zen Cart.

### Testing
To test Trustly payments, see [Testing](/docs/testing#banking-methods).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
