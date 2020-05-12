---
title : "Release Notes ZenCart plugin"
meta_title: "ZenCart plugin changelog - MultiSafepay Documentation Center"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

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
