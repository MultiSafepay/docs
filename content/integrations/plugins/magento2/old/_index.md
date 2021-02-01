---
title : "MultiSafepay Magento 2 (Deprecated)"
github_url : "https://github.com/MultiSafepay/Magento2Msp"
download_url: "https://github.com/MultiSafepay/Magento2Msp/releases/download/1.14.1/Plugin_Magento2_1.14.1.zip"
description : "This is the manual for the old Magento 2 plugin which has become deprecated. It can still be used, but please be aware that this plugin won't be receiving any more significant updates in the future."
meta_title: "Magento 2 plugin manual V1 - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
changelog: https://github.com/MultiSafepay/Magento2Msp/blob/master/CHANGELOG.md
layout: 'single'
faq: '.'
---

### Introduction

The installation can be carried out in three ways:

+ SFTP
+ Composer
+ Magento Marketplace.

In this manual we describe the installation via Composer.

{{% introduction_plugin "Magento 2" %}}

### 1. Requirements
- Magento Open Source version 2.2.x & 2.3.x & 2.4.x _(Open Source version supported)_*
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
1. Login on the backend of your webshop and navigate to _Stores_ -> _Configuration_ -> _MultiSafepay x.x.x_ -> _MultiSafepay Settings_.  
This page contains all main settings and is used for all gateways and gift cards.
{{% account_info %}}
Your Account ID is shown in the dashboard of your MultiSafepay Control in the top right corner

2. Navigate to _Stores_ -> _(Settings) Configuration_ -> _MultiSafepay x.x.x_-> _MultiSafepay Gateways_.  
This page contains the configuration options for all payment methods supported by MultiSafepay.  
Be sure that you have the selected payment methods active in your [MultiSafepay Control](https://merchant.multisafepay.com)

3. MultiSafepay Gift cards  
This page contains the configuration options for all gift cards supported by MultiSafepay.  
Gift cards need to be activated, more information can be found on our [gift card page](/payment-methods/prepaid-cards/gift-cards)

4. Fastcheckout  
This page contains the Fastcheckout specific settings.  
More information about the Fastcheckout can be found on https://www.multisafepay.com/fastcheckout-payments

### 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com> or start a discussion in our [Magento Slack channel](https://magentocommeng.slack.com) _#multisafepay-payments_

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
