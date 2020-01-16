---
title : "MultiSafepay Magento 1 installation & configuration manual"
meta_title: "Magento 1 plugin manual - MultiSafepay Documentation Center"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

### Introduction

This manual helps merchants process MultiSafepay payments as quickly as possible from a Magento 1 webshop. For some steps in this manual, assistance from your technical partner may be required.

Installation of the plugin can be done in three ways:

1. SFTP upload
2. .ZIP file upload in Connect
3. Via the MarketPlace.

In this manual we describe the SFTP upload method.
We recommend that you install the plugin first on a test environment, and make sure you have made a backup. Be sure Magento Compiler is disabled.


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
This page contains the Fastcheckout specific settings. More information about Fastcheckout can be found on the [dedicated page](https://www.multisafepay.com/fastcheckout-payments).

### 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>
