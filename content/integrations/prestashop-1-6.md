---
title: "PrestaShop 1.6"
category: 62962dd7e272a6002ebbbbc5
order: 11
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'prestashop-1-6'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/PrestaShop.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/prestashop-1.6-internal/releases/download/3.9.0/Plugin_PrestaShop_1_6_3.9.0.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

> ⚠️ Action required
>
> We are phasing out support for this plugin. We recommend migrating to our [PrestaShop 1.7 plugin](/docs/prestashop-1-7/) as soon as possible.

# Changelog

<details id="changelog">
<summary>Changelog</summary>
<br>

## 3.9.0
Release date: Dec 7th, 2022

### Changed
- Removed extra confirmation step in the checkout
- Component and tokenization configurations have been moved from global level, to payment method level settings. Please make sure configuration is still correct by navigating to **Modules > Module Manager > Select your payment method**
- It is now possible to upload modules in the PrestaShop backend
- All payment methods modules only can be activated when MultiSafepay main module is installed
- Re-brand AfterPay to Riverty

### Added
- MyBank
- Google Pay
- Alipay
- Alipay+
- Add checkout modal for direct payment methods

### Removed
- Erotiekbon
- Fietsenbon
- Givacard
- Goodcard
- Kelly gift card
- Nationale Verwen cadeaubon
- Winkelcheque
- ING Home'Pay
- Parfumcadeaukaart

---

**3.8.1**
Release date: Sep 28, 2022

**Fixed**
- PLGPRSS-455: Generic gateway code not used

---

**3.8.0**
Release date: Jul 13, 2022

**Added**
- PLGPRSS-427: Add 3 generic gateways

**Fixed**
- PLGPRSS-426: Fix invalid post data when using free shipping discount

**Changed**
- PLGPRSS-435: Update MultiSafepay branding and payment icons
- PLGPRSS-413: Remove separate API key for Pay After Delivery

---

**3.7.1**
Release date: Jan 7, 2022

**Changed**
PLGPRSS-423: Rename client class to MultiSafepayClient to avoid conflict with third party modules

---

**3.7.0**
Release date: Nov 25, 2021

**Added**
- DAVAMS-232: Add support for in3 payment method
- PLGPRSS-420: Add payment component support for cards
- PLGPRSS-409: Add support for gift card in the shopping_cart object
- PLGPRSS-406: Add support for Good4fun gift card

**Fixed**
- PLGPRSS-414: Fix locale code when submitting the create order request, which was generating errors where the customer's payment address code was different from the language selected

**Changed**
- PLGPRSS-408: When a payment is cancelled, the shopping_cart is no longer emptied
- DAVAMS-314: Add new Klarna logo
- DAVAMS-298: Re-brand direct bank transfer as Request to Pay

---

**3.6.0**
Release date: Jul 21, 2020

**Added**
- DAVAMS-269: Add CBC payment method

**Changed**
- DAVAMS-213: Add track & trace to shipment request
- PLGPRSS-404: Set order to status shipped for all payment methods

---

**3.5.0**
Release date: Apr 9, 2020

**Added**
- PLGPRSS-344: Add AfterPay

**Fixed**
- PLGPRSS-396: Correct spelling of ING Home'Pay
- PLGPRSS-397: Fix incorrect gateway code for ING Home'Pay

---

**3.4.0**
Release date: Apr 2, 2020

**Added**
- PLGPRSS-400: Add Apple Pay
- PLGPRSS-399: Add Direct Bank Transfer (Request to Pay)

---

**3.3.0**
Release date: Feb 26, 2020

**Fixed**
- PLGPRSS-309: Prevent multiple transactions being created for the same order
- PLGPRSS-391: Prevent duplicated orders by adding file locking
- PLGPRSS-267: Mobile presentation of payment methods is not fully responsive

**Changed**
- PLGPRSS-190: Send shopping cart data for all payment methods
- PLGPRSS-352: Improve parsing of address into street and apartment

---

**3.2.0**
Release date: Nov 8, 2017

