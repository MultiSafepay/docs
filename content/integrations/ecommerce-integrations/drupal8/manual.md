---
title : "MultiSafepay Drupal 8 & 9 installation & configuration manual"
meta_title: "Drupal 8 & 9 plugin manual - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases: 
    - /plugins/drupal8/manual
    - /integrations/plugins/drupal8/manual
    - /integrations/drupal8/manual
---

This technical manual is for installing and configuring the MultiSafepay plugin for Drupal 8 & 9 webshop. 

We recommend first installing the plugin in a test environment following the recommended Shopware 6 installation procedure. Make sure you have made a backup.

You can install the plugin via:

+ Composer
+ Your Drupal 8 & 9 backend

To install the plugin via Composer:

### Technical support
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

### Requirements
- MultiSafepay account – See [Getting started](/guides/getting-started/).
- Drupal 8.9 and above or Drupal 9.x
- Tested on PHP 7.2
- Drupal Commerce 2.x

### Installation
To install the latest stable version of our Drupal Commerce 2.x plugin, run the following command in your terminal:

```
composer require drupal/commerce_multisafepay_payments
```

The latest stable release is downloaded and installed in your Drupal Commerce 2.x webshop.

### Configuration  
1. Log in to the backend of your webshop.
2. Go to **Commerce** > **Configuration** > **Payments** > **MultiSafepay settings**.
3. Enter your account ID, site ID, site code or API key. {{% account_info %}}
4. Go to **Commerce** > **Configuration** > **Payments** > **Payment gateways**.
5. Configure the options for all supported payment methods activated in your [MultiSafepay Control](https://merchant.multisafepay.com).

For any questions about the plugin, email the Integration Team at <integration@multisafepay.com>

### Support phase out

Drupal no longer provides security updates for Drupal 8.9.x, and will only provide bugfix support until early 2021 and security fixes until November 2021. 

For more information about upgrading from Drupal 8 to Drupal 9, see Drupal - [Upgrading from Drupal 8 to Drupal 9 or higher](https://www.drupal.org/docs/upgrading-drupal/upgrading-from-drupal-8-to-drupal-9-or-higher).
