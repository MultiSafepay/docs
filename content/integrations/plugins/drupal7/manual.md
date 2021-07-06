---
title : "MultiSafepay Drupal 7 installation & configuration manual"
meta_title: "Drupal 7 plugin manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

## Introduction

{{% introduction_plugin "Drupal 7" %}}

## 1. Requirements
- Drupal 7.x
- Tested on PHP 7.0

## 2. Installation
 1. Unpack the content of the .ZIP file in the root of your webshop.

## 3. Configuration
1. Login into your backend and navigate to _Site Settings_ -> _Modules_. Enable the Commerce MultiSafepay JSON module, along with the payment method modules of your choice. Then click _Save configuration_ to save the changes you have made

2. In the backend of your webshop, navigate to _Store Settings -> Advanced Store Settings -> Payment methods_.
_Enable_ first the MultiSafepay core module ("multisafepay") and then _Enable_ the modules for each payment method.
Click the button _Edit_ under _Actions_ to configure the payment method

3. When the main module is installed, two rules are created by default, but left disabled:  
  * MultiSafepay Order paid in full: Order state to processing  
This rule will set the order to processing once the order has been paid in full  

  * MultiSafepay Order Complete: Shipped at MultiSafepay  
This rule will update the transaction order status to _shipped_ at MultiSafepay, causing the invoicing process to continue for Pay After Delivery, Klarna and E-invoicing.

## 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>
