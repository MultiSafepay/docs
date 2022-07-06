---
title: 'Request to Pay'
category: 6298bd782d1cf4006032e765
order: 113
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'request-to-pay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/RTP.svg" width="60" align="right" style="margin: 20px; max-height: 75px"/>

Request to Pay is a Deutsche Bank payment method based on the PSD2 Open Banking API. Customers are redirected to Deutsche Bank online banking to authenticate themselves, and authorize a secure SEPA transfer. Settlement is instant (if supported) or within 24 hours. 

The funds are transferred directly to your business bank account, instead of your account balance, which simplifies reconciliation.

Read how Request to Pay can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/request-to-pay)

> ⚠️ Availability
> Request to Pay is currently not available to new merchants. It is still supported for existing merchants. 

| Supports | Details |
|---|---|
| **Amount limits** | Minimum amount: 1 EUR, maximum amount: 15,000 EUR |
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Germany – More countries will follow as more banks migrate to PSD2 APIs. | 
| [Currencies](/docs/currencies/)  | EUR | 
| [Chargebacks](/docs/chargebacks/)  | No  | 
| [Payment pages](/docs/payment-pages/) | Yes (current version only) |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial <br> All refunds are processed by Deutsche Bank. |
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/request-to-pay-payment-flow.svg" alt="Request to Pay payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Deutsche Bank. | Initialized | Initialized |
| Deutsche Bank has authorized the transaction and is transfering the funds. | Completed  | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Deutsche Bank declined the transaction. | Declined | Declined   |
| The customer cancelled the transaction at Deutsche Bank. | Void | Void |
| The customer didn't complete payment within 1 hour. | Expired | Expired |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete. | Completed | Completed |
| Refund declined. | Declined | Declined |

# Activation

You can activate Request to Pay yourself in your dashboard. 

<details id="how-to-activate-request-to-pay"> 
<summary>How to activate Request to Pay</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings**. 
3. To activate the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
4. Select the checkbox for the payment method, and then click **Save changes**.

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>


</details>

# Integration

### API
- [Create order](/reference/createorder/) > Banking order.
- Examples > Request to Pay direct/redirect.
- Transactions expire after 1 hour.

### Ready-made integrations
**Not** supported in our [ready-made integrations](/docs/our-integrations/).

### Testing
You can't test Request to Pay in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
