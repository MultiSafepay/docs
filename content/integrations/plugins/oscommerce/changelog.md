---
title : "Release Notes OsCommerce plugin"
meta_title: "OsCommerce plugin changelog - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

## 3.0.0
Release date: May 9th, 2017
### Changes
+ This plugin now uses the JSON API, rather than the XML API.
+ Added all available payment methods as separate gateways
+ Added all available gift card methods

***

## 2.0.3
Release date: Oct 12, 2016
### Improvements
+ Added Klarna as a payment method.

### Changes
+ Changed MisterCash to Bancontact and replaced the payment method logo.

***

## 2.0.2
Release date: Jun 18, 2015
### Improvements
+ Add check for completed transactions so that the confirmation is only sent once for paid transactions
+ Added iDEAL selection to the payment selection page instead before the order confirmation
+ Added javascript that will auto select iDEAL as payment method when an issuer is selected

### Fixes
+ On extra offline action the status of the order was reset to initialized. This has now been solved
+ Zone restriction is now working correct again
+ Added extra check for Fee tax. This solves 1027 errors and invalid tax rate for shipping

***

## 2.0.1
Release date: Mar 28, 2014
### Improvements
+ Now compatible with OsCommerce 2.2
+ Added NL images
+ Added order total language files, untranslated
+ Added Multi-Currency support
+ Added OSC input validation
+ Added American Express Support to the OsCommerce plugin
+ Added SOFORT Banking support

### Changes
+ Changed language files. Added option to show only the gateway title, and no images. On request
+ Changed default order status to selected initial status
+ Updated curl combined files
+ Updated Pay After Delivery default order status to the init status
+ Disabled updating customer info as this is saved before the transaction

### Fixes
+ Fixed bug with weight-based shipping
+ Fixed amount bug
+ Fixed bug that caused a Pay After Delivery order not to show before a finished transaction
+ Fixed bug for cancel URL, use hardcoded method like nurl script
+ Fixed bug with single quotes
