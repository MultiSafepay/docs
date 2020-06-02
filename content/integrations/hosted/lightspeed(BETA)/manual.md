---
title : "MultiSafepay Lightspeed installation & configuration manual"
meta_title: "Lightspeed plugin manual - MultiSafepay Documentation Center"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

## Introduction

{{% introduction_hosted "LightSpeed 2" %}}

### 1. Installation 
Follow the following instructions to install the MultiSafepay Lightspeed app:

1. Login into your backend.
2. Navigate to Apps
3. Search for the MultiSafepay Payments app.
4. Click on "Install App" in the top right connor, you will be redirected to a login page.
5. Login using your lightspeed credentials
6. Goto next, approve the our required permission.
7. After approving the installation you will be redirected to <https://lightspeed.multisafepay.com/install> 
8. Fill in you MultiSafepay API key and the related environment and click the "Register and continue button"

__Congratulations__

You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>

### 2. Configuration
After installing the MultiSafepay Payments application you can acces the settings page. You will be redirected to this page automaticly after the installation or you can go there by the "Goto App" button on the in your lightspeed backend.

#### 2.1 Ordering payment methods
The section "Payment methods ordering" on the settings page allows you to change the order payment methods are shown on the checkout. The order can be changed by dragging and dropping the list items. Don't forget to save the settings after making a change!

If you want a different payment methods ordering for different languages you can do so aswell. In the dropdown menu under the "Payment methods ordering" header you can select a country and make change on a per language basis. 
"Default" is used if no specific ruleset for a country is found.

#### 2.2 Minimal order amount per payment method
You can change the minimal amount an order has to be before a payment method show up. To do so you have to open the payment method in the "Payment methods ordering" list. Enter a amount in EUR cents.

For example iDEAL with a minimal value of 1500 means iDEAL won't show up in the checkout unless the total order amount equals 15.00 EUR or more.

If you want a different minimal order amounts for different languages you can do so aswell. In the dropdown menu under the "Payment methods ordering" header you can select a country and make change on a per language basis. 
"Default" is used if no specific ruleset for a language is found.

#### 2.2 Maximum order amount per payment method
You can change the maximum amount an order has to be before a payment method show up. To do so you have to open the payment method in the "Payment methods ordering" list. Enter a amount in EUR cents into the maximum field. If you dont wan't a maximum amount enter "-1".

For example iDEAL with a maximum value of 1500 means iDEAL won't show up in the checkout unless the total order amount is less then 15.00 EUR.

If you want a different maximum order amounts for different languages you can do so aswell. In the dropdown menu under the "Payment methods ordering" header you can select a country and make change on a per language basis. 
"Default" is used if no specific ruleset for a language is found.

#### 2.3 Changing the API keys or environment
On the settings page goto "Environment & API key" and click on the link. You will be redirected to another page.
On this page you can update the API key or environment

#### 2.4 Disabling payment methods
If you don't want certain payment methods to show up at all, you can disable them in payment methods ordering list. Disabled payment methods will showup in th payment methods ordering list with a striketrough.

If you want a different payment methods disabled for different languages you can do so aswell. In the dropdown menu under the "Payment methods ordering" header you can select a country and make change on a per language basis. 
"Default" is used if no specific ruleset for a language is found.

Are you missing any payment methods? Make sure the payment methods are enabled first in [Merchant control](https://docs.multisafepay.com/tools/multisafepay-control/). Then goto the settings page of our lightspeed app and enable the payment method again. By default newly activated payment methods in Merchant Control are disabled in the lightspeed MultiSafepay Payments settings,

#### 2.5 Inline buy button
If you want to put an extra buy button near the selected payment method you can do so by putting this option on inline.

#### 2.6 Inline newsletter button
If you want to put an newsletter checkmark near the selected payment method you can do so by putting this option on inline.

Requires inline buy button set to inline.