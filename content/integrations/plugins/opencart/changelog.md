---
title : "Release Notes OpenCart plugin"
meta_title: "OpenCart plugin changelog - MultiSafepay Documentation Center"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

## 2.3.0
Release date: April 2nd, 2020

### Added
+ PLGOPNS-178: Add Apple Pay

### Fixed
+ PLGOPNS-170: Fix payment methods not visible in backend order

***

## 2.2.1
Release date: March 27th, 2019
### Added
+ PLGOPNS-134: Added payment logos in the backend of the webshop
+ PLGOPNS-118: Added payment logos in the checkout page for all payment methods
+ PLGOPNS-129: Added an unique identifier to the transaction for products with a variation
+ PLGOPNS-117: Added compatibility for Simple Payment Fee plugin

### Fixed
+ PLGOPNS-110: Fixed configuration for Multi-Store does not work properly
+ PLGOPNS-109: SEPA Direct Debit contained wrong source code
+ PLGOPNS-137: Fixed missing Webshop gift card title on checkout
+ PLGOPNS-131: Fixed Fastcheckout is unable to retrieve shipping methods
+ PLGOPNS-113: Notice message when tax is not defined in the backend of the webshop

### Changed
+ PLGOPNS-135: Updated frontend translations
+ PLGOPNS-125: Updated backend translations
+ PLGOPNS-136: Changed loading path of MultiSafepay.combined.php
+ PLGOPNS-105: Improved layout configuration screen
+ PLGOPNS-91: Renamed ING Homepay to ING Home'Pay
+ PLGOPNS-96: Renamed Mister Cash to Bancontact
+ PLGOPNS-102: Make sending of order update mail configurable
+ PLGOPNS-101: Make confirm_message configurable

### Removed
+ PLGOPNS-50: Removed the configuration option 'When to confirm order'
+ PLGOPNS-116: Removed configuration option 'payment_multisafepay_fco_tax_percent'

***

## 2.2.0
Release date: June 15th, 2018
### Added
+ PLGOPNS-72: Add support for Alipay/ING Home'Pay/Belfius/KBC
+ PLGOPNS-80: Add support for AfterPay
+ PLGOPNS-78: Add support for Santander Betaalplan
+ PLGOPNS-79: Add support for Trustly
+ PLGOPNS-73: Add VVV-Cadeaukaart as a gift card

### Improvements
+ PLGOPNS-59: Add the shipping address to the transaction request
+ PLGOPNS-86: Improve translations

### Fixed
+ PLGOPNS-74: MultiStore is now correctly supported
+ PLGOPNS-75: Configuration form is now applied for geozone and min/max amount

## 2.1.0
Release date: November 13th, 2017
### Improvements
+ Add payment method PaySafeCard.

### Changes
+ Make (only) compatible with OpenCart versions 3.x.

***

## 2.0.2
Release date: February 15th, 2017
### Improvements
+ Only compatible with OpenCart versions 2.3.x.

***

## 2.0.1
Release date: May 20, 2015
### Improvements
+ Added support for Multi-store..
+ Detect current template based on OpenCart version.
+ Added Klarna support.

### Fixed
+ Fixed undefined notices.
+ Fast Checkout wasn't visible after having set "Account type" to "Connect".

### Changes
+ Added VQMod as the preferred method for Fast Checkout integrations.

***

## 2.0.0
Release date: Mar 13, 2015

###  Fixes
+ Fixed problem with converting amount to other currency.

***

## 1.8.1
Release date: Mar 13, 2015

### Fixes
+ Fixed problem with converting amount to other currency.

***

## 2.0.0
Release date: Feb 13, 2015

***

## 1.8.1
Release date: Mar 10, 2014

### Improvements
+ Added support for American Express.
+ Added support for Spaarpunten.
+ Added support for Shipped status.

### Fixes
+ Fixed issue with preselect gateway.
+ Fixed unavailable $order_info bug.

***

## 1.8.0
Release date: Sep 2, 2013

### Improvements
+ Added support for install and configure separate gateways.
+ Added support for Multi-Currency.

### Changes
+ Gateways are now only visible for the supported currency. All available with EUR, Visa and Mastercard for EUR, USD and GBP.
+ Added geo zone support for all supported gateways. Gateway is not visible when address isn't within the selected zone.

### Fixes
+ Now the product-weight is converted correctly to kilogram.
+ Fixed issue when multiple products use multiple different VAT settings.

***

## 1.7.3
Release date: Aug 20, 2013
### Fixes
+ Fixed bug with weight-based shipping for Fast Checkout.
+ Fixed bug with database prefix for table names.
