---
title : "Release Notes Magento 1 plugin"
meta_title: "Magento 1 plugin changelog - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."

---

## 3.0.0
Release date: Oct. 21st, 2020

### Added
+ DAVAMS-234: Add in3
+ DAVAMS-262: Add CBC payment method
+ PLGMAGONE-699: Add Good4fun Giftcard

### Fixed
+ PLGMAGONE-678: Fix bug in calculating correct price and tax for Fooman surcharge
+ PLGMAGONE-671: Fix maximum nesting level error with Idev OneStepCheckout
+ PLGMAGONE-668: Fix non working days/seconds_active for backend orders

### Changed
+ PLGMAGONE-634: Switch from XML API to JSON API (Only API key is needed)
+ PLGMAGONE-472: Set order to status shipped for all payment methods
+ PLGMAGONE-674: Always set redirect_url
+ DAVAMS-28: Rebrand Santander Betaalplan to Pay per Month
+ DAVAMS-295: Rebrand Direct Bank Transfer to Request to Pay
+ DAVAMS-308: Rebrand Klarna to Klarna - buy now, pay later
+ Update payment method names
  + KBC
  + ING Home'Pay
  + Credit card
  + Pay After Delivery
  + E-Invoicing

***  

## 2.6.0
Release date: Apr. 2nd, 2020

### Added
+ PLGMAGONE-617: Add Apple Pay
+ PLGMAGONE-656: Add Direct Bank Transfer (Request to Pay)
+ PLGMAGONE-485: Add support for Fooman Surcharge
+ PLGMAGONE-562: Added support for PostNL pickup points for Afterpay.

### Fixed
+ PLGMAGONE-654: Fix incorrect character set for translations
+ PLGMAGONE-621: Fix layout issue when OneStepCheckout is used
+ PLGMAGONE-588: Fix missing site secure code in refund request
+ PLGMAGONE-572: Fixed payment fee description not being set
+ PLGMAGONE-526: Fixed undefined variable recurring on E_STRICT mode
+ PLGMAGONE-458: Count gives warning when PHP 7.2 is used

### Changed
+ PLGMAGONE-599: Hide Pay After Delivery when shipping address differs
+ PLGMAGONE-574: Prevent orders to be cancelled when set to processing
+ Update translations for "select your credit card"

***

## 2.5.1
Release date: Mar. 25th, 2019

### Added
+ PLGMAGONE-457: Added Handelsbanken iDEAL issuer logo
+ PLGMAGONE-406: Added support for Modman

### Changed
+ PLGMAGONE-344: Enable refund shipping amount when shipping includes tax

### Fixed
+ PLGMAGONE-465: Fixed service costs not showing with some third party modules
+ PLGMAGONE-456: Fixed service costs not working on clean installation
+ PLGMAGONE-448: Fixed Qwindo does not work in compiled mode
+ PLGMAGONE-431: Fixed notice "undefined index" on invoice creation

***

## 2.5.0
Release date: Sept. 21th, 2018
### Features
+ PLGMAGONE-339: Add Tokenization
+ PLGMAGONE-411: Added support for E-Invoice gateway for manually created orders

### Fixes
PLGMAGONE-429: Corrected Paysafecard gateway for manually created orders

***

## 2.4.2
Release date: Jun. 15th, 2018

### Fixed
+ PLGMAGONE-384: Log refund errors to order notes
+ PLGMAGONE-391: Fix undefined variable in error log when refund exception occurs
+ PLGMAGONE-374: Update Dutch translations

***

## 2.4.1
Release date: May. 25th, 2018

### Added
+ PLGMAGONE-378: Add support for Santander Betaal per Maand
+ PLGMAGONE-379: Add support for Afterpay
+ PLGMAGONE-380: Add support for Trustly
+ PLGMAGONE-381: Add Moneyou iDEAL issuer logo

### Fixed
+ PLGMAGONE-377: Uncaught error when saving empty grouped product while Qwindo was active
+ PLGMAGONE-382: Gateway ING not changed everywhere to INGHOME

***

