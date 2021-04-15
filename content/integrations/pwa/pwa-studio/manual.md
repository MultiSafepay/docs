---
title : "MultiSafepay PWA Studio Integration"
meta_title: "PWA Studio (Venia) integration plugin manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

### 1. Requirements
- To use the plugin you need a MultiSafepay account. You can [create a test account here](https://testmerchant.multisafepay.com/signup).
- Install the [MultiSafepay Magento 2 GraphQL plugin](https://github.com/MultiSafepay/magento2-graphql) to add support for GraphQL queries.
- Meet the [Magento's requirements](https://magento.github.io/pwa-studio/venia-pwa-concept/setup/#prerequisites) for PWA Studio (Venia) on Magento.

### 2. Supported payment methods
This extension supports all [payment methods supported by our Magento 2 plugin](https://docs.multisafepay.com/integrations/ecommerce-integrations/magento2/faq/available-payment-methods-magento2/) out of the box, except: 
- Request To Pay
- Direct Debit
- E-invoicing 
- Pay After Delivery  
However, you can easily integrate these payment methods yourself. For reference, you can take a look at our [PWA Studio components](https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration/tree/master/src/components) on GitHub.

### 3. Installation and configuration (GitHub)

If you want to install the MultiSafepay plugin into your PWA Studio application, follow the [installation instructions](https://github.com/MultiSafepay/pwastudio-multisafepay-payment-integration#installation-guide) on our GitHub page.

### Support
If you want to report a bug or suggest and improvement, create an issue on our repository. If you need help with your integration, please contact <integration@multisafepay.com>

We are also available on the [Magento's MultiSafepay Slack channel](https://magentocommeng.slack.com/messages/multisafepay-payments/).
Feel free to start a conversation or provide suggestions as to how we can refine our plugin.
