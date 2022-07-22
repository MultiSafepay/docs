---
title: "WooCommerce"
category: 62962dd7e272a6002ebbbbc5
order: 118
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free plugin."
slug: 'woocommerce'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/WooCommerce.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #006ba1; color: #ffffff; text-decoration: none;" href="https://github.com/MultiSafepay/WooCommerce/releases/download/4.17.2/Plugin_WooCommerce_4.17.2.zip" target="_self"><span>Download</span><i class="icon icon-download" style="margin-left: 0.6em;"> </i></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/WooCommerce" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/WooCommerce/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

# Prequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- Wordpress 5.0
- PHP 7.2

# How to install

> **Tip!** We recommend first installing the plugin in a test environment, following the WooCommerce installation procedure. Always make a backup.

There are two ways to install the plugin:

**Wordpress installation**

1. Sign in to your WooCommerce backend.
2. Go to **Plugins** > **Add new**.
3. Search for **MultiSafepay**.
4. For the **MultiSafepay plugin for WooCommerce**, click the **Install now** button.

**Manual installation**

1. Click the **Download** button above.
2. Sign in to your WooCommerce <<glossary:backend>>.
3. Go to **Plugins** > **Add new**. 
4. Click **Browse file**.
5. Upload the Plugin_WooCommerce_x.x.x.zip file.

# How to configure
1. Sign in to your WooCommerce backend.
2. Go to **WooCommerce** > **MultiSafepay settings**
3. On the **Account** tab, enter your [API key](/docs/sites#site-id-api-key-and-security-code).
4. On the **Order status** tab, confirm the match between WooCommerce order statuses and MultiSafepay order statuses, and then click **Save changes**.
4. On the **Options** tab, confirm your settings, and then click **Save changes**.
5. On the **WooCommerce** > **Settings** > **Payments**. Enable the relevant payment methods and confirm the settings.
<br>

---

# User guide

## Generic gateways

The plugin supports generic gateways, which allows you to add a payment method manually. This is particularly useful for integrating gift cards specific to your business. 

Supported since release: 4.5.0, March 31st 2021.

<details id="how-to-configure-generic-gateways">
<summary>How to configure generic gateways</summary>
<br>

1. Sign in to your backend.
2. Go to **Settings** > **Payments** tab > **Generic gateway**.
3. Set the relevant [payment method gateway IDs](/reference/gateway-ids/), and the gateway logo and label.
4. For <<glossary:BNPL>> orders, include the shopping cart in refunds.

You can:

- Filter the generic gateway by country, and minimum and maximum amount.
- Set a custom initial <<glossary:order status>>.
- Process full and partial refunds (except for <<glossary:BNPL>> orders), and backend orders.

</details>

## Languages

MultiSafepay payment pages and messages to customers (e.g. Second Chance emails, links, order confirmations) are supported in several languages. 

However, WooCommerce only supports the language of your ecommerce platform, irrespective of the customer's language or country, or the language of the webshop (if you use a third-party plugin for a multi-lingual webshop).

<details id="how-to-change-language">
<summary>How to change language</summary>
<br>

The plugin sets the language for payment pages and messages based on the Wordpress locale code `get_locale()` function.

To change this behavior, use the `multisafepay_customer_locale` filter hook in our plugin.

Ask your developer to read WordPress Developer Resources - [Filters in Wordpress](https://developer.wordpress.org/plugins/hooks/filters/).

Example implementation: 

``` 
add_filter('multisafepay_customer_locale', 'return_my_own_locale');
function return_my_own_locale($locale) {
  // Your conditions and logic to return a valid locale code
  return $custom_locale;
}
```
</details>

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

- Wordpress – [Filters in Wordpress](https://developer.wordpress.org/plugins/hooks/filters/)
- MultiSafepay GitHub – [MultiSafepay PHP-SDK](https://github.com/MultiSafepay/php-sdk/)

Example of how to implement and overwrite the shopping cart: 

``` 
add_filter('multisafepay_order_request', 'return_my_multisafepay_order_request');
function return_my_own_locale( \MultiSafepay\Api\Transactions\OrderRequest $order_request) {
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

<details id="how-to-activate-payment-components">
<summary>How to activate payment components</summary>
<br>

If you're new to accepting credit card payments, email a request to activate them to <sales@multisafepay.com>

1. Sign in to your Wordpress backend.
2. Go to **WooCommerce** > **MultiSafepay settings** > **Payment methods** > **Credit card**, and then click **Manage**.
3. Select the **Payment components** checkbox.
4. Click **Save changes**.

For questions, email <integration@multisafepay.com>

> **Note:** If you have a custom checkout and encounter a conflict with the payment component, the Integration Team will do their best to provide support, but we can't guarantee compatibility in all cases.

</details>

## Payment links

<details id="how-to-generate-payment-links-in-your-backend">
<summary>How to generate payment links in your backend</summary>
<br>

To generate a payment link in your backend once an order is created, follow these steps:

1. Sign in to your WooCommerce backend.
2. Go to **WooCommerce** > **Orders** > **Add order**.
3. For instructions to register the order details, see WooCommerce - [Managing orders](https://docs.woocommerce.com/document/managing-orders/#section-16).
4. In **Order actions** panel, select the **Email invoice / order details to customer** option.  
5. Click **Create order**.  
  An email is sent to the customer containing the order details and a payment link. The payment link is also available to the customer in their private account, under **Orders**. 

</details>

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/) (The credit card number field automatically detects the type of card (e.g. Visa) as the customer enters their card number.)
- Banking methods: All, except TrustPay
- <<glossary:BNPL>>: All
- Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
- Prepaid cards:
    - Baby Cadeaubon
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Good4fun](https://www.good4fun.nl)
    - Goodcard
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/docs/paysafecard/)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl/)

</details>

## Recurring payments

You need to [activate recurring payments](/docs/recurring-payments/) and then enable it in the plugin settings.

## Refunds

You can process [Full and partial refunds](/docs/refund-payments/) for all payment methods, **except** <<glossary:BNPL>> for which you can only process full refunds.

## Shipping orders

For <<glossary:BNPL>> orders, after shipment, you must change the order status from **Completed** to **Shipped**. This prevents the order expiring and triggers invoicing. 

If you change the <<glossary:order status>> to **Shipped** in your backend, the updated status is passed to your MultiSafepay dashboard automatically.

## Surcharges

You can apply [surcharges](/docs/surcharges/) in the plugin when combined with a relevant third-party package. 

> ⚠️ **Attention Dutch merchants** 
> We strongly recommend **not** applying surcharges to <<glossary:BNPL>> methods. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

<details id="how-to-apply-surcharges-with-third-party-packages">
<summary>How to apply surcharges with third-party packages</summary>
<br>

Third-party packages must follow WooCommerce and Wordpress development guidelines.

**Support**  

The Integration Team will do their best to help you install third-party packages, but we can't guarantee perfect compatibility.

</details>

## Updates

You can update the plugin in your backend and the CMS marketplace, or via SFTP.

<details id="how-to-update-in-your-backend">
<summary>How to update in your backend</summary>
<br>

> **Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

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