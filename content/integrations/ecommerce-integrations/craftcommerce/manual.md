---
title : "MultiSafepay Craft Commerce 3 installation and configuration manual"
meta_title: "Craft Commerce 3 plugin manual - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases: 
    - /plugins/craftcommerce/manual
    - /integrations/plugins/craftcommerce/manual
    - /integrations/craftcommerce/manual

---

This technical manual is for installing and configuring the MultiSafepay plugin for Craft Commerce 3.

You can install the plugin via:

+ [Craft Plugin Store](https://plugins.craftcms.com/multisafepay)
+ Composer

To install the plugin using Composer:

### Requirements
- Craft CMS version 3.2 or higher
- PHP 7.0 and higher
- Tested with PHP 7.0 

### Installation
Run the following commands in the CLI:

```
composer require multisafepay/craft-commerce
./craft plugin/install multisafepay
```

The latest stable release is downloaded and installed in your Craft Commerce webshop.

### Configuration
1. Sign in to the backend of your Craft Commerce webshop.
2. To configure the plugin settings, go to **MultiSafepay** > **Settings**.  
3. To add payment methods activated in your [MultiSafepay account](https://merchant.multisafepay.com) and configure gateways, go to **Commerce** > **System settings** > **Gateways**.  
  
For any questions about the plugin, email the Integration Team at <integration@multisafepay.com>

### Features

- Support for separate payment methods, billing suites, and gift cards
- Partial and full refunds for non-billing suite payment methods
- Customizable order statuses
- Shipment notifications for billing suite payment methods

### Discounts
Discounts are not supported by the MultiSafepay Craft Commerce 3 plugin.
