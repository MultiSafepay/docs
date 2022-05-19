---
title : "Magento 1 plugin"
download_url : "https://github.com/MultiSafepay/docs/raw/master/static/plugin-downloads/magento1/Plugin_Magento_3.1.3.zip"
faq: "."
type: 'Plugin'
meta_title: "Magento 1 plugin - MultiSafepay Docs"
meta_description: "Free plugin to integrate MultiSafepay payment solutions with Magento 1."
logo: "/logo/Plugins/Magento.svg"
changelog: https://docs.multisafepay.com/integration/ready-made/magento1/changelog/
weight: 02
title_short: "Magento 1"
layout: 'single'
url: '/magento-1/'
aliases: 
    - /plugins/magento1
    - /integrations/plugins/magento1
    - /integrations/magento1
    - /plugins/magento1/manual
    - /integrations/plugins/magento1/manual
    - /integrations/magento1/manual
    - /integrations/ecommerce-integrations/magento1
    - /payments/integrations/ecommerce-platforms/magento1/
    - /ecommerce-platforms/magento-1/
    - /integrations/magento1/faq/payment-fee-surcharges/
    - /payments/integrations/ecommerce-platforms/magento1/faq/applying-surcharges/
    - /magento-1/surcharges/
    - /integrations/ecommerce-integrations/magento1/faq/currency-automatically-converted-into-euro-magento1/
    - /payments/integrations/ecommerce-platforms/magento1/faq/changing-your-webshop-currency/
    - /magento-1/changing-currency/
    - /integrations/magento1/faq/how-can-i-update-the-plugin-for-magento1/
    - /integrations/magento1/faq/is-the-multisafepay-magento-1-plugin-compatible-with-picqer/
    - /payments/integrations/ecommerce-platforms/magento1/faq/compatibility-with-picqer/
    - /magento-1/picqer/
    - /integrations/ecommerce-integrations/magento1/faq/generic-gateways/
    - /payments/integrations/ecommerce-platforms/magento1/faq/generic-gateways/
    - /magento-1/configuring-generic-gateways/
    - /integrations/magento1/faq/tokenization-magento1/
    - /payments/integrations/ecommerce-platforms/magento1/faq/enabling-tokenization/
    - /magento-1/recurring-payments/
    - /integrations/magento1/faq/can-i-remove-the-gender-and-date-of-birth-field-for-the-klarna-payment-method-in-the-checkout/
    - /payments/integrations/ecommerce-platforms/magento1/faq/removing-klarna-fields/
    - /magento-1/checkout-fields/
    - /integrations/magento1/faq/request-refund/
    - /payments/integrations/ecommerce-platforms/magento1/faq/processing-refunds/
    - /magento-1/refunds/
    - /integrations/magento1/faq/ship-automatically-in-magento1/
    - /payments/integrations/ecommerce-platforms/magento1/faq/shipped-status/
    - /magento-1/shipped-status/
    - /payments/integrations/ecommerce-platforms/magento1/faq/supported-magento1-checkouts/
    - /magento-1/checkouts/
    - /integrations/ecommerce-integrations/magento1/faq/how-can-i-update-the-plugin-for-magento1/
    - /payments/integrations/ecommerce-platforms/magento1/faq/updating-the-plugin/
    - /magento-1/updates/
---