**Improvements**
- Add gift card Givacard.
- Error-messages are now showed according to the PrestaShop guidelines.
- Order Confirmation screen now also contains the order information.
- Changed the layout for gateways during checkout (iDEAL, Pay After Delivery, Klarna, E-Invoice, Bank transfer).
- Module descriptions are now uniform.
- Critical debug- and error messages are added to the PrestaShop-Logger, whether or not the debug function in the module is enabled.
- Tokenization is included.
- Some small ### Changes to the styling.
- Update translations.
- Changed the way and address is split into street and house number.

**Fixes**
- In some situations, the cart was accidentally emptied.
- The order-confirmation screen was also showed for non-MultiSafepay payment methods.

**Changes**
- Removed the configuration option for by-passing the order-confirmation screen. This because the order-confirmation screen is default PrestaShop behavior and mandatory for some payment methods.
- Removed the configuration option for HTTP or HTTPS since this was added in the past for one merchant having some issues.
- Removed the lock mechanism in the offline-action script. Since this was unnecessary.

---

**3.1.7**
Release date: Sept 8, 2017

**Improvements**
- Add ING Home'Pay as payment method.
- Add BKC as payment method.
- Add Belfius as payment method.
- Update Dutch translation-files.
- Resized all payment logos.
- Removed underscore in the name of all gift cards.
- Adjust birth date to correct layout for Klarna and Pay After Delivery.
- Removed own `order-confirmation.tpl` and use PrestaShop default.

**Fixes**
- Customer is now correct redirected to the order-confirmation page.
- Check whether or not update order status failed sometimes.
- Confirmation-form for Paysafecard was not loaded due to a misspelled filename.
- When using the Connect gateway the button for 'All payment methods' was not available.
- Shipping methods where selected based on language-code instead of country-code.
- When using the credit cards gateway the customer wasn't redirected to the correct payment page.
- In exceptional cases no order was created due to an invalid security-key.
- FastCheckout failed in updating the order status.
- FastCheckout did not support Free shipping.
- Transaction-ID was not always included in the order.
- Free Shipping information was not included in the transaction.

**Changes**
- Removed support for BVKPayment for FastCheckout. as this can configured within your MultiSafepay dashboard.

---

**3.1.5**
Release date: May 12, 2017

**Improvements**
- New logo for Mastercard.
- Add Paysafecard as payment method.

**Fixes**
- Order confirmation screen is now also showed when option 'Moment of order creation' is set to 'After order is paid in full'
- The system will try for maximal 10 seconds to check if transaction is paid.
- If failed (for example Bank transfer) the order history page is showed as fallback.
- Fixed issue for support of BVKPayment module.

---

**3.1.4**
Release date: Dec 20, 2016

**Improvements**
- MultiSafepay notices and error messages are now shown in the webshop (front-end).
- Added input field placeholders for the payment methods Klarna and Pay After Delivery.

**Fixes**
- Added a lock mechanism to prevent the creation of duplicate orders due to multiple Notification URL calls taking place in quick succession.

**Changes**
- Removed option 'After checkout completed' under the 'at what moment should the order be created' setting, as this option is identical to the 'After order confirmation' option.
- Date of birth provide in the webshop for Klarna and/or E-Invoice is carried over to the Payment page.
- Resolved unnecessary debug message #1006 being logged when creating transactions.

---

**3.1.2**
Release date: Nov 23, 2016

**Improvements**
- Added full support for BVK payment fees module; percentages, fixed amounts and combinations are supported.
- Added bundled gift card payment method; the separate gateways Visa, Mastercard, Maestro and American Express are not visible during checkout.
- Added some translation ### Improvements
- Add extra option in the configuration to select the HTTP / HTTPS protocol to use for Offline Actions.
- Added EPS.
- Added FerBuy.
- Errors are now shown on the PrestaShop storefront.

**Fixes**
- Multiple free shipping methods are now shown correctly instead of just one.
- Fixed issue where the customer was redirected to the order history page instead of the order-confirmation page.

