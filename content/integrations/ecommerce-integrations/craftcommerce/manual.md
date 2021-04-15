---
title : "MultiSafepay Craft Commerce 3 installation & configuration manual"
meta_title: "Craft Commerce 3 plugin manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
aliases: 
    - /plugins/craftcommerce/manual
    - /integrations/plugins/craftcommerce/manual
    - /integrations/craftcommerce/manual

---

### Introduction

The installation can be carried out in two ways:

+ [Craft Plugin Store](https://plugins.craftcms.com/multisafepay)
+ Composer

In this manual we describe the installation via Composer.

### 1. Requirements
- Craft CMS version 3.2 or higher
- PHP 7.0 and higher
- Tested with PHP 7.0 

### 2. Installation
Run the following commands via the CLI:

```
composer require multisafepay/craft-commerce
./craft plugin/install multisafepay
```

After running these commands, the latest stable release is downloaded and installed within your
Craft Commerce webshop.

### 3. Configuration
1. Log into the backend of your webshop and navigate to _MultiSafepay_ > _Settings_.  
This page contains all the plugin settings.

2. Navigate to _Commerce_ > _System Settings_ > _Gateways_.  
This page contains the gateway settings where you can find all payment methods and giftcards supported by MultiSafepay.  
Ensure that you have the selected payment methods active in your [MultiSafepay Control](https://merchant.multisafepay.com)

### 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>

### Features

- Support for separate payment methods.
- Support for billing suite payment methods.
- Support for gift cards.
- Partial and full refund support for non billing suite payment methods.
- Customizable order statuses.
- Shipment notification for billing suite payment methods.

### Discounts
Discounts are not supported by the MultiSafepay Craft Commerce plugin.