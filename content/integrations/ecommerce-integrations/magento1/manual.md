---
title : "MultiSafepay Magento 1 installation & configuration manual"
meta_title: "Magento 1 plugin manual - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases: 
    - /plugins/magento1/manual
    - /integrations/plugins/magento1/manual
    - /integrations/magento1/manual
---

{{< alert-notice >}} Magento 1 is end-of-life. If you are still running Magento 1, action is required. MultiSafepay has partnered with Mage One to continue supporting Magento 1. For more information and instructions, see the [MultiSafepay blog](https://bit.ly/2YX2LGL).{{< /alert-notice >}}

This technical manual is for installing and configuring the MultiSafepay plugin for Magento 1.

We recommend first installing the plugin in a test environment following the recommended Shopware 6 installation procedure. Make sure you have made a backup.

MultiSafepay supports most Magento functionalities. For any questions, email the Integration Team at <integration@multisafepay.com>

You can install the plugin via:

* SFTP upload
* .ZIP file upload in Connect
* MarketPlace

This manual is for SFTP upload.

### Technical support
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

### Requirements
- MultiSafepay account – See [Getting started](/getting-started/).
- Magento Open Source 1.7 - 1.9
- Tested on PHP 7.0

### Installation
 1. Unpack the content of the .ZIP file in the root of your webshop.
 2. Sign in to your Magento 1 backend.
 3. Go to **System** > **Configuration** > **Cache**. 
 4. Clear your invalid cache.
 5. Move all files and folders from Plugin_Magento_x.x.x to the root. Add the content of the app, lib, and media folders to the existing folders with the same name.
 6. Log out from the backend of your webshop.

### Configuration
1. Sign in to the backend of your Magento 1 webshop.
2. Go to **System** > **Configuration** > **MultiSafepay x.x.x** > **Connect settings**.  
    This page contains all main settings and is used for all gateways and gift cards.  
    To find your API key, see [API key](https://docs.multisafepay.com/tools/multisafepay-control/get-your-api-key).  
    From version 3.0.0, the plugin only needs your API key. Your account ID, site ID, and site secure code are not needed and have been removed from the settings.

3. Go to **System** > **Configuration** > **MultiSafepay x.x.x** > **Connect MultiSafepay gateways**.  
    This page contains the configuration options for all MultiSafepay payment methods.    
    Make sure your selected payment methods are actived in your [MultiSafepay account](https://merchant.multisafepay.com).

4. To configure MultiSafepay gift cards, go to the **MultiSafepay Gift Cards** page.  
    Make sure gift cards are activated in your MultiSafepay account. For more information, see [Gift cards](/payment-methods/prepaid-cards/gift-cards).

5. To configure FastCheckout settings, go to the **FastCheckout** page.    
    For more information, see [FastCheckout](/payment-methods/fastcheckout).

For any questions about the plugin:

- Email the Integration Team at <magento1@multisafepay.com> 
- Start a discussion in our [Magento Slack channel](https://magentocommeng.slack.com) _#multisafepay-payments_
