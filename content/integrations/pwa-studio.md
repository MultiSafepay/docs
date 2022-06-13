---
title: "PWA Studio (Venia) plugin"
category: 62962dd7e272a6002ebbbbc5
order: 115
hidden: false
parentDoc: 62a1d773f96fe80056354d84
excerpt: "Free plugin to integrate MultiSafepay payment solutions into your PWA Studio (Venia)  application."
slug: 'pwa-studio-venia'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Magento_PWA.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

> [View source code](https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration) :link:

> [Download](https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration.git) :arrow-down:

This technical manual is for installing and configuring MultiSafepay's plugin for PWA Studio (Venia).

<details id="requirements">
<summary>Requirements</summary>
<br>

- You will need a [MultiSafepay account](https://testmerchant.multisafepay.com/signup).
- To support GraphQL queries, install the [MultiSafepay Magento 2 GraphQL plugin](https://github.com/MultiSafepay/magento2-graphql).
- You must also meet Magento's requirements for PWA Studio (Venia). See Magento – [Prerequisites](https://magento.github.io/pwa-studio/venia-pwa-concept/setup/#prerequisites).

</details>

<details id="support">
<summary>Support</summary>
<br>

To report a bug or suggest an improvement, create an issue in our GitHub repository. 

For support:

- Email <integration@multisafepay.com>
- Post in the Magento – [MultiSafepay Slack channel](https://magentocommeng.slack.com/messages/multisafepay-payments/)

</details>

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

By default, this plugin supports all [payment methods supported by our Magento 2 plugin](/magento-2/#details-supported-payment-methods) out of the box, except: 
- Request To Pay
- Direct Debit
- E-Invoicing 
- Pay After Delivery  

You can integrate these payment methods yourself.  
See MultiSafepay GitHub – [PWA Studio components](https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration/tree/master/src/components).

</details>

# Installation and configuration 

To install the MultiSafepay plugin in your PWA Studio application, see MultiSafepay GitHub – [Installation guide](https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration#installation-guide).
