---
title : "MultiSafepay Magento 1 installation & configuration manual"
meta_title: "Magento 1 plugin manual - MultiSafepay Documentation Center"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

### Introduction

This manual helps merchants process MultiSafepay payments as quickly as possible from a Magento 1 webshop. For some steps in this manual, assistance from your technical partner may be required.

Installation of the plugin can be done in three ways:

- .ZIP file upload in Connect
- Via the MarketPlace.

In this manual we describe the SFTP upload method.
We recommend that you install the plugin first on a test environment, and make sure you have made a backup. Be sure Magento Compiler is disabled.

{{% contact_details %}}

### 1. Requirements
- Magento Open Source 1.7 - 1.9
- Tested on PHP 7.0

### 2. Installation
 - Unpack the content of the .ZIP file in the root of your webshop
 - Login in your backend and navigate to _System->Configuration->Cache_. Clear your invalid cache.

### 3. Configuration
- Login on the backend of your webshop and navigate to _System->Configuration->MultiSafepay x.x.x->Connect Settings_.
This page contains all main settings and is used for all gateways and gift card.
{{% account_info %}}
Your Merchant ID is shown in the dashboard of your MultiSafepay Control in the top right corner

- Navigate to _System->Configuration->MultiSafepay x.x.x->Connect MultiSafepay Gateways_.
This page contains the configuration options for all payment methods supported by MultiSafepay.  
Be sure that you have the selected payment methods active in your [MultiSafepay Control](https://merchant.multisafepay.com)

- MultiSafepay Gift Cards  
This page contains the configuration options for all gift card supported by MultiSafepay.
gift card need to be activated, more information can be found on our [gift card page](/payment-methods/giftcards/)

- Fastcheckout  
This page contains the Fastcheckout specific settings. More information about Fastcheckout can be found on https://www.multisafepay.com/fastcheckout-payments.

### 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>