## 2.4.0
Release date: Mar. 12th, 2018
### Fixes
+ Add support for Qwindo
+ PLGMAGONE-370: Updated Dutch translations
+ PLGMAGONE-369: Update Klarna payment method logo
+ PLGMAGONE-368: Add keep cart alive for ING Home'Pay, Belfius, KBC and iDEAL QR
+ PLGMAGONE-346: Add support for prefilled gender/dob fields in Klarna/Pay After Delivery
+ PLGMAGONE-195: Housenumber extension added when Onestepcheckout is used
+ PLGMAGONE-356: Support direct transactions for ING/KBC
+ PLGMAGONE-362: Update ING Home'Pay name within backend configuration
+ PLGMAGONE-341: Don't add payment fee twice to credit memo
+ PLGMAGONE-331: Add handling of chargeback status
+ PLGMAGONE-354: Add iDEAL QR gateway
+ PLGMAGONE-343: Don't update an order when it's closed (due to offline refund)
+ PLGMAGONE-337: Add check to only update order status when order exists
+ PLGMAGONE-338: Undefined index error on expired pretransactions
+ PLGMAGONE-357: Update ING gateway to INGHOME
+ PLGMAGONE-340: Prevent cancel on api error when order has already been paid
+ PLGMAGONE-342: Fixes headers already send error when credit card gateway is used
+ PLGMAGONE-336: Undefined index custom_refund_desc

***

## 2.3.6
Release date: Nov. 7th, 2017
### Fixes
+ PLGMAGONE-326: add daysactive/secondsactive for Klarna/Pay After Delivery
+ PLGMAGONE-327: Removed Klarna quote loading to prevent infinite loop
+ PLGMAGONE-159: Removed unused reverted status configurations
+ PLGMAGONE-323: Allow different billing/shipping addresses, reverted PLGMAG-304
+ PLGMAGONE-329: Fixed sorting on min/max amounts
+ PLGMAGONE-96: Restricted currencies used are now loaded from the correct store
+ PLGMAGONE-313: _selecteer uw credit card_ is now translatable
+ PLGMAGONE-33: Added support for AliPay
+ PLGMAGONE-96: Improvements to currency restriction in











t cards/gateways
+ PLGMAGONE-96: Restricted currencies used are now loaded from the correct store

***

## 2.3.5
Release date: Oct. 23th, 2017
### Fixes
+ Fixed an issue causing a double iDEAL issuer selection.

***

## 2.3.4
Release date: Aug. 3th, 2017
### Fixes
+ Fixed issue trying to get property of non-object payment_data.
+ Fixed issue where manual orders could be placed with decimals.
+ Fixed PLGMAGONE-132. Some undefined index notices got fixed.
+ Fixes PLGMAG-304. Only allow Klarna when billing and shipping address are the same (Klarna regulation).
+ Fixed issues with the Givacard gateway.
+ Fixed PLGMAGONE-105: getShippingAmount zero leads to NAN tax table.
+ Fixes an issue with de credit card gateway not processing the brand.

### Improvements
+ Added missing logo used for the credit card payment method option.
+ Updated the install script.
+ Updated Bancontact logo and title.
+ Removed Thumbs.db from the package.
+ Added delivery info to Pay After Delivery/Klarna requests.
+ Fixes PLGMAGONE-311 and PLGMAGONE-312. Added gateway codes for Paysafecard and American Express.

### Features
+ Added support for Paysafecard.
+ Added support for Belfius.
+ Added support for KBC/CBC.
+ Added support for ING Home'Pay.
+ Add customizable description to refund request.
+ Support for Seconds Active PLGMAGONE-259.

***

## 2.3.3
Release date: Feb. 16th, 2017
### Fixes
+ Resolved PHP7 deprecated warnings occuring in the MultiSafepay class file.

***

## 2.3.2
Release date: Jan 25th, 2017
### Fixes
+ Removed whitespace which resulted in the PHP error "headers already sent" being triggered when selecting the credit card gateway
+ Resolved an issue when used with OneStepCheckout causing the wrong gateway to be used.

***

## 2.3.0
Release date: Oct 12th, 2016
### Improvements
+ Added EPS and FerBuy as payment methods.
+ iDEAL issuerlist alignment improved.
+ Added official support for the FastCheckout productfeed v1.0
+ Added some missing German translations for Klarna.

### Fixes
+ Fixed an issue related product quantity when partially refunding Klarna payments.

