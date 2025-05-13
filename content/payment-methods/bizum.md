---
title: 'Bizum'
category: 6298bd782d1cf4006032e765
parentDoc: 62a728d48b97080046c1d220
order: 5
slug: 'bizum'
---

> ⚠️ Note:
> 
> We are currently in the pilot phase for this product in Spain.
> 
> If you are interested in participating in the next stage of our pilot, email  [sales@multisafepay.com](mailto:integration@multisafepay.com)

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Bizum.svg/122px-Bizum.svg.png" width="100" align="right" style="margin: 20px; max-height: 75px"/>


<a href="https://bizum.es/" target="_blank">Bizum</a><i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a mobile payment system in Spain that enables users to make instant transfers through their banking app, providing a quick and secure way to conduct payments.




| Supports                                                      | Details |
| ------------------------------------------------------------- | ------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Spain   |
| [Currencies](/docs/currencies/)                               | EUR     |
| [Chargebacks](/docs/chargebacks/)                             | No      |
| [Payment pages](/docs/payment-pages/)                         | Yes     |



# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.



<img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/diagrams/svg/bizum-payment-flow.svg" alt="Bizum payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px; width: 100%;">

***



# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description                                                                                      | Order status | Transaction status |
| ------------------------------------------------------------------------------------------------ | ------------ | ------------------ |
| The customer has initiated a transaction and gets redirected to Bizum. You can no longer cancel. | Initialized  | Initialized        |
| The customer has completed the authentication.                                                   | Completed    | Initialized        |
| The customer didn't complete payment within 30 minutes.                                          | Expired      | Expired            |
| The authentication failed.                                                                       | Declined     | Declined           |
| **Refunds:** Refund complete.                                                                    | Completed    | Initialized        |
| **Refunds:** Refund declined.                                                                   | Declined     | Declined           |

***



# Activation

1. Request merchant registration at your local bank, and follow guidelines provided by them (for example agreements).
2. Provide MultiSafepay with your **FUC** (Merchant Identification Code), **CSB**, and **Terminal**. 
3. We confirm activation.
4. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
5. To activate the payment method for:

- All websites, go to **Settings** > **Payment methods**.
- A specific website, go to **Websites**, and then click the relevant website.
- Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email [support@multisafepay.com](mailto:integration@multisafepay.com)



# Integration

## API

See API reference – [Create order](/reference/createorder/) > Banking order. 

<details id="example-requests"> 
<summary>Example requests</summary>
<br>

 For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Bizum direct/redirect**.



 Set `gateway` to `BIZUM`, and `type` to `direct` or `redirect`.

<div style="text-align: center;">
  <img
    src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif"
    alt="MultiSafepay Sandbox Test Process GIF"
    style="width: 40%; height: auto;"
  />
</div>

</details>


- Transactions expire after 30 minutes.



## Ready made solutions

Bizum is supported in most <a href="https://docs.multisafepay.com/docs/our-integrations" target="_blank">ready-made integrations</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

- Exceptions:
  - Craft Commerce
  - Odoo
  - OsCommerce
  - Zen Cart

## Testing

Testing will soon be available for this payment method. 



# User guides

## Amount limits

- Minimum order amount:  0.50 EUR
- Maximum order amount: 1,000 EUR
- Maximum amount per day: 2,000 EUR
- Maximum amount per month: 5,000 EUR



## Cancellation

You can no longer cancel a transaction after the status changes to **Initialized**.



## Refunds

You can process full and partial refunds in your dashboard.



[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]


[Top of page](#)