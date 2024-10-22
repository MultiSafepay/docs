---
title: "WooCommerce"
category: 62962dd7e272a6002ebbbbc5
order: 22
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'woocommerce'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/WooCommerce.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://wordpress.org/plugins/multisafepay/" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/WooCommerce" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/WooCommerce/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- Wordpress 5.0 or higher
- PHP 7.3 or 7.4

# Installation

&nbsp; **💡 Tip!** We recommend first installing the plugin in a test environment, following the WooCommerce installation procedure. Always make a backup.

There are two ways to install the plugin:

**Wordpress installation**

1. Sign in to your WooCommerce backend.
2. Go to **Plugins** > **Add new**.
3. Search for **MultiSafepay**.
4. For the **MultiSafepay plugin for WooCommerce**, click **Install now** > **Activate**.

**Manual installation**

1. Click the **Download** button above.
2. Sign in to your WooCommerce <<glossary:backend>>.
3. Go to **Plugins** > **Add new**. 
4. Click **Browse file**.
5. Upload the Plugin_WooCommerce_x.x.x.zip file.

# Configuration
1. Sign in to your WooCommerce backend.
2. Go to **WooCommerce** > **MultiSafepay settings**
3. On the **Account** tab, enter your [API key](/docs/sites#site-id-api-key-and-security-code).
4. On the **Order status** tab, confirm the match between WooCommerce order statuses and MultiSafepay order statuses, and then click **Save changes**.
4. On the **Options** tab, confirm your settings, and then click **Save changes**.
5. Go to **WooCommerce** > **Settings** > **Payments**. 
6. Enable the relevant payment methods and confirm the settings.
<br>

---

# User guide

## Languages

MultiSafepay payment pages and messages to customers (e.g. Second Chance emails, links, order confirmations) are supported in several languages. 

However, WooCommerce only supports the language of your ecommerce platform, irrespective of the customer's language or country, or the language of the webshop (if you use a third-party plugin for a multi-lingual webshop).

<details id="how-to-change-language">
<summary>How to change language</summary>
<br>

The plugin sets the language for payment pages and messages based on the Wordpress locale code `get_locale()` function.

To change this behavior, use the `multisafepay_customer_locale` filter hook in our plugin.

Ask your developer to read WordPress Developer Resources - <a href="https://developer.wordpress.org/plugins/hooks/filters/" target="_blank">Filters in Wordpress</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

Example implementation: 

``` 
add_filter('multisafepay_customer_locale', 'return_my_own_locale');
function return_my_own_locale($locale) {
  // Your conditions and logic to return a valid locale code
  return $custom_locale;
}
```
</details>

### TranslatePress

If you use the TranslatePress plugin for translations, to configure it for payment pages, follow these steps:

1. Sign in to your WooCommerce <<glossary:backend>>.
2. Go to **Settings** > **TranslatePress** > **Advanced**.
3. Scroll down and click **Exclude gettext string**.
4. In the **Domain** field, enter `multisafepay`.
5. Click **Add**.


## Notifications

<details id="multiSafepay-webhook">
<summary>MultiSafepay webhook</summary>
<br>

MultiSafepay uses a webhook to send you updates about orders and other notifications.

The webhook is triggered when the <<glossary:order status>> or <<glossary:transaction status>> changes, e.g. when:

- A customer completes payment.
- A customer's attempt to pay fails.
- You process a refund.

From WooCommerce version 4.7.0, notifications are sent via `POST` requests, instead of `GET` requests.  

However, sometimes the REST endpoint used to process notifications may be blocked by a firewall at server level, or by some WordPress plugins at application level. In this case, ensure you include MultiSafepay requests on your allow list.

</details>

## Order requests

<details id="how-to-modify-order-requests">
<summary>How to modify order requests</summary>
<br>

To change something in an OrderRequest before a transaction is processed, use the `multisafepay_order_request` filter hook in the plugin.

First, read the following:

- Wordpress – <a href="https://developer.wordpress.org/plugins/hooks/filters/" target="_blank">Filters in Wordpress</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- MultiSafepay GitHub – <a href="https://github.com/MultiSafepay/php-sdk/" target="_blank">MultiSafepay PHP-SDK</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

Example of how to implement and overwrite the shopping cart: 

``` javascript
add_filter( 'multisafepay_order_request', 'return_my_multisafepay_order_request' );
function return_my_multisafepay_order_request( \MultiSafepay\Api\Transactions\OrderRequest $order_request ) {
    // Your conditions and logic to return a valid order request
    // Register a CartItem
    $shopping_cart_items = array();
    $cart_item = new \MultiSafepay\ValueObject\CartItem();
    $cart_item->addName( 'The product name' )
              ->addQuantity( (int) 1 )
              ->addMerchantItemId( (string) 'SKU' )
              ->addUnitPrice( \MultiSafepay\WooCommerce\Utils\MoneyUtil::create_money( (float) 10.00, (string) 'EUR' ) )
              ->addTaxRate( '21' );
    $shopping_cart_items[] = $cart_item;
    // Register the CartItem in the ShoppingCart     
    $shopping_cart = new MultiSafepay\Api\Transactions\OrderRequest\Arguments\ShoppingCart($shopping_cart_items);
    // Overwrite the ShoppingCart    
    $order_request->addShoppingCart( $shopping_cart );
    // Overwrite the total amount of the transaction
    $order_request->addMoney(\MultiSafepay\WooCommerce\Utils\MoneyUtil::create_money( 12.10, 'EUR' ));
    return $order_request;
}
```
</details>

## Payment components

The plugin supports [payment components](/docs/payment-components/), which:

- Provide a seamless checkout experience to increase <<glossary:conversion>>.
- Encrypt customer payment details for secure processing.
- Shift responsibility for [PCI DSS compliance](/docs/pci-dss/) to MultiSafepay.

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: Amex, Maestro, Mastercard, and Visa
- <<glossary:BNPL>>: [Pay After Delivery installments](/docs/pay-after-delivery-installments)

</details>

<details id="how-to-activate-payment-components">
<summary>How to activate payment components</summary>
<br>

1. Sign in to your Wordpress backend.
2. Go to **WooCommerce** > **MultiSafepay settings** > **Payment methods** > 
3. Select the relevant payment methods, and click **Manage**.
4. In the **Payment Type** field, select **Payment component**.
5. Click **Save changes**.

💬 Support: If you're new to accepting card payments, email a request to activate them to <risk@multisafepay.com>

**⚠️ Note:*** If you have a custom checkout and encounter a conflict with the payment component, the Integration Team will do their best to provide support, but we can't guarantee compatibility in all cases.

</details>

## Payment links

<details id="how-to-generate-payment-links-in-your-backend">
<summary>How to generate payment links in your backend</summary>
<br>

To generate a payment link in your backend once an order is created, follow these steps:

1. Sign in to your WooCommerce backend.
2. Go to **WooCommerce** > **Orders** > **Add order**.
3. For instructions to register the order details, see WooCommerce - <a href="https://docs.woocommerce.com/document/managing-orders/#section-16" target="_blank">Managing orders</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
4. In **Order actions** panel, select the **Email invoice / order details to customer** option.  
5. Click **Create order**.  
  An email is sent to the customer containing the order details and a payment link. The payment link is also available to the customer in their private account, under **Orders**. 

</details>

## Payment methods

Before activating the relevant payment methods in your <<glossary:backend>>, you must first activate them in your MultiSafepay dashboard. See - [How to activate payment methods](/docs/payment-methods#activation).

By default, activated payment methods from your MultiSafepay account appear on the payment method list.

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/) (The card number field automatically detects the type of card (e.g. Visa) as the customer enters their card number.)
**💡 Tip!** In your settings, you can enable the function "group Credit cards" to show cards as a single payment method.
- Banking methods: All, except TrustPay
- <<glossary:BNPL>>: All
- Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [Google Pay](/docs/google-pay/), [PayPal](/docs/paypal/)
- Prepaid cards:
    - Baby Cadeaubon
    - Beauty and Wellness gift card
    - <a href="https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon" target="_blank">Boekenbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashioncheque.com/nl" target="_blank">Fashioncheque</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashion-giftcard.nl" target="_blank">Fashion gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Fietsenbon
    - <a href="https://www.good4fun.nl" target="_blank">Good4fun</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Goodcard
    - <a href="https://www.gezondheidsbon.nl/mhome" target="_blank">Gezondheidsbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.nationale-tuinbon.nl" target="_blank">Nationale tuinbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.parfumcadeaukaart.nl" target="_blank">Parfumcadeaukaart</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - [Paysafecard](/docs/paysafecard/)
    - <a href="https://www.podiumcadeaukaart.nl" target="_blank">Podium</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.sportenfitcadeau.nl" target="_blank">Sport en Fit</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.vvvcadeaukaarten.nl" target="_blank">VVV gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.webshopgiftcard.nl" target="_blank">Webshop gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.wellnessgiftcard.nl" target="_blank">Wellness gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Wijncadeau
    - <a href="https://www.winkelcheque.nl" target="_blank">Winkelcheque</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.yourgift.nl/" target="_blank">Yourgift</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

</details>

## Recurring payments

You need to [activate recurring payments](/docs/recurring-payments/) and then enable it in the plugin settings.

<details id="how-to-activate-recurring-payments">
<summary>How to activate recurring payments</summary>
<br>

1. Sign in to your Wordpress backend.
2. Go to **WooCommerce** > **MultiSafepay settings** > **Payment methods** 
3. Select relevant card payments, and then click **Manage**.
4. In the **Payment Type** field, select **Payment component**.
5. In the **Recurring payments** filed, select **Enabled**.
6. Click **Save changes**.

**⚠️ Note:** To activate recurring payments, ensure that the Payment component is enabled.

</details>

## Refunds

You can process [Full and partial refunds](/docs/refund-payments/) for all payment methods, **except** <<glossary:BNPL>> for which you can only process full refunds.

<details id="how-to-process-backend-refunds">
<summary>How to process refunds</summary>
<br>

1. Sign in to your WooCommerce <<glossary:backend>>. 
2. Go to **WooCommerce** > **Orders** and select the relevant order. 
3. In the item panel, click **Refund**.
4. You can select a full or a partial refund modifying the line items above. The amount will show in **Refund amount**.
5. There are two ways to process a refund:
   - **Refund via the selected payment method**, which will process the refund automatically (recommended).
   - **Refund manually**, where you will have to manually issue the payment through your MultiSafepay <<glossay:backend>>.

</details>

## Shipping orders

For <<glossary:BNPL>> orders, after shipment, you must change the order status from **Completed** to **Shipped**. This prevents the order expiring and triggers invoicing. 

If you change the <<glossary:order status>> to **Shipped** in your backend, the updated status is passed to your MultiSafepay dashboard automatically.

## Checkouts

The plugin supports the WooCommerce checkout and is compatible with most premium themes, unless you have a custom checkout.

### WooCommerce Checkout Blocks

You can use the Checkout Blocks for WooCommerce to customize your checkout. 
**⚠️ Note:** Only redirect payment methods are supported with this checkout at the moment.

## Second Chance

**MultiSafepay** will send two **Second Chance** reminder emails. In the emails, MultiSafepay will include a link to allow the consumer to finalize the payment. The first **Second Chance** email is sent **1 hour** after the transaction was initiated and the second after **24 hours**. To receive second chance emails, this option must also be activated within your **MultiSafepay** account. Otherwise, it will not work. See - [Second Chance - Activation](/docs/magento-2#second-chance) 

<details id="how-to-activate-second-chance">
<summary>How to activate Second Chance</summary>
<br>

1. Sign in to your **WooCommerce** <<glossary:backend>>.
2. Go to **WooCommerce** > **MultiSafepay Settings** > **Options** > **Second Chance**.
3. Check the box to activate **Second Chance** reminders.

</details>

## Surcharges

You can apply [surcharges](/docs/surcharges/) in the plugin when combined with a relevant third-party package. 

> ⚠️ Attention Dutch merchants
>
> We strongly recommend **not** applying surcharges to <<glossary:BNPL>> methods. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

<details id="how-to-apply-surcharges-with-third-party-packages">
<summary>How to apply surcharges with third-party packages</summary>
<br>

Third-party packages must follow WooCommerce and Wordpress development guidelines.

**Support**  

The Integration Team will do their best to help you install third-party packages, but we can't guarantee perfect compatibility.

</details>

## Troubleshooting

### Debug mode

<details id="how-to-activate-debug-mode">
<summary>How to activate debug mode</summary>
<br>

1. In your WooCommerce <<glossary:backend>>, go to **WooCommerce** > **MultiSafepay Settings** > **Options** > **Debug Mode**.
2. Click on the box to enable debug mode.

</details>

### Logs

<details id="how-to-access-MultiSafepay-logs">
<summary>How to access MultiSafepay logs</summary>
<br>

1. Sign in to your WooCommerce <<glossary:backend>>.
2. Go to **WooCommerce** > **MultiSafepay Settings** > **Logs**.
3. Select the relevant log and click **View**.

</details>

### Redirect URL not leading to thank you page 

- possible reasons

WC_Order::get_checkout_order_received_url() =>  
<https://woocommerce.github.io/code-reference/classes/WC-Order.html#method_get_checkout_order_received_url>  
does not return correct URL, which can be caused by a third party plugin making use of the "woocommerce_get_checkout_order_received_url" filter and returning a wrong value

- possible solutions

Use the filter "woocommerce_get_checkout_order_received_url", provided by WooCommerce, and re-format into the correct value.

 <a href="https://woocommerce.github.io/code-reference/files/woocommerce-includes-class-wc-order.html#source-view.1777" target="_blank">WooCommerce code reference</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>  
<a href="https://developer.wordpress.org/reference/functions/add_filter/" target="_blank">WooCommerce add filter</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

## Updates

You can update the plugin in your backend and the CMS marketplace, or via SFTP.

<details id="how-to-update-in-your-backend">
<summary>How to update in your backend</summary>
<br>

&nbsp; **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.
</details>
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: <a href=\"https://github.com/MultiSafepay/woocommerce/issues\" target=\"_blank\"> create a technical issue</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)
