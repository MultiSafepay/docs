---
title: "Magento 2"
category: 62962dd7e272a6002ebbbbc5
order: 5
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'magento-2'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Magento_2.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/Magento2" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/magento2/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

Our plugin is supported by a certified Magento 2 Solution Specialist and receives regular updates for the latest features from Magento and MultiSafepay.

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- Magento Open Source version 2.3.6+ & 2.4.x **or** Adobe Commerce version 2.4.x (For GraphQL, only Magento Open Source versions 2.4.x are supported)
- PHP 7.2+

# Modules

<details id="magento-modules">
<summary>Magento modules</summary>
<br>

The plugin consists of several Magento modules:

| Module                                                                                                                                                                                                    | Description  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| <a href="https://github.com/MultiSafepay/magento2-core" target="_blank">Multisafepay/magento2-core</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>                           | Provides core functionalities  |
| <a href="https://github.com/MultiSafepay/magento2-frontend" target="_blank">Multisafepay/magento2-frontend</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>                   | Enables payment <<glossary:gateways>> in the Magento checkout  |
| <a href="https://github.com/MultiSafepay/magento2-adminhtml" target="_blank">Multisafepay/magento2-adminhtml</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>                 | Enables/disables payment gateways, and changes settings in the Magento backend  |
| <a href="https://github.com/MultiSafepay/magento2-msi" target="_blank">Multisafepay/magento2-msi</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>                             | Handles stock when MSI is enabled  |
| <a href="https://github.com/MultiSafepay/magento2-catalog-inventory" target="_blank">Multisafepay/magento2-catalog-inventory</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> | Handles stock when MSI is disabled  |
| <a href="https://github.com/MultiSafepay/magento2" target="_blank">Multisafepay/magento2</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>                                     | Meta package that installs all the above  |
| <a href="https://github.com/MultiSafepay/magento2-graphql" target="_blank">Multisafepay/magento2-graphql</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>                     | For GraphQL support, extends and adds GraphQL queries and mutations |
| <a href="https://github.com/MultiSafepay/magento2-hyva-checkout" target="_blank">Multisafepay/hyva-checkout</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>                  | Adds support for Hyvä Checkout |

</details>

<details id="module-dependencies">
<summary>Module dependencies</summary>
<br>

The meta-package has a dependency on MSI. This means the MSI modules must be available (but not necessarily enabled) in your store. 

If you have removed MSI (e.g. with a composer-replace trick like <a href="https://github.com/yireo/magento2-replace-inventory" target="_blank">yireo/magento2-replace-inventory</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>), you can't install the meta-package. To integrate with MultiSafepay, instead of installing the meta-package, install the magento2-frontend module and the magento2-catalog-inventory module.

The magento2-frontend module has a dependency on the magento2-core and magento2-adminhtml modules, so they are all installed together. In some cases, you also then need a stock-handling module. Since MSI is not available, you can install the magento2-catalog-inventory module instead.

The installation process is the same for the Adobe Commerce version.

</details>

# Installation

1. We recommend installing the meta-package using Composer:
    ``` 
    composer require multisafepay/magento2
    php bin/magento setup:upgrade
    php bin/magento setup:di:compile
    php bin/magento setup:static-content:deploy
    ```
2. To enable all modules, run in the Magento 2 root directory:
    ```
    ./bin/magento module:enable `./bin/magento module:status | grep MultiSafepay_`
    ```

## Stock handling

When you disable MSI in Magento 2, you must also disable the MultiSafepay MSI module by running:
```
php bin/magento module:disable MultiSafepay_ConnectMSI
```
If you have a Magento 2 environment with MSI disabled, to enable the MultiSafepay `CatalogInventory` module instead, run:
```
php bin/magento module:enable MultiSafepay_ConnectCatalogInventory
```

# Configuration

