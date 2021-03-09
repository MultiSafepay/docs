---
title : "Release Notes ZenCart plugin"
meta_title: "ZenCart plugin changelog - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
aliases: [/integrations/zencart/changelog/]
---

## 3.1.0
Release date: Jul 14th, 2020

### Added
+ DAVAMS-213: Add track & trace to shipment request
+ PLGZENS-71: Add Apple Pay
+ PLGZENS-72: Add Direct Bank Transfer (Request to Pay)
+ PLGZENS-44: Add Santander Betaal per Maand
+ PLGZENS-51: Add plugin version to backend
+ PLGZENS-43: Add AfterPay
+ PLGZENS-46: Add Trustly
+ PLGZENS-47: Add Alipay
+ PLGZENS-24: Add Belfius, KBC and ING Home'Pay

### Fixed 
+ Adjust prices with currency rate for multicurrency
+ Fix missing tax table when shipping is free
+ PLGZENS-73: Fix incorrect shipping tax in shopping cart
+ PLGZENS-58: Fix product details missing in confirmation email
+ PLGZENS-53: Fix cannot save orders when images are enabled
+ PLGZENS-50: Fix error when not choosing an iDEAL issuer at "Select your bank" screen
+ PLGZENS-64: Fix orders getting an incorrect status
+ Update deprecated constructor

### Changed
+ Bank transfer, Klarna, iDEAL, Pay After Delivery, E-Invoicing are now direct only
+ PLGZENS-28: Let Zen Cart handle order saving
+ PLGZENS-65: Add 'MultiSafepay' to "Updated by" on order status update
+ Add quantity to the items list in the transaction request
+ PLGZENS-41: Update Klarna logo
+ PLGZENS-29: Send shopping cart data for all payment methods when creating transaction
+ PLGZENS-54: Set order to status shipped for all payment methods
+ PLGZENS-81: Use redirect transaction if required fields are not filled for iDEAL, Pay After Delivery, E-Invoicing

### Removed
+ PLGZENS-31: Remove unused admin folder
+ PLGZENS-60: Remove gift cards Lief, ParfumNL, Nationale Erotiekbon
+ PLGZENS-74: Remove FerBuy
+ PLGZENS-78: Remove branded gift cards Bloemen Cadeaubon, Brouwmarkt
+ PLGZENS-78: Remove branded gift cards De Grote Speelgoedwinkel, Jewelstore Giftcard
+ PLGZENS-78: Remove branded gift cards Kelly Giftcard

***

## 3.0.0
Release date: May 29th, 2017
### Improvements
+ Added all currently available payment methods and gift cards
+ Added translations for Dutch, French, German, Italian, Portuguese and Spanish
+ Added a setting for "days_active"; automatically close an unpaid order without transaction after X number of days.
+ Added a setting to enable or disable payment method icons during the checkout process.

### Fixes
+ Resolved an issue causing the homepage to be shown, rather than the order confirmation page, after a successful order.

### Changes
+ Changed the plugin to make use of the JSON API, rather than the XML API.

***

## 2.0.3
Release date: Nov 27, 2014
### Improvements
+ Create a record in the history of the order status when a payment is completed
+ Product attributes are now visible in backend
+ Added country restrictions to the shipping methods request
+ Added support for extra Pay After Delivery fee (when using the third party 'Surcharge Fee by Payment Method Order Total Module')
+ Added support for all coupons to the ZenCart plugin
+ Add support for several types of discount for use with Pay After Delivery
+ Added specific order statuses for Pay After Delivery

### Fixes
+ Fix for FastCheckout shipping request
+ Fix don't update on pretransaction
+ Fix for getting the correct tax-rate
+ Fix for not showing delivery address in the email
+ Fix on the cancel-URL for Fast Checkout

***

## 2.0.2
Release date: Mar 17, 2014
### Improvements
+ Added support for American Express.
+ Added coupon support for Pay After Delivery

### Fixes
+ Fixed shipping method and payment method code in order overview
+ Fixed product attributes, these are now available in overview and details page
+ Fixed missing order data bugs
+ Fixed empty email info for Pay After Delivery orders
+ Fixed bug that cause shipping method to be unavailable in backend
+ Fixed rounding amount

***

## 2.0.1
Release date: Feb 13, 2014
### Fixes
+ Order information is now visible in the order confirmation screen.
+ Empty the card after a payment
+ Fixed empty order history
+ Fixed empty delivery and shipping address within order email
+ Fixed empty products details within order email

***

## 2.0.0
Release date: Okt 28, 2013
### Improvements
+ Added support for install and configure separate gateways.
+ Added support for multi-currency
+ Added support for Fast Checkout
+ Added support for Pay After Delivery
