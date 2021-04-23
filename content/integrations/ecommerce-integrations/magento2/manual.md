---
title : "MultiSafepay Magento 2 installation & configuration manual"
meta_title: "Magento 2 plugin manual - MultiSafepay Docs"
layout: 'single'
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
aliases:
    - /support-tab/magento2/manual
    - /plugins/magento2/manual
    - /integrations/plugins/magento2/manual
    - /integrations/magento2/manual
---

### Introduction

We are proud to announce that we have been working on a brand new Magento 2 plugin. 
The new plugin is completely built from the ground up, leaving a lot of the older methods used in the current Magento 2 plugin behind.
It brings code improvements, unit/integration testing and it is built on top of the Magento payment provider gateway structure.

{{< alert-notice >}}
If you are on the deprecated plugin and want to upgrade, please read this [FAQ article](/integrations/ecommerce-integrations/magento2/faq/migrating-to-new-plugin/) about how you can migrate to the new plugin
{{< /alert-notice >}}

{{< alert-notice >}}
The FAQ items regarding the deprecated Magento 2 plugin have been moved to the [deprecated plugin page](/integrations/ecommerce-integrations/magento2/old) 
{{< /alert-notice >}}

{{< blue-notice >}}
We have recently added support for Magento Instant Purchase and Magento Vault.  
To learn more about these features, [read our blog](https://www.multisafepay.com/blog/magento-2-boost-conversion-through-magento-vault-instant-purchase)
{{< /blue-notice >}}

### 1. Features
Some of the new features include:

* Improved Magento backend configuration
* Improved translations
* Improved error handling and event & error logs
* Support information available in the Magento backend
* Clear explanation of each payment method with links to docs
* Modular setup, providing more flexibility during the installation process
* For some payment methods the hosted payment page is now skipped, resulting in a higher conversion rate
* As of version 2.4.0, we also support [Magento Vault](https://devdocs.magento.com/guides/v2.4/payments-integrations/vault/vault-intro.html) and [Instant Purchase](https://docs.magento.com/user-guide/sales/checkout-instant-purchase.html).  
  These features are based on MultiSafepay recurring payments. Please look at our docs page about [Recurring payments](/tools/recurring-payments/) for more information about this subject.
* PWA (GraphQL) endpoints


Some features are not available anymore, because they are not supported anymore or have been replaced:

* Tokenization (Replaced by Magento Vault and Instant Purchase)
* FastCheckout (Not supported anymore)
* PWA (REST) endpoints (Replaced by GraphQL endpoints)

{{< blue-notice >}}
MultiSafepay supports most functionalities of Magento. If you have any questions about the services we offer, do not hesitate to contact us at <integration@multisafepay.com>
{{< /blue-notice >}}

### 2. Requirements
- To use the plugin you need a MultiSafepay account. You can create a test account on https://testmerchant.multisafepay.com/signup
- Magento Open Source version 2.2.x & 2.3.x & 2.4.x or Magento Commerce version 2.3.x & 2.4.x (For GraphQL only Magento Open Source versions 2.4.x are supported)
- PHP 7.1+

### 3. Modules
The new MultiSafepay Magento 2 plugin consists of several Magento modules:

* [multisafepay-magento2-core](https://github.com/MultiSafepay/magento2-core) (Provides core functionalities)
* [multisafepay-magento2-frontend](https://github.com/MultiSafepay/magento2-frontend) (Enables use of the payment gateways in the Magento checkout)
* [multisafepay-magento2-adminhtml](https://github.com/MultiSafepay/magento2-adminhtml) (Makes it possible to enable/disable payment gateways and change the settings in the Magento backend)
* [multisafepay-magento2-msi](https://github.com/MultiSafepay/magento2-msi) (Handles stock when MSI is enabled)
* [multisafepay-magento2-catalog-inventory](https://github.com/MultiSafepay/magento2-catalog-inventory) (Handles stock when MSI is disabled)
* [multisafepay-magento2](https://github.com/MultiSafepay/magento2) (Meta package which installs all the above)

For GraphQL support there is a separate module:

* [multisafepay-magento2-graphql](https://github.com/MultiSafepay/magento2-graphql) (Extends and adds GraphQL queries and mutations)

### 4. Installation
For merchants, we recommend installing the meta-package via composer:

``` 
composer require multisafepay/magento2
php bin/magento setup:upgrade
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy
```

This will automatically install all the modules that are necessary to get started.

After installing, the following command can be used in the Magento 2 root directory to enable all the modules:
```
./bin/magento module:enable `./bin/magento module:status | grep MultiSafepay_`
```

#### 4.1 Stock handling

If you have disabled MSI inside Magento 2, then you can use the following command to disable the MultiSafepay MSI module:
```
php bin/magento module:disable MultiSafepay_ConnectMSI
```

If you have a Magento 2 installation with MSI enabled, you can use the following command to disable the MultiSafepay CatalogInventory module instead:
```
php bin/magento module:disable MultiSafepay_ConnectCatalogInventory
```

#### 4.2 Module dependencies
The meta-package has a dependency on MSI, which means that the MSI modules should be available (but not necessarily enabled) in your store. However, if you have removed it with, for example, a composer-replace trick like [yireo/magento2-replace-inventory](https://github.com/yireo/magento2-replace-inventory), you will not be able to install the meta-package. In this case it is still possible to integrate with MultiSafepay. You can then install the magento2-frontend module and the magento2-catalog-inventory module, instead of the meta-package.

The magento2-frontend module has a dependency on the magento2-core and magento2-adminhtml module, so they all will be installed. And then you need to have a module which handles the stock in some specific cases. Since MSI is not available, you can install the magento2-catalog-inventory module instead.

The installation process is the same for the Magento Commerce version.

### 5. Configuration
1. Log in to the backend of your webshop and navigate to _Stores_ > _Configuration_ > _MultiSafepay_ > _General Information_.  
This page contains all main support information and it is advised to read this.

2. Navigate to _Stores_ > _Configuration_ > _MultiSafepay_ > _General Settings_.   
This page contains all main settings and is used for all gateways and gift cards.
Information on where to find your Account ID, Site ID, Site code or [API key](/faq/general/glossary/#api-key) can be found on our [API key page](/tools/multisafepay-control/get-your-api-key).
Your Account ID is shown in the dashboard of your MultiSafepay Control in the top right corner.

2. Navigate to _Stores_ > _Configuration_ > _MultiSafepay_ > _Payment Methods_.   
This page contains the configuration options for all payment methods supported by MultiSafepay.  
Be sure that you have the selected payment methods active in your [MultiSafepay Control](https://merchant.multisafepay.com)

3. Navigate to _Stores_ > _Configuration_ > _MultiSafepay_ > _Gift Cards_.  
This page contains the configuration options for all gift cards supported by MultiSafepay.  
Gift cards need to be activated, more information can be found on our [gift card page](/payment-methods/prepaid-cards/gift-cards)

### 6. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com> or start a discussion in our [Magento Slack channel](https://magentocommeng.slack.com) _#multisafepay-payments_

### 7. Updates 
Run the following commands via the CLI:
```
composer update multisafepay/magento2 --with-dependencies
php bin/magento setup:upgrade
php bin/magento setup:di:compile
```

Depending on your webserver/webshop configuration, you also need to check:
- check the 'rights' on files correctly. Our files can be found at vendor/multisafepay
- Empty static files when running in production mode
- Flush cache.