1. Sign in to your Magento 2 <<glossary:backend>>.
2. Go to **Stores** > **Configuration** > **MultiSafepay**.
  
    <details id="specific-settings">
    <summary>Specific settings</summary>
    <br>

    - **General information:** Contains all the main support information. We recommend reading this first.
    - **General settings:** Contains all main settings.  
    - Here you can configure all <<glossary:gateways>> and gift cards.  
    - Enter your site [API key](/docs/sites#site-id-api-key-and-security-code).   
    - **Payment methods:** Contains the configuration options for all MultiSafepay payment methods.  
        - Make sure you have activated your selected payment methods in your MultiSafepay dashboard.
    - **Gift cards:** Contains the configuration options for all gift cards supported by MultiSafepay.  
        - Make sure you have activated your selected gift cards in your MultiSafepay dashboard.  
        - For more information, see [Gift cards](/docs/gift-cards/).
        
    </details>

<br>

---

# User guide

## Checkouts 

The plugin is compatible with most Magento checkouts.

<details id="supported-checkouts">
<summary>Supported checkouts</summary>
<br>

<table>
  <tr>
   <th><b>Checkout</b></th>
   <th><b>Module</b></th>
  </tr>
  <tr>
    <td><a href="https://amasty.com/one-step-checkout-for-magento-2.html" target="_blank">Amasty One Step Checkout</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i></td>
    <td>By default, Amasty One Step checkout is supported.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/hyva-themes/magento2-react-checkout" target="_blank"> Hyvä React checkout </a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>  </td>
    <td><a href="https://github.com/MultiSafepay/magento2-react-checkout-multisafepay" target="_blank"> Hyvä checkout module</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i></td>
  </tr>
  <tr>
    <td><a href="https://www.mageplaza.com/magento-2-one-step-checkout-extension" target="_blank">MagePlaza One Step checkout</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> </td>
    <td>By default, MagePlaza One Step checkout is supported. </td>
  </tr>
  <tr>
    <td><a href="https://docs.hyva.io/checkout/hyva-checkout/index.html " target="_blank"> Hyvä Checkout</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> </td>
    <td><a href="https://github.com/MultiSafepay/magento2-hyva-checkout" target="_blank"> Hyvä Checkout module</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i></td>
  </tr>
  <tr>
    <td> <a href="https://www.onestepcheckout.com/" target="_blank">OneStepCheckout.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> </td>
    <td>By default, OneStepCheckout.com is supported. </td>
  </tr>
</table>
<br>

**⚠️ Note:** We recommend testing compatibility with your configuration.

For support, email [integration@multisafepay.com](mailto:integration@multisafepay.com)

</details>

## Custom totals

From version 1.9.0 and higher, **all** order totals from shopping cards are automatically read and displayed on MultiSafepay payment pages.

Sometimes this results in unwanted custom totals appearing on payment pages.

<details id="how-to-exclude-custom-totals-from-payment-pages">
<summary>How to exclude custom totals from payment pages</summary>
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

## Custom URLs

<details id="how-to-set-up-custom-urls">
<summary>How to set up custom URLs</summary>
<br>

1. Sign in to your Magento 2 backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay**.
3. Select **General settings** > **Advanced settings**.
4. In the **Use custom return urls** field, select **Yes**.
5. Enter your custom URL in either:
  - The **Custom redirect url after canceling the payment** field, **or**
  - The **Custom "Success page" url** field.
6. Click **Save Config**.


</details>

## Generic gateways

The plugin supports generic gateways, which allows you to add a payment method manually. This is particularly useful for integrating gift cards specific to your business. 

Supported since release: 2.4.0, February 22nd 2021.

<details id="how-to-configure-generic-gateways">
<summary>How to configure generic gateways</summary>
<br>

1. Sign in to your Magento 2 backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay** > **Payment methods** > **Generic gateway**.
3. Set the relevant [payment method gateway IDs](/reference/gateway-ids/) and upload a custom gateway image.
4. For <<glossary:BNPL>> orders, specify whether to include a shopping cart.

</details>

## Logs

<details id="how-to-download-multiSafepay-logs">
<summary>How to download MultiSafepay logs</summary>
<br>

1. Sign in to your Magento backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay** > **General settings** > **MultiSafepay payment logs**.
3. Click **Download**.

You receive a ZIP package containing a system report file and any MultiSafepay log(s) stored in the `/var/log` directory.

</details>

## Magento Vault and Instant Purchase

Magento Vault enables you to use <a href="https://magento.com/innovations-lab/instant-purchase" target="_blank">Instant purchase</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, a feature that helps make repeat payments faster and easier, increasing your <<glossary:conversion>> rate. 

<details id="how-it-works">
<summary>How it works</summary>
<br>

1. After filling out their card number, CVC, and expiry date at checkout, customers can give permission to store these details for future payments. 
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

<details id="how-to-activate-magento-vault">
<summary>How to activate Magento Vault</summary>
<br>
 

To activate Magento Vault, and enable <a href="https://docs.multisafepay.com/docs/recurring-payments" target="_blank">recurring payments</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>, email a request to <sales@multisafepay.com>. 


</details>

<details id="vault-security">
<summary>Vault security</summary>
<br>
 
If you host Magento yourself, the security of the vault depends on the security of your server. 

However, the vault only contains tokens valid in your webshop. If your server is compromised, no actual payment details are at risk, only stored customer data.

</details>


## Manual Capture

The Magento 2 integration supports Manual Capture from version 3.7.0 and up. 

<details title="how-to-use-manual-capture-magento">
<summary>How to use manual capture in magento</summary>
<br>
It has been implemented for the following supported payment gateways:

- Card payments
- Maestro
- Mastercard
- Visa

For more information about Manual capture and how to enable it for your MultiSafepay account, please check our [Manual capture](/docs/manual-capture#integration) https://docs.multisafepay.com/docs/manual-capture#integration instructions.

To enable Manual capture in your Magento environment: 

1. Go to Stores > Configuration > MultiSafepay > Payment Gateways 
2. Select a supported payment gateway, e.g. 'Card Payment'
3. Select **Enable Manual Capture** > Yes

Please note that the full shipping amount will be captured whenever the first shipment has been made, even if it was just a partial shipment of the items. If the rest of the items in the order will not be shipped anymore, you can initiate a refund for the shipment costs of those items.

</details>

## Order lifetimes

The default lifetime of **Pending payment** orders in Magento 2 is 480 minutes (8 hours). For payment methods with a longer authorization period, the <<glossary:order status changes>> to **Cancelled** after 8 hours.

<details title="how-to-extend-order-lifetimes">
<summary>How to extend order lifetimes</summary>
<br>
 
To extend the lifetime of pending payments orders, increase the **Order Cron settings** value to longer than the validation period.

For instructions, see Magento – <a href="https://docs.magento.com/user-guide/sales/order-pending-payment-lifetime.html" target="_blank">Pending payment order lifetime</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

</details>

## Order requests

<details id="how-to-modify-order-requests">
<summary>How to modify order requests</summary>
<br>

To modify an OrderRequest before a transaction is processed, create an observer based on the `before_send_multisafepay_order_request` event in the plugin.

For an example, see MultiSafepay GitHub – <a href="https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/magento2/magento2-example-module.zip" target="_blank">Magento 2 example module</a>.

**ERP systems**

For ERP systems, if the <<glossary:order status>> is **Declined**, successful payments often fail to process for orders with **Cancelled** status.

The lifetime of bank transfers is 86400 minutes (60 days).

The <<glossary:order status>> in Magento 2 changes to **Cancelled** before the payment can be matched to the order.

 </details>

## Payment components

The plugin supports [Payment Components](/docs/payment-components/), which:

- Provide a seamless checkout experience to increase <<glossary:conversion>>.
- Encrypt customer payment details for secure processing.
- Shift responsibility for [PCI DSS compliance](/docs/pci-dss/) to MultiSafepay.

<details id="how-to-activate-payment-component-in-backend">
<summary>How to activate the payment component in your backend</summary>
<br>

1. Sign in to your Magento 2 backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay** > **Payment Gateways**.
3. Select the relevant payment methods and then click **Configure**.
3. Click **Payment type** and select **Card payment component**.
4. Click **Save config**.

**⚠️ Note:** If you have a custom checkout and encounter a conflict with the payment component, the Integration Team will do their best to provide support, but we can't guarantee compatibility in all cases.

</details>

## Payment links 

From version 2.0 and higher, [payment links](/docs/payment-links/) are automatically generated for every order.

<details id="how-to-fetch-payment-links">
<summary>How to fetch a payment link</summary>
<br>

To get a payment link for a customer, follow these steps:

1. Sign in to your Magento 2 backend.
2. Go to **Sales** > **Orders** > **Create new order**, and then create an order.
3. Go to the **Orders overview**, and then select the newly created order.
4. Go to **Comments history**.  
5. Under **Notes for this order**, copy the payment link.
6. Send the payment link to the customer.

</details>

<details id="how-to-add-payment-links-to-order-confirmation-emails">
<summary>How to add payment links to order confirmation emails</summary>
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

&nbsp; **💡 Tip!** You can also implement this directly in the email template files.

</details>

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/)
- Banking methods: All
- <<glossary:BNPL>>: All
- Wallets: All
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

The plugin is compatible with GraphQL queries and can be integrated into PWA stores using an additional <a href="https://github.com/MultiSafepay/magento2-graphql" target="_blank">GraphQL support module</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

We also offer full extensions for [ScandiPWA](/docs/scandipwa/) and [Vue Storefront](/docs/vue-storefront/). 

## Refunds

<details id="refund-rules">
<summary>Refund rules</summary>
<br>

| Platform | Supported refunds  |
|---|---|
| MultiSafepay dashboard | Full and partial refunds <br> Orders with [Fooman surcharges](/docs/magento-2#surcharges) <br> Orders from the deprecated plugin <br> **⚠️ Note:** Credit memos are **not** generated |
| Backend | Full and partial refunds, and credit memos <br> You can't refund more than the original amount in your backend |
| API | See [Refund order](/reference/refundorder/) > BNPL refund <br> PATCH requests **not** supported |

</details>

<details id="how-to-process-backend-refunds">
<summary>How to process refunds</summary>
<br>

To process backend refunds:

1. Sign in to your Magento 2 <<glossary:backend>>. 
2. On the **Invoices** tab, click the invoice created by MultiSafepay, and then click **Credit memo**. 
3. Click the relevant refund button:  
    - **Offline refund:** Doesn't send a refund request to MultiSafepay.
    - **Refund:** Sends a refund request to MultiSafepay.

To process refunds via the REST API:

1. Use the following endpoint in your request:

```
POST V1/invoice/:invoiceId/refund
```

For more information, see Magento REST API - <a href="https://devdocs.magento.com/guides/v2.3/rest/modules/sales/refunds.html#endpoint" target="_blank">Refunds</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

2. Add `is_online` parameter to the JSON body:

```
"is_online": true
```
</details>

## Second Chance

[Second Chance](/docs/second-chance/) emails are sent 1 hour and 24 hours after orders are created. By default, the <<glossary:order status>> changes from **Pending payment** to **Cancelled** after 8 hours (480 minutes).

If the customer pays via the **second** email (24 hours later), the payment is processed but the transaction update may not be handled correctly in Magento 2 because the order has expired. This may cause issues with external services, e.g. ERP/inventory management, if items are low in stock, or for one-off products like antiques.

To avoid this, match the order lifetime to the [payment link](/docs/payment-links/) lifetime.

See [Order lifetimes](#order-lifetimes) above. 

&nbsp; **💡 Tip!** We recommend setting order lifetimes to 2 days (2880 minutes) to allow enough time for the customer to pay, but avoid issues with external services.

<details id="how-to-set-payment-link-lifetimes">
<summary>How to set payment link lifetimes</summary>
<br>

1. Sign in to your Magento 2 backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay** > **Payment gateways**, and select the relevant <<glossary:gateway>>.
3. Go to **Custom payment link lifetime**, select **Pending payment order lifetime**, and set to **2880 minutes**.

</details>

## Shipment

When you ship <<glossary:BNPL>> orders, you need to change the <<glossary:order status>> from **Completed** to **Shipped**. This prevents the order expiring and triggers invoicing. 

If you do so in your Magento 2 backend, the updated status is passed to your MultiSafepay dashboard automatically.

## Surcharges

The plugin does not support [surcharges](/docs/surcharges/), but you can use third-party service Fooman to apply them. 

<details id="how-to-use-fooman-for-surcharges">
<summary>How to use Fooman for surcharges</summary>
<br>

To apply a surcharge or payment fee to a payment method, you can use the third-party <a href="https://store.fooman.co.nz/extensions/magento2" target="_blank">Fooman</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> package.

**Refunds**

You can refund orders with a Fooman surcharge applied in your MultiSafepay dashboard, but not from your Magento 2 backend. 

**BNPL orders**

For Dutch merchants, We strongly recommend **not** applying surcharges to <<glossary:BNPL>> orders. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM). 

**Support**

The Integration Team will do their best to support you with installing Fooman, but bear in mind that it is a third-party package. We can't guarantee perfect compatibility.

</details>

## Tax settings

<details id="how-to-configure-magento-tax-settings">
<summary>How to configure Magento tax settings</summary>
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

These recommended settings are based on Magento's standards. For more information, see Magento – <a href="https://docs.magento.com/user-guide/tax/warning-messages.html" target="_blank">Warning messages</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

</details>

## Updates

You can update the plugin via <a href="https://getcomposer.org" target="_blank">Composer</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

<details id="how-to-update">
<summary>How to update</summary>
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

---
## Troubleshooting

<details id="Magento 2 Troubleshooting">
<summary>How to troubleshoot Magento 2 issues</summary>
<br>

### Order Status Update

If you experience issues with order statuses not being updated correctly (e.g., incongruent pending and processing), this might happen randomly and be difficult to replicate. This is generally caused by third-party solutions interfering in the order processing flow and the observer being based on a different instance of the order object.

_Tip_: This issue might appear after upgrading to our latest plugin version, possibly due to faster notification processing times surfacing an already existing update conflict.

To debug this issue on your side:

1. Set to debug mode.
2. Use our <a href="https://github.com/MultiSafepay/magento2-order-save-inspector" target="_blank">Order Save Inspector</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> to check which module might interfere (for example, delivery software, ERP).
</details>


[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: <a href=\"https://github.com/MultiSafepay/magento2/issues/new/choose\" target=\"_blank\"> create a technical issue</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)