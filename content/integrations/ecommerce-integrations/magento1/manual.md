---
title : "MultiSafepay Magento 1 installation & configuration manual"
meta_title: "Magento 1 plugin manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
aliases: 
    - /plugins/magento1/manual
    - /integrations/plugins/magento1/manual
    - /integrations/magento1/manual
---

{{< alert-notice >}} Magento 1 is end-of-life. If you are still running Magento 1, action is required. MultiSafepay has partnered with Mage One to continue supporting Magento 1 in the future. Please read our [blog](https://bit.ly/2YX2LGL) for more information and the actions to take.{{< /alert-notice >}}

{{< blue-notice >}} Starting from 3.0.0 the plugin only needs your [API key](/faq/general/glossary/#api-key), Account ID, Site ID and Secure Code are not needed anymore and removed from the settings. {{< /blue-notice >}}

### Introduction

This manual helps merchants process MultiSafepay payments as quickly as possible from a Magento 1 webshop. For some steps in this manual, assistance from your technical partner may be required.

Installation of the plugin can be done in three ways:

* SFTP upload
* .ZIP file upload in Connect
* Via the MarketPlace.

In this manual we describe the SFTP upload method.

{{% introduction_plugin "Magento 1" %}}

{{< blue-notice >}}
MultiSafepay supports most functionalities of Magento. If you have any questions about the services we offer, do not hesitate to contact us at <integration@multisafepay.com>
{{< /blue-notice >}}

### 1. Requirements
- Magento Open Source 1.7 - 1.9
- Tested on PHP 7.0

### 2. Installation
 1. Unpack the content of the .ZIP file in the root of your webshop
 2. Log in to your backend and navigate to _System_ > _Configuration_ > _Cache_. Clear your invalid cache
 3. Move all files and folders from Plugin_Magento_x.x.x to the root. Contents in the folders app, lib and media should be added to the existing folders with the same name
 4. Logout from the backend of your webshop.

### 3. Configuration
1. Log in to the backend of your webshop and navigate to _System_ > _Configuration_ > _MultiSafepay x.x.x_ > _Connect Settings_.
This page contains all main settings and is used for all gateways and gift card.
Information on where to find your API key can be found on our [API key page](https://docs.multisafepay.com/tools/multisafepay-control/get-your-api-key)

2. Navigate to _System_ > _Configuration_ > _MultiSafepay x.x.x_ > _Connect MultiSafepay Gateways_.
This page contains the configuration options for all payment methods supported by MultiSafepay.  
Be sure that you have the selected payment methods active in your [MultiSafepay Control](https://merchant.multisafepay.com)

3. MultiSafepay Gift Cards  
This page contains the configuration options for all gift card supported by MultiSafepay.
gift card need to be activated, more information can be found on our [gift card page](/payment-methods/prepaid-cards/gift-cards)

4. FastCheckout  
This page contains the FastCheckout specific settings. More information about [FastCheckout](/payment-methods/fastcheckout) can be found on our official website.

### 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <magento1@multisafepay.com> or start a discussion in our [Magento Slack channel](https://magentocommeng.slack.com) _#multisafepay-payments_
