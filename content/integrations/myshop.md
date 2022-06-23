---
title: "myShop"
category: 62962dd7e272a6002ebbbbc5
order: 205
hidden: false
parentDoc: 62a9a54aba9800011a8bda88
slug: 'myshop'
excerpt: "Free app to integrate MultiSafepay payment solutions with myShop."
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/myShop.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

This technical manual is for installing and configuring myShop's free app for integrating with MultiSafepay.

<details id="requirements">
<summary>Requirements</summary>
<br>

You will need a [MultiSafepay account](/getting-started-guide/).

</details>

<details id="payment-methods">
<summary>Payment methods</summary>
<br>


- Cards: [American Express](/payment-methods/amex), [Mastercard](/payment-methods/mastercard), and [Visa](/payment-methods/visa)
- Pay later methods: [Klarna](/payment-methods/klarna) and [Pay After Delivery](/payment-methods/pay-after-delivery)
- Wallets: [PayPal](/payment-methods/paypal)
- Prepaid cards: [123TCS](/payments/methods/prepaid-cards/gift-cards), [Intersolve](/payments/methods/prepaid-cards/gift-cards), and [Fashioncheque](/payments/methods/prepaid-cards/gift-cards)
- Banking methods:
    - [Bancontact](/payment-methods/bancontact)
    - [Bank Transfer](/payment-methods/bank-transfer)
    - [Dotpay](/payment-methods/dotpay)
    - [EPS](/payment-methods/eps)
    - [Giropay](/payment-methods/giropay)
    - [iDEAL](/payment-methods/ideal)
    - [Maestro](/payment-methods/maestro)
    - [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
    - [Sofort](/payment-methods/sofort)
</details>

# How to install and configure

:warning: We recommend first installing the plugin in a test environment, following the myShop installation procedure. Always make a backup.

1. Sign in to your myShop <<glossary:backend>>.
2. Install the MultiSafepay app in the App Store.
3. Go to **Settings** > **MultiSafepay** or **iDEAL MultiSafepay**.
4. Enter your [account ID, site ID, and site secure code](/sites/#site-id-api-key-and-secure-code).  
5. If using a test account, select **Test mode**.
6. Click **Save**.

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <ul>\n    <li>For technical queries about the app, email myShop at <a href=\"mailto:support@myshop.com\">support@myshop.com</a></li>\n    <li>To contact MultiSafepay, email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></li>\n  </ul>  \n</blockquote>"
}
[/block]