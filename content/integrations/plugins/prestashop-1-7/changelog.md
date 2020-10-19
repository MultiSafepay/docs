---
title : "Release Notes PrestaShop plugin"
meta_title: "PrestaShop 1.7 plugin changelog - MultiSafepay Documentation Center"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

## 4.7.0
Release date: October 19th, 2020

### Added
+ PLGPRSS17-124: Add Good4fun Giftcard
+ DAVAMS-233: Add in3 payment method
+ PLGPRSS17-15: Add Spanish translations
+ PLGPRSS17-108: Add VVV Cadeaukaart as a giftcard
+ DAVAMS-213: Add track & trace to shipment request

### Fixed
+ PLGPRSS17-125: Gateways don't show for combination of conflicting shipping methods
+ PLGPRSS17-110: Align payment method names and logo with radio buttons
+ PLGPRSS17-46: Prevent bypassing Terms & Conditions during checkout by using enter
+ PLGPRSS17-74: Encryption function was called statically instead of non-static
+ PLGPRSS17-103: Fix warning not activated payment methods on php version < 7.0
+ PLGPRSS17-41: Fix rounding issue in the shopping cart
+ PLGPRSS17-119: Prevent order is created twice
+ PLGPRSS17-112: Validate IP addresses to prevent error 1000
+ PLGPRSS17-106: Fix gateway code for Webshop Giftcard
+ PLGPRSS17-107: Fix gateway code for Fashion Giftcard
+ PLGPRSS17-115: Fix Apple Pay issue with One Page Checkout PS
+ PLGPRSS17-104: Fix VAT issue when no tax is defined
+ PLGPRSS17-111: Fix JS error on Apple Pay with non-existing form element

### Changed
+ DAVAMS-315: Rebrand Klarna
+ DAVAMS-297: Rebrand Direct Bank Transfer to Request to Pay
+ PLGPRSS17-12: Bank transfer email send with MultiSafepay email systems
+ DAVAMS-285: Update name and logo for Santander
+ PLGPRSS17-120: Update Italian translations
+ PLGPRSS17-8: Remove default tax from shopping cart
+ PLGPRSS17-14: Change AfterPay from redirect to direct
+ PLGPRSS17-9: Improve address parser

### Removed
+ PLGPRSS17-93: Remove automatic API key validation
+ PLGPRSS17-88: Remove unsupported giftcards from plugin
+ PLGPRSS17-118: Remove VVV Bon

***

## 4.6.1
Release date: April 17th, 2020

### Fixed
+ PLGPRSS17-105: Gift cards not visible in checkout

***

## 4.6.0
Release date: March 27th, 2020

### Added
+ PLGPRSS17-97: Add Apple Pay
+ PLGPRSS17-96: Add Direct Bank Transfer (Request to Pay)

### Fixed
+ PLGPRSS17-94: Fix ClassNotFoundException when cURL returns an error

***

## 4.5.1
Release date: February 26th, 2020

### Fixed
+ PLGPRSS17-83: Fix transaction status was not updated when set to shipped

***

## 4.5.0
Release date: December 12th, 2019

### Added
+ PLGPRSS17-17: Add refund support within PrestaShop
+ PLGPRSS17-45: Add Bank transfer details to PrestaShop invoices
+ PLGPRSS17-49: Add PSR-4 namespaces

### Changed
+ PLGPRSS17-21: Set order to status shipped for all payment methods

### Fixed
+ PLGPRSS17-64: Fix groups restrictions for payment methods and gift cards
+ PLGPRSS17-44: Fix issue where a free gift was not recognized as free
+ PLGPRSS17-30: Fix notifications returning HTTP 302

***

## 4.4.0
Release date: July 3rd, 2019

### Added
+ PLGPRSS-244: Add support for tokenization

### Changed
+ PLGPRSS17-35: Display proper gateway name as used payment method, instead of gateway code

***

## 4.3.1
Release date: May 15th, 2019

### Fixed
+ PLGPRSS-372: Prevent creation of duplicate orders

