---
title : "Magento 1"
category: 62962dd7e272a6002ebbbbc5
order: 111
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Free plugin to integrate MultiSafepay payment solutions with Magento 1."
slug: 'magento-1'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Magento.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<details id="changelog">
<summary>Changelog</summary>
<br>

**3.1.3**
Release date: Nov. 24th, 2021

**Fixed**
- PLGMAGONE-736: Fix invalid method backendOrdersAllowed on backend orders

---

**3.1.2**
Release date: Nov. 23rd, 2021

**Fixed**
- PLGMAGONE-734: Fix unable to create backend orders (items not showing)
- PLGMAGONE-735: Fix conflict with service cost and non MultiSafepay plugins

---

** 3.1.1**
Release date: Sep 16, 2021

**Fixed**
- PLGMAGONE-730: Use correct invoice id when order is being updated to shipped
- PLGMAGONE-731: Remove unused tax tables which could generate wrong taxes

---

**3.1.0**
Release date: Jun 15, 2021

**Added**
- PLGMAGONE-710: Add support for [Generic Gateways](#generic-gateways) which can be used for branded gift cards
- PLGMAGONE-627: Add order number variable support to custom refund description

**Fixed**
- PLGMAGONE-719: Prevent a zero amount refund leading to a full refund
- PLGMAGONE-706: Show payment instructions for giftcards too

**Changed**
- DAVAMS-344: Update Trustly logo

---

**3.0.0**
Release date: Oct 21, 2020

**Added**
- DAVAMS-234: Add in3
- DAVAMS-262: Add CBC payment method
- PLGMAGONE-699: Add Good4fun Giftcard

**Fixed**
- PLGMAGONE-678: Fix bug in calculating correct price and tax for Fooman surcharge
- PLGMAGONE-671: Fix maximum nesting level error with Idev OneStepCheckout
- PLGMAGONE-668: Fix non working days/seconds_active for backend orders

**Changed**
- PLGMAGONE-634: Switch from XML API to JSON API (Only API key is needed)
- PLGMAGONE-472: Set order to status shipped for all payment methods
- PLGMAGONE-674: Always set redirect_url
- DAVAMS-28: Rebrand Santander Betaalplan to Pay per Month
- DAVAMS-295: Rebrand Direct Bank Transfer to Request to Pay
- DAVAMS-308: Rebrand Klarna to Klarna - buy now, pay later
- Update payment method names
  - KBC
  - ING Home'Pay
  - Credit card
  - Pay After Delivery
  - E-Invoicing

---  

**2.6.0**
Release date: Apr 2, 2020

**Added**
- PLGMAGONE-617: Add Apple Pay
- PLGMAGONE-656: Add Direct Bank Transfer (Request to Pay)
- PLGMAGONE-485: Add support for Fooman Surcharge
- PLGMAGONE-562: Added support for PostNL pickup points for AfterPay.

**Fixed**
- PLGMAGONE-654: Fix incorrect character set for translations
- PLGMAGONE-621: Fix layout issue when OneStepCheckout is used
- PLGMAGONE-588: Fix missing site secure code in refund request
- PLGMAGONE-572: Fixed payment fee description not being set
- PLGMAGONE-526: Fixed undefined variable recurring on E_STRICT mode
- PLGMAGONE-458: Count gives warning when PHP 7.2 is used

**Changed**
- PLGMAGONE-599: Hide Pay After Delivery when shipping address differs
- PLGMAGONE-574: Prevent orders to be cancelled when set to processing
- Update translations for "select your credit card"

---

**2.5.1**
Release date: Mar 25, 2019

**Added**
- PLGMAGONE-457: Added Handelsbanken iDEAL issuer logo
- PLGMAGONE-406: Added support for Modman

**Changed**
- PLGMAGONE-344: Enable refund shipping amount when shipping includes tax

**Fixed**
- PLGMAGONE-465: Fixed service costs not showing with some third-party modules
- PLGMAGONE-456: Fixed service costs not working on clean installation
- PLGMAGONE-448: Fixed Qwindo does not work in compiled mode
- PLGMAGONE-431: Fixed notice "undefined index" on invoice creation

---

**2.5.0**
Release date: Sept 21, 2018
**Features**
- PLGMAGONE-339: Add Tokenization
- PLGMAGONE-411: Added support for E-Invoice gateway for manually created orders

**Fixes**
PLGMAGONE-429: Corrected Paysafecard gateway for manually created orders

---

**2.4.2**
Release date: Jun 15, 2018

**Fixed**
- PLGMAGONE-384: Log refund errors to order notes
- PLGMAGONE-391: Fix undefined variable in error log when refund exception occurs
- PLGMAGONE-374: Update Dutch translations

---

**2.4.1**
Release date: May 25, 2018

**Added**
- PLGMAGONE-378: Add support for Santander Betaal per Maand
- PLGMAGONE-379: Add support for AfterPay
- PLGMAGONE-380: Add support for Trustly
- PLGMAGONE-381: Add Moneyou iDEAL issuer logo

**Fixed**
- PLGMAGONE-377: Uncaught error when saving empty grouped product while Qwindo was active
- PLGMAGONE-382: Gateway ING not changed everywhere to INGHOME

---

**2.4.0**
Release date: Mar 12, 2018
**Fixes**
- Add support for Qwindo
- PLGMAGONE-370: Updated Dutch translations
- PLGMAGONE-369: Update Klarna payment method logo
- PLGMAGONE-368: Add keep cart alive for ING Home'Pay, Belfius, KBC and iDEAL QR
- PLGMAGONE-346: Add support for prefilled gender/dob fields in Klarna/Pay After Delivery
- PLGMAGONE-195: Housenumber extension added when Onestepcheckout is used
- PLGMAGONE-356: Support direct transactions for ING/KBC
- PLGMAGONE-362: Update ING Home'Pay name within backend configuration
- PLGMAGONE-341: Don't add payment fee twice to credit memo
- PLGMAGONE-331: Add handling of chargeback status
- PLGMAGONE-354: Add iDEAL QR gateway
- PLGMAGONE-343: Don't update an order when it's closed (due to offline refund)
- PLGMAGONE-337: Add check to only update order status when order exists
- PLGMAGONE-338: Undefined index error on expired orders
- PLGMAGONE-357: Update ING gateway to INGHOME
- PLGMAGONE-340: Prevent cancel on api error when order has already been paid
- PLGMAGONE-342: Fixes headers already send error when credit card gateway is used
- PLGMAGONE-336: Undefined index custom_refund_desc

---

**2.3.6**
Release date: Nov 7, 2017
**Fixes**
- PLGMAGONE-326: add daysactive/secondsactive for Klarna/Pay After Delivery
- PLGMAGONE-327: Removed Klarna quote loading to prevent infinite loop
- PLGMAGONE-159: Removed unused reverted status configurations
- PLGMAGONE-323: Allow different billing/shipping addresses, reverted PLGMAG-304
- PLGMAGONE-329: Fixed sorting on min/max amounts
- PLGMAGONE-96: Restricted currencies used are now loaded from the correct store
- PLGMAGONE-313: _selecteer uw credit card_ is now translatable
- PLGMAGONE-33: Added support for AliPay
- PLGMAGONE-96: Improvements to currency restriction in cards/gateways
- PLGMAGONE-96: Restricted currencies used are now loaded from the correct store

---

**2.3.5**
Release date: Oct 23, 2017
**Fixes**
- Fixed an issue causing a double iDEAL issuer selection.

---

**2.3.4**
Release date: Aug 3, 2017
**Fixes**
- Fixed issue trying to get property of non-object payment_data.
- Fixed issue where manual orders could be placed with decimals.
- Fixed PLGMAGONE-132. Some undefined index notices got fixed.
- Fixes PLGMAG-304. Only allow Klarna when billing and shipping address are the same (Klarna regulation).
- Fixed issues with the Givacard gateway.
- Fixed PLGMAGONE-105: getShippingAmount zero leads to NAN tax table.
- Fixes an issue with de credit card gateway not processing the brand.

**Improvements**
- Added missing logo used for the credit card payment method option.
- Updated the install script.
- Updated Bancontact logo and title.
- Removed Thumbs.db from the package.
- Added delivery info to Pay After Delivery/Klarna requests.
- Fixes PLGMAGONE-311 and PLGMAGONE-312. Added gateway codes for Paysafecard and American Express.

**Features**
- Added support for Paysafecard.
- Added support for Belfius.
- Added support for KBC/CBC.
- Added support for ING Home'Pay.
- Add customizable description to refund request.
- Support for Seconds Active PLGMAGONE-259.

---

**2.3.3**
Release date: Feb 16, 2017
**Fixes**
- Resolved PHP7 deprecated warnings occuring in the MultiSafepay class file.

---

**2.3.2**
Release date: Jan 25, 2017
**Fixes**
- Removed whitespace which resulted in the PHP error "headers already sent" being triggered when selecting the credit card gateway
- Resolved an issue when used with OneStepCheckout causing the wrong gateway to be used.

---

**2.3.0**
Release date: Oct 12, 2016
**Improvements**
- Added EPS and FerBuy as payment methods.
- iDEAL issuerlist alignment improved.
- Added official support for the FastCheckout productfeed v1.0
- Added some missing German translations for Klarna.

**Fixes**
- Fixed an issue related product quantity when partially refunding Klarna payments.

**Changes**
- Changed the YourGift logo.

---

**2.2.9**
Release date: Aug 10, 2016

**Improvements**
- Status requests are now logged in multisafepay.log when debug option is enabled.

**Fixes**
- Resolved an issue where invoices aren't being generated.

---

**2.2.8**
Release date: June 21, 2016

**Improvements**
- Added E-Invoicing.
- Payment links are now only requested when creating new orders in the Magento backend, not when editing an order, resulting in a new order.

**Fixes**
- Fixed an undefined notice within the logs.
- Resolved an issue resulting in the transactional data not being set, such as; parent_id and additional_information

**Changes**
- Updated Bancontact image
- Changed the iDEAL issuer selection from dropdown to radio buttons with the bank's logo.

---

**2.2.7**
Release date: May 26, 2016
**Improvements**
- Added logging of refund requests.
- The currency is now retrieved from the order when creating a credit memo and refunding, rather than from the store.
- Added support for Fast Checkout product feed.
- Improvements were made to the confirmation page URL.
- Added improvements for the refunding of foreign currencies.

**Fixes**
- Resolved undefined notices.
- Resolved issues when refunding orders that have discounts.
- Resolved a bug when using webshop gift card.
- Resolved the doubled shippingtax bug causing incorrect invoice and/or credit memo amounts.

**Changes**
- Removed the refunding of fees.

---

**2.2.6**
Release date: March 10, 2016
**Fixes**
- Resolved incorrect tax amount visible in the invoice when using a fee.

---

**2.2.5**
Release date: March 4, 2016
**New features**

- Added Dotpay as payment method.

**Improvements**
- Invoices now show the correct payment method.

**Fixes**
- Resolved issues preventing orders from being opened once paid with PayPal or Bank transfer.
- Resolved error code 1035 occurring when refunding.
- Resolved credit memo issues.
- The total order amount of orders paid with Fast Checkout now include the shipping costs.

---

**2.2.2**
Release date: Dec 28, 2015
**Improvements**
- If paid amount difference from total order amount. A note is added with extra info. No invoice is created.
- Added (incl Tax) to totals line to make it more clear as other lines can be set in tax totals settings. Also added this for the frontend.
- Added configurable FastCheckout field for phone number.

**Fixes**
- Fixes undefined configMain notice.
- Added missing klarna.phtml
- In case an order is paid by Second Chance and an other payment method is used as the initial, the order will be updated with the correct payment method.
- Fixes bug with directdebit using a wrong gateway code
- Fixes for wrong credit memo amounts that are processed.
- Fixes Store id is now used to get the correct store URL's to redirect to
- Fixes cancelled status for Pay After Delivery and Klarna notifications are now ignored as the order was already set to Paid. If set to cancelled then a credit memo can't be created anymore.
- Fixes bug causing the order status set to "payment review" instead of "processing". This was caused because the order grandtotal had to be rounded to two so it matches the paid amount in the transaction.


**2.2.1**
Release date: Nov 12, 2015
**New features**
- Payment fee can now be refunded
- Added min/max amount restrictions for all gateways.

**Improvements**
- Added Klarna to the language file.

**Fixes**
- Fixed undefined variable isAllowConvert notice.
- Fixed undefined variable Currencies notice.
- Fixed issue using wrong StoreConfig.
- Fixed issue when selecting all the available currencies in the configuration.
- Fixed issue using the wrong account credentials for FastCheckout.
- Fixed issue causing shipping method not to be correct for Klarna and Pay After Delivery.
- Fixed issue which prevented accepting gender, bank account and date of birth twice when using Klarna.
- Fixed issue which resulted in 1 cent mismatch when using Klarna on older Magento installations.

---

**2.2.0**
Release date: Aug 20, 2015
**New features**
- Added Klarna as payment method.
- gift card now have their own API key config.
- Refunds now work for Klarna, Coupons and Pay After Delivery.
- Success page now visible when using a payment link or pay using Second Chance.
- FCO button now also language based.
- Fallback to configured gateway code if gateway is not available within the quote.
- Fallback if issuer is set but no gateway, then somehow we lost the gateway although iDEAL was selected. We now default to iDEAL.
- Added Beauty and Wellness gift card.
- Added Sport&Fit gift card.
- Added VVV gift card.
- Added PODIUM gift card.
- Added missing Gifcard logos.
- All available currencies can be selected when configuring the gateway.
- Added option to remove all buttons to the normal checkout for when only FCO is enabled.

**Improvements**
- Updated order of FastCheckout in menu.
- MultiSafepay menu added.
- Separated some configurations.

**Changes**
- Disabled gift card Ebon.
- Return-URL's are now always ending with only /success/ for better support for GUA module.
- Disabled FastCheckout payment method in normal checkout as this is causing confusion for merchants.
- Don't set state to cancelled when partial refunded as it still has to be processed partially.
- Disabled some gift cards that are for one merchant.
- Added FCO button on login/register page.
- Redirect URL always added for Pay After Delivery.
- Check for stock settings before processing stock.
- Now use current selected currency to recalculate fee. Fee is always configured in EUR.
- Removed old package file.
- Removed unused code.
- Set checkout session to be used instead of core for storing issuer data.
- Update xmlescape function.

**Fixes**
- Fixed Store name from order is used for manual paylink, not the admin site.
- Fixed some undefined fields causing a Notice error when PHP use a STRICT error logging.
- Fixed success URL for Direct Bank transfer (Request to Pay).
- Fixed some issues with the customer groups selected in the configuration of the gateways.
- Fixed prices including tax (Solved error 1027).
- Fixed some encoding issue.
- Fixed When sending the order confirmation after a payment, then this is ignored for a Bank transfer.
- Fixed fee now displayed correctly when using multi-currency.
- Fixed bug with gift card data and delivery data.

---

**2.1.2**
Release date: May 7th, 2015
**Improvements**
- Paymentlinks generated in the Magento Admin for manually created orders now use the 'Daysactive' setting in the main plugin configuration.
- The transaction status 'Expired' no longer triggers the plugin to cancel orders with an invoice.

**Changes**
- The 'Keep Cart Alive' plugin setting has been enabled by default.
- The 'Keep Cart Alive' plugin setting now only works for MultiSafepay payment methods.
- Fast Checkout no longer creates an order for an expired order

**Fixes**
- 'Allowed currencies' for the MultiSafepay Gateways were not requested correctly.
- Added delivery address data to orders for PayPal's Sellers Protection.
- Call to undefined method error occuring with the Pay After Delivery object
- Paymentlinks generated in the Magento backend for manually created orders always used the test environment
- Fixed double payment method titles
- Resolved DIRECTebanking gateway code bug
- Magento didn't always update and store the amount correctly when converting from USD to EUR resulting in the wrong amount paid after the plugin conversion.
- The Pay After Delivery (MultiFactor) rejection message has been added to the language files.
- The Pay After Delivery (MultiFactor) rejection message has been altered to only show relevant information to customers.
- Available payment methods are no longer shown when the visibility has been limited to specified user groups.
- The plugin processes the refund status and closes the order if the credit memo option isn't enabled when creating a credit memo

---

**2.1.1**
Release date: Mar 20, 2015
**Fixes**
- Fixed bug for outline gateway images

---

**2.1.0**
Release date: Mar 19, 2015
**New features**
- Coupons now use their own gateway settings so that multiple - MultiSafepay accounts can be used to support multiple MultiSafepay coupons
- Add a refund transaction to the Magento transactions order overview on refund or partial refund
- Support for partial refunds
- Special status for initialized Bank transfer transactions
- Added support for fixed fee and/or percentage fee for each gateway
- Show Pay After Delivery rejection notice within the store when transaction is rejected
- Added enable/disable config value for FCO product feed
- Feed action. Feed can be requested at /msp/standard/feed/
- Enable/disable config option check is now added. Check is also added for API key to check if the given key matches the configured key
- Order now using translation files
- Added updateInvoice function. Send Magento invoice ID to MultiSafepay, this will be added to the accountant export
- Added daysactive to connect
- When creating an order we now use the selected payment method for the manual transaction request
- Payment link added to a manually created order by an admin. When an admin creates an order manually, we will create a transaction request for it and add the payment link to the order. The merchant now doesn't need to Sign in to the Ewallet and manually create a payment link for the order

**Improvements**
- If there is an invoice, the order can't be cancelled anymore
- Added more language files
- Better support for Keep Cart alive, so it is compatible with Onestepcheckout
- Added check for - phone number for BNO trans. Compatibility with some Onestepcheckout modules that add - when phone number is empty or not available as custom field
- Check if payment is object, if not, default to standard gateway model This will solve the 1016 error message
- Manual payment link process has changed. Updated the observer. The payment link is now only added when the order is being created from the Magento Admin and no longer on every save action within the Magento Admin
- If title isn't added then fallback tot main gateway title
- Updated upgrade script
- Updated bno.phtml for better layout in OneStepCheckout
- Better support for gateway images. Works with default, onestepcheckout.com and Apptha checkout
- Removed disable option for text titles
- Disabled check for active table rates config. This was old code from when this was configured within the FCO configuration
- Transaction errors for normal transaction request now also result in a closed order
- Added extra check for enabled fee for the payment method
- After transaction error with DIRECT Pay After Delivery transactions we will close the order because replacing using another payment method will create a new order
- When status is refunded just return ok and exit. The Magento plugin can process partial refunds so we should ignore refunded status because this can update the order wrong with partial refunds. Status updates are done by creating the credit memo
- Added fallback for refund status for when new base.php is used with older releases
- Added transaction details to the transaction record that is created when creating an invoice automatically
- Added default config to the plugin that sets the fee after the shipping cost in the totals overviews
- Rewrite of the refund API integration. The implementation was wrong and causing every MultiSafepay refunded to be processed online. This supposed to be a choice by order to refund online. Merchants can now refund online when it's enabled within the configuration and by going to the invoice, click credit memo and then refund. Then can choose to refund, or refund offline where the refund offline won't submit the refund to MultiSafepay

**Changes**
- Removed fijncadeau references

**Fixes**
- Fixed bug for coupon settings
- Fixed bug for ordering same pages with different options results in an error 1027
- Pay After Delivery option for sending invoice email. When enabled resulted in NOT sending and vice-versa
- Fixed bug Maintransaction ID errors when auto redirect is enabled with direct iDEAL
- Reset fee before trying to set it. Solves issue with some installations not reseting, resulting in fee from other selected payment method
- Added extra setQuote to solve issues reported by one merchant where Magento didn't add the quote correctly to the order. To solve this bug with Magento, we set the quote manually within the order
- Fixed bug with payment details to be added to the transaction record. Payment details are now stored again within the transaction record
- Fixed bug with unpaid invoices when completed
- Fixed issue to treat order status cancelled or cancelled (American vs English) the same correct way
- Fixed bug that caused product from a manually created order to be in the cart for the customer that the order was created for when the customer returns to the store and logs in
- Fixed bug with paid status
- When creating an invoice, Magento gets the totalpaid value and add it to the total invoiced value. When we don't create an invoice automatically, we set the totalpaid to inform the merchant that the order was paid. This resulted in a double totalPaid value because Magento added the invoiced total to the totalPaid when manually creating the invoice. This is now changed so that we reset the Total Paid in this situation just before the invoice is created and Magento updates the totalPaid again

---

**2.0.2**
Release date: Oct 10, 2014
**Improvements**
- Added an option to set the daysactive for an Pay After Delivery transaction. When not payed in time, the transaction will expired and the webshop will be notified
- Added extra line to set the order total to paid if it hasn't been done
- Now use the fee price formatter so it includes the selected currency
- Force ordertotal set to paid when transaction is completed and invoice creation is disabled. Only show creation of transaction note once.
- Added version number to config title line.
- Textual improvements.
- Better check on order confirmation email sending.
- Rrecalculate the product price without tax as Magento round at 2 decimals by default and we use 4. This resulted in a amount mismatch when ordering larger quantities of the same product.
- Better support for special chars.
- Enabled locking again but return false instead of showing error and exit. This should avoid duplicate invoices when callback is called while before the redirect_url set the order status.

**Changes**
- FEE base is rewritten.
- Upgrade the php dependence to 5.5.1**2.
- Now get the selected gateway from the quote instead of the gateway model. This adds better compatibility with third-party onestepcheckout plugins.

**Fixes**
- Fixed bug for error #1016 on the Return-URL.
- Fixed bug with gateway title not being visible in checkout.
- Fixed bug with missing house number on connect transactions.
- Fixed bug with order email not being sent after transaction complete.
- Fixed bug with double totalPaid amount.

---

**2.0.0**
Release date: May 20, 2014
**Improvements**
- Added support for refunds from out of the backend of the webshop
- Fast Checkout now use the Magento Shipping methods
- When the order status of an Pay After Delivery order in the webshop is set to 'Shipped', the status of the transaction is also changed in the MultiSafepay backend.
- Currency not supported by MultiSafepay can now be converted to euro's.
- Programm structure of the plugin changed to the standard Magento convention.
- added support for Fashion-cheque.
- added support for Lief cadeaukaart.
- added support in the configuration for minimal order amount for iDEAL.
- added (limited) support for Magento Connect package (Only for new installations, not for an update from an older version of plugin).

**Changes**
- The 'Solve fee bug' setting has been removed from the configuration. This is fixed in the software.
- The gateway 'Fijncadeau' is deleted because it is no longer available.
- Transaction-ID is added to the redirect URL, for the case that our system doesn't.
- disable log for status-request to avoid large log files.
- lockfile systeem disabled.

**Fixes**
- Fixed bug in the American Express config.
- Fixed 500 error when developers mode is enabled and iDEAL is selected without bank preselection.
- Fixed bug with images in checkout.
- Fixed bug with currency for separate gateway's.
- Fixed bug with the language.
- The additional fee is removed by normal operation.(Bug reported in v1.4.4).
- Fixed memory limit bug cause by recursion in the Payafter.php model.
- Fixed undefined index notices.

---

**1.4.4**
Release date: Apr 28, 2014
**Improvements**
- Better support for OneStepCheckout.
- Better support for Apptha OneStepCheckout.

**Fixes**
- fixed bug with total amount when using conversion.
- Fixed bug with autocreate invoice.
- Fixed bug with double fee calculation.
- Fixed bug with fee by payments other than Pay After Delivery.

---

**1.4.3**
Release date: Apr 8, 2014
**Improvements**
- Filtering for special characters in XML.
- Added option to show the Pay After Delivery fee incl or excl tax during checkout, without changing calculations.
- Added Pay After Delivery template for direct Pay After Delivery transaction request.
- Added American Express as payment method.
- Added max amount for some gateways.

**Changes**
- Always get first IP address for customer IP and forwarded IP that it finds within the given value.
- Create invoice after payment has been completed, Magento changed things, if invoice isn't created then the order is processing with unpaid status.
- Changed default/template/msp/default.phtml files. This provides gateway html for other gateways other then MultiSafepay.
- Removed house number feature. If house number isn't available after parse the address then we use street2.
- Changed the way how discounts are processed.
- Change store name for connect transactions.
- No more redirect to checkoutcontroller for FCO transactions. All is done from within the standardcontroller. This solves 302 and 307 offline action errors.

**Fixes**
- Google checkout bug fix.
- Fixed bug with configurable product only show the correct pages and don't show up twice in pages listing.
- Fixed bug with order data.
- Fixed return to empty cart page when offline actions are slow.
- fixed issue on error 503 in offline actions. No need to fill in account details in 3 different places.
- Fixed bug with directdebit and SOFORT Banking.
- Fixed bug with empty return-url.

---

**1.4.2**
Release date: Feb 4, 2014
**Fixes**
- Invoice emails are now send correctly when using Magento 1.8.1
- Better support for Pay After Delivery

---

**1.4.1**
Release date: Sep 19, 2013
**Improvements**
- Support for free shipping method
- Fee configurable option for the amount.
- HTML instructions support for connect Gateway
- Support for the onestepcheckout house number feature. This function seperates the address and house number, with this option enabled Pay After Delivery would fail on missing data.
- Amount validation check. If the quote amount is not equal to the order amount the transaction creation will stoped to prevent an underpaid order.
- Currency selection support for each separate gateway. Now you can select the currencies that are supported, the gateway will only be visible with the selected currencies.
- Degrotespeelgoedwinkel coupon as supported gateway
- Support for gateway descriptions per gateway. You can also use html within the description field to add nice gateway descriptions.
- Configurable 'multisafepay servicekosten' label for Pay After Delivery. This label can now be changed
- Support for gateway images. Option to select only an image, the title, or both.
- Support for void, declined and expire status codes in combination with CANCELLED STATE.

**Changes**
- Direct e-banking is now SOFORT Banking
- Moved the fee line within the order totals table to above the tax
- The Fee tax description so it uses the configured label
- Disabled discontinued Fijncadeau coupon card
- Fooman surcharge fix no longer applies. To avoid confusion this is removed from the package.

**Fixes**
- Wrong fee percentage for BNO Tax
- Disable visibility for the (old) notification URL
- Language was missing by use of Fast Checkout
- Bank selection was alway visible with iDEAL, even when the option was disabled.
- Parfumcadeaukaart coupon is now working correctly
- 'The cart is not equal' is now solved for normal checkout as the one step checkout.
- When no fee is active the service cost's won't be visible.

---

**1.3.3**
Release date: Mar 26, 2013
**Improvements**
- Added an 'send order status update email' option
- Added an option to keep the cart active
- Added override for the order submit function. Now we can keep the cart active when a customer cancelled the order.
- Added the Fast Checkout method to the normal checkout process
- Added creation of an account within the store when a customer uses Fast Checkout.
- Better UTF-8 compatibility for Fast Checkout to prevent error 1000 messages.

---

**1.3.2**
Release date: Mar 10, 2013
**Improvements**
- Added Pay After Delivery support
- Added an extra check to that an invoice won't be created twice
- Added bank_id check
- Better one step checkout compatibility with iDEAL issuer selection

**Changes**
- Updated Gateway template for direct banking.
- Removed the Invoice observer to avoid problems with invoice creation. The observer activated an update function that isn't needed.
- Updated the default Fast Checkout logo

**Fixes**
- Fixed bug iDEAL issuers list with production environment.
- Fixed bug registered bank_id bug, now we have a select your bank option to avoid errors when customers forget to select a bank.
- Fixed bug for empty order status when an order was cancelled.
- Fixed bug that caused a duplicate transaction request
- Fixed store_id bug.
- Fixed bug that cause useless Notification notices within the error logs.

---

**1.3.1**
Release date: Jan 10, 2013
**Improvements**
- DirectXML for Bank transfer.

---

**1.3.0**
Release date: Dec 10, 2012
**Improvements**
- DirectXML for iDEAL.

---

**1.2.9**
Release date: Jan 12, 2011
**Improvements**
- New order email option is active, you can now set when you want to send the order emails.
- New feature added that allows for reopening cancelled orders. If a cancelled order got paid by using Second Chance etc, the order will be processed again and an invoice is created etc.
- Added gateways for ebon, baby gift card, boekenbon, erotiekbon, fijncadeau, webshopcard, parfumnl, parfumcadeaukaart.

**Fixes**
- Quantity didn't got updated correct when some statusses got processed.
- Fix bug that allowed the processing of the same status multiple times. Check added so that a status will only be processed once.

---

**1.2.8**
**Improvements**
- STATE_CANCELED changed to STATE_PENDING due to Second Chance.

**Fixes**
- Cancelled Orders will now actually be cancelled.

---

**1.2.7**
**Improvements**
- Better handling of manual invoice creation.
- Extra lock check that if an error occurs the status message is Not OK.
- use_shipping_notification set to false to overcome issue with "Cannot send order to **Specified** country.

**Fixes**
- Cancelled Orders will now actually be cancelled.

---

**1.2.6**
**Improvements**
- Send email on Processing (instead of initial).
- Manual create invoices for orders.
- Payment Overview Cancelled status for: Void, Declined & Expired.

___
</details>

> [Download](https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/magento1/Plugin_Magento_3.1.3.zip) :arrow-down:

:warning: Magento 1 is end-of-life. We recommend [upgrading as soon as possible](/magento-1/#upgrading).

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with Magento 1.

MultiSafepay supports most Magento functionalities. For any questions, email <integration@multisafepay.com>

<details id="requirements">
<summary>Requirements</summary>
<br>

- [MultiSafepay account](/getting-started/guide/)
- Magento Open Source 1.7 - 1.9
- Tested on PHP 7.0

</details>

<details id="support">
<summary>Support</summary>
<br>

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue
- [Magento Slack channel](https://magentocommeng.slack.com) #multisafepay-payments

Our Magento 1 plugin is professionally supported by a certified Magento 1 Solution Specialist and receives regular updates to support the latest features provided by Magento and MultiSafepay.

</details>

# Installation

These instructions are for SFTP upload. You can also install via .ZIP file upload in Connect.

:warning: Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Unpack the content of the .ZIP file in the root of your webshop.
2. Sign in to your Magento 1 backend.
3. Go to **System** > **Configuration** > **Cache**, and clear your invalid cache.
4. Move all files and folders from Plugin_Magento_x.x.x to the root.  
5. Add the content of the app, lib, and media folders to the existing folders with the same name.
6. Sign out.

# Configuration
1. Sign in to your Magento 1 backend.
2. Go to **System** > **Configuration** > **MultiSafepay x.x.x** > **Connect settings**.  
    This page contains all main settings and is used for all gateways and gift cards.  
    To find your API key, see [API key](/websites/#site-id-api-key-and-secure-code).  
    From version 3.0.0, the plugin only needs your API key. Your account ID, site ID, and site secure code are no longer needed.
3. To configure your selected payment methods, go to **System** > **Configuration** > **MultiSafepay x.x.x**:
    - **Connect MultiSafepay gateways**  
    - **MultiSafepay gift cards**  
    Make sure you have [activated the payment methods](/activating-payment-methods/) in your MultiSafepay dashboard.

# User guide

## Checkouts

The plugin is compatible with most Magento 1 checkouts. However, we cannot guarantee that all checkout features will function properly.

We test the plugin with Magento 1 core checkout and OneStepCheckout.com (Idev).

**Note:** Always test OneStepCheckout to make sure it is compatible with your configuration of the plugin.

## Currencies

The default currency is EUR. 

<details id="changing-the-default-currency">
<summary>Changing the default currency</summary>
<br>

1. Sign in to your Magento 1 backend. 
2. Go to **System** > **Configuration** > **MultiSafepay x.x.x** > **Connect settings**.
3. Under **Allow currency conversion to Euro**, change to **No**.

</details>

## Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/payment-pages/). This is particularly useful for integrating gift cards.

<details id="configuring-generic-gateways">
<summary>Configuring generic gateways</summary>
<br>

1. Sign in to your Magento 1 backend. 
2. Go to **System** > **Configuration** > **MultiSafepay** > **Connect gateways** > **Generic 1/2/3**.
3. Set the relevant [payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids) and the gateway label.
4. Set how to display the payment method logos. 
5. For pay later methods, set whether to include the shopping cart.

</details>

## Pay later orders

The status of all complete orders automatically changes to **Shipped** in order to collect funds from pay later payment methods.

<details id="disabling-klarna-checkout-fields">
<summary>Disabling Klarna checkout fields</summary>
<br>

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

## Payment methods

<details id="payment-methods">
<summary>Payment methods</summary>
<br>

- Cards: [All](/credit-debit-cards/) except V Pay
- Banking methods: [All](/banks/), **except** TrustPay
- Pay later methods: [All](/pay-later/)
- Wallets: [Alipay](/alipay), [Apple Pay](/apple-pay), [PayPal](/paypal)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Good4fun](https://www.good4fun.nl)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/paysafecard)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl)

</details>

## Picquer

<details id="enabling-compatibility-with-picquer">
<summary>Enabling compatibility with Picquer</summary>
<br>

To make the MultiSafepay Magento 1 plugin compatible with Picqer, follow two additional steps, because orders must not receive **Cancelled** status.

1. In your Magento 1 backend, go to the MultiSafepay Connect settings.
2. Link **Expired** status to **Waiting** status.
2. Open `app\code\community\MultiSafepay\Msp\Model\Base.php`, and then copy the file to the local folder in the Magento structure.
3. Find the line `$order > cancel();` at the expired signal and remove it.

All expired orders retain **Waiting** status until you cancel them:

- Manually
- With a custom cronjob 
- Using a plugin

</details>

## Recurring payments

<details id="enabling-recurring-payments">
<summary>Enabling recurring payments</summary>
<br>

1. Sign in to your Magento 1 backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay** > **MultiSafepay settings**.

For more information, see [Recurring Payments](/recurring-payments).

**Credit cards**
Recurring Payments are not available for the generic credit card gateway. You must enable the Visa, Mastercard, and/or Maestro gateways separately. This displays the **Save card** option at checkout.

</details>

## Refunds
<details id="refund-rules">
<summary>Refund rules</summary>
<br>

| | |
|---|---|
| MultiSafepay dashboard | Full refunds (may not appear in your backend) |
| Backend | Full refunds and [credit memos](https://docs.magento.com/m1/ce/user_guide/order-processing/credit-memo-create.html) <br> You can't refund more than the original amount |
| Pay later methods | You can only refund a selected item from the order, not a set amount. If you enter an amount instead of selecting an item, the entire order is refunded. |

</details>

<details id="processing-backend-refunds">
<summary>Processing backend refunds</summary>
<br>

1. Sign in to your Magento 1 backend. 
2. Go to **System** > **Configuration** > **MultiSafepay** > **Connect settings**.
3. Check that you have:
    - Entered an API key
    - Enabled the **Credit Memo** option
4. Search for and open the order you want to refund.
5. Click the **Invoices** tab on the left of the **Order overview**.
6. Open the invoice, and click **Credit memo** at the top right of the overview.
7. Enter the refund amount, and then click **Refund online** to send the request to MultiSafepay.

</details>

## Surcharges

You can:

- Apply [surcharges](/surcharges/) of a percentage or a fixed amount to transactions for every payment method.
- Set the tax class for surcharges.
- Show transaction amounts excluding the surcharge at checkout. Surcharges are always included at checkout.
- Show surcharges with our without VAT at checkout.

<details id="applying-surcharges-with-third-party-add-ons">
<summary>Applying surcharges with third-party add-ons</summary>
<br>

1. Sign in to your Magento 1 backend.
2. Select systems and configuration.
3. In the MultiSafepay module, select the **Option connect** gateway.
4. Select the relevant payment method.
5. Under **Payment fee amount**, enter a surcharge percentage or fixed amount. 
6. Place a test order to verify whether the fee has been correctly processed.

</details>

> ⚠️ **Attention Dutch merchants** 
> We strongly recommend **not** applying surcharges to [pay later methods](/pay-later/). This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

## Updates

You can update the plugin in your Magento 1 backend or the CMS marketplace, or via SFTP.

<details id="updating-via-sftp">
<summary>Updating via SFTP</summary>
<br>

:warning: Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.

</details>

## Upgrading

Magento 1 is end-of-life. If you are still running Magento 1, action is required. MultiSafepay has partnered with Mage One to continue supporting Magento 1. 

For more information and instructions, see MultiSafepay blog – [Magento 1: The final weeks](https://bit.ly/2YX2LGL).