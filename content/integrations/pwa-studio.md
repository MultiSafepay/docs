---
title: "PWA Studio (Venia)"
category: 62962dd7e272a6002ebbbbc5
order: 115
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for installing and configuring MultiSafepay's plugin for PWA Studio (Venia)."
slug: 'pwa-studio-venia'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Magento_PWA.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration.git" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

</div>

# Prerequisites

- You will need a [MultiSafepay account](https://testmerchant.multisafepay.com/signup).
- To support GraphQL queries, install the [MultiSafepay Magento 2 GraphQL plugin](https://github.com/MultiSafepay/magento2-graphql).
- You must also meet Magento's requirements for PWA Studio (Venia). See Magento – [Prerequisites](https://magento.github.io/pwa-studio/venia-pwa-concept/setup/#prerequisites).

# Payment methods

By default, this plugin supports all [payment methods supported by our Magento 2 plugin](/docs/magento-2#payment-methods) out of the box, except: 
- Request To Pay
- Direct Debit
- E-Invoicing 
- Pay After Delivery  

You can integrate these payment methods yourself.  
See MultiSafepay GitHub – [PWA Studio components](https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration/tree/master/src/components).

# How to install and configure 

To install the MultiSafepay plugin in your PWA Studio application, see MultiSafepay GitHub – [Installation guide](https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration#installation-guide).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+31020\">support@myshop.com</a></li>\n    <li>To contact MultiSafepay, email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></li>\n  </ul>  \n</blockquote>"
}
[/block]