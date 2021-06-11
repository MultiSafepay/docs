---
title: "Generic gateways"
weight: 13
meta_title: "FAQ General - Generic gateways - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
---

In our plugins, we use predefined gateways for specific payment methods. When we start supporting a new payment method, merchants need to update their plugin to use the new gateway. 

To avoid this, some of our plugins use generic gateways which include a flexible gateway code that lets them connect to almost every payment method we offer, without updating the plugin.

### Gift cards 

Generic gateways can be particularly useful for gift cards, because we don't support all open-loop gift cards in our ecommerce integrations and no [closed-loop gift cards](/faq/general/multisafepay-glossary/#closed-loop-gift-card). Therefore in some integrations, we use generic gift card gateways.

For more information about integrating open-loop and closed-loop gift cards in our platform, email the Integration Team at <integration@multisafepay.com>

### Requirements

We only support redirect gateways.

### Specific plugins
For more information about a specific plugin, see:

- [Craft commerce](/integrations/ecommerce-integrations/craftcommerce/faq/generic-gateways/)
- [Drupal 8 & 9](/integrations/ecommerce-integrations/drupal8/faq/generic-gateways/)
- [Magento 1](/integrations/ecommerce-integrations/magento1/faq/generic-gateways/)
- [Magento 2](/integrations/ecommerce-integrations/magento2/faq/generic-gateways/)
- [OpenCart](/integrations/ecommerce-integrations/opencart/faq/generic-gateways/)
- [Shopware 5](/integrations/ecommerce-integrations/shopware5/faq/generic-gateways/)
- [Shopware 6](/integrations/ecommerce-integrations/shopware6/faq/generic-gateways/)
- [WooCommerce](/integrations/ecommerce-integrations/woocommerce/faq/generic-gateways/)
