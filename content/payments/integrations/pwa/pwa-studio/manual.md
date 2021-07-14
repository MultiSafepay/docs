---
title : "MultiSafepay PWA Studio Integration"
meta_title: "PWA Studio (Venia) integration plugin manual - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< details title="Requirements" >}}

- You will need a [MultiSafepay account](https://testmerchant.multisafepay.com/signup).
- To support GraphQL queries, install the [MultiSafepay Magento 2 GraphQL plugin](https://github.com/MultiSafepay/magento2-graphql).
- You must also meet Magento's requirements for PWA Studio (Venia). See Magento – [Prerequisites](https://magento.github.io/pwa-studio/venia-pwa-concept/setup/#prerequisites).

{{< /details >}}

{{< details title="Supported payment methods" >}}

By default, this plugin supports all [payment methods supported by our Magento 2 plugin](/payments/integrations/ecommerce-platforms/magento2/faq/supported-payment-methods/) out of the box, except: 
- Request To Pay
- Direct Debit
- E-Invoicing 
- Pay After Delivery  
You can integrate these payment methods yourself. See MultiSafepay GitHub – [PWA Studio components](https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration/tree/master/src/components).

{{< /details >}}

### Installation and configuration 

To install the MultiSafepay plugin in your PWA Studio application, see MultiSafepay GitHub – [Installation guide](https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration#installation-guide).

### Support
To report a bug or suggest an improvement, create an issue in our GitHub repository. 

For support:

- Email the Integration Team at <integration@multisafepay.com>
- Post in the Magento – [MultiSafepay Slack channel](https://magentocommeng.slack.com/messages/multisafepay-payments/)