### Changes
+ Changed the YourGift logo.

***

## 2.2.9
Release date: Aug 10, 2016

### Improvements
+ Status requests are now logged in multisafepay.log when debug option is enabled.

### Fixes
+ Resolved an issue where invoices aren't being generated.

***

## 2.2.8
Release date: June 21st, 2016

### Improvements
+ Added E-Invoicing.
+ Payment links are now only requested when creating new orders in the Magento backend, not when editing an order, resulting in a new order.

### Fixes
+ Fixed an undefined notice within the logs.
+ Resolved an issue resulting in the transactional data not being set, such as; parent_id and additional_information

### Changes
+ Updated Bancontact image
+ Changed the iDEAL issuer selection from dropdown to radio buttons with the bank's logo.

***

## 2.2.7
Release date: May 26th, 2016
### Improvements
+ Added logging of refund requests.
+ The currency is now retrieved from the order when creating a credit memo and refunding, rather than from the store.
+ Added support for Fast Checkout product feed.
+ Improvements were made to the confirmation page URL.
+ Added improvements for the refunding of foreign currencies.

### Fixes
+ Resolved undefined notices.
+ Resolved issues when refunding orders that have discounts.
+ Resolved a bug when using webshop gift card.
+ Resolved the doubled shippingtax bug causing incorrect invoice and/or credit memo amounts.

### Changes
+ Removed the refunding of fees.

***

## 2.2.6
Release date: March 10th, 2016
### Fixes
+ Resolved incorrect tax amount visible in the invoice when using a fee.

***

## 2.2.5
Release date: March 4th, 2016
### New features

+ Added Dotpay as payment method.

### Improvements
+ Invoices now show the correct payment method.

### Fixes
+ Resolved issues preventing orders from being opened once paid with PayPal or Bank transfer.
+ Resolved error code 1035 occurring when refunding.
+ Resolved credit memo issues.
+ The total order amount of orders paid with Fast Checkout now include the shipping costs.

***

## 2.2.2
Release date: Dec 28th, 2015
### Improvements
+ If paid amount difference from total order amount. A note is added with extra info. No invoice is created.
+ Added (incl Tax) to totals line to make it more clear as other lines can be set in tax totals settings. Also added this for the frontend.
+ Added configurable FastCheckout field for phone number.

### Fixes
+ Fixes undefined configMain notice.
+ Added missing klarna.phtml
+ In case an order is paid by Second Chance and an other payment method is used as the initial, the order will be updated with the correct payment method.
+ Fixes bug with directdebit using a wrong gateway code
+ Fixes for wrong credit memo amounts that are processed.
+ Fixes Store id is now used to get the correct store URL's to redirect to
+ Fixes cancelled status for Pay After Delivery and Klarna notifications are now ignored as the order was already set to Paid. If set to cancelled then a credit memo can't be created anymore.
+ Fixes bug causing the order status set to "payment review" instead of "processing". This was caused because the order grandtotal had to be rounded to two so it matches the paid amount in the transaction.


## 2.2.1
Release date: Nov 12th, 2015
### New features
+ Payment fee can now be refunded
+ Added min/max amount restrictions for all gateways.

### Improvements
+ Added Klarna to the language file.

### Fixes
+ Fixed undefined variable isAllowConvert notice.
+ Fixed undefined variable Currencies notice.
+ Fixed issue using wrong StoreConfig.
+ Fixed issue when selecting all the available currencies in the configuration.
+ Fixed issue using the wrong account credentials for FastCheckout.
+ Fixed issue causing shipping method not to be correct for Klarna and Pay After Delivery.
+ Fixed issue which prevented accepting gender, bank account and date of birth twice when using Klarna.
+ Fixed issue which resulted in 1 cent mismatch when using Klarna on older Magento installations.

***

## 2.2.0
Release date: Aug 20th, 2015
### New features
+ Added Klarna as payment method.
+ gift card now have their own API key config.
+ Refunds now work for Klarna, Coupons and Pay After Delivery.
+ Success page now visible when using a payment link or pay using Second Chance.
+ FCO button now also language based.
+ Fallback to configured gateway code if gateway is not available within the quote.
+ Fallback if issuer is set but no gateway, then somehow we lost the gateway although iDEAL was selected. We now default to iDEAL.
+ Added Beauty and Wellness gift card.
+ Added Sport&Fit gift card.
+ Added VVV gift card.
+ Added PODIUM gift card.
+ Added missing Gifcard logos.
+ All available currencies can be selected when configuring the gateway.
+ Added option to remove all buttons to the normal checkout for when only FCO is enabled.

