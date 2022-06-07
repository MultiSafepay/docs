---
title : "WooCommerce plugin"
github_url : "https://github.com/MultiSafepay/WooCommerce"
download_url : "https://github.com/MultiSafepay/WooCommerce/releases/download/4.15.0/Plugin_WooCommerce_4.15.0.zip"
changelog_url : "."
repo_url : "MultiSafepay/WooCommerce"
meta_title: "WooCommerce plugin - MultiSafepay Docs"
meta_description: "Integrate MultiSafepay payment solutions into your Wordpress WooCommerce webshop. MultiSafepay Docs provides information about getting started, building and testing integrations."
logo: "/logo/Plugins/WooCommerce.svg"
weight: 03
title_short: "WooCommerce"
type: 'Plugin'
url: '/woo-commerce/'
layout: 'single'
changelog : "https://github.com/MultiSafepay/WooCommerce/blob/master/CHANGELOG.md"
aliases: 
    - /plugins/woocommerce
    - /integrations/plugins/woocommerce
    - /integrations/woocommerce
    - /plugins/woocommerce/manual
    - /integrations/plugins/woocommerce/manual
    - /integrations/woocommerce/manual
    - /integrations/ecommerce-integrations/woocommerce
    - /payments/integrations/ecommerce-platforms/woocommerce/manual
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/supported-payment-methods/
    - /payments/integrations/ecommerce-platforms/woocommerce/
    - /ecommerce-platforms/woocommerce/
    - /woo-commerce/payment-components/
    - /integrations/ecommerce-integrations/woocommerce/faq/rest-endpoint-is-blocked/
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/allowing-notifications/
    - /woo-commerce/notifications/
    - /integrations/woocommerce/faq/payment-fee-surcharges/
    - /woo-commerce/surcharges/
    - /integrations/ecommerce-integrations/woocommerce/faq/generic-gateways/
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/configuring-generic-gateways/
    - /woo-commerce/generic-gateways/
    - /woo-commerce/configuring-generic-gateways/
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/enabling-recurring-payments/
    - /woo-commerce/recurring-payments/
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/generating-payment-links/
    - /woo-commerce/payment-links/
    - /integrations/woocommerce/faq/how-can-i-customize-the-language-of-payment-page-and-emails/
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/modifying-order-requests/
    - /woo-commerce/modifying-order-requests/
    - /integrations/woocommerce/faq/refunding-woocommerce/
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/processing-refunds/
    - /woo-commerce/refunds/
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/changing-order-status-to-shipped/
    - /woo-commerce/shipping/
    - /integrations/woocommerce/faq/how-can-i-customize-the-language-of-payment-page-and-emails/
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/payment-page-and-messages-to-customer-in-other-language/
    - /woo-commerce/customer-language/
    - /integrations/woocommerce/faq/how-can-i-update-the-plugin-for-woocommerce/
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/updating-the-plugin/
    - /woo-commerce/updates/
    - /woo-commerce/credit-card-gateway/
---

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with WooCommerce, a free, open-source ecommerce platform for Wordpress.

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- Wordpress 5.0
- PHP 7.2

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

## Installation

{{< blue-notice >}} We recommend first installing the plugin in a test environment, following the WooCommerce installation procedure. Always make a backup. {{< /blue-notice >}}

There are two ways to install the plugin:

**Manual installation**

1. Click the **Download** button above.
2. Sign in to your WooCommerce backend.
3. Go to **Plugins** > **Add new**. 
4. Click **Browse file**.
5. Upload the Plugin_WooCommerce_x.x.x.zip file.

**Wordpress installation**

1. Sign in to your WooCommerce backend.
2. Go to **Plugins** > **Add new**.
3. Search for **MultiSafepay**. 
4. For the **MultiSafepay plugin for WooCommerce**, click the **Install now** button.

## Configuration
1. Sign in to your WooCommerce backend.
2. Go to **WooCommerce** > **MultiSafepay settings**
3. On the **Account** tab, enter your [API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).
4. On the **Order status** tab, confirm the match between WooCommerce order statuses and MultiSafepay order statuses, and then click **Save changes**.
4. On the **Options** tab, confirm your settings, and then click **Save changes**.
5. On the **WooCommerce** > **Settings** > **Payments**. Enable the relevant payment methods and confirm the settings.

## User guide

### Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/payment-pages/). This is particularly useful for integrating gift cards.

{{< details title="Configuring generic gateways" >}}

1. Sign in to your backend.
2. Go to **Settings** > **Payments** tab > **Generic gateway**.
3. Set the relevant [payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids), and the gateway logo and label.
4. For [pay later](/payment-methods/pay-later/) methods, include the shopping cart in refunds.

You can:

- Filter the generic gateway by country, and minimum and maximum amount.
- Set a custom initial order status.
- Process full and partial refunds (except for pay later methods), and backend orders.

{{< /details >}}

### Languages

MultiSafepay payment pages and messages to customers (e.g. Second Chance emails, links, order confirmations) are supported in several languages. 

