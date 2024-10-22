---
title: "Shopware 6"
category: 62962dd7e272a6002ebbbbc5
order: 17
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manuals for MultiSafepay's free plugins."
slug: 'shopware-6'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Shopware_6.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<div style="display: flex; flex-wrap: wrap;">

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/shopware6/" target="_blank"><i class="icon-external-link"></i> <span>Source code</span></a>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://github.com/MultiSafepay/shopware6/blob/master/CHANGELOG.md" target="_blank"><span>Changelog</span></a>

</div>

## Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- Shopware 6.4.11.x or higher, 6.5.x.x and 6.6.x.x <!--_(<a href="https://www.shopware.com/en/pricing" target="_blank">Starter Edition</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> supported)_-->
- Tested on Shopware 6.4.20.2, 6.5.8.11, 6.6.3.0 and PHP 8.1–8.2

## Installation and configuration

&nbsp; **💡 Tip!** We recommend first installing the plugin in a test environment, following the Shopware 6 installation procedure. Always make a backup.

### Marketplace installation
Get the free MultiSafepay plugin from the <a href="https://store.shopware.com/en/mltis59465832976f/multisafepay-online-payments-for-shopware-ideal-cards-klarna-alipay-etc..html" target="_blank">Shopware 6 marketplace</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> and connect your webshop with your Shopware account.

### Configuration

1. Sign in to your Shopware 6 <<glossary:backend>>.
2. Go to **Extensions** > **My extensions**.
3. In the **MultiSafepay** module, click **⋯** > **Configure**.
4. Set the environment to **Test** or **Live**.
5. In the **API key** field, enter your <a href="https://docs.multisafepay.com/docs/sites#site-id-api-key-and-security-code" target="_blank">API key</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> and click **Validate API credentials**.
6. Click **Save**.

### Composer installation
Run the following command in the root of your Shopware root directory. Make sure the composer is installed on your hosting server.

```
composer require multisafepay/shopware6
```

<br>

---

## User guide

### Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/docs/payment-pages/). This is particularly useful for integrating gift cards.

<details id="how-to-configure-generic-gateways">
<summary>How to configure generic gateways</summary>
<br>

1. Sign in to your Shopware 6 backend.
2. Go to **MultiSafepay settings**.
3. Set the relevant [payment method gateway IDs](/reference/gateway-ids/).

You can filter generic gateways by country, and minimum and maximum amount.

</details>

### Payment components

The plugin supports [payment components](/docs/payment-components/), which:

- Provide a seamless checkout experience to increase <<glossary:conversion>>.
- Encrypt customer payment details for secure processing.
- Shift responsibility for [PCI DSS compliance](/docs/pci-dss/) to MultiSafepay.

<details id="how-to-activate-payment-components">
<summary>How to activate payment components</summary>
<br>

If you're new to accepting card payments, email a request to activate them to <risk@multisafepay.com>

1. Sign in to your Shopware backend.
2. Go to **Settings** > **Payment**.
3. Select each payment method, and then enable the **Component** toggle.

For questions, email <integration@multisafepay.com>

**⚠️ Note:** If you have a custom checkout and encounter a conflict with the payment component, the Integration Team will do their best to provide support, but we can't guarantee compatibility in all cases.

</details>

### Payment methods

Before activating the relevant payment methods in your <<glossary:backend>>, you must first activate them in your MultiSafepay dashboard. See - [How to activate payment methods](/docs/payment-methods#activation).

<details id="activate-payment-methods">
<summary>How to activate payment methods</summary>
<br>

1. Sign in to your Shopware 6 <<glossary:backend>>.
2. Go to **Settings** > **Payment Methods**.
3. Filter the relevant payment methods that have been activated in your MultiSafepay dashboard, e.g.,  
   Mastercard | MultiSafepay module for Shopware 6.
4. Click **Activate**.

**💡 Tip!** You can handle the positioning of payment methods in the checkout by clicking **Edit display order in checkout**.

</details>

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- Cards: [All](/docs/card-payments/)
- Banking methods: All, except iDEAL QR
- <<glossary:BNPL>>: All
- Wallets: [Alipay](/docs/alipay/), [Amazon Pay](/docs/amazon-pay/), [Apple Pay](/docs/apple-pay/),  [Google Pay](/docs/google-pay), and [PayPal](/docs/paypal/), [WeChat Pay](/docs/wechat-pay/),
- Prepaid cards:
    - Beauty and Wellness gift card
    - <a href="https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon" target="_blank">Boekenbon</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashioncheque.com/nl" target="_blank">Fashioncheque</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - <a href="https://www.fashion-giftcard.nl" target="_blank">Fashion gift card</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
    - Fietsenbon
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

### Recurring payments

[Recurring payments](/docs/recurring-payments) are supported.

<details id="how-to-enable-recurring-payments">
<summary>How to enable recurring payments</summary>
<br>

[Activate recurring payments](/docs/recurring-payments) and then:
1. Sign in to your Shopware backend.
2. Go to **Settings** > **Payment**.
3. Select each payment method, and then enable the **Tokenization** toggle.

</details>

### Refunds

[Full and partial refunds](/docs/refund-payments/) **except** for <<glossary:BNPL>> methods are supported in your MultiSafepay dashboard and backend.  
You cannot refund more than the original amount in your backend.

<details id="how-to-process-backend-refunds">
<summary>How to process backend refunds</summary>
<br>

1. In your Shopware 6 backend, go to the **Order details** page.
2. In the **Refund** field, enter the refund amount. 

</details>

### Shipping orders

For <<glossary:BNPL>> orders, after shipment, you must change the order status from **Completed** to **Shipped**. This prevents the order expiring and triggers invoicing. 

If you change the <<glossary:order status>> to **Delivered** in your backend, the updated status is passed to your MultiSafepay dashboard automatically.

## Updates

&nbsp; **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

### Marketplace update
Following the steps described in the installation process from <a href="https://store.shopware.com/en/mltis59465832976f/multisafepay-online-payments-for-shopware-ideal-cards-klarna-alipay-etc..html" target="_blank">Shopware 6 marketplace</a>.

### Composer update
By executing the following command within the root directory of Shopware 6:

```
composer update multisafepay/shopware6
```

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+31020\">support@myshop.com</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: <a href=\"https://github.com/MultiSafepay/shopware6/issues\" target=\"_blank\"> create a technical issue</a></li>\n    <li>Join the <a href=\"https://join.slack.com/t/shopwarenederland/shared_invite/zt-61exftia-TFYlw5LzmIBnz7Epq07goQ\">official Shopware 6 Slack channel</a></li>\n    <li>Join the private <a href=\"https://shopwarenederland.slack.com/archives/G0146NKFJTT\">MultiSafepay Shopware 6 Slack channel</a></li>\n  </ul>  \n  <p>For support for Shopware 6 Professional/Enterprise, email <a href=\"mailto:sales@multisafepay.com\">sales@multisafepay.com</p>\n</blockquote>"
}
[/block]

[Top of page](#)
