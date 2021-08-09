---
title : "Release Notes VirtueMart plugin"
meta_title: "VirtueMart plugin changelog - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases: [/integrations/virtuemart/changelog/]
---

## 2.2.2
Release date: April 25, 2019
### Fixed
+ PLGVIRS-44: Prevent creation of index.html in administrator folder
+ PLGVIRS-47: 500 error after installing MultiSafepay plugin

## 2.2.1
Release date: July 28, 2017
### Added
+ Added Klarna payment method
+ Added images for all payment methods
+ PLGVIR-27: Added Paysafecard payment method
+ PLGVIRS-26: Added support for E-Invoicing payment method

### Fixed
+ PLGVIRS-32: update id of shiping item within cart data
+ PLGVIRS-33: product_PriceWithoutTax should become product_priceWithoutTax
+ Fixed an issue with prices causing a 1027 error when using discounted prices

## 2.2.0
Release date: May 07, 2015
### Improvements
+ Added support for VirtueMart2+3 and Joomla2.5 and 3
+ Plugin is now installable and had basic functions in VM3.
+ Added gateway images, these need to be uploaded manually. See manual
+ Added option in the config for send confirmation email
+ Added Fast Checkout as payment method.

### Changes
+ Moved daysactive option to extra settings instead of account settings tab

### Fixes
+ Min/Max restrictions now work for another PM than iDEAL.
+ Untranslated language constant now translated.
+ Response on notification callback now correct.
+ Payment data is now added correctly to db. Function added to get data from db and add it to the order view.
+ Shipping now correct added to order totals.
+ Updates on order totals.
+ Fixed discount issues for Pay After Delivery
+ Order total discounts are now added to pre-transaction.
+ Products now added to the order correct in VM3, calculations done in order totals.
