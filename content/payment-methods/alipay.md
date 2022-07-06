---
title: 'Alipay'
category: 6298bd782d1cf4006032e765
order: 501
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'alipay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/Alipay.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

[Alipay](https://global.alipay.com/platform/site/ihome) is a leading global payment method that lets Chinese customers link their credit card or bank account to a digital wallet. It supports online, QR, and contactless POS payments, as well as international money transfers.

For Chinese customers, Alipay accounts are verified and linked to their Chinese bank account. Since 2021, non-Chinese customers can also pay with Alipay using the Tour Pass.

Read how Alipay can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/alipay)

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Worldwide  | 
| [Currencies](/docs/currencies/)  | EUR, USD (currency conversion in EUR only)  | 
| [Chargebacks](/docs/chargebacks/)  | No  |
| [Discounts](/docs/discounts/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current version only)  |
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds | 
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/alipay-payment-flow.svg" alt="Alipay payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Alipay. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| The customer didn't complete payment within 5 hours, or it was cancelled. | Expired | Expired |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete.  | Completed | Completed |


# Activation 

First apply to MultiSafepay, and then activate in your dashboard. 

<details id="how-to-activate-Alipay"> 
<summary>How to activate Alipay</summary>
<br>

1. Email a request to <risk@multisafepay.com> 
2. We check your eligibilty and if approved, activate the payment method for your account. 
3. Once approved, sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
4. Go to **Settings**. 
5. To activate the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
6. Select the checkbox for the payment method, and then click **Save changes**.

> **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>


</details>

# Integration

### API
- [Create order](/reference/createorder/) > Wallet order.
- Examples > Alipay direct/redirect.
- Transactions expire after 5 hours.

### Ready-made integrations
- Supported in all [ready-made integrations](/docs/our-integrations/) (direct).
- Exceptions: PrestaShop 1.6, OsCommerce, and Zen Cart.

### Testing
To test Alipay payments, see [Testing](/docs/testing#wallets).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
