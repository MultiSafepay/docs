---
title : "Release Notes X-Cart plugin"
meta_title: "X-Cart plugin changelog - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases: [/integrations/x-cart/changelog/]
---

## 2.3.0
Release date: Mar 20th, 2020

### Added
+ PLGXCTS-97: Add refund support (full and partial for non billing suite)
+ PLGXCTS-98: Add support for shipment updates
+ PLGXCTS-82: Add compatibility with Value Added Tax / Goods and Service tax module

### Fixed
+ PLGXCTS-89: Correct broken ING Home'Pay title
+ PLGXCTS-86: Fix fatal error when using SOFORT Banking

### Changed
+ PLGXCTS-81: Bump plugin version to become compatible with X-Cart 5.4.x

***

## 2.2.0
Release date: Apr 24th, 2019

### Added
+ PLGXCTS-40: Added Trustly direct and redirect payment method.
+ PLGXCTS-45: Added AfterPay, Alipay, iDEAL QR and Santander Betaal per Maand as payment methods.
+ PLGXCTS-35: Added shopping cart data to all payment gateways.
+ PLGXCTS-22: Added Belfius, KBC and ING Home'Pay as payment methods.

### Fixed
+ PLGXCTS-5: Fixed missing invoice number in confirmation mail.
+ PLGXCTS-25: Fixed getTranslation error in shipping.
+ PLGXCTS-64: Fixed crash on returning from successful payment for some payment methods.

## 2.1.0
Release date: Dec 15th, 2015
### Changes
+ Added Klarna as a payment method.
+ Added Refund API support.

## 2.0.0
Release date: Jul 3th, 2015
### New features
+ Now supports Pay After Delivery
+ Now supports separate gateways, so the gateways are directly showed on the checkout page
+ Now supports direct IDEAL
+ Refunds are now processed correct.

### Improvements
+ Plugin is total rewritten for X-Cart 5 and higher.
+ All purchased pages are now listed in the transaction.
+ Order description now contains value of the invoice..
