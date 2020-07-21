---
title : "Release Notes PrestaShop plugin"
meta_title: "PrestaShop 1.6 plugin changelog - MultiSafepay Documentation Center"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

## 3.6.0
Release date: Jul 21st, 2020

### Added
+ DAVAMS-269: Add CBC payment method

### Changed
+ DAVAMS-213: Add track & trace to shipment request
+ PLGPRSS-404: Set order to status shipped for all payment methods

***

## 3.5.0
Release date: Apr 9th, 2020

### Added
+ PLGPRSS-344: Add AfterPay

### Fixed
+ PLGPRSS-396: Correct spelling of ING Home'Pay
+ PLGPRSS-397: Fix incorrect gateway code for ING Home'Pay

***

## 3.4.0
Release date: Apr 2nd, 2020

### Added
+ PLGPRSS-400: Add Apple Pay
+ PLGPRSS-399: Add Direct Bank Transfer

***

## 3.3.0
Release date: Feb 26th, 2020

### Fixed
+ PLGPRSS-309: Prevent multiple transactions being created for the same order
+ PLGPRSS-391: Prevent duplicated orders by adding file locking
+ PLGPRSS-267: Mobile presentation of payment methods is not fully responsive

### Changed
+ PLGPRSS-190: Send shopping cart data for all payment methods
+ PLGPRSS-352: Improve parsing of address into street and apartment

***

## 3.2.0
Release date: Nov. 8th, 2017
### Improvements
+ Add gift card Givacard.
+ Error-messages are now showed according to the PrestaShop guidelines.
+ Order Confirmation screen now also contains the order information.
+ Changed the layout for gateways during checkout (iDEAL, Pay After Delivery, Klarna, E-Invoice, Bank transfer).
+ Module descriptions are now uniform.
+ Critical debug- and error messages are added to the PrestaShop-Logger, wether or not the debug function in the module is enabled.
+ Tokenization is included.
+ Some small ### Changes to the styling.
+ Update translations.
+ Changed the way and address is split into street and house number.

### Fixes
+ In some situations, the cart was accidentally emptied.
+ The order-confirmation screen was also showed for non-MultiSafepay payment methods.

### Changes
+ Removed the configuration option for by-passing the order-confirmation screen. This because the order-confirmation screen is default PrestaShop behaviour and mandatory for some payment methods.
+ Removed the configuration option for HTTP or HTTPS since this was added in the past for one merchant having some issues.
+ Removed the lock mechanism in the offline-action script. Since this was unnecessary.

***

## 3.1.7
Release date: Sept. 8th, 2017
### Improvements
+ Add ING Home'Pay as payment method.
+ Add BKC as payment method.
+ Add Belfius as payment method.
+ Update Dutch translation-files.
+ Resized all payment logos.
+ Removed underscore in the name of all gift cards.
+ Adjust birthdate to correct layout for Klarna and Pay After Delivery.
+ Removed own order-confirmation.tpl and use PrestaShop default.

### Fixes
+ Customer is now correct redirected to the order-confirmation page.
+ Check whether or not update order status failed sometimes.
+ Confirmation-form for PaySafecard was not loaded due to a misspelled filename.
+ When using the Connect gateway the button for 'All payment methods' was not available.
+ Shipping methods where selected based on language-code instead of country-code.
+ When using the CreditCard gateway the customer wasn't redirect to the correct payment-page.
+ In exceptional cases no order was created due to an invalid security-key.
+ FastCheckout failed in updating the order status.
+ FastCheckout did not support Free shipping.
+ Transaction-ID was not always included in the order.
+ Free Shipping information was not included in the transaction.

### Changes
+ Removed support for BVKPayment for FastCheckout. as this can configured within the MultiSafepay Control.

***

## 3.1.5
Release date: May. 12th, 2017
### Improvements
+ New logo for Mastercard.
+ Add PaySafeCard as payment method.

### Fixes
+ Order confirmation screen is now also showed when option 'Moment of order creation' is set to 'After order is paid in full'
+ The system will try for maximal 10 seconds to check if transaction is paid.
+ If failed (for example Bank transfer) the order history page is showed as fallback.
+ Fixed issue for support of BVKPayment module.

***

## 3.1.4
Release date: Dec. 20th, 2016
### Improvements
+ MultiSafepay notices and error messages are now shown in the webshop (front-end).
+ Added input field placeholders for the payment methods Klarna and Pay After Delivery.

### Fixes
+ Added a lock mechanism to prevent the creation of duplicate orders due to multiple Notification URL calls taking place in quick succession.

### Changes
+ Removed option 'After checkout completed' under the 'at what moment should the order be created' setting, as this option is identical to the 'After order confirmation' option.
+ Date of birth provide in the webshop for Klarna and/or E-Invoice is carried over to the Payment page.
+ Resolved unnecessary debug message #1006 being logged when creating transactions.

***

## 3.1.2
Release date: Nov. 23th, 2016
### Improvements
+ Added full support for BVK payment fees module; percentages, fixed amounts and combinations are supported.
+ Added bundled gift card payment method; the seperate gateways Visa, Mastercard, Maestro and American Express are not visible during checkout.
+ Added some translational ### Improvements
+ Add extra option in the configuration to select the HTTP / HTTPS protocol to use for Offline Actions.
+ Added EPS.
+ Added Ferbuy.
+ Errors are now shown on the Prestashop storefront.

### Fixes
+ Multiple free shipping methods are now shown correctly instead of just one.
+ Fixed issue where the customer was redirected to the order history page instead of the order-confirmation page.

