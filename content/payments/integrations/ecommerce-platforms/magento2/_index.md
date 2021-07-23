---
title: "MultiSafepay plugin for Magento 2"
breadcrumb_title: "Magento 2"
github_url : "https://github.com/MultiSafepay/Magento2"
old_url : "/payments/integrations/ecommerce-platforms/magento2/old/"
changelog_url : "."
faq: "."
layout: 'single-old-button'
meta_title: "Magento 2 plugin - MultiSafepay Docs"		
meta_description: "Free plugin to integrate MultiSafepay payment solutions into your Magento 2 platform"
changelog: https://github.com/MultiSafepay/magento2/blob/master/CHANGELOG.md
weight: 01
logo: "/logo/Plugins/Magento_2.svg"
title_short: "Magento 2"
aliases: 
    - /plugins/magento2
    - /integrations/plugins/magento2
    - /integrations/magento2
    - /support-tab/magento2/manual
    - /plugins/magento2/manual
    - /integrations/plugins/magento2/manual
    - /integrations/magento2/manual
    - /integrations/ecommerce-integrations/magento2
    - /integrations/plugins/magento2/beta
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Magento 2 webshop.

{{< details title="Classic plugin" >}}
&nbsp;  

If you are using the classic Magento 2 plugin and want to upgrade, see [Migrating to the new plugin](/payments/integrations/ecommerce-platforms/magento2/faq/migrating-to-new-plugin/).

For user guidance on the classic plugin, see [MultiSafepay Magento 2 (Deprecated)](/payments/integrations/ecommerce-platforms/magento2/old).
{{< /details >}}

{{< details title="Support" >}}
&nbsp;  
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue
- [Magento Slack channel](https://magentocommeng.slack.com) #multisafepay-payments

Our plugin is supported by a certified Magento 2 Solution Specialist and receives regular updates for the latest features from Magento and MultiSafepay.

We support most Magento functionalities. For any questions, email the Integration Team at <integration@multisafepay.com>

{{< /details >}}

{{< details title="Requirements" >}}
&nbsp;  
- MultiSafepay account – See [Getting started](/getting-started/).
- Magento Open Source version 2.2.x & 2.3.x & 2.4.x **or** Adobe Commerce version 2.3.x & 2.4.x (For GraphQL, only Magento Open Source versions 2.4.x are supported)
- PHP 7.1+

{{< /details >}}

### Features
The new plugin features code improvements, and unit and integration testing. It is built on top of the Magento payment provider gateway structure. Some payment methods now skip the MultiSafepay payment page, which increases conversion.

{{< details title="View new features" >}}
Other new features include:

* Improved:
    * Magento backend configuration
    * Translations
    * Error handling
    * Event and error logs
* Support information available in the Magento backend
* Clear explanation of each payment method with links to docs
* Modular setup, providing more installation flexibility
* PWA (GraphQL) endpoints

As of version 2.4.0, we also support [Magento Vault](https://devdocs.magento.com/guides/v2.4/payments-integrations/vault/vault-intro.html) and [Instant Purchase](https://docs.magento.com/user-guide/sales/checkout-instant-purchase.html). For more information, see MultiSafepay Blog - [Magento 2: Boost conversion through Magento Vault & Instant Purchase](https://www.multisafepay.com/blog/magento-2-boost-conversion-through-magento-vault-instant-purchase). 

These features are based on MultiSafepay recurring payments. For more information, see [Recurring payments](/payments/features/recurring-payments/).

{{< /details >}}

{{< details title="View obsolete features" >}}
Features that are no longer available:

* Tokenization – replaced by Magento Vault and Instant Purchase
* FastCheckout – no longer supported
* PWA (REST) endpoints – replaced by GraphQL endpoints

{{< /details >}}

### Modules

{{< details title="View modules" >}}
The plugin consists of several Magento modules:

| Module  | Description  |
|---|---|
| [Multisafepay-magento2-core](https://github.com/MultiSafepay/magento2-core)   | Provides core functionalities  |
| [Multisafepay-magento2-frontend](https://github.com/MultiSafepay/magento2-frontend)  | Enables payment gateways in the Magento checkout  |
| [Multisafepay-magento2-adminhtml](https://github.com/MultiSafepay/magento2-adminhtml)  | Enables/disables payment gateways, and changes settings in the Magento backend  |
| [Multisafepay-magento2-msi](https://github.com/MultiSafepay/magento2-msi)  | Handles stock when MSI is enabled  |
| [Multisafepay-magento2-catalog-inventory](https://github.com/MultiSafepay/magento2-catalog-inventory)  | Handles stock when MSI is disabled  |
| [Multisafepay-magento2](https://github.com/MultiSafepay/magento2)  | Meta package that installs all the above  |
| [Multisafepay-magento2-graphql](https://github.com/MultiSafepay/magento2-graphql)| For GraphQL support, extends and adds GraphQL queries and mutations |

{{< /details >}}

{{< details title="View module dependencies" >}}

The meta-package has a dependency on MSI. This means the MSI modules must be available (but not necessarily enabled) in your store. 

If you have removed MSI (e.g. with a composer-replace trick like [yireo/magento2-replace-inventory](https://github.com/yireo/magento2-replace-inventory)), you can't install the meta-package. To integrate with MultiSafepay, instead of installing the meta-package, install the magento2-frontend module and the magento2-catalog-inventory module.

The magento2-frontend module has a dependency on the magento2-core and magento2-adminhtml modules, so they are all installed together. In some cases, you also then need a stock-handling module. Since MSI is not available, you can install the magento2-catalog-inventory module instead.

The installation process is the same for the Adobe Commerce version.

{{< /details >}}

## Installation

**Note:** First make sure you have [uninstalled the deprecated plugin](/payments/integrations/ecommerce-platforms/magento2/faq/deleting-deprecated-plugin/).

**1.** We recommend installing the meta-package using Composer:

``` 
composer require multisafepay/magento2
php bin/magento setup:upgrade
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy
```

**2.** To enable all the modules, use the following command in the Magento 2 root directory:
```
./bin/magento module:enable `./bin/magento module:status | grep MultiSafepay_`
```

### Stock handling

If you have disabled MSI in Magento 2, to disable the MultiSafepay MSI module, use the following command:
```
php bin/magento module:disable MultiSafepay_ConnectMSI
```
If you have enabled MSI in Magento 2, to disable the MultiSafepay CatalogInventory module, use the following command:
```
php bin/magento module:disable MultiSafepay_ConnectCatalogInventory
```

## Configuration
Sign in to your Magento 2 backend, and go to **Stores** > **Configuration** > **MultiSafepay**. This section contains the following pages:

- **General information:** Contains all the main support information. We recommend reading this first.
- **General settings:** Contains all main settings.  
  - Here you can configure all gateways and gift cards.  
  - For finding your account ID, site ID, site secure code, or [API key](/faq/general/multisafepay-glossary/#api-key), see [Get your API key](/tools/multisafepay-control/get-your-api-key).   
  - Your account ID appears in the top-right corner of your MultiSafepay account.
- **Payment methods:** Contains the configuration options for all MultiSafepay payment methods.  
    - Make sure you have activated your selected payment methods in your [MultiSafepay account](https://merchant.multisafepay.com).
- **Gift cards:** Contains the configuration options for all gift cards supported by MultiSafepay.  
    - Make sure you have activated your selected gift cards in your [MultiSafepay account](https://merchant.multisafepay.com).  
    - For more information, see [Gift cards](/payments/methods/prepaid-cards/gift-cards).
  
