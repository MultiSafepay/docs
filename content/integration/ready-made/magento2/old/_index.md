---
title : "MultiSafepay Magento 2 (Deprecated)"
github_url : "https://github.com/MultiSafepay/Magento2Msp"
description : "This manual is for the deprecated Magento 2 plugin."
meta_title: "Magento 2 plugin manual V1 - MultiSafepay Docs"
changelog: https://github.com/MultiSafepay/Magento2Msp/blob/master/CHANGELOG.md
layout: 'single'
faq: '.'
noindex: 'true'
---

{{< alert-notice >}} **Alert!** This plugin is end-of-life and we are phasing out support. Migrate to the [new plugin](/payments/integrations/ecommerce-platforms/magento2/) as soon as possible. {{< /alert-notice >}}

You can install the plugin via:

+ SFTP
+ Composer
+ Magento Marketplace

This manual is for installation via Composer.

{{% introduction_plugin "Magento 2" %}}

### Requirements
- Magento Open Source version 2.2.x & 2.3.x & 2.4.x 
- PHP 7.0 and higher
- Tested with PHP 7.0 (Magento 2.3.x adds support for 7.2)

_*If you are using [Magento Commerce](https://business.adobe.com/products/magento/magento-commerce.html), contact us at <integration@multisafepay.com>_

## Installation
Run the following commands via the CLI:

```
composer require multisafepay/magento2msp
php bin/magento setup:upgrade
php bin/magento setup:static-content:deploy
```

After running these commands, the latest stable release is downloaded and installed in your Magento 2 webshop.

Depending on your webserver/webshop configuration, you may also need to:

- Set the rights on files correctly. Our files can be found at vendor/multisafepay/magento2msp.
- Empty static files when running in production mode.
- Flush your cache.

## Configuration
1. Sign in to your [backend](/glossaries/multisafepay-glossary/#backend). 
2. Go to **Stores** > **Configuration** > **MultiSafepay x.x.x** > **MultiSafepay settings**.  

This page contains all main settings and is used for all gateways and gift cards.
{{% account_info %}}
Your account ID appears in the top-right corner of your MultiSafepay dashboard. 

3. Go to **Stores** > **(Settings) Configuration** > **MultiSafepay x.x.x** > **MultiSafepay gateways**.  

This page contains the configuration options for all payment methods supported by MultiSafepay.  
Make sure the selected payment methods are actived for your [MultiSafepay account](https://merchant.multisafepay.com).

4. MultiSafepay gift cards  
This page contains the configuration options for all gift cards supported by MultiSafepay.  
For how to activate gift cards, see [Gift cards](/payment-methods/gift-cards).

For support:

 - Email the Integration Team at <integration@multisafepay.com> 
 - Start a discussion in our [Magento Slack channel](https://magentocommeng.slack.com) _#multisafepay-payments_

## Updates 
Run the following commands via the CLI:
```
composer update multisafepay/magento2msp 
php bin/magento setup:upgrade
```

Depending on your webserver/webshop configuration, you may also need to:

- Set the rights on files correctly. Our files can be found at vendor/multisafepay/magento2msp.
- Empty static files when running in production mode.
- Flush your cache.
