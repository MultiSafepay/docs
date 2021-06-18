---
title : "Release Notes CS-Cart plugin"
meta_title: "CS-Cart plugin changelog - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases: [/integrations/cs-cart/changelog/]
---
## 1.6.0
Release date - Jun 18th, 2021

### Added
+ DAVAMS-271: Add CBC payment method
+ PLGCSCS-121: Add Request to Pay

### Fixed
+ Include address2 field for house number parsing
+ PLGCSCS-124: Fix incorrect shopping cart when multiple discounts are used

### Changed
+ DAVAMS-347: Update Trustly logo
+ DAVAMS-286: Update name and logo for Santander
+ PLGCSCS-99: Set order to status shipped for all payment methods

***

## 1.5.0
Release date - April 1st, 2020

### Added
+ PLGCSCS-117: Add Apple Pay

### Changed
+ PLGCSCS-113: Rename MultiSafepay Wallet to MultiSafepay

***

##  1.4.0
Release date - February 26th, 2020

### Added
+ PLGCSCS-88: Add "Kies uw Bank" as first issuer option

### Changed
+ PLGCSCS-100: Make merchant_item_id unique for product options
+ PLGCSCS-94: Rename Direct Ebanking to SOFORT Banking
+ PLGCSCS-92: Correct payment methods names
+ PLGCSCS-91: Change the number of decimals from 2 to 10 on all shopping cart items in transaction requests

### Fixed
+ PLGCSCS-93: Fix webshop version number in transaction request
+ PLGCSCS-83: Fix iDEAL issuer list not showing when user tries to place an order

***

## 1.3.0
Release date: Oct 8th, 2018

### Features
+ PLGCSCS-60: Add AfterPay as payment method
+ PLGCSCS-61: Add EPS as payment method
+ PLGCSCS-62: Add iDEAL QR as payment method
+ PLGCSCS-63: Add TrustPay as payment method
+ PLGCSCS-40: Add Trustly as direct payment method to plugin
+ PLGCSCS-43: Add Alipay as payment method
+ PLGCSCS-54: Add Santander as payment method
+ PLGCSCS-23: Add payment logo's
+ PLGCSCS-5: Add support for partial_refunded status

### Changes
+ PLGCSCS-59: Make logical sequence of displaying order statuses in the backend
+ PLGCSCS-53: Support direct transactions for PayPal
+ PLGCSCS-46: Support direct transactions for ING Home'Pay / Alipay
+ PLGCSCS-30: Support direct transactions for KBC
+ PLGCSCS-39: Added disclaimer to new PHP files
+ PLGCSCS-77: Change defaults for order statuses
+ PLGCSCS-80: Status update on refund and partial refund

#### Fixes
+ PLGCSCS-47: Refactor checkout_data when taxes are not set
+ PLGCSCS-44: Change gatewaycode for ING'HomePay to INGHOME
+ PLGCSCS-42: Make user notifications depend on status parameters instead of fixed
+ PLGCSCS-37: Surcharge title was not used in transaction requests
+ PLGCSCS-45: Rename KBC/CBC to KBC
+ PLGCSCS-38: Locale has wrong format within the transaction request

***

## 1.2.0
Release date: Jan 17th, 2018
### Changes
+ Add Belfius & KBC/CBC & ING Home'Pay to plugin
+ Send shopping cart data for all payment methods when creating transaction
+ Add PaySafeCard as payment method to plugin
+ Update header information.
+ Code formatting.
+ When selecting another currency then default the wrong values were added to the transaction
+ Install script did not update existing records
+ Correct Wallet gateway code.
+ Empty Pay After Delivery Fee is added for every transaction
+ Fix checkout_data prices when taxes are used
+ Set correct payment fee id, the same for the shipping method

## 1.1.0
Release date: Jan 27, 2017
### Improvements
+ Add support for PHP-7

### Bugfix
+ Added missing templates for manual order creation using the backend

## 1.0.2
Release date: Dec 30, 2014
### Improvements

+ Better support for updating the order status

## 1.0.1
Release date: Mar 24, 2014
### Improvements
+ Support for American Express.

### Bugfix
+ Fixed bug with Bank transfer on returning.
+ Added billing country check for Pay After Delivery. If billing country is not 'NL' then don't show gateway.
+ Changed locale, use order language if available.

## 1.0.0
Release date: Nov 15, 2013

+ Supports all payment methods including Pay After Delivery
+ Support minimum and maximum value-restricions for showing a gateway.