### Improvements
+ Updated order of FastCheckout in menu.
+ MultiSafepay menu added.
+ Separated some configurations.

### Changes
+ Disabled gift card Ebon.
+ Return-URL's are now always ending with only /success/ for better support for GUA module.
+ Disabled FastCheckout payment method in normal checkout as this is causing confusion for merchants.
+ Don't set state to cancelled when partial refunded as it still has to be processed partially.
+ Disabled some gift cards that are for one merchant.
+ Added FCO button on login/register page.
+ Redirect URL always added for Pay After Delivery.
+ Check for stock settings before processing stock.
+ Now use current selected currency to recalculate fee. Fee is always configured in EUR.
+ Removed old package file.
+ Removed unused code.
+ Set checkout session to be used instead of core for storing issuer data.
+ Update xmlescape function.

### Fixes
+ Fixed Store name from order is used for manual paylink, not the admin site.
+ Fixed some undefined fields causing a Notice error when PHP use a STRICT error logging.
+ Fixed success URL for Direct Bank transfer (Request to Pay).
+ Fixed some issues with the customer groups selected in the configuration of the gateways.
+ Fixed prices including tax (Solved error 1027).
+ Fixed some encoding issue.
+ Fixed When sending the order confirmation after a payment, then this is ignored for a Bank transfer.
+ Fixed fee now displayed correctly when using multi-currency.
+ Fixed bug with gift card data and delivery data.

***

## 2.1.2
Release date: May 7th, 2015
### Improvements
+ Paymentlinks generated in the Magento Admin for manually created orders now use the 'Daysactive' setting in the main plugin configuration.
+ The transaction status 'Expired' no longer triggers the plugin to cancel orders with an invoice.

### Changes
+ The 'Keep Cart Alive' plugin setting has been enabled by default.
+ The 'Keep Cart Alive' plugin setting now only works for MultiSafepay payment methods.
+ Fast Checkout no longer creates an order for an expired pretransaction

### Fixes
+ 'Allowed currencies' for the MultiSafepay Gateways were not requested correctly.
+ Added delivery address data to pretransactions for PayPal's Sellers Protection.
+ Call to undefined method error occuring with the Pay After Delivery object
+ Paymentlinks generated in the Magento backend for manually created orders always used the test environment
+ Fixed double payment method titles
+ Resolved DIRECTebanking gateway code bug
+ Magento didn't always update and store the amount correctly when converting from USD to EUR resulting in the wrong amount paid after the plugin conversion.
+ The Pay After Delivery (MultiFactor) rejection message has been added to the language files.
+ The Pay After Delivery (MultiFactor) rejection message has been altered to only show relevant information to customers.
+ Available payment methods are no longer shown when the visibility has been limited to specified user groups.
+ The plugin processes the refund status and closes the order if the credit memo option isn't enabled when creating a credit memo

***

## 2.1.1
Release date: Mar 20, 2015
### Fixes
+ Fixed bug for outline gateway images

***

## 2.1.0
Release date: Mar 19, 2015
### New features
+ Coupons now use their own gateway settings so that multiple + MultiSafepay accounts can be used to support multiple MultiSafepay coupons
+ Add a refund transaction to the Magento transactions order overview on refund or partial refund
+ Support for partial refunds
+ Special status for initialized Bank transfer transactions
+ Added support for fixed fee and/or percentage fee for each gateway
+ Show Pay After Delivery rejection notice within the store when transaction is rejected
+ Added enable/disable config value for FCO product feed
+ Feed action. Feed can be requested at /msp/standard/feed/
+ Enable/disable config option check is now added. Check is also added for API key to check if the given key matches the configured key
+ Order now using translation files
+ Added updateInvoice function. Send Magento invoice ID to MultiSafepay, this will be added to the accountant export
+ Added daysactive to connect
+ When creating an order we now use the selected payment method for the manual transaction request
+ Payment link added to a manually created order by an admin. When an admin creates an order manually, we will create a transaction request for it and add the payment link to the order. The merchant now doesn't need to login to the Ewallet and manually create a payment link for the order

