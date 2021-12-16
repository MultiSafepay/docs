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

Some of our ready-made integrations use a generic gateway, which connects to almost all payment methods we offer. Simply specify the payment method name, logo, and code. 

This avoids the need to update your plugin to support the unique gateway for new payment methods. 

Generic gateways support [redirect requests](/developer/api/difference-between-direct-and-redirect/) only.

## Applications

### Gift cards 

Use the generic gateway to integrate [custom gift cards](/payment-methods/gift-cards/custom-cards/).

The generic gateway is particularly useful for gift cards, because we don't support all [open-loop gift cards](/payment-methods/gift-cards/open-loop-closed-loop/) in our ready-made integrations and **no** closed-loop gift cards. 

For support, email the Integration Team at <integration@multisafepay.com>

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
- [PrestaShop](/payments/integrations/ecommerce-platforms/prestashop-1-7/faq/configuring-generic-gateways/)
- [Shopware 5](/payments/integrations/ecommerce-platforms/shopware5/faq/configuring-generic-gateways/)
- [Shopware 6](/payments/integrations/ecommerce-platforms/shopware6/faq/generic-gateways/)
- [WooCommerce](/payments/integrations/ecommerce-platforms/woocommerce/faq/configuring-generic-gateways/)
