---
title: 'Giropay'
category: 6298bd782d1cf4006032e765
order: 109
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'giropay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Giropay.svg" width="90" align="right" style="margin: 20px; max-height: 75px"/>

[Giropay](https://www.giropay.de/) is the leading inter-bank payment method in Germany, connecting all major German retail banks. Customers pay from their own online banking environment. Settlement is instant and guaranteed.

Read how Giropay can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/giropay)

| Overview | Details |
|---|---|
| **Chargebacks**  | No  | 
| **Countries**  | Germany  | 
| **Currencies**  | EUR | 
| **Payment pages** | [Yes](/payment-pages/) (current and deprecated versions) |
| **Refunds** | [Yes](/refunds/): Full and partial |
| **Second Chance** | [Yes](/second-chance/) |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/giropay-payment-flow.svg" alt="Giropay payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses   

- **Order status:** Changes as the customer's order with you progresses towards shipment 
- **Transaction status:** Changes as the funds progress towards settlement in your account balance

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer cancelled the transaction. | Void   | Void   |
| The customer didn't complete payment within 10 minutes. | Expired | Expired |

</details>

<details id="refund-statuses">
<summary>Refund statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| Refund initiated. | Initialized | Initialized |
| Refund complete. | Completed | Completed |

</details>

# Activation

You can activate Giropay yourself in your dashboard. 

<details id="how-to-activate-Giropay"> 
<summary>How to activate Giropay</summary>
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

To test 

| Integration | Details |
|---|---|
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Giropay redirect  |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/). |
<br>

> ℹ️ Testing
> To test Giropay payments, see [Testing](/testing/#banking-methods).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
