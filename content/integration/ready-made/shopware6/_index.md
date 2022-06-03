---
title : "Shopware 6 plugin"
meta_title: "Shopware 6 plugin - MultiSafepay Docs"
github_url : "https://github.com/MultiSafepay/shopware6/"
download_url : "https://github.com/MultiSafepay/shopware6/releases/download/2.5.3/Plugin_Shopware6_2.5.3.zip"
logo: "/logo/Plugins/Shopware_6.svg"
weight: 06
title_short: "Shopware 6"
type: 'Plugin'
layout: 'single'
changelog : "https://github.com/MultiSafepay/shopware6/blob/master/CHANGELOG.md"
url: '/shopware-6/'
aliases: 
    - /plugins/shopware6
    - /integrations/plugins/shopware6
    - /integrations/shopware6
    - /plugins/shopware6/manual
    - /integrations/plugins/shopware6/manual
    - /integrations/shopware6/manual
    - /integrations/ecommerce-integrations/shopware6
    - /payments/integrations/ecommerce-platforms/shopware6/
    - /ecommerce-platforms/shopware-6/
    - /integrations/ecommerce-integrations/shopware6/faq/generic-gateways/
    - /payments/integrations/ecommerce-platforms/shopware6/faq/generic-gateways/
    - /shopware-6/generic-gateways/
    - /shopware-6/configuring-generic-gateways/
    - /integrations/ecommerce-integrations/shopware6/faq/enable-tokenization-within-shopware6
    - /payments/integrations/ecommerce-platforms/shopware6/faq/enabling-tokenization/
    - /shopware/recurring-payments/
    - /integrations/shopware6/faq/how-can-i-update-the-plugin-for-shopware/
    - /payments/integrations/ecommerce-platforms/shopware6/faq/updating-the-plugin/
    - /shopware-6/updates/
---

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with Shopware 6.

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- Shopware 6.3.x, 6.4.x _([Starter Edition](https://www.shopware.com/en/pricing) supported)_*
- Tested on PHP 7.2.0

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue
- Join the official [Shopware 6 Slack channel](https://join.slack.com/t/shopwarenederland/shared_invite/zt-61exftia-TFYlw5LzmIBnz7Epq07goQ) 
- Join the private MultiSafepays [Shopware 6 Slack channel](https://shopwarenederland.slack.com/archives/G0146NKFJTT)

For support for Shopware 6 Professional/Enterprise, email <sales@multisafepay.com>

{{< /details >}}

## Installation and configuration

{{< blue-notice >}} We recommend first installing the plugin in a test environment, following the Shopware 6 installation procedure. Always make a backup. {{< /blue-notice >}}

1. Navigate to our [Shopware 6 GitHub repository](https://github.com/MultiSafepay/shopware6/releases).
2. Under **Assets**, download the latest release, which starts with Plugin_Shopware6_x.x.x.zip.
3. Sign in to your Shopware 6 backend.
4. Go to **Settings** > **System** on the left hand side.
5. Select **Plugins**.
6. Click **Upload plugin** at the top of the page, and then select the file you downloaded in step 2.
7. When the plugin appears, make sure the **Activated** button is toggled.
8. Click the **...** (more) button, and then select **Config**.
9. In the drop-down menu, select **Test**.
10. In the **API key** field, enter your [API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).
11. Fill out the other fields as required.

### Marketplace installation
Get the free MultiSafepay plugin from the [Shopware 6 marketplace](https://store.shopware.com/en/mltis59465832976f/multisafepay-online-payments-for-shopware-ideal-cards-klarna-alipay-etc..html) and connect your webshop with your Shopware account.

### Composer installation
Run the following command in the root of your Shopware root directory. Make sure the composer is installed on your hosting server.

```
composer require multisafepay/shopware6
```

## User guide

### Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/payment-pages/). You can use them to integrate custom gift cards, or co-branded credit cards. 

{{< details title="Configuring generic gateways" >}}

1. Sign in to your Shopware 6 backend.
2. Go to **MultiSafepay settings**.
3. Set the relevant [payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids).

Generic gateways support:

- All payment methods (filter by country, and minimum/maximum amount)
- [Split payments](/payments/split-payments/), [Second Chance reminders](/features/second-chance/) and [virtual IBANs](/payments/virtual-ibans/)
- [Redirect requests](https://docs-api.multisafepay.com/reference/introduction#direct-vs-redirect) only

**Gift cards**

Generic gateways are particularly useful for integrating [gift cards](/payment-methods/gift-cards/), including [custom gift cards](/payment-methods/gift-cards/custom-cards/). This is because we don't support all [open-loop gift cards](/payment-methods/gift-cards/open-loop-closed-loop/) in our ready-made integrations and *no* closed-loop gift cards.

**Co-branded credit cards**

You can integrate Visa co-branded credit cards ([Cartes Bancaires](/payment-methods/cartes-bancaires/), [Dankort](/payment-methods/dankort/), and [V Pay](/payment-methods/vpay/)), using the generic `VISA` gateway.

For the logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons/tree/master/methods).

{{< /details >}}

### Payment methods

{{< details title="Payment methods" >}}

- Cards: [All](/payment-methods/credit-debit-cards/)
- Banking methods: [All](/payment-methods/banks/), except iDEAL QR
- Pay later methods: [All](/payment-methods/pay-later/)
- Wallets: [Alipay](/payment-methods/alipay), [Apple Pay](/payment-methods/apple-pay), [PayPal](/payment-methods/paypal)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
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

You need to [enable recurring payments](/features/recurring-payments) in your MultiSafepay dashboard and then in the gateway settings. 

### Refunds

[Full and partial refunds](/refunds/#full-and-partial-refunds) **except** for [pay later methods](/payment-methods/pay-later) are supported in your MultiSafepay dashboard and backend.  
You cannot refund more than the original amount in your backend.

{{< details title="Processing backend refunds" >}}

1. In your Shopware 6 backend, go to the **Order details** page.
2. In the **Refund** field, enter the refund amount. 

{{< /details >}}

### Updates

You can update the plugin in your backend and the CMS marketplace, or via using SFTP.

{{< details title="Updating in your backend" >}}

**Note:** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 3.

{{< /details >}}