However, WooCommerce only supports the language of your ecommerce platform, irrespective of the customer's language or country, or the language of the webshop (if you use a third-party plugin for a multi-lingual webshop).

{{< details title="Changing language" >}}

The plugin sets the language for payment pages and messages based on the Wordpress locale code `get_locale()` function.

To change this behavior, use the `multisafepay_customer_locale` filter hook in our plugin.

Ask your developer to read WordPress Developer Resources - [Filters in Wordpress](https://developer.wordpress.org/plugins/hooks/filters/).
&nbsp;

Example implementation: 

``` 
add_filter('multisafepay_customer_locale', 'return_my_own_locale');
function return_my_own_locale($locale) {
  // Your conditions and logic to return a valid locale code
  return $custom_locale;
}
```
{{< /details >}}

### Notifications

{{< details title="MultiSafepay webhook" >}}

MultiSafepay uses a webhook to send you updates about orders and other notifications.

The webhook is triggered when the order or transaction status changes, e.g. when:

- A customer completes payment.
- A customer's attempt to pay fails.
- You process a refund.

From WooCommerce version 4.7.0, notifications are sent via `POST` requests, instead of `GET` requests.  

However, sometimes the REST endpoint used to process notifications may be blocked by a firewall at server level, or by some WordPress plugins at application level. In this case, ensure you include MultiSafepay requests on your allow list. 

For more information, see [Webhook](/integrations/webhooks/).

{{< /details >}}

### Order requests

{{< details title="Modifying order requests" >}}

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
{{< /details >}}

### Payment components

The plugin supports [payment components](/payment-components/), which:

- Provide a seamless checkout experience to increase conversion.
- Encrypt customer payment details for secure processing.
- Shift responsibility for [PCI DSS compliance](/glossaries/multisafepay-glossary/#payment-card-industry-data-security-standard-pci-dss) to MultiSafepay.

{{< details title="Activating payment components" >}}

If you're new to accepting credit card payments, email a request to activate them to <sales@multisafepay.com>

1. Sign in to your Wordpress backend.
2. Go to **WooCommerce** > **MultiSafepay settings** > **Payment methods** > **Credit card**, and then click **Manage**.
3. Select the **Payment components** checkbox.
4. Click **Save changes**.

For questions, email <integration@multisafepay.com>

**Note:** If you have a custom checkout and encounter a conflict with the payment component, the Integration Team will do their best to provide support, but we can't guarantee compatibility in all cases.

{{< /details >}}

### Payment links

{{< details title="Generating payment links in your backend" >}}

To generate a payment link in your backend once an order is created, follow these steps:

1. Sign in to your WooCommerce backend.
2. Go to **WooCommerce** > **Orders** > **Add order**.
3. For instructions to register the order details, see WooCommerce - [Managing orders](https://docs.woocommerce.com/document/managing-orders/#section-16).
4. In **Order actions** panel, select the **Email invoice / order details to customer** option.  
5. Click **Create order**.  
  An email is sent to the customer containing the order details and a payment link. The payment link is also available to the customer in their private account, under **Orders**. 

  {{< /details >}}

### Payment methods

{{< details title="Payment methods" >}}

- Cards: [All](/payment-methods/credit-debit-cards/) (The credit card number field automatically detects the type of card (e.g. Visa) as the customer enters their card number.)
- Banking methods: [All](/payment-methods/banks/), except TrustPay
- Pay later methods: [All](/payment-methods/pay-later/)
- Wallets: [Alipay](/payment-methods/alipay), [Apple Pay](/payment-methods/apple-pay), [PayPal](/payment-methods/paypal)
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
    - [Paysafecard](/payment-methods/paysafecard)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl/)

{{< /details >}}

### Recurring payments

You need to [enable recurring payments](/features/recurring-payments/) in your MultiSafepay dashboard and then in the plugin settings.

### Refunds

You can process [full and partial refunds](/refunds/#full-and-partial-refunds) for all payment methods, **except** [pay later methods](/payment-methods/pay-later) for which you can only process full refunds.

### Shipping orders

For [pay later](/payment-methods/pay-later/) orders, after shipment, you must change the order status from **Completed** to **Shipped**. This prevents the order expiring and triggers invoicing. 

If you change the order status to **Shipped** in your backend, the updated status is passed to your MultiSafepay dashboard automatically.

### Surcharges

You can apply [surcharges](/surcharges/) in the plugin when combined with a relevant third-party package. 

{{< details title="Applying surcharges with third-party packages" >}}
Third-party packages must follow WooCommerce and Wordpress development guidelines.

**Support**  
The Integration Team will do their best to help you install third-party packages, but we can't guarantee perfect compatibility.

**Attention Dutch merchants** 

We strongly recommend **not** applying surcharges to [pay later methods](/payment-methods/pay-later/). This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).
{{< /details >}}

### Updates

You can update the plugin in your backend and the CMS marketplace, or via SFTP.

{{< details title="Updating in your backend" >}}

**Notes:** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.
{{< /details >}}