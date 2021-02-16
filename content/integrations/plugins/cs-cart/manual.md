---
title : "MultiSafepay CS-Cart installation & configuration manual"
meta_title: "CS-Cart plugin manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

### Introduction

{{% introduction_plugin "CS-Cart" %}}

### 1. Requirements
- CS-Cart 4.x
- Tested on PHP 7.0

### 2. Installation
 1. Unpack the content of the .ZIP file in the root of your webshop
 2. Go to yourdomain.com/msp_installer.php. This will trigger the installation
 3. Delete the msp_installer.php file
 4. Enter your notification URL in your [MultiSafepay Control](https://merchant.multisafepay.com)<br> 
 More information can be found on [our Notification URL page](/tools/multisafepay-control/set-your-notification-url)

### 3. Configuration
1. Login into your backend and navigate to _Adminination_ → _Payment Method_
2. Then click on the _+_ symbol to add a payment method
3. In the next screen you enter a name that will be shown during checkout. In the _Processing unit_ field, you specify the desired payment method. The other fields can be filled according to your own wishes. Click on _Create_
4.  Then click on the _Configure_ tab
5. Enter your Account ID, Site ID & Site Code. {{% account_info %}}
Your Account ID is shown in the dashboard of your MultiSafepay Control in the top right corner

Note:
There are also a number of extra options such as _IP-Validation_ and _debugmode_. These serve especially for developers and can remain unchanged.

### 4. Congratulations
You have installed and configured the plugin successfully. If you have any questions regarding the plugin, feel free to contact our Integration Team at <integration@multisafepay.com>
