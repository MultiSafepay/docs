---
title : "MultiSafepay Shopware 6 installation & configuration manual"
meta_title: "Shopware 6 plugin manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
aliases: [/integrations/shopware6/manual/]
---

### Introduction

{{% introduction_plugin "Shopware 6" %}}

### 1. Requirements
- Shopware 6.2.x _([Starter Edition](https://www.shopware.com/en/pricing) supported)_*
- Tested on PHP 7.2.0

_*Contact your account manager if you require support for Professional/Enterprise of Shopware 6_

### 2. Installation & Configuration
1. Navigate to our [Shopware 6 GitHub repository](https://github.com/MultiSafepay/shopware6/releases)
2. Download the latest release which can be found in the assets list and starts with Plugin_Shopware6_x.x.x.zip
3. Log in to your (Shopware 6) backend and navigate to _Settings_ and select _System_ on the left hand side
4. Select _Plugins_
5. Press on _Upload plugin_ at the top of the page and select the file you downloaded in step 2
6. When the plugin is visible, make sure the _Activated_ button is toggled
7. Press on the "..." (more) button and select _Config_
8. Select _Test_ in the drop-down menu
9. Look for the field named _API key_ and enter your [API key](/faq/general/glossary/#api-key)

Information on where to find your API key can be found on our [API key page](https://docs.multisafepay.com/tools/multisafepay-control/get-your-api-key).

The other fields can be filled accordingly to your own preferences.

#### Composer installation steps

Run the following command in the root of your Shopware root directory. Make sure the composer is installed on your hosting server.

```
composer require multisafepay/shopware6

```
#### Marketplace installation steps

Get the free MultiSafepay plugin from the [Shopware 6 marketplace](https://store.shopware.com/en/mltis59465832976f/multisafepay-online-payments-for-shopware-ideal-cards-klarna-alipay-etc..html) and connect your webshop with your Shopware account.

### 3. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>

You can also join the official [Shopware 6 Slack channel](https://join.slack.com/t/shopwarenederland/shared_invite/zt-61exftia-TFYlw5LzmIBnz7Epq07goQ) for questions as well as MultiSafepays' private [Shopware 6 Slack channel](https://shopwarenederland.slack.com/archives/G0146NKFJTT)
