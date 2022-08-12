---
title: 'Sofort'
category: 6298bd782d1cf4006032e765
order: 115
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'sofort'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/SOFORT.svg" width="80" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.klarna.com/pay-now/" target="_blank">Sofort</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a banking payment method by Klarna. It integrates directly with the customer's bank like a direct bank transfer. The customer verifies the payment, which reduces the risks associated with traditional transfers. 
Once payment is completed, the customer cannot reverse it and Sofort guarantees <<glossary:settlement>>.

Read how Sofort can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/sofort" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |  
|---|---|
| **Amount limit** | Minimum amount: 0,10 EUR |
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Austria, Belgium, Germany, Italy, Spain, Switzerland, Poland <br> ❗ Transactions processed in non-supported countries return a [1024 error](/docs/troubleshooting#error-1024-transaction-refused). |
| [Currencies](/docs/currencies/)  | CHF, EUR, GBP, HUF, PLN | 
| [Chargebacks](/docs/chargebacks/)  | No |
| [Payment components](/docs/payment-components/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current version only) |
| [Recurring payments](/docs/recurring-payments/) | Yes|
| [Refunds](/docs/refund-payments/) | Yes: Full and partial  |
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/sofort-payment-flow.svg" alt="Sofort payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized |
| The customer's bank has authorized the transaction and is transfering the funds. This may take up to 3 business days for all amounts. <br> Do **not** ship yet! MultiSafepay assumes no responsibility if you ship and the transaction fails. | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction via Sofort. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 1 day. | Expired | Expired |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete. | Completed | Completed |
<br>

> ℹ Note
> Amounts less than 100 EUR are transfered immediately. The status of orders over 100 EUR changes to **Uncleared** and then to **Completed** after 24 hours.

# Activation

You can activate Sofort yourself in your dashboard.

<details id="how-to-activate-sofort"> 
<summary>How to activate Sofort</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
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
- Examples > Sofort direct/redirect.
- Transactions expire after 1 day.

### Ready-made integrations
Supported in all [ready-made integrations](/docs/our-integrations/). 

### Testing
To test Sofort payments, see [Testing](/docs/testing#banking-methods).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
