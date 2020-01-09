---
title : "MultiSafepay Magento 2 installation & configuration manual"
meta_title: "Magento 2 plugin manual - MultiSafepay Documentation Center"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

### Introduction

This manual helps merchants to process MultiSafepay payments as quickly as possible from a Magento 2 webshop. For some steps in this manual, assistance from your technical partner may be required.

The installation can be carried out in three ways:

+ SFTP
+ Composer
+ Magento Marketplace.

In this manual we describe the installation via Composer.
We recommend that you install the plugin first on a test environment, and make sure you have made a backup.

### 1. Requirements
- Magento Open Source version 2.1.x, 2.2.x & 2.3.x
- PHP 7.0 and higher
- Tested on PHP 7.0 (Magento 2.3.x on 7.2)

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

2. Navigate to _Stores_ -> _Configuration_ -> _MultiSafepay x.x.x_-> _MultiSafepay Gateways_.  
This page contains the configuration options for all payment methods supported by MultiSafepay.  
Be sure that you have the selected payment methods active in your [MultiSafepay Control](https://merchant.multisafepay.com)

3. MultiSafepay Giftcards  
This page contains the configuration options for all gift cards supported by MultiSafepay.  
Giftcards need to be activated, more information can be found on our [gift card page](/payment-methods/giftcards/)

4. Fastcheckout  
This page contains the Fastcheckout specific settings.  
More information about the Fastcheckout can be found on https://www.multisafepay.com/fastcheckout-payments.

### 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>
