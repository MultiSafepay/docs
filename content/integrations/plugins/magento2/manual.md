---
title : "MultiSafepay Magento 2 installation & configuration manual"
meta_title: "Magento 2 plugin manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
aliases:
    - /support-tab/magento2/manual
---

### Introduction
We are proud to announce that we have been working on a brand new Magento 2 plugin. 
The new plugin is completely built from the ground up, leaving a lot of the older methods used in the current Magento 2 plugin behind.
It brings code improvements, unit/integration testing and it is built on top of the Magento payment provider gateway structure.

**Please uninstall the old plugin first, before installing the new one.**

{{< alert-notice >}}
The FAQ items regarding the old Magento 2 plugin have been moved to the [old plugin page](https://docs.multisafepay.com/integrations/plugins/magento2/old) 
{{< /alert-notice >}}

### 1. Features
There are a lot of new features, but there are also some features that are not available as of yet.
The following features are not available in the new Magento 2 plugin:

* Tokenization
* Fastcheckout
* PWA (REST) endpoints

Some of the new features include:

* Improved Magento backend configuration with less bugs
* Improved translations
* Improved error handling and event & error logs
* Support information available in the Magento backend
* Clear explanation of each payment method with links to docs
* Modular setup, providing more flexibility during the installation process
* For some payment methods the hosted payment page is now skipped, resulting in a higher conversion rate

### 2. Requirements
- To use the plugin you need a MultiSafepay account. You can create a test account on https://testmerchant.multisafepay.com/signup
- Magento Open Source version 2.2.x & 2.3.x & 2.4.x
- PHP 7.1+

_* If you are using [Magento Commerce](https://magento.com/products/magento-commerce), contact us at <integration@multisafepay.com>_

### 3. Modules
The new MultiSafepay Magento 2 plugin consists of several Magento modules:

* [multisafepay-magento2-core](https://github.com/MultiSafepay/magento2-core) (Provides core functionalities)
* [multisafepay-magento2-frontend](https://github.com/MultiSafepay/magento2-frontend) (Enables use of the payment gateways in the Magento checkout)
* [multisafepay-magento2-adminhtml](https://github.com/MultiSafepay/magento2-adminhtml) (Makes it possible to enable/disable payment gateways and change the settings in the Magento backend)
* [multisafepay-magento2-msi](https://github.com/MultiSafepay/magento2-msi) (Handles stock when MSI is enabled)
* [multisafepay-magento2-catalog-inventory](https://github.com/MultiSafepay/magento2-catalog-inventory) (Handles stock when MSI is disabled)
* [multisafepay-magento2](https://github.com/MultiSafepay/magento2) (Meta package which installs all the above)

### 4. Installation
For merchants, we recommend installing the meta-package via composer:

```shell
composer require multisafepay/magento2
php bin/magento setup:upgrade
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy
```

This will automatically install all the modules that are necessary to get started.

After installing, the following command can be used in the Magento 2 root directory to enable all the modules:
```shell
./bin/magento module:enable `./bin/magento module:status | grep MultiSafepay_`
```

#### 4.1 Stock handling

If you have disabled MSI inside Magento 2, then you can use the following command to disable the MultiSafepay MSI module:
```shell
php bin/magento module:disable MultiSafepay_ConnectMSI
```

If you have a Magento 2 installation with MSI enabled, you can use the following command to disable the MultiSafepay CatalogInventory module instead:
```shell
php bin/magento module:disable MultiSafepay_ConnectCatalogInventory
```

### 5. Configuration
1. Login on the backend of your webshop and navigate to _Stores_ → _Configuration_ → _Payment Methods_ → _MultiSafepay_ → _General Information_.  
This page contains all main support information and it is advised to read this.

2. Navigate to _Stores_ → _Configuration_ → _Payment Methods_ → _MultiSafepay_ → _General Settings_.   
This page contains all main settings and is used for all gateways and gift cards.
Information on where to find your Account ID, Site ID, Site code or API key can be found on our [API key page](/tools/multisafepay-control/get-your-api-key).
Your Account ID is shown in the dashboard of your MultiSafepay Control in the top right corner.

2. Navigate to _Stores_ → _Configuration_ → _Payment Methods_ → _MultiSafepay_ → _Payment Methods_.   
This page contains the configuration options for all payment methods supported by MultiSafepay.  
Be sure that you have the selected payment methods active in your [MultiSafepay Control](https://merchant.multisafepay.com)

3. Navigate to _Stores_ → _Configuration_ → _Payment Methods_ → _MultiSafepay_ → _Gift Cards_.  
This page contains the configuration options for all gift cards supported by MultiSafepay.  
Gift cards need to be activated, more information can be found on our [gift card page](/payment-methods/prepaid-cards/gift-cards)

### 6. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com> or start a discussion in our [Magento Slack channel](https://magentocommeng.slack.com) _#multisafepay-payments_

### 7. Updates 
Run the following commands via the CLI:
```shell
composer update multisafepay/magento2 --with-dependencies
php bin/magento setup:upgrade
php bin/magento setup:di:compile
```

Depending on your webserver/webshop configuration, you also need to check:
- check the 'rights' on files correctly. Our files can be found at vendor/multisafepay
- Empty static files when running in production mode
- Flush cache.
