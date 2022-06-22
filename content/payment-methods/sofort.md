---
title: 'Sofort'
category: 6298bd782d1cf4006032e765
order: 114
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'sofort'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/SOFORT.svg" width="80" align="right" style="margin: 20px; max-height: 75px"/>

[Sofort](https://www.klarna.com/pay-now/) is a banking payment method by Klarna. It integrates directly with the customer's bank like a direct bank transfer. The customer verifies the payment, which reduces the risks associated with traditional transfers. 
Once payment is completed, the customer cannot reverse it and Sofort guarantees settlement.

Read how Sofort can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/sofort)

| Overview | Details |  
|---|---|
| **Amount limit** | Minimum amount: 0,10 EUR |
| **Chargebacks**  | No | 
| **Countries**  | Austria, Belgium, Germany, Italy, Spain, Switzerland, Poland <br> ❗ Transactions processed in non-supported countries return a [1024 error](/docs/errors#error-1024-transaction-refused).  | 
| **Currencies**  | EUR (GBP, CHF, PLN **not** supported) | 
| **Expiration** | Transactions expire after 1 day. |
| **Payment components** | [Yes](/docs/payment-components/) |
| **Payment pages** | [Yes](/docs/payment-pages/) (current version only) |
| **Recurring payments** | [Yes](/docs/recurring-payments/)|
| **Refunds** | [Yes](/docs/refund-payments/): Full and partial  |
| **Second Chance** | [Yes](/docs/second-chance/) |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/sofort-payment-flow.svg" alt="Sofort payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

| Description | <<glossary:Order status>> | <<glossary:Transaction status>> |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized |
| The customer's bank has authorized the transaction and is transfering the funds. This may take up to 3 business days for all amounts. <br> Do **not** ship yet! MultiSafepay assumes no responsibility if you ship and the transaction fails. | Uncleared | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction via Sofort. | Void   | Void/Cancelled   |
| The customer didn't complete payment within 1 day. | Expired | Expired |

</details>

<details id="refund-statuses">
<summary>Refund statuses</summary>
<br>

| Description | <<glossary:Order status>> | <<glossary:Transaction status>> |
|---|---|---|
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |
<br>

> ℹ️ Note
> Amounts less than 100 EUR are transfered immediately. The status of orders over 100 EUR changes to **Uncleared** and then to **Completed** after 24 hours.

</details>

# Activation

You can activate Sofort yourself in your dashboard.

<details id="how-to-activate-sofort"> 
<summary>How to activate Sofort</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings**. 
3. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
4. Select the checkbox for the relevant payment method, and then click **Save changes**.

> 💬  Support
> If the payment method isn't visible in your dashboard, email <integration@multisafepay.com> 

</details>

# Integration

| Integration | Details |
|---|---|
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Sofort direct/redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/docs/our-integrations/). |
<br>

> ℹ️ Testing
> To test Sofort payments, see [Testing](/docs/testing#banking-methods).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
