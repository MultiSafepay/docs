---
title : "Release Notes WooCommerce plugin"
meta_title: "WooCommerce plugin changelog - MultiSafepay Documentation Center"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

## 3.4.0
Release date January 6th, 2020

### Added
+ PLGWOOS-287: Add maximum amount restriction for credit cards
+ PLGWOOS-321: Add Ohmygood Cadeaukaart

### Changed
+ PLGWOOS-115: Make suitable for WordPress.org Plugin Directory
+ PLGWOOS-260: Change VVV Bon to VVV Cadeaukaart

### Fixed
+ PLGWOOS-319: Disable payment fields when payment description is empty

## 3.3.0
Release date December 13th, 2019
### Added
+ PLGWOOS-291: Add IP validation when WooCommerce returns multiple IP addresses
+ PLGWOOS-203: Add compatibility with WPML

### Changed
+ PLGWOOS-245: Change Klarna from direct to redirect
+ PLGWOOS-275: Improve Dutch translation for 'Activate'
+ PLGWOOS-263: Correct ING Home'Pay spelling

### Removed
+ PLGWOOS-208: Remove the send invoice option from the backend

### Fixed
+ PLGWOOS-285: Fix the fatal error "Cannot redeclare error_curl_not_installed"
+ PLGWOOS-102: Prevent the Notification URL from executing when not initialized by MultiSafepay
+ PLGWOOS-266: Prevent errors from appearing in logs for notifications of pre-transactions
+ PLGWOOS-290: Resolve DivisionByZeroError bug occurring with fees 
+ Fix PHP notice incorrect use of reset in function parseIpAddress
+ Fix PHP notice undefined property when order set to shipped

## 3.2.0
Release date July 5th, 2018
### Improvements
+ PLGWOOS-232: Add TrustPay payment method
+ PLGWOOS-213: Add support for external fee plugin(s)
### Fixes
+ PLGWOOS-176: Restrict autoload to load only MultiSafepay classes
+ PLGWOOS-191: Refactor the way an order and transaction are retrieved
+ PLGWOOS-241: Remove status request on setting to shipped
+ PLGWOOS-195: Update Klarna Invoice link
+ PLGWOOS-231: Update Klarna payment method logo
+ PLGWOOS-197: Correct MultiFactor Terms and Condition link
+ PLGWOOS-242: Remove terms and conditions for E-Invoicing
+ PLGWOOS-244: Shipment name now used on Payment page instead of type
+ PLGWOOS-243: Payment page shopping cart reorganized
+ PLGWOOS-253: FastCheckout load correct first and last name
+ PLGWOOS-235: Rename KBC/CBC to KBC
+ PLGWOOS-236: Rename ING-Homepay to ING HomePay
+ PLGWOOS-247: Notice message 'Undefined variable' for E-Invoice, Pay After Delivery and Klarna
+ PLGWOOS-249: Remove whitespace at file headers
***

## 3.1.0
Release date: June 8th, 2018
### Improvements
+ PLGWOOS-215 Add support for Santander Betaalplan
+ PLGWOOS-214 Add support for Afterpay
+ PLGWOOS-216 Add support for Trustly

### Fixes
+ PLGWOOS-221: Do not add Klarna invoice link when setting order to Completed
+ PLGWOOS-218: Fixed undefined property in error logs when cancelling order
+ PLGWOOS-226: getTimeActive didn't respect seconds
***

Release date: Feb 2nd, 2018
### Improvements
+ PLGWOOS-169 Support direct transactions for Alipay/ING/Belfius/KBC
+ PLGWOOS-174 Remove usage of deprecated functions
+ PLGWOOS-175 Remove unnecessary use of file_exists
+ PLGWOOS-178 Order status is only changed to 'expired' in case the current status is 'pending' or 'on-hold'.
+ PLGWOOS-179 Add text domain for iDEAL issuer error message
+ PLGWOOS-182 Add Alipay as payment method
+ PLGWOOS-186 Add dynamic retrieve of shipping methods during Fast Checkout
+ PLGWOOS-187 Do not allow refund when amount is zero or less
+ PLGWOOS-192 Check/add all translations

### Fixes
+ PLGWOOS-173 Fix deprecated notice getRealPaymentMethod
+ PLGWOOS-180 Incorrect order-id used to load the order for updating
+ PLGWOOS-181 function getGatewayCode not implemented for FastCheckout
+ PLGWOOS-183 Update version number of plugin failed
+ PLGWOOS-184 Incorrect check if field is empty
+ PLGWOOS-193 Fix deprecated notice FastCheckout
+ PLGWOOS-194 Refund function checks wrong variable to determine if refund was successful
+ PLGWOOS-199 Correct wc_get_cart_url and wc_get_checkout_url
+ PLGWOOS-200 FastCheckout doesn't redirect to order-confirmation screen
+ PLGWOOS-202: Payment method updated for Second Chance on Processing