**Changes**
- Removed option 'After checkout completed' under the 'at what moment should the order be created' setting, as this option is identical to the 'After order confirmation' option.
- Checkout fields for Klarna are now mandatory.
- Pay After Delivery fields are now mandatory when using direct Pay After Delivery.

---

**3.1.1**
Release date: Oct 17, 2016

**Improvements**
- Resolved an issue resulting in the wrong calculations being applied for shipping and wrapping taxes.
- A check was added to see whether or not SSL has been enabled in the webshop. Resulting in HTTP301 not occurring when calling the Notification URL.
- A check was added to see if the current plugin version is the latest version available on our website.
- Added support for % fee when using BVKPayment module.
- Added new logo for YourGiftcard.

**Fixes**
- Resolved a bug preventing order's from being created using certain configurations.

**Changes**
- Layout of the configuration screens now have standard PrestaShop design.

---

**3.0.3**
Release date: July 27, 2016

**Fixes**
- Resolved a bug preventing order's from being created using certain configurations.

---

**3.0.2**
Release date: July 12, 2016

**Improvements**
- Orders are now created for initialized Bank transfer payments and uncleared transactions when using the setting; "Only when an order was paid in full".
- Added E-Invoicing as a payment method.
- The PSP ID is added to the order, so it can be used to find the corresponding transaction in your MultiSafepay dashboard.

**Fixes**
- Fixed issue with crypt function were no 'salt' was used. This resulted in a notice when using PHP 5.6 or above.

**Changes**
- Textual ### Changes to the plugin configuration.
- Changed the name and logo "MisterCash" to "Bancontact".

---

**3.0.0**
Release date: Apr 15, 2016

**Improvements**
- The payment method shown in the Fast Checkout orders are now updated to show the payment method eventually used.
- Added (limited) support for the BVK Additional Payment Fees module; payment fees can be applied per payment method.
- Added `daysactive` to the configuration. Orders are cancelled after X number of days when configured.
- An extra configuration option has been added for skipping the default extra confirmation screen before payment.
- Added Dotpay as a payment method.
- Added E-Invoicing as a payment method.
- Added tool tips to the configuration options in the plugin.
- Improved the payment logos.
- Added a debug configuration option. Debug output are logged to: `prestashop_root_directory/log/MultiSafepay.log`.
- Added the following gift cards:

1.	Wellness & Beauty
2.	Brouwmarkt
3.	Fashion Giftcard
4.	Fietsenbon
5.	Gezondheidsbon
6.	Good4fun
7.	Jewelstore
8.	Kelly Fashion Giftcard
9.	Liefcadeaukaart
10.	Nationale tuinbon
11.	Nationale verwen cadeaubon
12.	Parfumcadeaukaart
13.	Parfumnl
14.	Podium
15.	Sportenfit
16.	Webshopgiftcard
17.	Wellness-gift card
18.	Wijncadeau
19.	Winkelcheque

**Fixes**
- Order status was not updated in case of a partial refund.
- In specific situations there was still a Payment Error.
- Minor ### Improvements to the iDEAL gateway layout to match the other payment methods.
- Improved translations.
- Changs bank account input field from 10 to 34 characters.

**Changes**
- Removed Babygiftcard.
- In specific situations there was still a Payment Error.
- Order status are no longer removed when uninstalling the core MultiSafepay module, resulting in existing orders maintaining the correct order status.
- This plugin has been rewritten from scratch and uses the JSON API rather than the XML API.
- Changed the Fast Checkout logo.
- The order history page is shown when redirected back to the webshop after a successful payment.

---

**2.1.1**
Release date: Nov 2, 2015

**Improvements**
- Added support for gift card VVV Cadeaukaart.
- During installation of the plugin, the order states will not be removed anymore. So old orders remain their correct order status.

**Fixes**
- Order status was not updated in case of a partial refund.
- In specific situations there was still a Payment Error.

---

**2.1.0**