### Improvements
+ If there is an invoice, the order can't be cancelled anymore
+ Added more language files
+ Better support for Keep Cart alive, so it is compatible with Onestepcheckout
+ Added check for - phone number for BNO trans. Compatibility with some Onestepcheckout modules that add - when phone number is empty or not available as custom field
+ Check if payment is object, if not, default to standard gateway model This will solve the 1016 error message
+ Manual payment link process has changed. Updated the observer. The payment link is now only added when the order is being created from the Magento Admin and no longer on every save action within the Magento Admin
+ If title isn't added then fallback tot main gateway title
+ Updated upgrade script
+ Updated bno.phtml for better layout in OneStepCheckout
+ Better support for gateway images. Works with default, onestepcheckout.com and Apptha checkout
+ Removed disable option for text titles
+ Disabled check for active table rates config. This was old code from when this was configured within the FCO configuration
+ Transaction errors for normal transaction request now also result in a closed order
+ Added extra check for enabled fee for the payment method
+ After transaction error with DIRECT Pay After Delivery transactions we will close the order because replacing using another payment method will create a new order
+ When status is refunded just return ok and exit. The Magento plugin can process partial refunds so we should ignore refunded status because this can update the order wrong with partial refunds. Status updates are done by creating the credit memo
+ Added fallback for refund status for when new base.php is used with older releases
+ Added transaction details to the transaction record that is created when creating an invoice automatically
+ Added default config to the plugin that sets the fee after the shipping cost in the totals overviews
+ Rewrite of the refund API integration. The implementation was wrong and causing every MultiSafepay refunded to be processed online. This supposed to be a choice by order to refund online. Merchants can now refund online when it's enabled within the configuration and by going to the invoice, click credit memo and then refund. Then can choose to refund, or refund offline where the refund offline won't submit the refund to MultiSafepay

### Changes
+ Removed fijncadeau references

### Fixes
+ Fixed bug for coupon settings
+ Fixed bug for ordering same pages with different options results in an error 1027
+ Pay After Delivery option for sending invoice email. When enabled resulted in NOT sending and vice-versa
+ Fixed bug Maintransaction ID errors when auto redirect is enabled with direct iDEAL
+ Reset fee before trying to set it. Solves issue with some installations not reseting, resulting in fee from other selected payment method
+ Added extra setQuote to solve issues reported by one merchant where Magento didn't add the quote correctly to the order. To solve this bug with Magento, we set the quote manually within the order
+ Fixed bug with payment details to be added to the transaction record. Payment details are now stored again within the transaction record
+ Fixed bug with unpaid invoices when completed
+ Fixed issue to treat order status cancelled or cancelled (American vs English) the same correct way
+ Fixed bug that caused product from a manually created order to be in the cart for the customer that the order was created for when the customer returns to the store and logs in
+ Fixed bug with paid status
+ When creating an invoice, Magento gets the totalpaid value and add it to the total invoiced value. When we don't create an invoice automatically, we set the totalpaid to inform the merchant that the order was paid. This resulted in a double totalPaid value because Magento added the invoiced total to the totalPaid when manually creating the invoice. This is now changed so that we reset the Total Paid in this situation just before the invoice is created and Magento updates the totalPaid again

***

## 2.0.2
Release date: Oct 10, 2014
### Improvements
+ Added an option to set the daysactive for an Pay After Delivery transaction. When not payed in time, the transaction will expired and the webshop will be notified
+ Added extra line to set the order total to paid if it hasn't been done
+ Now use the fee price formatter so it includes the selected currency
+ Force ordertotal set to paid when transaction is completed and invoice creation is disabled. Only show creation of transaction note once.
+ Added version number to config title line.
+ Textual improvements.
+ Better check on order confirmation email sending.
+ Rrecalculate the product price without tax as Magento round at 2 decimals by default and we use 4. This resulted in a amount mismatch when ordering larger quantities of the same product.
+ Better support for special chars.
+ Enabled locking again but return false instead of showing error and exit. This should avoid duplicate invoices when callback is called while before the redirect_url set the order status.

