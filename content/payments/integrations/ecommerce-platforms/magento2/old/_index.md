---
title : "MultiSafepay Magento 2 (Deprecated)"
github_url : "https://github.com/MultiSafepay/Magento2Msp"
download_url: "https://github.com/MultiSafepay/Magento2Msp/releases/download/1.14.1/Plugin_Magento2_1.14.1.zip"
description : "This manual is for the deprecated Magento 2 plugin."
meta_title: "Magento 2 plugin manual V1 - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
changelog: https://github.com/MultiSafepay/Magento2Msp/blob/master/CHANGELOG.md
layout: 'single'
faq: '.'
---

{{< alert-notice >}} **Alert!** This plugin is end-of-life and we are phasing out support. Migrate to the [new plugin](/payments/integrations/ecommerce-platforms/magento2/) as soon as possible. {{< /alert-notice >}}

### Introduction

The installation can be carried out in three ways:

+ SFTP
+ Composer
+ Magento Marketplace.

In this manual we describe the installation via Composer.

{{% introduction_plugin "Magento 2" %}}

### 1. Requirements
- Magento Open Source version 2.2.x & 2.3.x & 2.4.x 
- PHP 7.0 and higher
- Tested with PHP 7.0 (Magento 2.3.x adds support for 7.2)

_*If you are using [Magento Commerce](https://magento.com/products/magento-commerce), contact us at <integration@multisafepay.com>_

### 2. Installation
Run the following commands via the CLI:

```
composer require multisafepay/magento2msp
php bin/magento setup:upgrade
php bin/magento setup:static-content:deploy
```

After running these commands, the latest stable release is downloaded and installed within your
Magento 2 webshop.

Depending on your webserver/webshop configuration you also need to check:

- Set rights on files correctly. Our files can be found at vendor/multisafepay/magento2msp
- Empty static files when running in production mode
- Flush cache.

### 3. Configuration
1. Sign in to the backend of your webshop and navigate to _Stores_ > _Configuration_ > _MultiSafepay x.x.x_ > _MultiSafepay Settings_.  
This page contains all main settings and is used for all gateways and gift cards.
{{% account_info %}}
Your Account ID is shown in the dashboard of your MultiSafepay account in the top right corner

2. Navigate to _Stores_ > _(Settings) Configuration_ > _MultiSafepay x.x.x_ > _MultiSafepay Gateways_.  
This page contains the configuration options for all payment methods supported by MultiSafepay.  
Be sure that you have the selected payment methods active in your [MultiSafepay account](https://merchant.multisafepay.com)

3. MultiSafepay Gift cards  
This page contains the configuration options for all gift cards supported by MultiSafepay.  
Gift cards need to be activated, more information can be found on our [gift card page](/payments/methods/prepaid-cards/gift-cards)

4. FastCheckout  
This page contains the FastCheckout specific settings.  
More information about the FastCheckout can be found in our [documentation of FastCheckout](https://docs.multisafepay.com/payment-methods/fastcheckout/)

### 4. Congratulations
For any questions about the plugin:

 - Email the Integration Team at <integration@multisafepay.com> 
 - Start a discussion in our [Magento Slack channel](https://magentocommeng.slack.com) _#multisafepay-payments_

### 5. Updates 
Run the following commands via the CLI:
```
composer update multisafepay/magento2msp 
php bin/magento setup:upgrade
```

Depending on your webserver/webshop configuration you also need to check:
- check the rights on files correctly. Our files can be found at vendor/multisafepay/magento2msp
- Empty static files when running in production mode
- Flush cache.
