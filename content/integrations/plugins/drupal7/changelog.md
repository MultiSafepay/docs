---
title : "Release Notes Drupal 7 plugin"
meta_title: "Drupal 7 plugin changelog - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
aliases: [/integrations/drupal7/changelog/]
---

## 2.2.0
Release date: Apr 1st, 2020

### Added
+ PLGDRPC-266: Add Apple Pay
+ PLGDRPC-264: Add Direct Bank Transfer (Request to Pay)

### Changed
+ PLGDRPC-256: Changed Bank transfer from redirect to direct

***

## 2.1.0
Release date: Sep 1th, 2017
### Changes
+ PLGDRPC-55 - Add feature to ship order when order is complete
+ PLGDRPC-54 - Import default rule for setting order to processing when paid
+ PLGDRPC-51 - Process shipped order status update for all payment methods
+ PLGDRPC-46 - Change forwarded_ip to use X-Forwarded-For instead of remote_addr
+ PLGDRPC-50 - Improve shipping call
+ PLGDRPC-45 - Added support for AliPay, Dotpay, E-invoicing, EPS, TrustPay
+ PLGDRPC-44 - Gateway parfumcadeaukaart is wrong
+ PLGDRPC-43 - Add debug logger
+ PLGDRPC-41 - update Bancontact default name
+ PLGDRPC-38 - Change BTWO to BTW0, could cause tax issues
+ PLGDRPC-36 - Refactor commerce_multisafepay_json_payment_redirect/callback
+ PLGDRPC-37 - Add disclaimer file to root and disclaimer headers to files
+ PLGDRPC-35 - Remove unused .install files
+ PLGDRPC-34 - Add readme
+ PLGDRPC-33 - Make api account customizable by rules
+ PLGDRPC-32 - Add hooking ability to transaction request
+ PLGDRPC-31 - Added support for KBC, ING Home'Pay and Belfius
+ PLGDRPC-30 - Add PaySafeCard
+ PLGDRPC-29 - Send shopping cart data for all payment methods when creating transaction

## 2.0.0
Release date: July 7th, 2015
### New features
+ This plugin has been rewritten
+ Uses the MultiSafepay JSON API.
+ Added Direct iDEAL.
+ Added Refund API support.
+ Pay After Delivery and Klarna orders can now be set to shipped from the backend.
+ The payment method used is now shown in the order overview.
+ Added (watchdog) logging functionality for MultiSafepay requests.
+ Added coupon and discount support.
+ Added support for Commerce Fees module to support order/shipping/payment fees.
+ Added support for Rules.