## 4.3.0
Release date: April 25th, 2019

### Added
+ PLGPRSS-274: Add iDEAL QR payment method
+ PLGPRSS-311: Add transaction ID to payment details when viewing order in backend

### Changed
+ PLGPRSS-225: Change way path to plugin js/css files is determined to prevent sporadic loading issue
+ PLGPRSS-351: Change merchant_item_id to support product variants
+ PLGPRSS-261: Improve parsing of address into street and apartment
+ PLGPRSS-335: Correct spelling ING Home'Pay

### Fixed
+ PLGPRSS-353: Fix no payment methods visible after updating carriers
+ PLGPRSS-356: Fix refund issue for products with a variation
+ PLGPRSS-348: Fix when installing through commandline, config is not initialized
+ PLGPRSS-347: Fix warning during sorting of gateways and gift cards
+ PLGPRSS-345: Prevent order status be changed on not MultiSafepay orders

### Removed
+ PLGPRSS-283: Remove Klarna invoice link

***

## 4.2.0
Release date: May 25th, 2018

### Improvements
+ PLGPRSS-312: Add support for Santander Betaal per Maand payment method
+ PLGPRSS-313: Add support for AfterPay payment method
+ PLGPRSS-314: Add support for Trustly payment method

***

## 4.1.0
Release date: May 8th, 2018

### Improvements
+ PLGPRSS-222 Add Dutch translations
+ PLGPRSS-240 Support direct transactions for iDEAL, Pay After Delivery, E-Invoice, bank transfer, ING Home'Pay, KBC and PayPal
+ PLGPRSS-246 Add check to see if test/live option corresponds with the used API key
+ PLGPRSS-253 Add warning when enable gateway and not available in MultiSafepay Control
+ PLGPRSS-276 Multiple transactions created after multiple clicks on the order-confirmation button
+ PLGPRSS-277 Update Klarna payment method logo
+ PLGPRSS-278 Remove MultiSafepay.js from the front-end
+ PLGPRSS-280 Add Italian translation
+ PLGPRSS-286 Remove debugging statement
+ PLGPRSS-310 Add message to order in case amount paid is not equal to order amount

### Fixes
+ PLGPRSS-248 When in debug mode a long list of warnings is displayed when entering the configuration.
+ PLGPRSS-254 Gateway not visible when min_amount is filled and Max_amount not.
+ PLGPRSS-255 Changes in the configuration are not showed
+ PLGPRSS-257 Parsing address failed when the house-number is on the second address row.
+ PLGPRSS-258 Order-confirmation page not always shown, due order not existing yet
+ PLGPRSS-268 Change gateway-code ING to INGHOME
+ PLGPRSS-269 Updates within payment method configuration are not updated on save
+ PLGPRSS-281 gateway_info undefined when using direct transactions
+ PLGPRSS-285 No gateways available for virtual products
+ PLGPRSS-287 Fix spelling mistake gezondheidsbon
+ PLGPRSS-288 Update uninstall function to unregister missing hooks
+ PLGPRSS-293 Wrong spelling of some gateway names
+ PLGPRSS-294 Pay After Delivery uncleared stays on 'Payment accepted' after declining from MultiSafepay side.
+ PLGPRSS-301 Pay After Delivery E-invoice form layout error with non-English languages
+ PLGPRSS-303 Order creation failed when order amount differs from paid amount

### Changes
+ PLGPRSS-245 Combine Live- Test- API key to just one API-Key
+ PLGPRSS-249 Remove min/max amount for gift cards in the configuration
+ PLGPRSS-250 Remove IP-restriction in the configuration of PAD/KLARNA/E-INVOICE
+ PLGPRSS-265 Replace DAYS_ACTIVE by SECONDS_ACTIVE
+ PLGPRSS-275 Make form fields required for iDEAL, Pay After Delivery, E-Invoice
+ PLGPRSS-297 Change the message of the redirect to the order-history page

***

## 4.0.0
Release date: January 9th, 2018

### Improvements
+ Initial release for PrestaShop 1.7

***
