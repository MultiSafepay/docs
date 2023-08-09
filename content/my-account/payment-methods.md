---
title: "Payment methods"
category: 62962dcdbccb9a001d4bbc81
order: 11
hidden: false
parentDoc: 62b0845857c8ab006af6a4f7
slug: 'payment-methods'
excerpt: 'Activate payment methods for your account.'
---
<!-- Some payment methods you can activate yourself in your dashboard, but for some you need to apply to MultiSafepay first. Other methods with specific requirements follow their own activation flow.  

| Activation flow | Payment methods |
|---|---|
| [Apply to MultiSafepay](#apply-to-multisafepay) then activate in dashboard | Credit and debit cards and wallets (**except** PayPal), direct debit, Dotpay, in3, Pay After Delivery |
| [Activate in dashboard](#activate-in-dashboard) | Banking methods, E-Invoicing   |
| [Own flow](#own-flow) | Betaal per Maand, Klarna, Edenred, gift cards, Paysafecard, PayPal, Riverty |

### Ready-made integrations

If you use a [ready-made integration](/docs/our-integrations/), first check that the payment method is supported. 
Once the method is activated, also enable it in your <<glossary:backend>>.

### Payment methods by country

<details id="payment-methods-by-country">
<summary>Payment methods by country</summary>
<br>

| Country | Payment methods |
|---|---|
| All countries | Alipay, Alipay+, American Express, Apple Pay, E-Invoicing, Google Pay, Maestro, Mastercard, PayPal, Paysafecard, Visa, WeChat Pay |
| Austria | EPS, Klarna, PayPal, Sofort, Trustly |
| Belgium | Bancontact, Belfius, CBC/KBC, Edenred, gift cards, Klarna, PayPal, Riverty, Sofort, Trustly |
| Bulgaria | PayPal, Trustly |
| Croatia | PayPal, Trustly |
| Cyprus | PayPal, Trustly |
| Czech Republic | PayPal, Trustly, TrustPay |
| Denmark | Dankort, Klarna, PayPal, Trustly |
| Estonia | PayPal, Trustly |
| Europe (SEPA area) | Bank transfer, direct debit, PayPal |
| Finland | PayPal, Trustly |
| France | Cartes Bancaires, Klarna, PayPal |
| Germany | Giropay, Klarna, Request to Pay, PayPal, Sofort, Trustly |
| Greece | PayPal, Trustly |
| Hungary | PayPal, Trustly |
| Ireland | PayPal, Trustly |
| Italy | Klarna, MyBank, PayPal, Postepay, Sofort, Trustly |
| Latvia | PayPal, Trustly |
| Lithuania | PayPal, Trustly |
| Luxembourg | PayPal, Trustly |
| Malta | PayPal, Trustly |
| Netherlands | Betaal per Maand, gift cards, iDEAL, in3, Klarna, Pay After Delivery, PayPal, Riverty, Trustly |
| Norway | Klarna, PayPal, Trustly |
| Poland | Dotpay, PayPal, Sofort, Trustly |
| Portugal | PayPal, Trustly |
| Romania | PayPal, Trustly |
| Slovakia | PayPal, Trustly |
| Slovenia | PayPal, Trustly |
| Spain | Klarna, PayPal, Sofort, Trustly |
| Sweden | Klarna, PayPal, Trustly |
| Switzerland | PayPal, Sofort |
| United Kingdom | PayPal, Trustly |

</details>

# Apply to MultiSafepay 

1. Email a request to <sales@multisafepay.com> 
    
    <details id="required-information-for-cards-apple-google"> 
    <summary>Required information for cards, Apple Pay, and Google Pay</summary>
    <br>
    
    For cards, Apple Pay, and Google Pay, include in the request your: 
    - Average, minimum, and maximum transaction amount 
    - Annual turnover 

    <br>

    </details>

    <details id="required-information-for-direct-debits"> 
    <summary>Required information for direct debits</summary>
    <br>

    For direct debits, include in the request the following information:
    - Monthly and annual direct debit transaction volume
    - Minimum and maximum transaction amount
    - Type of products sold using this payment method
    - Whether you want to accept [recurring payments](/docs/recurring-payments/)
    - Whether any subscriptions are monthly, quarterly, or annual
    - Any additional information we request  

    <br>

    We send you an agreement to sign and email back to us.
    
    </details>
2. We check your eligibility and if approved, activate the payment method for your account. 
3. Once approved, activate the method in your dashboard as below.

# Activate in dashboard

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. To activate the payment method for:
    - All sites, go to **Settings** > **Payment methods**.
    - A specific site:
        - Go to **Sites**, and then click the relevant site.
        - Under **Payment methods**, click **Select payment methods**.
3. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com>

-->

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
3. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email [support@multisafepay.com](mailto:support@multisafepay.com)

For instructions to activate additional payment methods, see the respective pages.

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