Release date: Oct 8, 2015

**Improvements**

- Added support for the BVK Payments module for the payment method Pay After Delivery.
- MultiSafepay Transaction IDs are now added to, and visible within, the PrestaShop order.
- Changed the Fast Checkout button.
- The payment method used to pay for an order is now shown within the order overview.
- The payment hook template now uses the default PrestaShop style within the checkout and can be overruled by template overrides.
- Added Fashioncheque.

**Changes**
- The iDEAL bank list is now shown under the payment method iDEAL, rather than the next step.
- Removed the E-Bon gift card.

**Fixes**
- Resolved double paid/invoice notices.
- Fixed bug to show payment method when the Min and Max amount in the configuration are equal.
- Fixed undefined index notice warnings.
- Fixed double payment method titles.
- Improved the support of shipping methods, coupons, taxes, free shipping and free products.
- Shipping prices were always handled by Fast Checkout as including tax.

---

**2.0.0**
Release date: Nov 11, 2014

**Improvements**
- Added special NL configuration files.
- Added Italian language files.
- Added Gateway image for Wallet.
- Added support for PrestaShop 1.6.x.
- Added support for erotiekbon.
- Added support for e-bon.
- Added support for degrotespeelgoedwinkel.
- Added support for Boekenbon.
- Added support for babygiftcard.
- Added Notification info field to FastCheckout configuration for when only Fast Checkout is active.
- Added better support for IP6.

**Changes**
- Made some ### Changes to the configuration screen.
- Updated local images.
- Updated language files ES en FR.

**Fixes**
- Fixed bug with wrong Shipping price calculation.
- Fixed bug to show payment method when the Min and Max amount in the configuration are equal.