### Changes
+ Removed option 'After checkout completed' under the 'at what moment should the order be created' setting, as this option is identical to the 'After order confirmation' option.
+ Checkout fields for Klarna are now mandatory.
+ Pay After Delivery fields are now mandatory when using direct Pay After Delivery.

***

## 3.1.1
Release date: Okt 17th, 2016
### Improvements
+ Resolved an issue resulting in the wrong calculations being applied for shipping and wrapping taxes.
+ A check was added to see whether or not SSL has been enabled in the webshop. Resulting in HTTP301 not occurring when calling the Notification URL.
+ A check was added to see if the current plugin version is the latest version available on our website.
+ Added support for % fee when using BVKPayment module.
+ Added new logo for YourGiftcard.

### Fixes
+ Resolved a bug preventing order's from being created using certain configurations.

### Changes
+ Layout of the configuration screens now have standard PrestaShop design.

***

## 3.0.3
Release date: July 27th, 2016
### Fixes
+ Resolved a bug preventing order's from being created using certain configurations.

***

## 3.0.2
Release date: July 12th, 2016
### Improvements
+ Orders are now created for initialized Bank transfer payments and uncleared transactions when using the setting; "Only when an order was paid in full".
+ Added E-Invoicing as a payment method.
+ The PSP ID is added to the order, so it can be used to find the corresponding transaction in the MultiSafepay Control.

### Fixes
+ Fixed issue with crypt function were no 'salt' was used. This resulted in a notice when using PHP 5.6 or above.

### Changes
+ Textual ### Changes to the plugin configuration.
+ Changed the name and logo "MisterCash" to "Bancontact".

***

## 3.0.0
Release date: Apr 15th, 2016
### Improvements
+ The payment method shown in the Fast Checkout orders are now updated to show the payment method eventually used.
+ Added (limited) support for the BVK Additional Payment Fees module; payment fees can be applied per payment method.
+ Added "daysactive" to the configuration. Orders are cancelled after X number of days when configured.
+ An extra configuration option has been added for skipping the default extra confirmation screen before payment.
+ Added Dotpay as a payment method.
+ Added e-Invoice as a payment method.
+ Added tooltips to the configuration options in the plugin.
+ Improved the payment logos.
+ Added a debug configuration option. Debug output are logged to: 'prestashop_root_directory/log/MultiSafepay.log'.
+ Added the following gift cards:

1.	Beautyandwellness
2.	Brouwmarkt
3.	Fashiongiftcard
4.	Fietsenbon
5.	Gezondheidsbon
6.	Goodcard
7.	Jewelstore
8.	Kellygiftcard
9.	Liefcadeaukaart
10.	Nationaletuinbon
11.	Nationaleverwencadeaubon
12.	Parfumcadeaukaart
13.	Parfumnl
14.	Podium
15.	Sportenfit
16.	Webshopgiftcard
17.	Welness-gift card
18.	Wijncadeau
19.	Winkelcheque

### Fixes
+ Order status was not updated in case of a partial refund.
+ In specific situations there was still a Payment Error.
+ Minor ### Improvements to the iDEAL gateway layout to match the other payment methods.
+ Improved translations.
+ Changs bank account input field from 10 to 34 characters.

### Changes
+ Removed Babygiftcard.
+ In specific situations there was still a Payment Error.
+ Order status are no longer removed when uninstalling the core MultiSafepay module, resulting in existing orders maintaining the correct order status.
+ This plugin has been rewritten from scratch and uses the JSON API rather than the XML API.
+ Changed the Fast Checkout logo.
+ The order history page is shown when redirected back to the webshop after a successful payment.

***

## 2.1.1 (Nov 2, 2015
### Improvements
+ Added support for gift card VVV-Bon.
+ During installation of the plugin, the order states will not be removed anymore. So old orders remain their correct order status.

### Fixes
+ Order status was not updated in case of a partial refund.
+ In specific situations there was still a Payment Error.

***

## 2.1.0
Release date: Oct 8, 2015
### Improvements
+ Added support for the BVK Payments module for the payment method Pay After Delivery.
+ MultiSafepay Transaction IDs are now added to, and visible within, the Prestashop order.
+ Changed the Fast Checkout button.
+ The payment method used to pay for an order is now shown within the order overview.
+ The payment hook template now uses the default Prestashop style within the checkout and can be overruled by template overrides.
+ Added Fashzoncheque.

### Changes
+ The iDEAL bank list is now shown under the payment method iDEAL, rather than the next step.
+ Removed the E-Bon gift card.

### Fixes
+ Resolved double paid/invoice notices.
+ Fixed bug to show payment method when the Min and Max amount in the config are equal.
+ Fixed undefined index notice warnings.
+ Fixed double payment method titles.
+ Improved the support of shipping methods, coupons, taxes, free shipping and free products.
+ Shipping prices were always handled by Fast Checkout as including tax.

***

## 2.0.0
Release date: Nov 11, 2014
### Improvements
+ Added special NL config files.
+ Added Italian language files.
+ Added Gateway image for Wallet.
+ Added support for Prestashop 1.6.x.
+ Added support for erotiekbon.
+ Added support for e-bon.
+ Added support for degrotespeelgoedwinkel.
+ Added support for boekenbon.
+ Added support for babygiftcard.
+ Added Notification info field to FCO config for when only Fast Checkout is active.
+ Added better support for IP6.

### Changes
+ Make some ### Changes to the config screen.
+ Updated language files.
+ Updated local images.
+ Updated lang files ES en FR.

### Fixes
+ Fixed bug with wrong Shipping price calculation.
+ Fixed bug to show payment method when the Min and Max amount in the config are equal.
