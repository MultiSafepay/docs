---
title: "ScandiPWA"
category: 62962dd7e272a6002ebbbbc5
order: 2
hidden: false
parentDocs: 67e1463616608a00475c5f28
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'scandipwa'
---
> ❗️ Important:
> 
> This plugin is at end-of-life. It may contain security vulnerabilities, compatibility issues, and lack the latest features. MultiSafepay provides no support for these plugins.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/ScandiPWA.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/scandipwa-multisafepay-payment-integration.git" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/scandipwa-multisafepay-payment-integration" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

</div>

# Prerequisites

- You will need a <a href="https://testmerchant.multisafepay.com/signup" target="_blank">MultiSafepay account</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
- To support GraphQL queries, install the <a href="https://github.com/MultiSafepay/magento2-graphql" target="_blank">MultiSafepay Magento 2 GraphQL</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> plugin.
- You must also meet ScandiPWA and Magento requirements. See ScandiPWA – <a href="https://docs.scandipwa.com/getting-started/getting-started/magento-integration#prerequisites" target="_blank">Prerequisites</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/)
- Banking methods: All
- <<glossary:BNPL>>: All
- Wallets: All
- Prepaid cards:
    - Baby gift card
    - Beauty and Wellness gift card
    - Boekenbon
    - Edenred
    - Fashioncheque
    - Fashion gift card
    - Fietsenbon
    - Gezondheidsbon
    - Givacard
    - Good4fun
    - Goodcard
    - Nationale tuinbon
    - Paysafecard
    - Parfumcadeaukaart
    - Podium
    - Sport en Fit
    - VVV gift card
    - Webshop gift card
    - Wellness gift card
    - Wijncadeau
    - Winkelcheque
    - YourGift

</details>

# Installation

1. Install the MultiSafepay plugin for supporting `GraphQL` queries, which also installs the `MultiSafepay Core`, `Frontend` and `Adminhtml` plugins. For instructions, see MultiSafepay GitHub <a href="https://github.com/MultiSafepay/magento2-graphql" target="_blank">Magento 2 GraphQL</a>.    
2. Configure the payment methods and your API keys in the Magento admin panel.  
3. To configure URLs to your success and cancellation pages, go to **Stores** > **Configuration** > **MultiSafepay** > **General settings** > **Advanced settings** > **Use custom return URLs for PWA storefront integration**.
    - For the **Custom redirect URL after canceling the payment**, we recommend using: `{{store.secure_base_url}}cart`
    - For the **Custom success page url**, we recommend using: `{{store.secure_base_url}}checkout/success?incrementId={{order.increment_id}}&paymentCode={{payment.code}}`
4. Install the ScandiPWA frontend plugin from this repository into your ScandiPWA theme. For instructions, see ScandiPWA - <a href="https://docs.scandipwa.com/stack/extensions/installing-an-extension" target="_blank">Installing an extension</a>.
5. Explore the checkout in your ScandiPWA application:  
<img width="1000" alt="Screenshot 2021-03-12 at 12 56 42" src="https://user-images.githubusercontent.com/78361324/110949265-b0124680-8342-11eb-8d99-55c926e76f3d.png">
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+31020\">support@myshop.com</a></li>\n    <li>To contact MultiSafepay, email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)