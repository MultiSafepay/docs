---
title: 'Dotpay'
category: 6298bd782d1cf4006032e765
order: 107
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'dotpay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/dotpay.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.dotpay.pl/en" target="_blank">Dotpay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is an inter-bank payment method that links all major Polish retail banks. 
Customers pay from their own online banking environment.

Read how Dotpay can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/dotpay" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Poland  | 
| [Currencies](/docs/currencies/)  | EUR, PLN | 
| [Chargebacks](/docs/chargebacks/)  | No | 
| [Payment pages](/docs/payment-pages/) | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial |
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/dotpay-payment-flow.svg" alt="Dotpay payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized|
| MultiSafepay has collected payment. | Completed | Completed |
| The customer didn't complete payment within 3 days. | Expired | Expired |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete. | Completed | Completed |

# Activation 

First apply to MultiSafepay, and then activate in your dashboard. 

<details id="how-to-activate-dotpay"> 
<summary>How to activate Dotpay</summary>
<br>

1. Email a request to <risk@multisafepay.com> 
2. We check your eligibilty and if approved, activate the payment method for your account. 
3. Once approved, sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
4. Go to **Settings**. 
5. To activate the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
6. Select the checkbox for the payment method, and then click **Save changes**.

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>


</details>

# Integration

### API
- [Create order](/reference/createorder/) > Banking order. 
- Examples > Dotpay redirect.
- Transactions expire after 3 days.

### Ready-made integrations
Supported in all [ready-made integrations](/docs/our-integrations/). 

### Testing
To test Dotpay payments, see [Testing](/docs/testing#banking-methods).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