### Changes
+ FEE base is rewritten.
+ Upgrade the php dependence to 5.5.12.
+ Now get the selected gateway from the quote instead of the gateway model. This adds better compatibility with third party onestepcheckout plugins.

### Fixes
+ Fixed bug for error #1016 on the Return-URL.
+ Fixed bug with gateway title not being visible in checkout.
+ Fixed bug with missing house number on connect transactions.
+ Fixed bug with order email not being sent after transaction complete.
+ Fixed bug with double totalPaid amount.

***

## 2.0.0
Release date: May 20, 2014
### Improvements
+ Added support for refunds from out of the backend of the webshop
+ Fast Checkout now use the Magento Shipping methods
+ When the order status of an Pay After Delivery order in the webshop is set to 'Shipped', the status of the transaction is also changed in the MultiSafepay backend.
+ Currency not supported by MultiSafepay can now be converted to euro's.
+ Programm structure of the plugin changed to the standard Magento convention.
+ added support for Fashion-cheque.
+ added support for Lief cadeaukaart.
+ added support in the configuration for minimal order amount for iDEAL.
+ added (limited) support for Magento Connect package (Only for new installations, not for an update from an older version of plugin).

### Changes
+ The 'Solve fee bug' setting has been removed from the configuration. This is fixed in the software.
+ The gateway 'Fijncadeau' is deleted because it is no longer available.
+ Transaction-ID is added to the redirect URL, for the case that our system doesn't.
+ disable log for status-request to avoid large log files.
+ lockfile systeem disabled.

### Fixes
+ Fixed bug in the American Express config.
+ Fixed 500 error when developers mode is enabled and iDEAL is selected without bank preselection.
+ Fixed bug with images in checkout.
+ Fixed bug with currency for separate gateway's.
+ Fixed bug with the language.
+ The additional fee is removed by normal operation.(Bug reported in v1.4.4).
+ Fixed memory limit bug cause by recursion in the Payafter.php model.
+ Fixed undefined index notices.

***

## 1.4.4
Release date: Apr 28, 2014
### Improvements
+ Better support for OneStepCheckout.
+ Better support for Apptha OneStepCheckout.

### Fixes
+ fixed bug with total amount when using conversion.
+ Fixed bug with autocreate invoice.
+ Fixed bug with double fee calculation.
+ Fixed bug with fee by payments other than Pay After Delivery.

***

## 1.4.3
Release date: Apr 8, 2014
### Improvements
+ Filtering for special characters in XML.
+ Added option to show the Pay After Delivery fee incl or excl tax during checkout, without changing calculations.
+ Added Pay After Delivery template for direct Pay After Delivery transaction request.
+ Added American Express as payment method.
+ Added max amount for some gateways.

### Changes
+ Always get first IP address for customer IP and forwarded IP that it finds within the given value.
+ Create invoice after payment has been completed, Magento changed things, if invoice isn't created then the order is processing with unpaid status.
+ Changed default/template/msp/default.phtml files. This provides gateway html for other gateways other then MultiSafepay.
+ Removed house number feature. If house number isn't available after parse the address then we use street2.
+ Changed the way how discounts are processed.
+ Change store name for connect transactions.
+ No more redirect to checkoutcontroller for FCO transactions. All is done from within the standardcontroller. This solves 302 and 307 offline action errors.

### Fixes
+ Google checkout bug fix.
+ Fixed bug with configurable product only show the correct pages and don't show up twice in pages listing.
+ Fixed bug with order data.
+ Fixed return to empty cart page when offline actions are slow.
+ fixed issue on error 503 in offline actions. No need to fill in account details in 3 different places.
+ Fixed bug with directdebit and SOFORT Banking.
+ Fixed bug with empty return-url.

***

## 1.4.2
Release date: Feb 4, 2014
### Fixes
+ Invoice emails are now send correctly when using Magento 1.8.1
+ Better support for Pay After Delivery

***

