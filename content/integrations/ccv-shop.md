---
title: "CCV Shop"
category: 62962dd7e272a6002ebbbbc5
order: 25
hidden: false
parentDoc: 62a9a54aba9800011a8bda88
slug: 'ccv-shop'
excerpt: "Technical manual for MultiSafepay's free app."
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/CCVShop.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

# Prerequisites

You will need a [MultiSafepay account](/docs/getting-started-guide/).

# Installation and configuration

✅ &nbsp; **Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Sign in to your CCV Shop <<glossary:backend>> and install the MultiSafepay app from the App Store.
2. Enter your [site API key](/docs/sites#site-id-api-key-and-security) and then click **Install**.
**Note:** Your MultiSafepay environment is based on your API Key.
3. To enable refunds:
- Click **Edit**, and then click the **Enable/disable automatic refunds** toggle. 
- Click **Update**.
4. To update payment methods,
- Click **Edit**, and then click **Update payment methods**. 
- Click **Update**.
<br>
___

# User guide

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/) 
- BNPL:
  - [Betaal per Maand (Santander)](/docs/betaal-per-maand)
  - [E-invoicing](/docs/E-invoicing/)
  - [in3](/docs/in3)
  - [Klarna](/docs/klarna)
  - [Pay After Delivery](/docs/pay-after-delivery)
  - [Riverty (AfterPay)](/docs/riverty)
- Banking methods:
  - [Bancontact](/docs/bancontact/)
  - [Bank transfer](/docs/bank-transfer/)
  - [Belfius](/doc/belfius)
  - [Direct debit](/doc/direct-debit)
  - [Dotpay](/docs/dotpay)
  - [EPS](/doc/eps)
  - [Giropay](/docs/giropay/)
  - [iDEAL](/docs/ideal/)
  - [CBC/KBC](/doc/cbc-kbc)
  - [MyBank](/docs/mybank)
  - [Request to Pay](/doc/request-to-pay)
  - [Sofort](/docs/sofort/)
  - [Trustly](/doc/trustly)
  - [TrustPay](/doc/trustpay)
- Prepaid cards:
  - [Edenred](/docs/edenred)
  - [Paysafecard](/docs/paysafecard)
- Wallets: 
  - [Alipay](/docs/alipay)
  - [Alipay+](/docs/alipay-plus)
  - [Amazon Pay](/docs/amazon-pay)
  - [Google Pay](/docs/google-pay)
  - [PayPal](/doc/paypal)
  - [WeChat Pay](/doc/wechat-pay)

</details>

## Refunds

You can process refunds from your MultiSafepay dashboard, and <<glossary:backend>>.

**Note:** To process refunds from your <<glossary:backend>>, you need to have refunds enabled in your MultiSafepay app.

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <ul>\n    <li>For technical queries about the app, email CCV Shop at <a href=\"mailto:support@ccvshop.nl\">support@ccvshop.nl</a></li>\n    <li>To contact MultiSafepay, email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)