### Changes
+ PLGWOOS-189 Update version number to 3.0.4
+ PLGWOOS-198 Update ING gateway to INGHOME

***

## 3.0.3
Release date: Oct 10th, 2017

(Requires WooCommerce 2.2+)

### Fixes

+ Menus are able to edit again.
+ In some cases, the customer was redirected to the cancel-url after a successful iDEAL transaction.

***

## 3.0.2
Release date: Okt 10nd, 2017
### Improvements
+ Add ING Home'Pay as payment method.
+ Add Belfius as payment method.
+ Add KBC/CBC as payment method.
+ Add configuration option for Google-Analytic code.
+ Add shopping-cart information to the transaction.
+ Update payment method in order, in case a customer pays the second chance with another payment method.
+ Update the Dutch translations.

### Fixes
+ Fixed issue to prevent a warning message when the title of a gateway wasn't filled in the config.
+ Fixed issue with retrieve the correct external transaction ID.
+ Fixed issue on error 1027 (Invalid cart amount) caused by an invalid shipping-tax.
+ Fixed issue in function to set order-status to shipped for Pay After Delivery, Klarna and E-Invoiced.
+ Fixed warning issue on function setToShipped.
+ Fixed issue on not accepting Pay After Delivery orders caused by a divide by zero error.

Changes
+ Remove (beta)functionality to determine if there is a new version available.
+ Restrict use of the plugin to WooCommerce 2.2 and above.

***

## 3.0.0
Release date: April 5nd, 2017
### Improvements
+ Compatible with PHP-7
+ Installation by standard Wordpress method
+ Added Dutch language file
+ Added configuration option Karna Merchant-EID (for future use.)
+ Added Terms and Conditions for Klarna, Pay After Delivery and E-Invoicing.
+ Improve the way errors are logged.
+ Added PaySafeCard as payment method.
+ Added Nationale bioscoopbon as a gift card.
+ Added option to the global MultiSafepay settings to enable/disable the giftcards as payment method.

### Fixes
+ Better algorithm to split address into street, house number
+ After complete FastCheckout transaction no order confirmation page was showed

Changes
+ General plugin settings moved to the general checkout-options
+ Remove BabyGiftcard as payment method

***

## 2.2.7
Release date: November 2nd, 2016
### Improvements
+ Added EPS and FerBuy as payment methods
+ Added support for E-Invoicing
+ Added an extra payment method gateway called "Credit cards"; grouping credit card payment methods as a single dropdown option.

### Fixes
+ Resolved an issue resulting in not being able to pay using Direct iDEAL.
+ Resolved an issue where expiring payment sessions result in orders being marked as new after 30 days.

### Changes
+ Changed Bank transfer to direct bank transfer

***

## 2.2.6
Release date: July 14th, 2016
### Improvements
+ Added support for WooCommerce version 2.6.2.

### Fixes
+ Resolved an issue resulting in not being able to pay using Direct iDEAL.

***

## 2.2.5
Release date: June 24th, 2016
### Improvements
+ Added support for partial refunds for orders paid using Klarna and Pay After Delivery.
+ Added support for Fast Checkout order refunds.
+ ### Improvements were made to the iDEAL banklist selector, and a notice will be shown if no bank was selected.

### Fixes
+ Updated the Bancontact logo

### Fixes
+ Resolved issues occurring with Pay After Delivery and Klarna when using discounts.
+ Made compatible with WooCommerce version 2.6.



## 2.2.4
Release date: March 8th, 2016
### Improvements
+ Pay After Delivery is now only visible for orders placed in The Netherlands.
+ Textual ### Improvements for the option "Send the order confirmation".
+ Started orders with bank transfer, are now set to On Hold, rather than "Pending Payment".
+ Uncleared orders are now set to On Hold, rather than "Pending Payment".
+ Improved the iDEAL description shown when no iDEAL issuer/bank has been selected.

### Fixes
+ Resolved a bug causing Error 1035 when refunding.
+ Changed the way coupons are applied, which previously resulted in a mismatch in paid totals.

***

## 2.2.3
Release date: Feb 18, 2016
### Improvements
+ Added Dotpay as a payment method
+ Klarna and Pay After Delivery transactions are now set to Shipped, if enabled and the order is set to Completed.
+ Pay After Delivery is now only available as a payment method if the selected country is "The Netherlands".
+ Multistores in WooCommerce are now supported.
+ Added bunq as a supported iDEAL issuer

