---
title: "Generic gateways in ready-made integrations"
weight: 13
meta_title: "Generic gateways in ready-made integrations - MultiSafepay Docs"
read_more: "."
url: '/integrations/generic-gateways/'
aliases:
    - /faq/general/generic-gateways/
    - /developer/general/generic-gateways/
---

Some of our ready-made integrations use generic gateways, which connect to almost all payment methods we offer. Simply specify the payment method name, logo, and code. 

This avoids the need to update your plugin when we start supporting a new payment method to add its unique gateway. 

Generic gateways support [redirect requests](/developer/api/difference-between-direct-and-redirect/) only.

## Applications

### Gift cards 

Generic gateways can be particularly useful for gift cards, because we don't support all [open-loop gift cards](/payment-methods/gift-cards/open-loop-closed-loop/) in our ready-made integrations and **no** closed-loop gift cards. 

To use generic gateways for gift cards, email the Integration Team at <integration@multisafepay.com>

### Co-branded credit cards

You can integrate Visa co-branded credit cards ([Cartes Bancaires](/payment-methods/cartes-bancaires/), [Dankort](/payment-methods/dankort/), [V&nbsp;Pay](/payment-methods/vpay/)), using the generic `VISA` gateway.  

For the logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons/tree/master/methods).

## Specific plugins
For more information about generic gateways for a specific plugin, see:

- [Craft commerce](/payments/integrations/ecommerce-platforms/craftcommerce/faq/generic-gateways/)
- [Drupal 8 & 9](/payments/integrations/ecommerce-platforms/drupal8/faq/configuring-generic-gateways/)
- [Magento 1](/payments/integrations/ecommerce-platforms/magento1/faq/generic-gateways/)
- [Magento 2](/payments/integrations/ecommerce-platforms/magento2/faq/configuring-generic-gateways/)
- [Odoo](/payments/integrations/ecommerce-platforms/odoo/faq/generic-gateways/)
- [OpenCart](/payments/integrations/ecommerce-platforms/opencart/faq/configuring-generic-gateways/)
- [Shopware 5](/payments/integrations/ecommerce-platforms/shopware5/faq/configuring-generic-gateways/)
- [Shopware 6](/payments/integrations/ecommerce-platforms/shopware6/faq/generic-gateways/)
- [WooCommerce](/payments/integrations/ecommerce-platforms/woocommerce/faq/configuring-generic-gateways/)
