---
title: "Magento 2 plugin"
category: 62962dd7e272a6002ebbbbc5
order: 102
hidden: false
parentDoc: 62a1d773f96fe80056354d84
excerpt: "Free plugin to integrate MultiSafepay payment solutions with Magento 2."
slug: 'magento-2'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Magento_2.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

> [Changelog](https://github.com/MultiSafepay/magento2/blob/master/CHANGELOG.md) :link:

> [View source code](https://github.com/MultiSafepay/Magento2) :link:

:warning: If you are still using the deprecated plugin, we recommend [upgrading to the latest version](/magento-2/#upgrading) as soon as possible.

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with Magento 2.

<details id="requirements">
<summary>Requirements</summary>
<br>

- [MultiSafepay account](/getting-started/guide/)
- Magento Open Source version 2.3.x & 2.4.x **or** Adobe Commerce version 2.3.x & 2.4.x (For GraphQL, only Magento Open Source versions 2.4.x are supported)
- PHP 7.1+

</details>

<details id="support">
<summary>Support</summary>
<br>

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue
- [Magento Slack channel](https://magentocommeng.slack.com) #multisafepay-payments

Our plugin is supported by a certified Magento 2 Solution Specialist and receives regular updates for the latest features from Magento and MultiSafepay.

</details>

# Modules

<details id="magento-modules">
<summary>Magento modules</summary>
<br>

The plugin consists of several Magento modules:

| Module  | Description  |
|---|---|
| [Multisafepay-magento2-core](https://github.com/MultiSafepay/magento2-core)   | Provides core functionalities  |
| [Multisafepay-magento2-frontend](https://github.com/MultiSafepay/magento2-frontend)  | Enables payment gateways in the Magento checkout  |
| [Multisafepay-magento2-adminhtml](https://github.com/MultiSafepay/magento2-adminhtml)  | Enables/disables payment gateways, and changes settings in the Magento backend  |
| [Multisafepay-magento2-msi](https://github.com/MultiSafepay/magento2-msi)  | Handles stock when MSI is enabled  |
| [Multisafepay-magento2-catalog-inventory](https://github.com/MultiSafepay/magento2-catalog-inventory)  | Handles stock when MSI is disabled  |
| [Multisafepay-magento2](https://github.com/MultiSafepay/magento2)  | Meta package that installs all the above  |
| [Multisafepay-magento2-graphql](https://github.com/MultiSafepay/magento2-graphql)| For GraphQL support, extends and adds GraphQL queries and mutations |

</details>

<details id="module-dependencies">
<summary>Module dependencies</summary>
<br>

The meta-package has a dependency on MSI. This means the MSI modules must be available (but not necessarily enabled) in your store. 

If you have removed MSI (e.g. with a composer-replace trick like [yireo/magento2-replace-inventory](https://github.com/yireo/magento2-replace-inventory)), you can't install the meta-package. To integrate with MultiSafepay, instead of installing the meta-package, install the magento2-frontend module and the magento2-catalog-inventory module.

The magento2-frontend module has a dependency on the magento2-core and magento2-adminhtml modules, so they are all installed together. In some cases, you also then need a stock-handling module. Since MSI is not available, you can install the magento2-catalog-inventory module instead.

The installation process is the same for the Adobe Commerce version.

</details>

# Installation

**1.** We recommend installing the meta-package using Composer:

``` 
composer require multisafepay/magento2
php bin/magento setup:upgrade
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy
```

**2.** To enable all modules, run in the Magento 2 root directory:
```
./bin/magento module:enable `./bin/magento module:status | grep MultiSafepay_`
```

## Stock handling

When you disable MSI in Magento 2, you must also disable the MultiSafepay MSI module by running:
```
php bin/magento module:disable MultiSafepay_ConnectMSI
```
If you have enabled MSI in Magento 2, to disable the MultiSafepay CatalogInventory module, run:
```
php bin/magento module:disable MultiSafepay_ConnectCatalogInventory
```

# Configuration
1. Sign in to your Magento 2 backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay**.  

<details id="specific-settings">
<summary>Specific settings</summary>
<br>

- **General information:** Contains all the main support information. We recommend reading this first.
- **General settings:** Contains all main settings.  
  - Here you can configure all gateways and gift cards.  
  - Enter your [account ID, site ID, site secure code](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).   
- **Payment methods:** Contains the configuration options for all MultiSafepay payment methods.  
    - Make sure you have activated your selected payment methods in your MultiSafepay dashboard.
- **Gift cards:** Contains the configuration options for all gift cards supported by MultiSafepay.  
    - Make sure you have activated your selected gift cards in your MultiSafepay dashboard.  
    - For more information, see [Gift cards](/gift-cards).

</details>

# User guide

## Checkouts 

The plugin is compatible with most Magento checkouts.

<details id="supported-checkouts">
<summary>Supported checkouts</summary>
<br>

- [Amasty One Step Checkout](https://amasty.com/one-step-checkout-for-magento-2.html)
- Hyvä: Compatible with Hyvä's [themes](https://hyva.io/hyva-themes-license.html) and [checkout](https://hyva.io/hyva-checkout.html)
- Magento 2 core checkout: Works out of the box, based on the Luma theme
- [MagePlaza One Step Checkout](https://www.mageplaza.com/magento-2-one-step-checkout-extension)
- [OneStepCheckout.com](https://www.onestepcheckout.com/): MultiSafepay is an official partner, and the plugin is compatible with the latest version of the OneStepCheckout extension. Always test first to check compatibility with your configuration.

For support, email [integration@multisafepay.com](mailto:integration@multisafepay.com)

</details>

## Custom totals

From version 1.9.0 and higher, **all** order totals from shopping cards are automatically read and displayed on MultiSafepay payment pages.

Sometimes this results in unwanted custom totals appearing on payment pages.

<details id="excluding-custom-totals-from-payment-pages">
<summary>Excluding custom totals from payment pages</summary>
<br>

1. Sign in to your Magento 2 backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay**.
3. Select **General settings** > **Advanced settings** > **Exclude custom totals**.

If you have included a custom total and it is **not** being read, make sure it implements the following methods:

- getCode()
- getTitle() or getLabel()
- getValue() or getAmount() and getBaseAmount()
- getTaxRate() or getBaseTaxRate()
- getTaxAmount() or getBaseTaxAmount()

The base values are required if you have enabled the `use base currency` setting under **MultiSafepay** > **General settings**.

</details>

## Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/payment-pages/). You can use them to integrate custom gift cards, or co-branded credit cards. 

<details id="configuring-generic-gateways">
<summary>Configuring generic gateways</summary>
<br>

1. Sign in to your Magento 2 backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay** > **Payment methods** > **Generic gateway**.
3. Set the relevant [payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids) and upload a custom gateway image.
4. For pay later methods, specify whether to include a shopping cart.

Generic gateways support:

- All payment methods (filter by country, and minimum/maximum amount)
- [Split payments](/payments/split-payments/), [Second Chance reminders](/features/second-chance/) and [virtual IBANs](/payments/virtual-ibans/)
- [Redirect requests](https://docs-api.multisafepay.com/reference/introduction#direct-vs-redirect) only

**Gift cards**

Generic gateways are particularly useful for integrating [gift cards](/payment-methods/gift-cards/), including [custom gift cards](/payment-methods/gift-cards/custom-cards/). This is because we don't support all [open-loop gift cards](/payment-methods/gift-cards/open-loop-closed-loop/) in our ready-made integrations and *no* closed-loop gift cards.

**Co-branded credit cards**

You can integrate Visa co-branded credit cards ([Cartes Bancaires](/payment-methods/cartes-bancaires/), [Dankort](/payment-methods/dankort/), and [V Pay](/payment-methods/vpay/)), using the generic `VISA` gateway.

For the logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons/tree/master/methods).

</details>

## Logs

<details id="downloading-multiSafepay-logs">
<summary>Downloading MultiSafepay logs</summary>
<br>

1. Sign in to your Magento backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay** > **General settings** > **MultiSafepay payment logs**.
3. Click **Download**.

You receive a ZIP package containing a system report file and any MultiSafepay log(s) stored in the `/var/log` directory.

</details>

## Magento Vault and Instant Purchase

Magento Vault enables you to use [Instant purchase](https://magento.com/innovations-lab/instant-purchase), a feature that helps make repeat payments faster and easier, increasing your conversion. 

<details id="how-it-works">
<summary>How it works</summary>
<br>

1. After filling out their credit card number, CVC, and expiry date at checkout, customers can give permission to store these details for future payments. 
2. MultiSafepay encrypts the sensitive payment details and stores the encrypted version on our secure, GDPR compliant servers. 
3. We return a non-sensitive identifier for the payment details, known as a token, which can only be used in your Magento webshop. 
4. The token is automatically stored in your Magento Vault. 
5. For subsequent payments, the customer can simply click **Instant purchase** at checkout. They don't need to re-provide any details. 

</details>

<details id="mastercard-and-visa-requirements">
<summary>Mastercard and Visa requirements</summary>
<br>

You must:  

- Include a checkbox at checkout for customers to give permission to tokenize their payment details (provided as standard by Magento Vault).
- Explain in your terms and conditions how you use and store their details.
- Inform customers how they can delete stored payment details.

</details>

<details id="activating-magento-vault">
<summary>Activating Magento Vault</summary>
<br>
 
To activate Magento Vault, email a request to enable [recurring payments](/features/recurring-payments/) to <sales@multisafepay.com>

</details>

<details id="vault-security">
<summary>Vault security</summary>
<br>
 
If you host Magento yourself, the security of the vault depends on the security of your server. 

However, the vault only contains tokens valid in your webshop. If your server is compromised, no actual payment details are at risk, only stored customer data.

</details>

## Order lifetimes

The default lifetime of **Pending payment** orders in Magento 2 is 480 minutes (8&nbsp;hours). For payment methods with a longer authorization period, the order status changes to **Cancelled** after 8 hours.

<details title="extending-order-lifetimes">
<summary>Extending order lifetimes</summary>
<br>
 
To extend the lifetime of pending payments orders, increase the **Order Cron settings** value to longer than the validation period.

For instructions, see Magento – [Pending payment order lifetime](https://docs.magento.com/user-guide/sales/order-pending-payment-lifetime.html).

**ERP systems**

For ERP systems, if the order status is **Declined**, successful payments often fail to process for orders with **Cancelled** status.

The lifetime of bank transfers is 86400 minutes (60 days).

The order status in Magento 2 changes to **Cancelled** before the payment can be matched to the order.

 </details>

## Payment components

The plugin supports [Payment Components](/payment-components/), which:

- Provide a seamless checkout experience to increase conversion.
- Encrypt customer payment details for secure processing.
- Shift responsibility for [PCI DSS compliance](/payment-regulations/pci-dss/) to MultiSafepay.

<details id="activating-the-payment-component-in-your-backend">
<summary>Activating the payment component in your backend</summary>
<br>

1. Sign in to your Magento 2 backend.
2. Go to **Configuration** > **Credit card**, and then click **Configure**.
3. Click **Payment type** and select **Credit card component**.
4. Click **Save config**.

For questions, email <integration@multisafepay.com>

**Note:** If you have a custom checkout and encounter a conflict with the payment component, the Integration Team will do their best to provide support, but we can't guarantee compatibility in all cases.

</details>

## Payment links 

From version 2.0 and higher, [payment links](/account/payment-links/) are automatically generated for every order.

<details id="getting-payment-links">
<summary>Getting payment links</summary>
<br>

To get a payment link for a customer, follow these steps:

1. Sign in to your Magento 2 backend.
2. Go to **Sales** > **Orders** > **Create new order**, and then create an order.
3. Go to the **Orders overview**, and then select the newly created order.
4. Go to **Comments history**.  
5. Under **Notes for this order**, copy the payment link.
6. Send the payment link to the customer.

</details>

<details id="adding-payment-links-to-order-confirmation-emails">
<summary>Adding payment links to order confirmation emails</summary>
<br>

1. Sign in to your Magento 2 backend.
2. Go to **Marketing** > **Email templates**.
3. Under **New order**, import a template.
4. Add the following code snippet to the template:

```
{{depend order.getPayment().getAdditionalInformation('payment_link')}}
<a href="{{var order.getPayment().getAdditionalInformation('payment_link')}}">Pay now with {{var order.getPayment().getAdditionalInformation('method_title')}}</a>
{{/depend}}
```

**Magento 2.3.4+**

The email template syntax is different for Magento 2.3.4+. Add this code snippet instead:

```
{{depend order.payment.additional_information.payment_link}}
<a href="{{var order.payment.additional_information.payment_link}}">Pay now with {{var order.payment.additional_information.method_title}}</a>
{{/depend}}
```

**Backend emails**

To add payment links to order confirmation emails from your Magento **backend**, you can use the `payment_link` variable and an `if/else` statement in the template. 

**Frontend emails**

You cannot add payment links to order confirmation emails created in your **frontend**, but you can display the name of the payment method:

```
{{if payment_link}}
<a href="{{var payment_link}}">Pay now with {{var order.payment.additional_information.method_title}}</a>
{{else}}
<p>{{var order.payment.additional_information.method_title}}</p>
{{/if}}
```

1. Go to **Stores** > **Configuration** > **Sales** > **Sales emails**.
2. Replace the **New order confirmation template** with your template.
3. Test the template to confirm it is working.

**Note:** You can also implement this directly in the email template files.

</details>

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/credit-debit-cards/)
- Banking methods: [All](/banks/)
- Pay later methods: [All](/pay-later/)
- Wallets: [All](/wallets/)
- Prepaid cards:
    - Baby gift card
    - Beauty and Wellness gift card
    - Boekenbon
    - Edenred
    - Fashioncheque
    - Fashion gift card
    - Fietsenbon
    - Gezondheidsbon
    - Givacard
    - Good4fun
    - Goodcard
    - Nationale tuinbon
    - Paysafecard
    - Parfumcadeaukaart
    - Podium
    - Sport en Fit
    - VVV gift card
    - Webshop gift card
    - Wellness gift card
    - Wijncadeau
    - Winkelcheque
    - Yourgift

</details>

## Progressive web apps

The plugin is compatible with GraphQL queries and can be integrated into PWA stores using an additional [GraphQL support module](https://github.com/MultiSafepay/magento2-graphql).

We also offer full extensions for [ScandiPWA](/scandipwa/) and [Vue Storefront](/vue-storefront/). 

## Refunds

<details id="refund-rules">
<summary>Refund rules</summary>
<br>

|  |   |
|---|---|
| MultiSafepay dashboard | - Full and partial refunds <br> - Orders with [Fooman surcharges](/payments/integrations/ecommerce-platforms/magento2/faq/applying-surcharges/) <br> - Orders from the deprecated plugin |
| Backend | - Full and partial refunds, and credit memos <br> - You can't refund more than the original amount in your backend |
| API | - See [Refund order](https://docs-api.multisafepay.com/reference/refundorder) > Pay later refund <br> - PATCH requests **not** supported |

</details>

<details id="processing-backend-refunds">
<summary>Processing backend refunds</summary>
<br>

1. Sign in to your Magento 2 backend. 
2. On the **Invoices** tab, click the invoice created by MultiSafepay, and then click **Credit memo**. 
3. Click the relevant refund button:  
    - **Offline refund**: Doesn't send a refund request to MultiSafepay.
    - **Refund**: Sends a refund request to MultiSafepay.

</details>

## Second Chance

[Second Chance](/second-chance/) emails are sent 1 hour and 24 hours after orders are created. By default, the order status changes from **Pending payment** to **Cancelled** after 8 hours (480 minutes).

If the customer pays via the **second** email (24 hours later), the payment is processed but the transaction update may not be handled correctly in Magento 2 because the order has expired. This may cause issues with external services, e.g. ERP/inventory management, if items are low in stock, or for one-off products like antiques.

To avoid this, match the order lifetime to the [payment link](/account/payment-links/) lifetime.

See [Setting order lifetimes](#order-lifetimes) above. 

**Note:** We recommend setting order lifetimes to 2 days (2880 minutes) to allow enough time for the customer to pay, but avoid issues with external services.

<details id="setting-payment-link-lifetimes">
<summary>Setting payment link lifetimes</summary>
<br>

1. Sign in to your Magento 2 backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay** > **Payment gateways**, and select the relevant gateway
3. Go to **Custom payment link lifetime**, select **Pending payment order lifetime**, and set to **2880 minutes**.

</details>

## Shipping orders

When you ship [pay later](/pay-later/) orders, you need to change the order status from **completed** to **shipped**. This prevents the order expiring and triggers invoicing. 

If you do so in your Magento 2 backend, the updated status is passed to your MultiSafepay dashboard automatically.

## Surcharges

The plugin does not support [surcharges](/surcharges/), but you can use third-party service Fooman to apply them. 

<details id="using-fooman-for-surcharges">
<summary>Using Fooman for surcharges</summary>
<br>

To apply a surcharge or payment fee to a payment method, you can use the third-party [Fooman](https://store.fooman.co.nz/extensions/magento2) package.

**Refunds**

You can refund orders with a Fooman surcharge applied in your MultiSafepay dashboard, but not from your Magento 2 backend. 

**Pay later methods**

For Dutch merchants, We strongly recommend **not** applying surcharges to [pay later methods](/pay-later/). This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM). 

**Support**

The Integration Team will do their best to support you with installing Fooman, but bear in mind that it is a third-party package. We can't guarantee perfect compatibility.

</details>

## Tax settings

<details id="configuring-magento-tax-settings">
<summary>Configuring Magento tax settings</summary>
<br>

To configure tax settings in Magento, go to **Stores** > **Configuration** > **Sales** > **Tax** > **Calculation settings**.

**Recommended tax settings**

To avoid discrepancies between item amounts in MultiSafepay transactions and Magento orders, we recommend using the following tax settings in Magento.

To show prices **excluding** tax, use the following settings:

- **Tax calculation method based on**: Row total
- **Catalog prices**: Excluding tax
- **Apply customer tax**: After discount
- **Apply discount on prices**: Excluding tax

To show prices **including** tax, use the following settings:

- **Tax calculation method based on**: Row total
- **Catalog prices**: Including tax
- **Apply customer tax**: After discount
- **Apply discount on prices**: Including tax

These recommended settings are based on Magento's standards. For more information, see Magento – [Warning messages](https://docs.magento.com/user-guide/tax/warning-messages.html).

</details>

## Updates

You can also update the plugin via [Composer](https://getcomposer.org) or in your Magento 2 backend.

<details id="backend-updates">
<summary>Backend updates</summary>
<br>

1. Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.
2. Sign in to your Magento 2 backend.
3. Run the following commands via the CLI:
```
composer update multisafepay/magento2 --with-all-dependencies
php bin/magento setup:upgrade
php bin/magento setup:di:compile
```

4. Depending on your webserver/webshop configuration, you may also need to:
    - Check the 'rights' on files are correct. For the MultiSafepay files, see vendor/multisafepay.
    - Empty static files when running in production mode.
    - Clear your cache.

</details>

## Upgrading 
If you are still using the [deprecated plugin](https://github.com/MultiSafepay/Magento2Msp), we recommend upgrading to the latest version as soon as possible.

<details id="why-upgrade">
<summary>Why upgrade?</summary>
<br>

The new plugin features code improvements, and unit and integration testing. It is built on top of the Magento payment provider gateway structure. Some payment methods now skip the MultiSafepay payment page, which increases conversion.

We support most Magento functionalities. For any questions, email <integration@multisafepay.com>

**New features**

- Improved:
    - Magento backend configuration, including support information
    - Translations
    - Error handling, and event and error logs
- Documentation for payment methods 
- Modular setup for greater installation flexibility
- PWA (GraphQL) endpoints
- Support for [Magento Vault](https://devdocs.magento.com/guides/v2.4/payments-integrations/vault/vault-intro.html) and [Instant Purchase](https://docs.magento.com/user-guide/sales/checkout-instant-purchase.html) (replace [recurring payments](/features/recurring-payments/))

**Configuration fields**

We have removed or altered the following configuration fields:

_Emailing invoices to customers_

This feature now uses a Magento core configuration field: **Sales** > **Sales emails** > **Invoice** > **Enabled**.

_Order statuses and flow_

As of version 2.16, you can assign the following MultiSafepay statuses to a Magento order status:

- Cancelled
- Chargeback
- Declined
- Expired
- Initialized
- Partial refunded
- Refunded
- Reserved
- Uncleared
- Void

We have updated the order status flow from version 2.5.0:

- All new orders first receive **Pending** status.
- When redirecting the customer, the status changes to **Pending payment**, until the customer reaches your success page. 
- If the payment is succesfully received at this point, the status changes to **Processing**. 
- Around the same time, the webhook is triggered and the invoice is created. The webhook changes the status to **Processing** (if it isn't already). 
- For bank transfers, the status doesn't change to **Pending payment**, therefore the order isn't automatically cancelled after a set period of time to give the customer more time to pay.

_Payment links_ 

Payment links are now generated automatically. 

_Reset gateway_  

When creating an order in your Magento 2 backend, you can now select the MultiSafepay payment gateway instead. The payment gateway displays all active payment gateways to the customer based on the site settings in your MultiSafepay account. 

To enable or disable the gateway on your checkout page, we have added a **Can use checkout** configuration field.

_Keep cart alive_  

The cart is now always kept alive when the customer clicks **Back** on the MultiSafepay payment page.

_Checkout_

We have changed the default payment flow from [redirect to direct](https://docs-api.multisafepay.com/reference/introduction#direct-vs-redirect) for:

- AfterPay, E-Invoicing, in3, Pay After Delivery 
- Direct Debit, Request to Pay

We have included extra fields in the checkout for these payment methods. If you use a custom checkout, you must account for the iDEAL issuers checkout field and the new checkout fields for these payment methods.

Alternatively, you can disable additional checkout fields for these payment methods and change the flow back to redirect. Go to **Stores** > **Configuration** > **MultiSafepay** > **Payment gateways** > **Gateway** > **Additional checkout fields**.

</details>

<details id="deleting-the-deprecated-plugin">
<summary>Deleting the deprecated plugin</summary>
<br>

Make sure you finish processing all orders created in the deprecated plugin before you delete it. The deprecated payment gateways are no longer available in Magento after deletion. 

You can refund transactions processed through the deprecated plugin in your MultiSafepay dashboard, but **not** from your Magento 2 backend.

The way you delete the deprecated plugin depends on the way you installed it:

**Composer**

There are two options:

Option 1: Remove the code base

``` 
composer remove multisafepay/magento2msp
php bin/magento setup:upgrade
```

Option 2: Do a complete uninstall

This includes removing database entries and configuration.
``` 
bin/magento module:uninstall MultiSafepay_Connect --remove-data --clear-static-content
php bin/magento setup:upgrade
```

_Backups_

You can back up certain parts of the plugin by adding the following parameters: 

- `--backup-code`
- `--backup-media`
- `--backup-db`

For information about all parameters, see Magento - [Uninstall modules](https://devdocs.magento.com/guides/v2.4/install-gde/install/cli/install-cli-uninstall-mods.html#instgde-cli-uninst-mod-uninst).
If you want a field from the deprecated plugin back, email <integration@multisafepay.com>

**app/code**

**1.** Disable the plugin:
``` 
php bin/magento module:disable --clear-static-content
php bin/magento setup:upgrade
```

**2.** To remove the code base, delete the app/code/MultiSafepay/Connect directory:
```
cd app/code/MultiSafepay
rm -rf Connect
```

**Marketplace**

If you installed the plugin via the Magento Marketplace, go to **System** > **Web setup wizard** > **Extension manager** > **Update / uninstall**.
</details>
