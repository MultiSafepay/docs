---
title : "MultiSafepay Magento 1 installation & configuration manual"
meta_title: "Magento 1 plugin manual - MultiSafepay Documentation Center"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

{{< alert-notice >}} Magento 1 has reached End-of-life. If you are still running Magento 1, action is required. Read more in our article [_Magento 1 - thGe final weeks_](https://bit.ly/2YX2LGL){{< /alert-notice >}}


### Introduction

This manual helps merchants process MultiSafepay payments as quickly as possible from a Magento 1 webshop. For some steps in this manual, assistance from your technical partner may be required.

Installation of the plugin can be done in three ways:

* SFTP upload
* .ZIP file upload in Connect
* Via the MarketPlace.

In this manual we describe the SFTP upload method.

{{% introduction_plugin "Magento 1" %}}


### 1. Requirements
- Magento Open Source 1.7 - 1.9
- Tested on PHP 7.0

### 2. Installation
 1. Unpack the content of the .ZIP file in the root of your webshop
 2. Login in your backend and navigate to _System_ -> _Configuration_ -> _Cache_. Clear your invalid cache
 3. Logout from the backend of your webshop.

### 3. Configuration
1. Login into the backend of your webshop and navigate to _System_ -> _Configuration_ -> _MultiSafepay x.x.x_ -> _Connect Settings_.
This page contains all main settings and is used for all gateways and gift card.
{{% account_info %}}
Your Account ID is shown in the dashboard of your MultiSafepay Control in the top right corner.

2. Navigate to _System_ -> _Configuration_ -> _MultiSafepay x.x.x_ -> _Connect MultiSafepay Gateways_.
This page contains the configuration options for all payment methods supported by MultiSafepay.  
Be sure that you have the selected payment methods active in your [MultiSafepay Control](https://merchant.multisafepay.com)

3. MultiSafepay Gift Cards  
This page contains the configuration options for all gift card supported by MultiSafepay.
gift card need to be activated, more information can be found on our [gift card page](/payment-methods/prepaid-cards/gift-cards/)

4. Fastcheckout  
This page contains the Fastcheckout specific settings. More information about [Fastcheckout](https://www.multisafepay.com/fastcheckout-payments) can be found on our official website.

### 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <magento1@multisafepay.com> or start a discussion in our [Magento Slack channel](https://magentocommeng.slack.com) _#multisafepay-payments_