### Fixes
+ Refunds from within WooCommerce now also work when using the WooCommerce Sequential Order Numbers plugin.
+ Issues with Gateway restrictions based on minimum and maximum amount are resolved for Klarna and Pay After Delivery.
+ Fixed a bug causing the postalcode not to be added to the order when using Fast Checkout.
+ Removed WooCommerce mailer functions in the plugin, which was added to avoid mailing issues.

***

## 2.2.2
Release date: Dec 14, 2015

### Improvements
+ Added Klarna reservationcode and link to the invoice in the order comments.
+ For KLARNA and Pay After Delivery the order status is set to shipped when order status is set to completed and this option is enabled in the configuration.
+ Added Goodcard as gift card.

### Fixes
+ Fixed performance issue due to our plugin loaded the iDEAL issuers on every page.
+ Fixed house number is now correct parsed when using both address fields.
+ Fixed issue with wrong processing of some order statuses.
+ Fixed the FastCheckout button was not completely visible with latest updates of WooCommerce default template.

***

## 2.2.1
Release date: Sep 30, 2015

### Improvements
+ Added Klarna as payment method.

### Fixes
+ Fixed issue that prevents MultiSafepay to add the order status in the order comment.

***

## 2.2.0
Release date: May 21, 2015
### Improvements
+ Added an extra check to determine if the MultiSafepay class exists.
+ Debug option added to the plugin for troubleshooting purposes.
+ Added improved payment method icons.
+ Added the MultiFactor agreement hyperlink.
+ Added Refund API support. Refunds via MultiSafepay can now be executed from the WooCommerce backend.
+ Added a check to see if WooCommerce is active. The plugin will not be loaded if not the case.

Changes
Changed add_error(); to wc_add_notice();

### Fixes
+ Fixed some undefined notices and improved checks for page_id and the loading of the plugins.
+ Resolved the 'Cannot redeclare class' error.

***

## 2.1.0
Release date: Oct 15, 2014
### Improvements
+ Added Fast Checkout
+ Added coupon support for FCO
+ Added option to enable/disable fco button
+ Added DB Table to check if order is already created and if so, go to normal updating process when using Fast Checkout
+ Added amount check that compares the calculated order total after creating the order and the transaction amount. If they are not equal, then set to wc-on-hold status and add a note about the mismatch in amounts
+ Added Pay After Delivery as a separate plugin
+ Added American Express as a separate plugin
+ Added PayPal as a separate plugin
+ Added Visa as a separate plugin
+ Added Mistercash as a separate plugin
+ Added Mastercard as a separate plugin
+ Added Maestro as a separate plugin
+ Added Giropay as a separate plugin
+ Added SOFORT Banking as a separate plugin
+ Added DirectDebit as a separate plugin
+ Added Bank transfer as a separate plugin
+ Added iDEAL as a separate plugin

### Changes
+ Changed the processing of the offline actions so that FCO transactions work
+ Process stock on process_payment
+ Use ordernumber instead of orderid so that the plugin is compatible with third-party sequential ordernumbers plugins
+ Removed gateway method from the main module. Gateways are now separate plugins
+ Removed images from main module. These are now loaded from each separate plugin
+ Removed version checks as this version is only for 2.2 and higher
+ Removed useless code from all plugins
+ Removed country and amount restrictions. WooCommerce changed things and broke the function

### Fixes
+ Fixed bug with status updates
+ Fixed new bug with coupons not being processed because of extra check on cart or order discount
+ Small ### Fixes (o.a. reported by Mark Roeling)

***

## 1.0.6
Release date: Apr 15, 2014
### Improvements
+ Added support for direct Pay After Delivery

***

## 1.0.5
Release date: Mar 21, 2014
### Improvements
+ Added support for
+ Added house number check

### Fixes
+ Fixed bug when customer cancelled a payment
+ Fixed bug that causes an empty status
+ Fixed bug in refund check

***

## 1.0.4
Release date: Mar 06, 2014
### Improvements
+ Auto spit house number from address if needed

### Fixes
+ Fixed bug when customer cancelled a payment
+ Fixed bug that causes an empty status
+ Fixed bug in refund check

***

## 1.0.3
Release date: Feb 19, 2014
### Improvements
+ Added support for WooCommerce 2.1.x
+ Added payment method Pay After Delivery
+ Changed payment name 'directebanking' to 'SOFORT Banking
+ Added support for third-party payment surcharge module
+ Added support for dollars and GBP
+ Added check for available issuers when paying by iDEAL
+ added orderid to the return URL

### Fixes
+ Fixed bug that caused no order data to show on success page

***

## 1.0.2
Release date: Aug 21, 2013
### Improvements
+ Optional send an invoice email

### Fixes
+ Fixed bug in update order status
