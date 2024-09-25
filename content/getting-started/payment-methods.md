---
title: "Payment methods"
category: 627bbcf80c1c9c0050320b60
order: 9
hidden: false
parentDoc: 62b0845857c8ab006af6a4f7
slug: 'payment-methods'
excerpt: 'Activate payment methods for your account.'
---

MultiSafepay offers a wide range of payment methods.

[block:html]
{
  "html": "<div class=\"auto-grid\">\n    <div class=\"card-container\">\n        <a href=\"/docs/banking-methods\" style=\"text-decoration: none;\">\n            <div>\n                <img src=\"https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Banks.png\" style=\"margin: 15px; max-height: 40px\">\n                <div class=\"container\">\n                    <h4><b>Banking methods</b></h4>\n                </div>\n            </div>\n        </a>\n    </div>\n    <div class=\"card-container\">\n        <a href=\"/docs/bnpl\" style=\"text-decoration: none;\">\n            <div>\n                <img src=\"https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/BNPL.png\" style=\"margin: 15px; max-height: 40px\">\n                <div class=\"container\">\n                    <h4><b>Buy Now Pay Later</b></h4>\n                </div>\n            </div>\n        </a>\n    </div>\n    <div class=\"card-container\">\n        <a href=\"/docs/cards\" style=\"text-decoration: none;\">\n            <div>\n                <img src=\"https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/creditcard2.png\" style=\"margin: 15px; max-height: 40px\">\n             \t<div class=\"container\">\n                    <h4><b>Credit and debit cards</b></h4>\n                </div>\n            </div>\n        </a>\n    </div>\n    <div class=\"card-container\">\n        <a href=\"/docs/prepaid-cards\" style=\"text-decoration: none;\">\n            <div>\n                 <img src=\"https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/PrepaidCards.png\" style=\"margin:15px; max-height: 40px\">\n                <div class=\"container\">\n                    <h4><b>Prepaid cards</b></h4>\n                </div>\n            </div>\n        </a>\n    </div>\n     <div class=\"card-container\">\n        <a href=\"/docs/wallets\" style=\"text-decoration: none;\">\n            <div>\n                <img src=\"https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Digital.png\" style=\"margin:15px; max-height: 40px\">\n                <div class=\"container\">\n                    <h4><b>Wallets</b></h4>\n                </div>\n            </div>\n        </a>\n    </div>\n  </div>\n\n<style>\n\nb {\n  color: #384248 !important;\n}\n  \n.auto-grid {\n  --auto-grid-min-size: 175px;\n  \n  display: grid;\n  grid-template-columns: repeat(auto-fill, minmax(var(--auto-grid-min-size), 1fr));\n}\n\n.card-container {\n  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* this adds the \"card\" effect */\n  padding: 16px;\n  text-align: center;\n  border-radius: 5px;\n  margin: 8px\n} \n\n.card-container:hover {\n  box-shadow: 0 8px 16px 0 rgb(0 0 0 / 20%);\n  transform: translateY(-0.2rem);\n  transition: all 0.2s;\n  cursor: pointer;\n}  \n\n</style>"
}
[/block]

### Activation

Some payment methods, especially Banking methods, can be activated directly via your dashboard.

<details id="how-to-activate-your-payment-methods">
<summary> How to activate standard payment methods</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. To activate the payment method for:
- All sites, go to **Settings** > **Payment methods**.
- A specific site, go to **Sites**, and then click the relevant site.
This overwrites your global selection. Only the payment methods selected for the site will then be available.
3. Select the checkbox for the payment method, and then click **Save changes**.

**💡 Tip**: if you do not set site-specific methods, the global configuration will be applied.

💬  **Support:** If the payment method isn't visible in your dashboard, email [support@multisafepay.com](mailto:support@multisafepay.com)

<details id="how-to-activate-additional-payment-methods">
<summary> How to activate optional payment methods</summary>
<br>
For instructions to activate additional payment methods, see the respective pages and follow individual activation steps.
\


</details>
<br>

If you use a [ready-made integration](/docs/our-integrations/), first check that the payment method is supported.

### Testing

Before you start processing real transactions, test each payment method.  For more information - see [Testing payment methods](/docs/testing)

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)