## 1.4.1
Release date: Sep 19, 2013
### Improvements
+ Support for free shipping method
+ Fee configurable option for the amount.
+ HTML instructions support for connect Gateway
+ Support for the onestepcheckout house number feature. This function seperates the address and house number, with this option enabled Pay After Delivery would fail on missing data.
+ Amount validation check. If the quote amount is not equal to the order amount the transaction creation will stoped to prevent an underpaid order.
+ Currency selection support for each separate gateway. Now you can select the currencies that are supported, the gateway will only be visible with the selected currencies.
+ Degrotespeelgoedwinkel coupon as supported gateway
+ Support for gateway descriptions per gateway. You can also use html within the description field to add nice gateway descriptions.
+ Configurable 'multisafepay servicekosten' label for Pay After Delivery. This label can now be changed
+ Support for gateway images. Option to select only an image, the title, or both.
+ Support for void, declined and expire status codes in combination with CANCELLED STATE.

### Changes
+ Direct e-banking is now SOFORT Banking
+ Moved the fee line within the order totals table to above the tax
+ The Fee tax description so it uses the configured label
+ Disabled discontinued Fijncadeau coupon card
+ Fooman surcharge fix no longer applies. To avoid confusion this is removed from the package.

### Fixes
+ Wrong fee percentage for BNO Tax
+ Disable visibility for the (old) notification URL
+ Language was missing by use of Fast Checkout
+ Bank selection was alway visible with iDEAL, even when the option was disabled.
+ Parfumcadeaukaart coupon is now working correctly
+ 'The cart is not equal' is now solved for normal checkout as the one step checkout.
+ When no fee is active the service cost's won't be visible.

***

## 1.3.3
Release date: Mar 26, 2013
### Improvements
+ Added an 'send order status update email' option
+ Added an option to keep the cart active
+ Added override for the order submit function. Now we can keep the cart active when a customer cancelled the order.
+ Added the Fast Checkout method to the normal checkout process
+ Added creation of an account within the store when a customer uses Fast Checkout.
+ Better UTF-8 compatibility for Fast Checkout to prevent error 1000 messages.

***

## 1.3.2
Release date: Mar 10, 2013
### Improvements
+ Added Pay After Delivery support
+ Added an extra check to that an invoice won't be created twice
+ Added bank_id check
+ Better one step checkout compatibility with iDEAL issuer selection

### Changes
+ Updated Gateway template for direct banking.
+ Removed the Invoice observer to avoid problems with invoice creation. The observer activated an update function that isn't needed.
+ Updated the default Fast Checkout logo

### Fixes
+ Fixed bug iDEAL issuers list with production environment.
+ Fixed bug registered bank_id bug, now we have a select your bank option to avoid errors when customers forget to select a bank.
+ Fixed bug for empty order status when an order was cancelled.
+ Fixed bug that caused a duplicate transaction request
+ Fixed store_id bug.
+ Fixed bug that cause useless Notification notices within the error logs.

***

## 1.3.1
Release date: Jan 10, 2013
### Improvements
+ DirectXML for Bank transfer.

***

## 1.3.0
Release date: Dec 10, 2012
### Improvements
+ DirectXML for iDEAL.

***

## 1.2.9
Release date: Jan 12, 2011
### Improvements
+ New order email option is active, you can now set when you want to send the order emails.
+ New feature added that allows for reopening cancelled orders. If a cancelled order got paid by using Second Chance etc, the order will be processed again and an invoice is created etc.
+ Added gateways for ebon, baby gift card, boekenbon, erotiekbon, fijncadeau, webshop




card, parfumnl, parfumcadeaukaart.

### Fixes
+ Quantity didn't got updated correct when some statusses got processed.
+ Fix bug that allowed the processing of the same status multiple times. Check added so that a status will only be processed once.

***

## 1.2.8
### Improvements
+ STATE_CANCELED changed to STATE_PENDING due to Second Chance.

### Fixes
+ Cancelled Orders will now actually be cancelled.

***

## 1.2.7
### Improvements
+ Better handling of manual invoice creation.
+ Extra lock check that if an error occurs the status message is Not OK.
+ use_shipping_notification set to false to overcome issue with "Cannot send order to ##Specified## country.

### Fixes
+ Cancelled Orders will now actually be cancelled.

***

## 1.2.6
### Improvements
+ Send email on Processing (instead of initial).
+ Manual create invoices for orders.
+ Payment Overview Cancelled status for: Void, Declined & Expired.
