---
title: "PWA Studio (Venia) plugin"
breadcrumb_title: "PWA Studio"
github_url : "https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration"
download_url : "https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration.git"
changelog_url : "."
layout: 'single'
meta_title: "PWA Studio (Venia) plugin - MultiSafepay Docs"		
meta_description: "Free plugin to integrate MultiSafepay payment solutions with PWA Studio."
weight: 17
logo: "https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Magento_PWA.svg"
url: "/pwa-studio/"
title_short: "PWA Studio (Venia)"
type: "PWA"
description_short: "Free plugin to integrate MultiSafepay payment solutions into your PWA Studio (Venia)  application."
aliases:
  - /payments/integrations/pwa/pwa-studio/
---
This technical manual is for installing and configuring MultiSafepay's plugin for PWA Studio (Venia).

{{< details title="Requirements" >}}

- You will need a [MultiSafepay account](https://testmerchant.multisafepay.com/signup).
- To support GraphQL queries, install the [MultiSafepay Magento 2 GraphQL plugin](https://github.com/MultiSafepay/magento2-graphql).
- You must also meet Magento's requirements for PWA Studio (Venia). See Magento – [Prerequisites](https://magento.github.io/pwa-studio/venia-pwa-concept/setup/#prerequisites).

{{< /details >}}

{{< details title="Support" >}}

To report a bug or suggest an improvement, create an issue in our GitHub repository. 

For support:

- Email <integration@multisafepay.com>
- Post in the Magento – [MultiSafepay Slack channel](https://magentocommeng.slack.com/messages/multisafepay-payments/)

{{< /details >}}

{{< details title="Payment methods" >}}

By default, this plugin supports all [payment methods supported by our Magento 2 plugin](/magento-2/#details-supported-payment-methods) out of the box, except: 
- Request To Pay
- Direct Debit
- E-Invoicing 
- Pay After Delivery  

You can integrate these payment methods yourself.  
See MultiSafepay GitHub – [PWA Studio components](https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration/tree/master/src/components).

{{< /details >}}

### Installation and configuration 

To install the MultiSafepay plugin in your PWA Studio application, see MultiSafepay GitHub – [Installation guide](https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration#installation-guide).
