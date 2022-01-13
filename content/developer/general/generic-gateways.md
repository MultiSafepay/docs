---
title: "Generic gateways in ready-made integrations"
weight: 13
meta_title: "Generic gateways in ready-made integrations - MultiSafepay Docs"
read_more: "."
url: '/developer/generic-gateways/'
aliases:
    - /faq/general/generic-gateways/
    - /developer/general/generic-gateways/
    - /integrations/multisafepay-gateway/
    - /integrations/generic-gateways/
---
Some of our ready-made integrations use a generic gateway, which redirects customers from your webshop checkout to a MultiSafepay payment page displaying your selected payment methods. You can specify which methods to include, and how to display their logos on the page.

Generic gateways support:

- All payment methods
- All [payment features](/payment-features/), except [Recurring payments](/features/recurring-payments/)
- [Redirect requests](/developer/api/difference-between-direct-and-redirect/) only

Using a generic gateway means you don't need to update your integration when we add new payment methods. 

### Gift cards 

Generic gateways are particularly useful for integrating [gift cards](/payment-methods/gift-cards/), including [custom gift cards](/payment-methods/gift-cards/custom-cards/). This is because we don't support all [open-loop gift cards](/payment-methods/gift-cards/open-loop-closed-loop/) in our ready-made integrations and **no** closed-loop gift cards. 

For support, email the Integration Team at <integration@multisafepay.com>

### Co-branded credit cards

You can integrate Visa co-branded credit cards ([Cartes Bancaires](/payment-methods/cartes-bancaires/), [Dankort](/payment-methods/dankort/), and [V&nbsp;Pay](/payment-methods/vpay/)), using the generic `VISA` gateway.  

For the logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons/tree/master/methods).

## Configuring generic gateways

For how to configure generic gateways, see the manual of your ready-made integration:

- [Craft Commerce](/craft-commerce/configuring-generic-gateways/)
- [Drupal 8 & 9](/drupal-8-9/configuring-generic-gateways/)
- [Magento 2](/magento-2/generic-gateways/), [Magento 1](/magento-1/configuring-generic-gateways/)
- [Odoo](/odoo/generic-gateways/)
- [OpenCart](/opencart/generic-gateways/)
- [PrestaShop 1.7](/prestashop-1-7/generic-gateways/)
- [Shopware 5](/shopware-5/generic-gateways/), [Shopware 6](/shopware-6/generic-gateways/)
- [WooCommerce](/woo-commerce/generic-gateways/)

Use the relevant [payment method gateway IDs](/developer/gateway-ids).

## MultiSafepay gateways

Our ready-made integrations also support a MultiSafepay payment gateway. This redirects customers from your webshop checkout to a MultiSafepay payment page displaying **all** of your activated payment methods. 

To activate the MultiSafepay gateway for all websites in your account:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com/).
2. Go to **Settings** > **Payment methods**.
3. Under **Standard payment methods**, select the **MultiSafepay** checkbox.
4. Click **Save changes**.

