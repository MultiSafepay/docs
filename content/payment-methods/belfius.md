---
title: 'Belfius'
category: 6298bd782d1cf4006032e765
order: 105
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'belfius'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Belfius.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

[Belfius](https://www.belfius.be/common/EN/fw/language.html) is a popular online banking payment method for Belfius bank customers in Belgium.

Read how Belfius can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/belfius)

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Belgium  | 
| [Currencies](/docs/currencies/)  | EUR | 
| [Chargebacks](/docs/chargebacks/)  | No | 
| [Payment pages](/docs/payment-pages/) | Yes (current version only) |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial (1 business day after payment is completed) |
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow
This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/belfius-payment-flow.svg" alt="Belfius payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

> **Note:** MultiSafepay doesn’t automatically receive the customer's IBAN when a transaction is completed, but we import our bank statements daily. All incoming payments are then completed. 

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Belfius. | Initialized | Initialized |
| MultiSafepay has collected payment.| Completed | Completed |
| You cancelled the transaction. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 5 days. | Expired | Expired |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete. | Completed | Completed |

> **Note:** If the customer doesn’t click the **Return to website** button, MultiSafepay doesn’t receive an update and the <<glossary:transaction status>> remains **Initialized**. We import our bank statements daily and finalize all incoming payments. 

# Activation 

You can activate Belfius yourself in your dashboard. 

<details id="how-to-activate-belfius"> 
<summary>How to activate Belfius</summary>
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
- Examples > Belfius direct/redirect.
- Transactions expire after 5 days.

### Ready-made integrations
- Supported in most [ready-made integrations](/docs/our-integrations/).
- Exceptions: OsCommerce and ZenCart.

### Testing
To test Belfius payments, see [Testing](/docs/testing#banking-methods).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
