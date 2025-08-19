---
title: Magento 1
category:
  uri: Integrations
slug: magento-1
position: 5
privacy:
  view: public
parent:
  uri: our-integrations
content:
  excerpt: Technical manual for MultiSafepay's free plugin.
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Magento.svg" width="50" align="right" style={{margin: '20px', maxHeight: '75px'}} />

<a className="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#006ba1', color: '#ffffff', textDecoration: 'none'}} href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/magento1/Plugin_Magento_3.8.0.zip" target="_self"><span>Download</span><i className="icon icon-download" style={{marginLeft: '0.6em'}}> </i></a>

> ⚠️ Action required
>
> Magento 1 is end-of-life. We recommend [upgrading as soon as possible](/docs/magento-1#upgrades).

# Changelog

<details id="changelog">
  <summary>Changelog</summary>

  <br />

  **3.8.0**\
  Release date: Aug. 7th, 2025

  ### Added

  * DAVAMS-863: Add Billink
  * DAVAMS-827: Add Bizum
  * PLGMAGONE-776: Add generic payment methods instructions

  ### Removed

  * DAVAMS-903: Remove ALIPAY payment method
  * DAVAMS-816: Remove gender checkout field from iDEAL in3

  ***
  **3.7.0**\
  Release date: Nov. 28th, 2024

  ### Changed

  * DAVAMS-796: Rebrand Afterpay-Riverty Logo
  * DAVAMS-744: Rebranding in3 B2C

  ### Fixed

  * PLGMAGONE-771: Fix surcharges where percentage not applied when fixed amount is 0

  ### Removed

  * PLGMAGONE-773: Remove issuers from iDEAL
  * DAVAMS-709: Remove Santander Betaal per Maand

  ***

  **3.6.0**\
  Release date: Oct. 16th, 2023

  ### Added

  * DAVAMS-660: Add Zinia payment method

  ***

  **3.5.1**\
  Release date: Jun. 16th, 2023

  ### Changed

  * DAVAMS-605: Rename "Credit Card" payment method as "Card payment"

  ***

  **3.5.0**\
  Release date: May 18th, 2023

  ### Added

  * DAVAMS-576: Add Pay After Delivery Installments payment method

  ### Removed

  * DAVAMS-569: Remove Google Analytics tracking ID, within the OrderRequest data

  **3.4.0**\
  Release date: Dec. 15th, 2022

  ### Changed

  * DAVAMS-541: AfterPay rebranded as Riverty

  ### Fixed

  * PLGMAGONE-759: Fix difference between xml declaration and file name (letter-case sensitive) which might be preventing display the template in rare cases.

  ***

  **3.3.0**\
  Release date: Oct 4, 2022

  ### Added

  * DAVAMS-528: Add Alipay+ payment method

  ### Fixed

  * PLGMAGONE-757: Fixed issue to ensure all payment methods display in the checkout, related to the case sensitivity declaration in the configuration file

  ***

  **3.2.0**\
  Release date: Sep. 16th, 2022

  ### Added

  * DAVAMS-518: Add Amazon Pay payment method
  * DAVAMS-489: Add MyBank payment method
  * PLGMAGONE-744: Add Date Picker for birthday checkout fields
  * PLGMAGONE-742: Add Second Chance settings field for each payment method

  ### Changed

  * PLGMAGONE-753: Klarna is updated to work as a redirect payment method, removing the related checkout fields

  ### Fixed

  * PLGMAGONE-740: Include the shipping email address missing in the shipping object within the order request

  ***

  **3.1.3**\
  Release date: Nov. 24, 2021

  **Fixed**

  * PLGMAGONE-736: Fix invalid method `backendOrdersAllowed` on backend orders

  ***

  **3.1.2**\
  Release date: Nov. 23, 2021

  **Fixed**

  * PLGMAGONE-734: Fix unable to create backend orders (items not showing)
  * PLGMAGONE-735: Fix conflict with service cost and non MultiSafepay plugins

  ***

  **3.1.1**\
  Release date: Sep 16, 2021

  **Fixed**

  * PLGMAGONE-730: Use correct invoice id when order is being updated to shipped
  * PLGMAGONE-731: Remove unused tax tables which could generate wrong taxes

  ***

  **3.1.0**\
  Release date: Jun 15, 2021

  **Added**

  * PLGMAGONE-710: Add support for [Generic Gateways](#generic-gateways) which can be used for branded gift cards
  * PLGMAGONE-627: Add order number variable support to custom refund description

  **Fixed**

  * PLGMAGONE-719: Prevent a zero amount refund leading to a full refund
  * PLGMAGONE-706: Show payment instructions for gift cards too

  **Changed**

  * DAVAMS-344: Update Trustly logo

  ***

  **3.0.0**\
  Release date: Oct 21, 2020

  **Added**

  * DAVAMS-234: Add in3
  * DAVAMS-262: Add CBC payment method
  * PLGMAGONE-699: Add Good4fun Giftcard

  **Fixed**

  * PLGMAGONE-678: Fix bug in calculating correct price and tax for Fooman surcharge
  * PLGMAGONE-671: Fix maximum nesting level error with `Idev` OneStepCheckout
  * PLGMAGONE-668: Fix non working days/seconds\_active for backend orders

  **Changed**

  * PLGMAGONE-634: Switch from XML API to JSON API (Only API key is needed)
  * PLGMAGONE-472: Set order to status shipped for all payment methods
  * PLGMAGONE-674: Always set redirect\_url
  * DAVAMS-28: Re-brand Santander Betaalplan to Pay per Month
  * DAVAMS-295: Re-brand direct bank transfer to Request to Pay
  * DAVAMS-308: Re-brand Klarna to Klarna - buy now, pay later
  * Update payment method names
    * KBC
    * ING Home'Pay
    * Credit card
    * Pay After Delivery
    * E-Invoicing

  ***

  **2.6.0**\
  Release date: Apr 2, 2020

  **Added**

  * PLGMAGONE-617: Add Apple Pay
  * PLGMAGONE-656: Add Direct Bank Transfer (Request to Pay)
  * PLGMAGONE-485: Add support for Fooman Surcharge
  * PLGMAGONE-562: Added support for PostNL pickup points for AfterPay.

  **Fixed**

  * PLGMAGONE-654: Fix incorrect character set for translations
  * PLGMAGONE-621: Fix layout issue when OneStepCheckout is used
  * PLGMAGONE-588: Fix missing site security code in refund request
  * PLGMAGONE-572: Fixed payment fee description not being set
  * PLGMAGONE-526: Fixed undefined variable recurring on E\_STRICT mode
  * PLGMAGONE-458: Count gives warning when PHP 7.2 is used

  **Changed**

  * PLGMAGONE-599: Hide Pay After Delivery when shipping address differs
  * PLGMAGONE-574: Prevent orders to be cancelled when set to processing
  * Update translations for "select your credit card"

  ***

  **2.5.1**\
  Release date: Mar 25, 2019

  **Added**

  * PLGMAGONE-457: Added Handelsbanken iDEAL issuer logo
  * PLGMAGONE-406: Added support for `Modman`

  **Changed**

  * PLGMAGONE-344: Enable refund shipping amount when shipping includes tax

  **Fixed**

  * PLGMAGONE-465: Fixed service costs not showing with some third-party modules
  * PLGMAGONE-456: Fixed service costs not working on clean installation
  * PLGMAGONE-448: Fixed Qwindo does not work in compiled mode
  * PLGMAGONE-431: Fixed notice "undefined index" on invoice creation

  ***

  **2.5.0**\
  Release date: Sept 21, 2018\
  **Features**

  * PLGMAGONE-339: Add Tokenization
  * PLGMAGONE-411: Added support for E-Invoice gateway for manually created orders

  **Fixes**\
  PLGMAGONE-429: Corrected Paysafecard gateway for manually created orders

  ***

  **2.4.2**\
  Release date: Jun 15, 2018

  **Fixed**

  * PLGMAGONE-384: Log refund errors to order notes
  * PLGMAGONE-391: Fix undefined variable in error log when refund exception occurs
  * PLGMAGONE-374: Update Dutch translations

  ***

  **2.4.1**\
  Release date: May 25, 2018

  **Added**

  * PLGMAGONE-378: Add support for Santander Betaal per Maand
  * PLGMAGONE-379: Add support for AfterPay
  * PLGMAGONE-380: Add support for Trustly
  * PLGMAGONE-381: Add Moneyou iDEAL issuer logo

  **Fixed**

  * PLGMAGONE-377: Uncaught error when saving empty grouped product while Qwindo was active
  * PLGMAGONE-382: Gateway ING not changed everywhere to INGHOME

  ***

  **2.4.0**\
  Release date: Mar 12, 2018\
  **Fixes**

  * Add support for Qwindo
  * PLGMAGONE-370: Updated Dutch translations
  * PLGMAGONE-369: Update Klarna payment method logo
  * PLGMAGONE-368: Add keep cart alive for ING Home'Pay, Belfius, KBC and iDEAL QR
  * PLGMAGONE-346: Add support for pre-filled gender/dob fields in Klarna/Pay After Delivery
  * PLGMAGONE-195: House number extension added when OneStepCheckout is used
  * PLGMAGONE-356: Support direct transactions for ING/KBC
  * PLGMAGONE-362: Update ING Home'Pay name within backend configuration
  * PLGMAGONE-341: Don't add payment fee twice to credit memo
  * PLGMAGONE-331: Add handling of chargeback status
  * PLGMAGONE-354: Add iDEAL QR gateway
  * PLGMAGONE-343: Don't update an order when it's closed (due to offline refund)
  * PLGMAGONE-337: Add check to only update order status when order exists
  * PLGMAGONE-338: Undefined index error on expired orders
  * PLGMAGONE-357: Update ING gateway to `INGHOME`
  * PLGMAGONE-340: Prevent cancel on api error when order has already been paid
  * PLGMAGONE-342: Fixes headers already send error when card payment gateway is used
  * PLGMAGONE-336: Undefined index `custom_refund_desc`

  ***

  **2.3.6**\
  Release date: Nov 7, 2017\
  **Fixes**

  * PLGMAGONE-326: add daysactive/secondsactive for Klarna/Pay After Delivery
  * PLGMAGONE-327: Removed Klarna quote loading to prevent infinite loop
  * PLGMAGONE-159: Removed unused reverted status configurations
  * PLGMAGONE-323: Allow different billing/shipping addresses, reverted PLGMAG-304
  * PLGMAGONE-329: Fixed sorting on min/max amounts
  * PLGMAGONE-96: Restricted currencies used are now loaded from the correct store
  * PLGMAGONE-313: *selecteer uw credit card* is now translatable
  * PLGMAGONE-33: Added support for AliPay
  * PLGMAGONE-96: Improvements to currency restriction in cards/gateways
  * PLGMAGONE-96: Restricted currencies used are now loaded from the correct store

  ***

  **2.3.5**\
  Release date: Oct 23, 2017\
  **Fixes**

  * Fixed an issue causing a double iDEAL issuer selection.

  ***

  **2.3.4**\
  Release date: Aug 3, 2017\
  **Fixes**

  * Fixed issue trying to get property of non-object payment\_data.
  * Fixed issue where manual orders could be placed with decimals.
  * Fixed PLGMAGONE-132. Some undefined index notices got fixed.
  * Fixes PLGMAG-304. Only allow Klarna when billing and shipping address are the same (Klarna regulation).
  * Fixed issues with the Givacard gateway.
  * Fixed PLGMAGONE-105: getShippingAmount zero leads to NAN tax table.
  * Fixes an issue with de credit card gateway not processing the brand.

  **Improvements**

  * Added missing logo used for the card payment method option.
  * Updated the install script.
  * Updated Bancontact logo and title.
  * Removed Thumbs.db from the package.
  * Added delivery info to Pay After Delivery/Klarna requests.
  * Fixes PLGMAGONE-311 and PLGMAGONE-312. Added gateway codes for Paysafecard and American Express.

  **Features**

  * Added support for Paysafecard.
  * Added support for Belfius.
  * Added support for KBC/CBC.
  * Added support for ING Home'Pay.
  * Add customizable description to refund request.
  * Support for Seconds Active PLGMAGONE-259.

  ***

  **2.3.3**\
  Release date: Feb 16, 2017\
  **Fixes**

  * Resolved PHP7 deprecated warnings occurring in the MultiSafepay class file.

  ***

  **2.3.2**\
  Release date: Jan 25, 2017\
  **Fixes**

  * Removed whitespace which resulted in the PHP error "headers already sent" being triggered when selecting the card gateway
  * Resolved an issue when used with OneStepCheckout causing the wrong gateway to be used.

  ***

  **2.3.0**\
  Release date: Oct 12, 2016\
  **Improvements**

  * Added EPS and FerBuy as payment methods.
  * iDEAL issuer list alignment improved.
  * Added official support for the FastCheckout product feed v1.0
  * Added some missing German translations for Klarna.

  **Fixes**

  * Fixed an issue related product quantity when partially refunding Klarna payments.

  **Changes**

  * Changed the YourGift logo.

  ***

  **2.2.9**\
  Release date: Aug 10, 2016

  **Improvements**

  * Status requests are now logged in multisafepay.log when debug option is enabled.

  **Fixes**

  * Resolved an issue where invoices aren't being generated.

  ***

  **2.2.8**\
  Release date: June 21, 2016

  **Improvements**

  * Added E-Invoicing.
  * Payment links are now only requested when creating new orders in the Magento backend, not when editing an order, resulting in a new order.

  **Fixes**

  * Fixed an undefined notice within the logs.
  * Resolved an issue resulting in the transaction data not being set, such as; parent\_id and additional\_information

  **Changes**

  * Updated Bancontact image
  * Changed the iDEAL issuer selection from dropdown to radio buttons with the bank's logo.

  ***

  **2.2.7**\
  Release date: May 26, 2016\
  **Improvements**

  * Added logging of refund requests.
  * The currency is now retrieved from the order when creating a credit memo and refunding, rather than from the store.
  * Added support for Fast Checkout product feed.
  * Improvements were made to the confirmation page URL.
  * Added improvements for the refunding of foreign currencies.

  **Fixes**

  * Resolved undefined notices.
  * Resolved issues when refunding orders that have discounts.
  * Resolved a bug when using webshop gift card.
  * Resolved the doubled shippingtax bug causing incorrect invoice and/or credit memo amounts.

  **Changes**

  * Removed the refunding of fees.

  ***

  **2.2.6**\
  Release date: March 10, 2016\
  **Fixes**

  * Resolved incorrect tax amount visible in the invoice when using a fee.

  ***

  **2.2.5**\
  Release date: March 4, 2016\
  **New features**

  * Added Dotpay as payment method.

  **Improvements**

  * Invoices now show the correct payment method.

  **Fixes**

  * Resolved issues preventing orders from being opened once paid with PayPal or Bank transfer.
  * Resolved error code 1035 occurring when refunding.
  * Resolved credit memo issues.
  * The total order amount of orders paid with Fast Checkout now include the shipping costs.

  ***

  **2.2.2**\
  Release date: Dec 28, 2015\
  **Improvements**

  * If paid amount difference from total order amount. A note is added with extra info. No invoice is created.
  * Added (incl Tax) to totals line to make it more clear as other lines can be set in tax totals settings. Also added this for the frontend.
  * Added configurable FastCheckout field for phone number.

  **Fixes**

  * Fixes undefined `configMain` notice.
  * Added missing `klarna.phtml`
  * In case an order is paid by Second Chance and an other payment method is used as the initial, the order will be updated with the correct payment method.
  * Fixes bug with direct debit using a wrong gateway code
  * Fixes for wrong credit memo amounts that are processed.
  * Fixes Store id is now used to get the correct store URLs to redirect to
  * Fixes cancelled status for Pay After Delivery and Klarna notifications are now ignored as the order was already set to Paid. If set to cancelled then a credit memo can't be created anymore.
  * Fixes bug causing the order status set to "payment review" instead of "processing". This was caused because the order total had to be rounded to two so it matches the paid amount in the transaction.

  **2.2.1**\
  Release date: Nov 12, 2015\
  **New features**

  * Payment fee can now be refunded
  * Added min/max amount restrictions for all gateways.

  **Improvements**

  * Added Klarna to the language file.

  **Fixes**

  * Fixed undefined variable `isAllowConvert` notice.
  * Fixed undefined variable `Currencies` notice.
  * Fixed issue using wrong `StoreConfig`.
  * Fixed issue when selecting all the available currencies in the configuration.
  * Fixed issue using the wrong account credentials for FastCheckout.
  * Fixed issue causing shipping method not to be correct for Klarna and Pay After Delivery.
  * Fixed issue which prevented accepting gender, bank account and date of birth twice when using Klarna.
  * Fixed issue which resulted in 1 cent mismatch when using Klarna on older Magento installations.

  ***

  **2.2.0**\
  Release date: Aug 20, 2015\
  **New features**

  * Added Klarna as payment method.
  * gift card now have their own API key configuration.
  * Refunds now work for Klarna, Coupons and Pay After Delivery.
  * Success page now visible when using a payment link or pay using Second Chance.
  * FastCheckout button now also language based.
  * Fallback to configured gateway code if gateway is not available within the quote.
  * Fallback if issuer is set but no gateway, then somehow we lost the gateway although iDEAL was selected. We now default to iDEAL.
  * Added Beauty and Wellness gift card.
  * Added Sport\&Fit gift card.
  * Added VVV gift card.
  * Added PODIUM gift card.
  * Added missing Gifcard logos.
  * All available currencies can be selected when configuring the gateway.
  * Added option to remove all buttons to the normal checkout for when only FastCheckout is enabled.

  **Improvements**

  * Updated order of FastCheckout in menu.
  * MultiSafepay menu added.
  * Separated some configurations.

  **Changes**

  * Disabled gift card Ebon.
  * Return-URL's are now always ending with only /success/ for better support for GUA module.
  * Disabled FastCheckout payment method in normal checkout as this is causing confusion for merchants.
  * Don't set state to cancelled when partial refunded as it still has to be processed partially.
  * Disabled some gift cards that are for one merchant.
  * Added FastCheckout button on login/register page.
  * Redirect URL always added for Pay After Delivery.
  * Check for stock settings before processing stock.
  * Now use current selected currency to recalculate fee. Fee is always configured in EUR.
  * Removed old package file.
  * Removed unused code.
  * Set checkout session to be used instead of core for storing issuer data.
  * Update xmlescape function.

  **Fixes**

  * Fixed Store name from order is used for manual paylink, not the admin site.
  * Fixed some undefined fields causing a Notice error when PHP use a STRICT error logging.
  * Fixed success URL for Direct Bank transfer (Request to Pay).
  * Fixed some issues with the customer groups selected in the configuration of the gateways.
  * Fixed prices including tax (Solved error 1027).
  * Fixed some encoding issue.
  * Fixed When sending the order confirmation after a payment, then this is ignored for a Bank transfer.
  * Fixed fee now displayed correctly when using multi-currency.
  * Fixed bug with gift card data and delivery data.

  ***

  **2.1.2**\
  Release date: May 7th, 2015\
  **Improvements**

  * Payment links generated in the Magento Admin for manually created orders now use the `Daysactive` setting in the main plugin configuration.
  * The transaction status 'Expired' no longer triggers the plugin to cancel orders with an invoice.

  **Changes**

  * The 'Keep Cart Alive' plugin setting has been enabled by default.
  * The 'Keep Cart Alive' plugin setting now only works for MultiSafepay payment methods.
  * Fast Checkout no longer creates an order for an expired order

  **Fixes**

  * 'Allowed currencies' for the MultiSafepay Gateways were not requested correctly.
  * Added delivery address data to orders for PayPal's Sellers Protection.
  * Call to undefined method error occurring with the Pay After Delivery object
  * Payment links generated in the Magento backend for manually created orders always used the test environment
  * Fixed double payment method titles
  * Resolved DIRECT banking gateway code bug
  * Magento didn't always update and store the amount correctly when converting from USD to EUR resulting in the wrong amount paid after the plugin conversion.
  * The Pay After Delivery (MultiFactor) rejection message has been added to the language files.
  * The Pay After Delivery (MultiFactor) rejection message has been altered to only show relevant information to customers.
  * Available payment methods are no longer shown when the visibility has been limited to specified user groups.
  * The plugin processes the refund status and closes the order if the credit memo option isn't enabled when creating a credit memo

  ***

  **2.1.1**\
  Release date: Mar 20, 2015\
  **Fixes**

  * Fixed bug for outline gateway images

  ***

  **2.1.0**\
  Release date: Mar 19, 2015\
  **New features**

  * Coupons now use their own gateway settings so that multiple - MultiSafepay accounts can be used to support multiple MultiSafepay coupons
  * Add a refund transaction to the Magento transactions order overview on refund or partial refund
  * Support for partial refunds
  * Special status for initialized Bank transfer transactions
  * Added support for fixed fee and/or percentage fee for each gateway
  * Show Pay After Delivery rejection notice within the store when transaction is rejected
  * Added enable/disable configuration value for FastCheckout product feed
  * Feed action. Feed can be requested at `/msp/standard/feed/`
  * Enable/disable configuration option check is now added. Check is also added for API key to check if the given key matches the configured key
  * Order now using translation files
  * Added `updateInvoice` function. Send Magento invoice ID to MultiSafepay, this will be added to the accountant export
  * Added `daysactive` to connect
  * When creating an order we now use the selected payment method for the manual transaction request
  * Payment link added to a manually created order by an admin. When an admin creates an order manually, we will create a transaction request for it and add the payment link to the order. The merchant now doesn't need to Sign in to the E-wallet and manually create a payment link for the order

  **Improvements**

  * If there is an invoice, the order can't be cancelled anymore
  * Added more language files
  * Better support for Keep Cart alive, so it is compatible with OneStepCheckout
  * Added check for - phone number for BNO trans. Compatibility with some OneStepCheckout modules that add - when phone number is empty or not available as custom field
  * Check if payment is object, if not, default to standard gateway model This will solve the 1016 error message
  * Manual payment link process has changed. Updated the observer. The payment link is now only added when the order is being created from the Magento Admin and no longer on every save action within the Magento Admin
  * If title isn't added then fallback tot main gateway title
  * Updated upgrade script
  * Updated `bno.phtml` for better layout in OneStepCheckout
  * Better support for gateway images. Works with `default`, `onestepcheckout.com` and `Apptha` checkout
  * Removed disable option for text titles
  * Disabled check for active table rates configuration. This was old code from when this was configured within the FastCheckout configuration
  * Transaction errors for normal transaction request now also result in a closed order
  * Added extra check for enabled fee for the payment method
  * After transaction error with DIRECT Pay After Delivery transactions we will close the order because replacing using another payment method will create a new order
  * When status is refunded just return OK and exit. The Magento plugin can process partial refunds so we should ignore refunded status because this can update the order wrong with partial refunds. Status updates are done by creating the credit memo
  * Added fallback for refund status for when new `base.php` is used with older releases
  * Added transaction details to the transaction record that is created when creating an invoice automatically
  * Added default configuration to the plugin that sets the fee after the shipping cost in the totals overviews
  * Rewrite of the refund API integration. The implementation was wrong and causing every MultiSafepay refunded to be processed online. This supposed to be a choice by order to refund online. Merchants can now refund online when it's enabled within the configuration and by going to the invoice, click credit memo and then refund. Then can choose to refund, or refund offline where the refund offline won't submit the refund to MultiSafepay

  **Changes**

  * Removed fijncadeau references

  **Fixes**

  * Fixed bug for coupon settings
  * Fixed bug for ordering same pages with different options results in an error 1027
  * Pay After Delivery option for sending invoice email. When enabled resulted in NOT sending and vice-versa
  * Fixed bug Maintransaction ID errors when auto redirect is enabled with direct iDEAL
  * Reset fee before trying to set it. Solves issue with some installations not resetting, resulting in fee from other selected payment method
  * Added extra `setQuote` to solve issues reported by one merchant where Magento didn't add the quote correctly to the order. To solve this bug with Magento, we set the quote manually within the order
  * Fixed bug with payment details to be added to the transaction record. Payment details are now stored again within the transaction record
  * Fixed bug with unpaid invoices when completed
  * Fixed issue to treat order status cancelled or cancelled (American vs English) the same correct way
  * Fixed bug that caused product from a manually created order to be in the cart for the customer that the order was created for when the customer returns to the store and logs in
  * Fixed bug with paid status
  * When creating an invoice, Magento gets the `totalPaid` value and add it to the total invoiced value. When we don't create an invoice automatically, we set the `totalPaid` to inform the merchant that the order was paid. This resulted in a double `totalPaid` value because Magento added the invoiced total to the `totalPaid` when manually creating the invoice. This is now changed so that we reset the Total Paid in this situation just before the invoice is created and Magento updates the `totalPaid` again

  ***

  **2.0.2**\
  Release date: Oct 10, 2014\
  **Improvements**

  * Added an option to set the daysactive for an Pay After Delivery transaction. When not payed in time, the transaction will expired and the webshop will be notified
  * Added extra line to set the order total to paid if it hasn't been done
  * Now use the fee price formatter so it includes the selected currency
  * Force ordertotal set to paid when transaction is completed and invoice creation is disabled. Only show creation of transaction note once.
  * Added version number to configuration title line.
  * Textual improvements.
  * Better check on order confirmation email sending.
  * Rrecalculate the product price without tax as Magento round at 2 decimals by default and we use 4. This resulted in a amount mismatch when ordering larger quantities of the same product.
  * Better support for special chars.
  * Enabled locking again but return false instead of showing error and exit. This should avoid duplicate invoices when callback is called while before the redirect\_url set the order status.

  **Changes**

  * FEE base is rewritten.
  * Upgrade the PHP dependence to 5.5.1\*\*2.
  * Now get the selected gateway from the quote instead of the gateway model. This adds better compatibility with third-party OneStepCheckout plugins.

  **Fixes**

  * Fixed bug for error #1016 on the Return-URL.
  * Fixed bug with gateway title not being visible in checkout.
  * Fixed bug with missing house number on connect transactions.
  * Fixed bug with order email not being sent after transaction complete.
  * Fixed bug with double `totalPaid` amount.

  ***

  **2.0.0**\
  Release date: May 20, 2014\
  **Improvements**

  * Added support for refunds from out of the backend of the webshop
  * Fast Checkout now use the Magento Shipping methods
  * When the order status of an Pay After Delivery order in the webshop is set to 'Shipped', the status of the transaction is also changed in the MultiSafepay backend.
  * Currency not supported by MultiSafepay can now be converted to euro's.
  * Program structure of the plugin changed to the standard Magento convention.
  * Added support for Fashion-cheque.
  * Added support for Liefcadeaukaart.
  * Added support in the configuration for minimal order amount for iDEAL.
  * Added (limited) support for Magento Connect package (Only for new installations, not for an update from an older version of plugin).

  **Changes**

  * The 'Solve fee bug' setting has been removed from the configuration. This is fixed in the software.
  * The gateway `Fijncadeau` is deleted because it is no longer available.
  * Transaction-ID is added to the redirect URL, for the case that our system doesn't.
  * Disable log for status-request to avoid large log files.
  * Lock file system disabled.

  **Fixes**

  * Fixed bug in the American Express configuration.
  * Fixed 500 error when developers mode is enabled and iDEAL is selected without bank pre-selection.
  * Fixed bug with images in checkout.
  * Fixed bug with currency for separate gateway's.
  * Fixed bug with the language.
  * The additional fee is removed by normal operation.(Bug reported in v1.4.4).
  * Fixed memory limit bug cause by recursion in the `Payafter.php` model.
  * Fixed undefined index notices.

  ***

  **1.4.4**\
  Release date: Apr 28, 2014\
  **Improvements**

  * Better support for OneStepCheckout.
  * Better support for Apptha OneStepCheckout.

  **Fixes**

  * fixed bug with total amount when using conversion.
  * Fixed bug with autocreate invoice.
  * Fixed bug with double fee calculation.
  * Fixed bug with fee by payments other than Pay After Delivery.

  ***

  **1.4.3**\
  Release date: Apr 8, 2014\
  **Improvements**

  * Filtering for special characters in XML.
  * Added option to show the Pay After Delivery fee incl or excl tax during checkout, without changing calculations.
  * Added Pay After Delivery template for direct Pay After Delivery transaction request.
  * Added American Express as payment method.
  * Added max amount for some gateways.

  **Changes**

  * Always get first IP address for customer IP and forwarded IP that it finds within the given value.
  * Create invoice after payment has been completed, Magento changed things, if invoice isn't created then the order is processing with unpaid status.
  * Changed `default/template/msp/default.phtml` files. This provides gateway html for other gateways other then MultiSafepay.
  * Removed house number feature. If house number isn't available after parse the address then we use street2.
  * Changed the way how discounts are processed.
  * Change store name for connect transactions.
  * No more redirect to `checkoutcontroller` for FastCheckout transactions. All is done from within the `standardcontroller`. This solves 302 and 307 offline action errors.

  **Fixes**

  * Google checkout bug fix.
  * Fixed bug with configurable product only show the correct pages and don't show up twice in pages listing.
  * Fixed bug with order data.
  * Fixed return to empty cart page when offline actions are slow.
  * fixed issue on error 503 in offline actions. No need to fill in account details in 3 different places.
  * Fixed bug with direct debit and SOFORT Banking.
  * Fixed bug with empty return-url.

  ***

  **1.4.2**\
  Release date: Feb 4, 2014\
  **Fixes**

  * Invoice emails are now send correctly when using Magento 1.8.1
  * Better support for Pay After Delivery

  ***

  **1.4.1**\
  Release date: Sep 19, 2013\
  **Improvements**

  * Support for free shipping method
  * Fee configurable option for the amount.
  * HTML instructions support for connect Gateway
  * Support for the OneStepCheckout house number feature. This function separates the address and house number, with this option enabled Pay After Delivery would fail on missing data.
  * Amount validation check. If the quote amount is not equal to the order amount the transaction creation will stop to prevent an underpaid order.
  * Currency selection support for each separate gateway. Now you can select the currencies that are supported, the gateway will only be visible with the selected currencies.
  * Degrotespeelgoedwinkel coupon as supported gateway
  * Support for gateway descriptions per gateway. You can also use html within the description field to add nice gateway descriptions.
  * Configurable `multisafepay servicekosten` label for Pay After Delivery. This label can now be changed
  * Support for gateway images. Option to select only an image, the title, or both.
  * Support for void, declined and expire status codes in combination with CANCELLED STATE.

  **Changes**

  * Direct e-banking is now SOFORT Banking
  * Moved the fee line within the order totals table to above the tax
  * The Fee tax description so it uses the configured label
  * Disabled discontinued Fijncadeau coupon card
  * Fooman surcharge fix no longer applies. To avoid confusion this is removed from the package.

  **Fixes**

  * Wrong fee percentage for BNO Tax
  * Disable visibility for the (old) notification URL
  * Language was missing by use of Fast Checkout
  * Bank selection was always visible with iDEAL, even when the option was disabled.
  * Parfumcadeaukaart coupon is now working correctly
  * 'The cart is not equal' is now solved for normal checkout as the one step checkout.
  * When no fee is active the service cost's won't be visible.

  ***

  **1.3.3**\
  Release date: Mar 26, 2013\
  **Improvements**

  * Added an 'send order status update email' option
  * Added an option to keep the cart active
  * Added override for the order submit function. Now we can keep the cart active when a customer cancelled the order.
  * Added the Fast Checkout method to the normal checkout process
  * Added creation of an account within the store when a customer uses Fast Checkout.
  * Better UTF-8 compatibility for Fast Checkout to prevent error 1000 messages.

  ***

  **1.3.2**\
  Release date: Mar 10, 2013\
  **Improvements**

  * Added Pay After Delivery support
  * Added an extra check to that an invoice won't be created twice
  * Added bank\_id check
  * Better one step checkout compatibility with iDEAL issuer selection

  **Changes**

  * Updated Gateway template for direct banking.
  * Removed the Invoice observer to avoid problems with invoice creation. The observer activated an update function that isn't needed.
  * Updated the default Fast Checkout logo

  **Fixes**

  * Fixed bug iDEAL issuers list with production environment.
  * Fixed bug registered bank\_id bug, now we have a select your bank option to avoid errors when customers forget to select a bank.
  * Fixed bug for empty order status when an order was cancelled.
  * Fixed bug that caused a duplicate transaction request
  * Fixed store\_id bug.
  * Fixed bug that cause useless Notification notices within the error logs.

  ***

  **1.3.1**\
  Release date: Jan 10, 2013\
  **Improvements**

  * `DirectXML` for Bank transfer.

  ***

  **1.3.0**\
  Release date: Dec 10, 2012\
  **Improvements**

  * `DirectXML` for iDEAL.

  ***

  **1.2.9**\
  Release date: Jan 12, 2011\
  **Improvements**

  * New order email option is active, you can now set when you want to send the order emails.
  * New feature added that allows for reopening cancelled orders. If a cancelled order got paid by using Second Chance etc, the order will be processed again and an invoice is created etc.
  * Added gateways for ebon, baby gift card, boekenbon, erotiekbon, fijncadeau, webshopcard, parfumnl, parfumcadeaukaart.

  **Fixes**

  * Quantity didn't got updated correct when some statusses got processed.
  * Fix bug that allowed the processing of the same status multiple times. Check added so that a status will only be processed once.

  ***

  **1.2.8**\
  **Improvements**

  * STATE\_CANCELED changed to STATE\_PENDING due to Second Chance.

  **Fixes**

  * Cancelled Orders will now actually be cancelled.

  ***

  **1.2.7**\
  **Improvements**

  * Better handling of manual invoice creation.
  * Extra lock check that if an error occurs the status message is Not OK.
  * use\_shipping\_notification set to false to overcome issue with "Cannot send order to **Specified** country.

  **Fixes**

  * Cancelled Orders will now actually be cancelled.

  ***

  **1.2.6**\
  **Improvements**

  * Send email on Processing (instead of initial).
  * Manual create invoices for orders.
  * Payment Overview Cancelled status for: Void, Declined & Expired.

  [Top of page](#)

  ***
</details>

# Prerequisites

* [MultiSafepay account](/docs/getting-started-guide/)
* Magento Open Source 1.7 - 1.9
* Tested on PHP 7.0

# Installation

These instructions are for SFTP upload. You can also install via .ZIP file upload in Connect.

  **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Unpack the content of the .ZIP file in the root of your webshop.\
   **⚠️Note:** When upgrading to a newer version of your plugin, always make sure to remove all outdated plugin files and folders.
2. Sign in to your Magento 1 <Glossary>backend</Glossary>.
3. Go to **System** > **Configuration** > **Cache**, and clear your invalid cache.
4. Move all files and folders from Plugin\_Magento\_x.x.x to the root.
5. Add the content of the app, lib, and media folders to the existing folders with the same name.
6. Sign out.

# Configuration

1. Sign in to your Magento 1 backend.
2. Go to **System** > **Configuration** > **MultiSafepay x.x.x** > **Connect settings**.\
   This page contains all main settings and is used for all <Glossary>gateways</Glossary> and gift cards.
   To find your API key, see [API key](/docs/sites#site-id-api-key-and-security-code).
   From version 3.0.0, the plugin only needs your API key. Your account ID, website ID, and website security code are no longer needed.
3. To configure your selected payment methods, go to **System** > **Configuration** > **MultiSafepay x.x.x**:
   * **Connect MultiSafepay gateways**
     * **MultiSafepay gift cards**\
       Make sure you have [activated the payment methods](/docs/payment-methods/) in your MultiSafepay dashboard.\ <br />

***

# User guide

## BNPL orders

The status of all complete orders automatically changes to **Shipped** in order to collect funds from <Glossary>BNPL</Glossary> methods.

<details id="how-to-disable-klarna-checkout-fields">
  <summary>How to disable Klarna checkout fields</summary>

  <br />

  Klarna requires the customer's gender and date of birth. By default, the customer enters their birthday in the Magento checkout in the Klarna payment method fields, and their gender is automatically populated by the core Magento field.

  You can disable both fields in the checkout. The customer enters this information on the MultiSafepay payment page instead.

  **Disabling Klarna checkout fields**

  This change is only for Magento developers. We recommend testing the change and placing it in your local folder.

  1. Open `app\code\community\MultiSafepay\Msp\Model\Gateway\Klarna.php`.
  2. Comment this line `protected $_formBlockType = 'msp/klarna';`
  3. Save the file.
  4. Clear your cache.
  5. Test the change.
</details>

## Checkouts

The plugin is compatible with most Magento 1 checkouts. However, we cannot guarantee that all checkout features will function properly.

We test the plugin with Magento 1 core checkout and OneStepCheckout.com (`Idev`).

  **💡 Tip!** Always test OneStepCheckout to make sure it is compatible with your configuration of the plugin.

## Currencies

The default currency is EUR.

<details id="how-to-change-the-default-currency">
  <summary>How to change the default currency</summary>

  <br />

  1. Sign in to your Magento 1 backend.
  2. Go to **System** > **Configuration** > **MultiSafepay x.x.x** > **Connect settings**.
  3. Under **Allow currency conversion to Euro**, change to **No**.
</details>

## Generic gateways

The plugin supports generic gateways, which allows you to add a payment method manually. This is particularly useful for integrating gift cards specific to your business.

Supported since release: 3.1.0, June 15th 2021.

<details id="how-to-configure-generic-gateways">
  <summary>How to configure generic gateways</summary>

  <br />

  1. Sign in to your Magento 1 backend.
  2. Go to **System** > **Configuration** > **MultiSafepay** > **Connect gateways** > **Generic 1/2/3**.
  3. Set the relevant [payment method gateway IDs](/reference/gateway-ids/) and the gateway label.
  4. Set how to display the payment method logos.
  5. For <Glossary>BNPL</Glossary> orders, set whether to include the shopping cart.
</details>

## Payment methods

<details id="supported-payment-methods">
  <summary>Supported payment methods</summary>

  <br />

  * Cards: [All](/docs/card-payments/) except V Pay
  * Banking methods: All, **except** TrustPay
  * <Glossary>BNPL</Glossary>: All
  * Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
  * Prepaid cards:
    * Beauty and Wellness gift card
    * <a href="https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon" target="_blank">Boekenbon</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.fashioncheque.com/nl" target="_blank">Fashioncheque</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.fashion-giftcard.nl" target="_blank">Fashion gift card</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * Fietsenbon
    * <a href="https://www.gezondheidsbon.nl/mhome" target="_blank">Gezondheidsbon</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.good4fun.nl" target="_blank">Good4fun</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.nationale-tuinbon.nl" target="_blank">Nationale tuinbon</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.parfumcadeaukaart.nl" target="_blank">Parfumcadeaukaart</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * [Paysafecard](/docs/paysafecard/)
    * <a href="https://www.podiumcadeaukaart.nl" target="_blank">Podium</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.sportenfitcadeau.nl" target="_blank">Sport en Fit</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.vvvcadeaukaarten.nl" target="_blank">VVV gift card</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.webshopgiftcard.nl" target="_blank">Webshop gift card</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.wellnessgiftcard.nl" target="_blank">Wellness gift card</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * Wijncadeau
    * <a href="https://www.winkelcheque.nl" target="_blank">Winkelcheque</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
    * <a href="https://www.yourgift.nl" target="_blank">Yourgift</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />
</details>

## Picquer

<details id="how-to-enable-compatibility-with-picquer">
  <summary>How to enable compatibility with Picquer</summary>

  <br />

  To make the MultiSafepay Magento 1 plugin compatible with Picqer, follow two additional steps, because orders must not receive **Cancelled** status.

  1. In your Magento 1 backend, go to the MultiSafepay Connect settings.
  2. Link **Expired** status to **Waiting** status.
  3. Open `app\code\community\MultiSafepay\Msp\Model\Base.php`, and then copy the file to the local folder in the Magento structure.
  4. Find the line `$order > cancel();` at the expired signal and remove it.

  All expired orders retain **Waiting** status until you cancel them:

  * Manually
  * With a custom cronjob
  * Using a plugin
</details>

## Recurring payments

[Recurring payments](/docs/recurring-payments) are supported.

<details id="how-to-enable-recurring-payments">
  <summary>How to enable recurring payments</summary>

  <br />

  1. Sign in to your Magento 1 backend.
  2. Go to **Stores** > **Configuration** > **MultiSafepay** > **MultiSafepay settings**.

  **Card payments**

  Recurring Payments are not available for the generic card payments gateway. You must enable the Visa, Mastercard, and/or Maestro gateways separately. This displays the **Save card** option at checkout.
</details>

## Refunds

<details id="refund-rules">
<summary>Refund rules</summary>
<br>

| Platform | Details |
|---|---|
| MultiSafepay dashboard | Full refunds (may not appear in your backend) |
| Backend | Full refunds and <a href="https://docs.magento.com/m1/ce/user_guide/order-processing/credit-memo-create.html" target="_blank">credit memos</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> <br> You can't refund more than the original amount |
| <<glossary:BNPL>> orders | You can only refund a selected item from the order, not a set amount. If you enter an amount instead of selecting an item, the entire order is refunded. |

  <Table>
    <thead>
      <tr>
        <th>
          Platform
        </th>
        <th>
          Details
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>
          MultiSafepay dashboard
        </td>
        <td>
          Full refunds (may not appear in your backend)
        </td>
      </tr>
      <tr>
        <td>
          Backend
        </td>
        <td>
          Full refunds and <a href="https://docs.magento.com/m1/ce/user_guide/order-processing/credit-memo-create.html" target="_blank">credit memos</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> <br /> You can't refund more than the original amount
        </td>
      </tr>
      <tr>
        <td>
          <Glossary>BNPL</Glossary>
          orders
        </td>
        <td>
          You can only refund a selected item from the order, not a set amount. If you enter an amount instead of selecting an item, the entire order is refunded.
        </td>
      </tr>
    </tbody>
  </Table>
</details>

<details id="how-to-process-backend-refunds">
  <summary>How to process backend refunds</summary>

  <br />

  1. Sign in to your Magento 1 backend.
  2. Go to **System** > **Configuration** > **MultiSafepay** > **Connect settings**.
  3. Check that you have:
     * Entered an API key
     * Enabled the **Credit Memo** option
  4. Search for and open the order you want to refund.
  5. Click the **Invoices** tab on the left of the **Order overview**.
  6. Open the invoice, and click **Credit memo** at the top right of the overview.
  7. Enter the refund amount, and then click **Refund online** to send the request to MultiSafepay.
</details>

## Surcharges

You can:

* Apply [surcharges](/docs/surcharges/) of a percentage or a fixed amount to transactions for every payment method.
* Set the tax class for surcharges.
* Show transaction amounts excluding the surcharge at checkout. Surcharges are always included at checkout.
* Show surcharges with our without VAT at checkout.

<details id="how-to-apply-surcharges-with-third-party-add-ons">
  <summary>How to apply surcharges with third-party add-ons</summary>

  <br />

  1. Sign in to your Magento 1 backend.
  2. Select systems and configuration.
  3. In the MultiSafepay module, select the **Option connect** gateway.
  4. Select the relevant payment method.
  5. Under **Payment fee amount**, enter a surcharge percentage or fixed amount.
  6. Place a test order to verify whether the fee has been correctly processed.
</details>

> ⚠️ Attention Dutch merchants
>
> We strongly recommend **not** applying surcharges to <Glossary>BNPL</Glossary> orders. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

## Updates

You can update the plugin in your Magento 1 backend or the CMS marketplace, or via SFTP.

<details id="how-to-update-via-sftp">
  <summary>How to update via SFTP</summary>

  <br />

    **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

  1. Download the plugin again above.
  2. Follow the Installation and configuration instructions from step 2.
</details>

## Upgrades

Magento 1 is end-of-life. If you are still running Magento 1, action is required. MultiSafepay has partnered with Mage One to continue supporting Magento 1.

For more information and instructions, see MultiSafepay blog – <a href="https://bit.ly/2YX2LGL" target="_blank">Magento 1: The final weeks</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.\ <br />

***

<blockquote className="callout callout_info">
  <h3 className="callout-heading false">
    <span className="callout-icon">💬</span>
    <p>Support</p>
  </h3>
  <p>Contact MultiSafepay:</p>
  <ul>
    <li>
      Telephone: <a href="tel:+310208500500">+31 (0)20 8500 500</a>
    </li>
    <li>
      Email: <a href="mailto:integration@multisafepay.com">integration@multisafepay.com</a>
    </li>
  </ul>
</blockquote>

[Top of page](#)