[Top of page](#)

---
</details>

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- PrestaShop 1.6
- Tested on PHP 7.0

# Installation and configuration

✅ &nbsp; **Tip!** We recommend first installing the plugin in a test environment, following the PrestaShop 1.6 installation procedure. Always make a backup.

1. Unpack the contents of the .zip archive and upload the **Modules** folder via SFTP to the PrestaShop root directory, merging the two folders.
2. Sign in to your PrestaShop 1.6 <<glossary:backend>>.
3. Go to **Modules and services** > **Payments and gateways**.  
    **Note:** You must install and configure the MultiSafepay Core Module (MultiSafepay) because all payment methods require certain settings and/or the API key in the core module.
4. In the next screen, proceed with the installation.
5. Enter your [API key](/docs/sites#site-id-api-key-and-security-code), and then click **Save**.
6. On the **Payments** tab, enable the relevant payment methods.
<br>

---

# User guide

## Confirmation page

PrestaShop 1.6 version 3.1.7 lets you skip the extra confirmation page so that the customer is redirected straight to the MultiSafepay payment page.

This is no longer supported from version 3.2.0. If you want to skip the extra confirmation page, you can <a href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/prestashop-1-6/Plugin_PrestaShop1.6_3.7.1.zip" target="_blank">download version 3.1.7</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. New features might be lost when downgrading.

## Generic gateways

The plugin supports generic gateways, which let you add payment methods manually. This is particularly useful for integrating gift cards specific to your business. 

Supported since release: 3.8.0, Jul 13, 2022

<details id="how-to-configure-generic-gateways">
<summary>How to configure generic gateways</summary>
<br>

1. Sign in to your PrestaShop 1.6 <<glossary:backend>>.
2. Go to **Modules and services**.
3. Search for "generic gateway", select gateway 1, 2, or 3, and then click **Install**.
4. In the **Gateway title** field, enter the name of the payment method. 
5. In the **Gateway ID** field, enter the [gateway ID](/reference/gateway-ids).
6. Optionally:
    - Upload the <a href="https://github.com/MultiSafepay/MultiSafepay-icons" target="_blank">payment method logo</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
    - Enter minimum and maximum order amounts.
7. Click **Save**. 

✅ &nbsp; Success! The payment method is now active.

</details>

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/)
- <<glossary:BNPL>>: All, except Betaal per Maand
- Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
- Banking methods: 
    - [Bancontact](/docs/bancontact/)
    - [Bank transfer](/docs/bank-transfer/)
    - [Belfius](/docs/belfius/)
    - [CBC/KBC](/docs/cbc-kbc/)
    - [Dotpay](/docs/dotpay/)
    - [EPS](/docs/eps/)
    - [Giropay](/docs/giropay/)
    - [iDEAL](/docs/ideal/)
    - [Request to Pay](/docs/request-to-pay/)
    - [Direct debit](/docs/direct-debit/)
    - [Sofort](/docs/sofort/)
- Prepaid cards:
    - Beauty and Wellness gift card
    - Boekenbon
    - Degrotespeelgoedwinkel
    - Fashioncheque
    - Fashion gift card
    - Fietsenbon
    - Gezondheidsbon
    - Good4fun
    - Parfumcadeaukaart
    - Paysafecard
    - Sport en Fit
    - VVV gift card
    - Webshop gift card
    - Wijncadeau
    - YourGift

</details>

## Matching orders

In PrestaShop 1.6, the order ID is generated after the payment, which causes a mismatch with the order ID in your MultiSafepay dashboard. You can match orders using the transaction ID. 

<details id="how-to-view-transaction-ids">
<summary>How to view transaction IDs</summary>
<br>

1. Sign in to your PrestaShop 1.6 backend.
2. Go to **Payment** > **Order details**. 

</details>

## Payment components

The plugin supports [payment components](/docs/payment-components/), which:

- Provide a seamless checkout experience to increase <<glossary:conversion>>.
- Encrypt customer payment details for secure processing.
- Shift responsibility for [PCI DSS compliance](/docs/pci-dss/) to MultiSafepay.

<details id="how-to-activate-payment-components">
<summary>How to activate payment components</summary>
<br>

If you're new to accepting credit card payments, email a request to activate them to <sales@multisafepay.com>

1. Sign in to your PrestaShop 1.6 backend.
2. Go to **Modules and services** > **MultiSafepay**.
3. Slide the **Payment component** radio button to **Yes**.
4. Click **Save**.

</details>

## Payment links

Payment links generated manually in your MultiSafepay dashboard don't automatically create or update orders in your PrestaShop 1.6 backend.

## Recurring payments

[Recurring payments](/docs/recurring-payments) are supported.

<details id="how-to-enable-recurring-payments">
<summary>How to enable recurring payments</summary>
<br>

1. Sign in to your PrestaShop 1.6 backend. 
2. Go to **Modules and services** > **Modules and services** > **MultiSafepay**.
3. Click **Configure**.
4. Set the **Tokenization** field to **YES**.
5. Click **Save**.

</details>

## Refunds

You can process [full and partial refunds](/docs/refund-payments/) from your MultiSafepay dashboard.  
Backend refunds are **not** supported.

## Surcharges

[Surcharges](/docs/surcharges/) are not supported by default.

<details id="applying-surcharges-with-bvk">
<summary>Applying surcharges with BVK</summary>
<br>

To apply a surcharge or payment fee to a payment method, you can use the third-party <a href="https://www.bvkyazilim.com/cart/prestashop-modules" target="_blank">BVK</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> package.

The Integration Team will do their best to support you with installing BVK, but bear in mind that it is a third-party package. We can't guarantee perfect compatibility.

> ⚠️ **Attention Dutch merchants** 
> We strongly recommend **not** applying surcharges to <<glossary:BNPL>> methods. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

</details>

## Thirty Bees

For support for the PrestaShop <a href="https://thirtybees.com/blog/what-is-thirty-bees" target="_blank">Thirty Bees</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> fork, email <integration@multisafepay.com>

## Updates

You can update the plugin in your backend and the CMS marketplace, or via SFTP.

<details id="how-to-update-via-sftp">
<summary>How to update via SFTP</summary>
<br>

✅ &nbsp; **Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.

</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: create a technical issue</li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)