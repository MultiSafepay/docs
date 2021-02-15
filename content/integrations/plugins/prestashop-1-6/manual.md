---
title : "MultiSafepay PrestaShop 1.6 installation & configuration manual"
weight:
meta_title: "PrestaShop 1.6 plugin manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

### Introduction

{{% introduction_plugin "PrestaShop 1.6" %}}

### 1. Requirements
- PrestaShop 1.6
- Tested on PHP 7.0

### 2. Integration
1. Unpack the contents of the .zip archive and upload the "modules" folder via SFTP to the PrestaShop root directoy, merging the two folders.

### 3. Configuration
1. Navigate to the backend of your webshop and navigate to _Modules and Services-> Payments and Gateways_

_It is essential that the MultiSafepay Core Module (MultiSafepay) is installed and configured. Reason being that all payment methods are more or less dependent on settings and/or the API key in the core module_

2. In the next screen proceed with the installation

3. Set your [API key](/faq/general/glossary/#api-key) and save the page. {{% account_info %}}


4. Click on the Payments tab and enable the payment methods you would like to offer.

_Notice: Manually generated payment links in the MultiSafepay Control will not create/update orders automatically in the backend of Prestashop_

### 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>
