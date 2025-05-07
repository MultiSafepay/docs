---
title: 'Amazon Pay'
category: 6298bd782d1cf4006032e765
order: 2
hidden: false
parentDoc: 62a6ec51d7a8100053916d99
slug: 'amazon-pay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/amazonpay.svg" width="150" align="right" style="margin: 20px; max-height: 100px"/>

<a href="https://pay.amazon.eu/" target="_blank">Amazon Pay</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a payment method that Amazon customers can use to purchase goods on other sites using their Amazon account. Amazon customers can use any of their stored addresses or payment methods, such as credit or debit cards.

Read how Amazon Pay can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/amazonpay" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country) | Austria, Belgium, Cyprus, Denmark, France, Germany, Hungary, Ireland, Italy, Luxembourg, Netherlands, Portugal, Spain, Sweden, and Switzerland | 
| [Currencies](/docs/currencies/)  | AUD, CHF, DKK, EUR, GBP, HKD, JPY, NOK, NZD, SEK, USD, ZAR <br> **Note:** Settlement currency is **only** available in EUR.| 
| [Chargebacks](/docs/chargebacks/)  | Yes |
| [Discounts](/docs/discounts/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current version only)  |
| [Refunds](/docs/refund-payments/) | Yes: Full, partial, and API refunds | 
| [Second Chance](/docs/second-chance/) | Yes |

# Payment flow

This diagram shows the flow of a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/amazon-pay-payment-flow.svg" alt="Amazon Pay payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

> ℹ **Note** 
>
> MultiSafepay does **not** collect funds for Amazon Pay transactions.

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to Amazon Pay. | Initialized | Initialized |
| The customer has confirmed the order. | Completed | Initialized  |
| Amazon Pay has declined the order. | Declined | Declined |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete.  | Completed | Completed |

# Activation 

To activate Amazon Pay, you must meet the following requirements:

  - Amazon Pay must be activated in your MultiSafepay account. Email a request to <sales@multisafepay.com>.
  We check your eligibility, and if approved, <a href="https://merchant.multisafepay.com" target="_blank">activate the payment method</a> for your account.
  - You need to have an Amazon Payments merchant account .
  - Add all domains that you plan to integrate with Amazon Pay to the JavaScript Origins in <a href="https://sellercentral-europe.amazon.com/ap/signin?clientContext=261-3274178-1964801&openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fsellercentral-europe.amazon.com%2Fexternal-payments%2Famazon-pay%2Fintegration-central%2Flwa%3F&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=sc_eu_amazon_v2&openid.mode=checkid_setup&language=en_GB&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=sc_amazon_v3_unified&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&mons_redirect=sign_in&ssoResponse=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.8v0nzcUNfvg87h79JzMgFgUezwKdM5Ml0uceIqcZEFofO9OhlWYI8Q.lPsF7E7Sbuflzfz3.DGZ_K1zIZSJW7bokKvKfYDl9PIntIAnwF2yZOV5bVUm9R2HRFhLHui0PBc69qJUh3_B2nY6_kbDBSn_NftsloX4ngqKs30Y4mbuWBieo6p2Pe012-drfSkOAmEgtl8WREgd1pl2WZL6dnkeutDGV6apzKELHb5A-dm1DCHmI2eHvzqxwOcSlocwYLemEM8HL1HoitUuOkg.EegmMY7Ej3whmku3BzG5sw" target="_blank">Seller Central</a>:
      -	Your domain
      -	MSP domain: https://payv2.multisafepay.com
      -	A possible DEV URL.
  - All domains must comply with <a href="https://pay.amazon.eu/help/6023" target="_blank">Amazon Pay's Acceptable Use Policy</a>.


<br>
<details id="create-amazon-pay-account">
<summary>How to create an Amazon Payments merchant account
</summary>
<br>

After Amazon Pay has been activated in your MultiSafepay dashboard, follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Settings** > **Payment methods**.
3. Under **Additional payment methods**, click **Amazon** > **Merchant registration**. 
  You are redirected to create an Amazon Payments merchant account at Amazon Pay.
4. Choose a country and click **Create an Amazon Payments merchant account**.
5. Enter the required information to create an account.
  Amazon sends you a confirmation email.

  
    **💡 Tip!** If you already have an **Amazon Payments merchant account**, click **Sign in** at the bottom of the **Create an account** box.

</details>
<br>
💬  **Support:** If the payment method isn't visible in your dashboard, email <support@multisafepay.com>

# Integration

Our integration with Amazon Pay supports an additional payment button. 
For more information, see Amazon Pay – <a href="https://developer.amazon.com/docs/amazon-pay-recurring-apb-checkout/additional-payment-button-overview.html" target="_blank">Additional payment button</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

### API
- See API reference – [Create order](/reference/createorder/) > Wallet order.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Amazon Pay direct/redirect**.
  Set `type` to `direct` or `redirect`.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- Transactions expire after 24 hours.

### Ready-made integrations

Available for redirect transactions via our [integrations](/docs/our-integrations/).

Supported in:
- [Lightspeed](/docs/lightspeed/)
- [Magento 1](/docs/magento-1/) and [Magento 2](/docs/magento-2/) 
- [OpenCart 3](/docs/opencart-3/) and [OpenCart 4](/docs/opencart-4/)
- [PrestaShop](/docs/prestashop/)
- [Shopware 6](/docs/shopware-6/)
- [Shopware 5](/docs/shopware-5/)
- [WooCommerce](/docs/woocommerce/)

### Testing
To test Amazon Pay payments, see Testing – [Wallets](/docs/testing#wallets).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