{{< alert-notice >}} Magento 1 is end-of-life. If you are still running Magento 1, action is required. MultiSafepay has partnered with Mage One to continue supporting Magento 1. For more information and instructions, see MultiSafepay blog – [Magento 1: The final weeks](https://bit.ly/2YX2LGL).{{< /alert-notice >}}

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with Magento 1 via SFTP upload.

You can also install the plugin via .ZIP file upload in Connect.

MultiSafepay supports most Magento functionalities. For any questions, email <integration@multisafepay.com>

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- Magento Open Source 1.7 - 1.9
- Tested on PHP 7.0

{{< /details >}}

{{< details title="Support" >}}
&nbsp; 
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue
- [Magento Slack channel](https://magentocommeng.slack.com) #multisafepay-payments

Our Magento 1 plugin is professionally supported by a certified Magento 1 Solution Specialist and receives regular updates to support the latest features provided by Magento and MultiSafepay.

{{< /details >}}

{{< details title="Payment methods" >}}

- Cards: All except V Pay
- Banking methods: All, **except** TrustPay
- Pay later methods: All
- Wallets: [Alipay](/payment-methods/alipay), [Apple Pay](/payment-methods/apple-pay), [PayPal](/payment-methods/paypal)
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
    - [Paysafecard](/payment-methods/paysafecard)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl)

See also [MultiSafepay gateway](/developer/generic-gateways/#multisafepay-gateways).

{{< /details >}}

## Installation

 1. Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.
 2. Unpack the content of the .ZIP file in the root of your webshop.
 3. Sign in to your Magento 1 backend.
 4. Go to **System** > **Configuration** > **Cache**, and clear your invalid cache.
 5. Move all files and folders from Plugin_Magento_x.x.x to the root.  
 6. Add the content of the app, lib, and media folders to the existing folders with the same name.
 7. Sign out.

## Configuration
1. Sign in to your Magento 1 backend.
2. Go to **System** > **Configuration** > **MultiSafepay x.x.x** > **Connect settings**.  
    This page contains all main settings and is used for all gateways and gift cards.  
    To find your API key, see [API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).  
    From version 3.0.0, the plugin only needs your API key. Your account ID, site ID, and site secure code are no longer needed.
3. To configure your selected payment methods, go to **System** > **Configuration** > **MultiSafepay x.x.x**:
    - **Connect MultiSafepay gateways**  
    - **MultiSafepay gift cards**  
    Make sure you have [activated the payment methods](/payments/activating-payment-methods/) in your MultiSafepay dashboard.

## User guide

### Refunds

- [MultiSafepay dashboard](/refunds/full-partial/): Full refunds (may not appear in your backend)
-  Magento 1 backend:  
    - Full refunds and [credit memos](https://docs.magento.com/m1/ce/user_guide/order-processing/credit-memo-create.html)
    - Refunding more than the original transaction is **not** supported
- For [pay later methods](/payments/methods/pay-later/), you can only refund a selected item from the order, not a set amount. If you enter an amount instead of selecting an item, the entire order is refunded.

{{< details title="Processing backend refunds" >}}

1. Sign in to your Magento 1 backend. 
2. Go to **System** > **Configuration** > **MultiSafepay** > **Connect settings**.
3. Check that you have:
    - Entered an [API key](/glossaries/multisafepay-glossary/#api-key)
    - Enabled the **Credit Memo** option
4. Search for and open the order you want to refund.
5. Click the **Invoices** tab on the left of the **Order overview**.
6. Open the invoice, and click **Credit memo** at the top right of the overview.
7. Enter the refund amount, and then click **Refund online** to send the request to MultiSafepay.

{{< /details >}}

### Updates

You can update the plugin in your Magento 1 backend or the CMS marketplace, or using SFTP.

{{< details title="Updating via SFTP" >}}

1. Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.
2. From the [Magento 1 manual](/payments/integrations/ecommerce-platforms/magento1/#manual), download the plugin again.
3. Follow the Installation and configuration instructions from step 2.

{{< /details >}}

### Surcharges

You can:

- Apply [surcharges](/about-payments/surcharges/) of a percentage or a fixed amount to transactions for every payment method.
- Set the tax class for surcharges.
- Show transaction amounts excluding the surcharge at checkout. Surcharges are always included at checkout.
- Show surcharges with our without VAT at checkout.

{{< details title="Applying surcharges in your backend" >}}

1. Sign in to your Magento 1 backend.
2. Select systems and configuration.
3. In the MultiSafepay module, select the **Option connect** gateway.
4. Select the relevant payment method.
5. Under **Payment fee amount**, enter a surcharge percentage or fixed amount. 
6. Place a test order to verify whether the fee has been correctly processed.

{{< /details >}}

{{< alert-notice >}} **Attention Dutch merchants** <br>  We strongly recommend that you do **not** apply surcharges to [pay later methods](/payment-methods/pay-later/). This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM). {{< /alert-notice >}}

### Generic gateways

The Magento 1 plugin offers 3 [generic gateways](/developer/generic-gateways/) and 3 generic gift cards. Generic gateways support:

- All payment methods
- Refunds 
- [Backend](/glossaries/multisafepay-glossary/#backend) orders

You can filter generic gateways by country, and minimum and maximum amount.

{{< details title="Configuring generic gateways" >}}

1. Sign in to your Magento 1 backend. 
2. Go to **System** > **Configuration** > **MultiSafepay** > **Connect gateways** > **Generic 1/2/3**.
3. Set the relevant [payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids) and the gateway label.
4. Set how to display the payment method logos. 
5. For pay later methods, set whether to include the shopping cart.

{{< /details >}}

### Currencies

The default currency is EUR. 

{{< details title="Changing the default currency" >}}

1. Sign in to your Magento 1 backend. 
2. Go to **System** > **Configuration** > **MultiSafepay x.x.x** > **Connect settings**.
3. Under **Allow currency conversion to Euro**, change to **No**.

{{< /details >}}

### Recurring payments

{{< details title="Enabling recurring payments" >}}

1. Sign in to your Magento 1 backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay** > **MultiSafepay settings**.

For more information, see [Recurring Payments](/features/recurring-payments).

**Credit cards**
Recurring Payments are not available for the generic credit card gateway. You must enable the Visa, Mastercard, and/or Maestro gateways separately. This displays the **Save card** option at checkout.

{{< /details >}}

### Pay later orders

The status of all complete orders automatically changes to **Shipped** in order to collect funds from pay later payment methods.

#### Checkout fields for Klarna

Klarna requires the customer's gender and date of birth. By default, the customer enters their birthday in the Magento checkout in the Klarna payment method fields, and their gender is automatically populated by the core Magento field.

You can disable both fields in the checkout. The customer enters this information on the MultiSafepay payment page instead.

{{< details title="Disabling Klarna checkout fields" >}}

This change is only for Magento developers. We recommend testing the change and placing it in your local folder.

1. Open `app\code\community\MultiSafepay\Msp\Model\Gateway\Klarna.php`.
2. Comment this line `protected $_formBlockType = 'msp/klarna';`
3. Save the file.
4. Clear your cache.
5. Test the change.

{{< /details >}}

### Picquer

{{< details title="Enabling compatibility with Picquer" >}}

To make the MultiSafepay Magento 1 plugin compatible with Picqer, follow two additional steps, because orders must not receive **Cancelled** status.

1. In your Magento 1 [backend](/glossaries/multisafepay-glossary/#backend), go to the MultiSafepay Connect settings.
2. Link **Expired** status to **Waiting** status.
2. Open `app\code\community\MultiSafepay\Msp\Model\Base.php`, and then copy the file to the local folder in the Magento structure.
3. Find the line `$order > cancel();` at the expired signal and remove it.

All expired orders retain **Waiting** status until you cancel them:

- Manually
- With a custom cronjob 
- Using a plugin

{{< /details >}}

### Checkouts

The plugin is compatible with most Magento 1 checkouts. However, we cannot guarantee that all checkout features will function properly.

We test the plugin with Magento 1 core checkout and OneStepCheckout.com (Idev).

**Note:** Always test OneStepCheckout to make sure it is compatible with your configuration of the plugin.

