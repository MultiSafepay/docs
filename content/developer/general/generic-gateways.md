---
title: "Generic gateways"
weight: 13
meta_title: "General developer information - Generic gateways - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/general/generic-gateways/
---

In our plugins, we use predefined gateways for specific payment methods. When we start supporting a new payment method, merchants need to update their plugin to use the new gateway. 

To avoid this, some of our plugins use generic gateways which include a flexible gateway code that lets them connect to almost every payment method we offer, without updating the plugin.

### Gift cards 

Generic gateways can be particularly useful for gift cards, because we don't support all open-loop gift cards in our ecommerce integrations and no [closed-loop gift cards](/faq/general/multisafepay-glossary/#closed-loop-gift-card). Therefore in some integrations, we use generic gift card gateways.

For more information about integrating open-loop and closed-loop gift cards in our platform, email the Integration Team at <integration@multisafepay.com>

### Requirements

We only support [`redirect`](/developer/api/difference-between-direct-and-redirect/) gateways.

### Specific plugins
For more information about a specific plugin, see:

- [Craft commerce](/payments/integrations/ecommerce-platforms/craftcommerce/faq/generic-gateways/)
- [Drupal 8 & 9](/payments/integrations/ecommerce-platforms/drupal8/faq/configuring-generic-gateways/)
- [Magento 1](/payments/integrations/ecommerce-platforms/magento1/faq/generic-gateways/)
- [Magento 2](/payments/integrations/ecommerce-platforms/magento2/faq/configuring-generic-gateways/)
- [Odoo](/payments/integrations/ecommerce-platforms/odoo/faq/generic-gateways/)
- [OpenCart](/payments/integrations/ecommerce-platforms/opencart/faq/configuring-generic-gateways/)
- [Shopware 5](/payments/integrations/ecommerce-platforms/shopware5/faq/configuring-generic-gateways/)
- [Shopware 6](/payments/integrations/ecommerce-platforms/shopware6/faq/generic-gateways/)
- [WooCommerce](/payments/integrations/ecommerce-platforms/woocommerce/faq/configuring-generic-gateways/)
