---
title : "MultiSafepay WooCommerce installation & configuration manual"
meta_title: "WooCommerce plugin manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
aliases: [/integrations/woocommerce/manual/]
---

### Introduction

{{% introduction_plugin "WooCommerce" %}}

### 1. Requirements
- Wordpress 5.0
- PHP 7.2

### 2. Installation
There are two ways in which the plugin for WooCommerce can be downloaded. If your working on a new webshop and would like to retrieve our plugins, you can find them at the [Wordpress plugin page](https://wordpress.org/plugins/multisafepay)

If you already have a webshop with our plugin, please turn on the automatic check for module updates. Go to _Administration_ → _Preferences_ → _General_ → _Automatic check for module updates_. By doing this, the system will give you a suggestion to upgrade.

You can also download the plugin directly on this page:

1. Download the plugin by clicking the Download button in this [page](/integrations/plugins/woocommerce)
2. Navigate to the backend of your webshop and go to _Plugins_ -> _Add New_. Click on _Browse file_
3. Upload the Plugin_WooCommerce_x.x.x.zip file.

### 3. Configuration
1. Login in your WooCommerce Admin and navigate to _WooCommerce_ -> _MultiSafepay Settings_
2. Navigate to _Account_ tab, set the API key. Information about the API key can be found on our [API key page](/tools/multisafepay-control/get-your-api-key)
3. Navigate to _Order Status_ tab and confirm the match between WooCommerce order statuses and MultiSafepay order statuses clicking on "Save Changes" button.
4. Navigate to _Options_ tab and confirm the settings clicking on "Save Changes" button.
5. Navigate to _WooCommerce_ -> _Settings_ -> _Payments_. Enable the payment methods you would like to offer, check and confirm the settings for those been enable.

### 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>
