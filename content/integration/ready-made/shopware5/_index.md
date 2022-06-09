---
title : "Shopware 5 plugin"
download_url : "https://store.shopware.com/en/mltis39871819230f/multisafepay-online-payments-free-plugin-with-20-payment-methods.html"
github_url : "https://github.com/MultiSafepay/Shopware"
meta_title: "Shopware 5 plugin - MultiSafepay Docs"
logo: "/logo/Plugins/Shopware_5.svg"
weight: 07
title_short: "Shopware 5"
type: 'Plugin'
layout: 'single'
changelog : "https://github.com/MultiSafepay/Shopware/blob/master/CHANGELOG.md"
url: '/shopware-5/'
aliases: 
    - /plugins/shopware5
    - /integrations/plugins/shopware5
    - /integrations/shopware5
    - /plugins/shopware5/manual
    - /integrations/plugins/shopware5/manual
    - /integrations/shopware5/manual
    - /integrations/ecommerce-integrations/shopware5
    - /payments/integrations/ecommerce-platforms/shopware5/
    - /ecommerce-platforms/shopware-5/
    - /integrations/ecommerce-integrations/shopware5/faq/generic-gateways
    - /payments/integrations/ecommerce-platforms/shopware5/faq/configuring-generic-gateways/
    - /shopware-5/generic-gateways/
    - /shopware-5/configuring-generic-gateways/
    - /integrations/ecommerce-integrations/shopware5/faq/shopware-6-migration/
    - /payments/integrations/ecommerce-platforms/shopware5/faq/migrating-to-shopware-6/
    - /shopware-5/shopware-6-migration/
    - /payments/integrations/ecommerce-platforms/shopware5/faq/missing-session-data/
    - /shopware/session-data/
    - /integrations/shopware5/faq/refunding-shopware/
    - /payments/integrations/ecommerce-platforms/shopware5/faq/processing-refunds/
    - /shopware/refunds/
    - /payments/integrations/ecommerce-platforms/shopware5/faq/changing-order-status-to-shipped/
    - /shopware-5/shipping-orders/
    - /payments/integrations/ecommerce-platforms/shopware5/faq/transaction-number-order-number/
    - /shopware-5/transaction-order-numbers/
    - /integrations/shopware5/faq/how-can-i-update-the-plugin-for-shopware/
    - /payments/integrations/ecommerce-platforms/shopware5/faq/updating-the-plugin/
    - /shopware-5/updates/
---

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with Shopware 5.

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- Shopware 5.6.x or 5.5.7 and above.
- Tested on PHP 7.0

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

## Installation and configuration

{{< blue-notice >}} We recommend first installing the plugin in a test environment, following the Shopware 5 installation procedure. Always make a backup. {{< /blue-notice >}}

1. Sign in to your Shopware 5 backend.
2. Go to **Configuration** > **Plugin manager**.
3. Search for the MultiSafepay plugin and click **Download now**.
4. Go to **Configuration** > **Plugin manager** > **Installed**.
5. Search for the installed MultiSafepay plugin and click on the pencil icon.
6. In the **API key** field, enter your [API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).
7. Fill out the other fields as required.
8. Go to **Configuration** and select the required payment methods.

## User guide

### Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/payment-pages/). You can use them to integrate custom gift cards, or co-branded credit cards. 

{{< details title="Configuring generic gateways" >}}

1. Sign in to your Shopware 5 backend.
2. Go to **MultiSafepay settings**.
3. Set the relevant [payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids).
4. Upload a custom gateway image, if relevant.
5. For [pay later](/payment-methods/pay-later/) methods, specify whether to include a shopping cart.

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
- Banking methods: [All](/payment-methods/banks/)
- Pay later methods: [All](/payment-methods/pay-later/)
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
    - [Yourgift](https://www.yourgift.nl/)

{{< /details >}}

### Refunds

You can process [full refunds](/refunds/#full-and-partial-refunds) for all Shopware 5 payment methods **except** [pay later methods](/payment-methods/pay-later) from your MultiSafepay dashboard and backend.  
You cannot refund more than the original amount in your backend.

### Session data

{{< details title="Missing session data" >}}

Shopware 5 can remove sessions before the order is created in the backend.
To prevent this, we recommend making the following changes to the [config.php](https://developers.shopware.com/developers-guide/shopware-config/).

```
'session' => [
    'save_handler' => 'db',
    'gc_probability' => 0,
    'gc_divisor' => 1000
],
```

For more information, see Shopware – [Blocking transactions](https://developers.shopware.com/sysadmins-guide/sessions/#blocking-transactions).

{{< /details >}}

### Shipment

For [pay later](/payments/methods/pay-later/) orders, after shipment, you must change the order status from **completed** to **shipped**. This prevents the order expiring and triggers invoicing. 

If you change the order status to **Delivered** in your backend, the updated status is passed to your MultiSafepay dashboard automatically.

### Transaction and order numbers

Shopware 5 generates an order number and a transaction number.

The order number is generated **after** the payment is completed (unlike most ecommerce integrations where it is generated at the beginning of the order). 

The transaction number is generated when the transaction is initialized. MultiSafepay uses this number as the **order ID** in transactions.

### Updates

You can update the plugin in your backend or the CMS marketplace, or via SFTP.

{{< details title="Updating in your backend" >}}

**Note:** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.
{{< /details >}}

### Upgrading to Shopware 6

{{< details title="Upgrading to Shopware 6" >}}

**About Shopware 6**  
Shopware 6 is the latest version of the Shopware ecommerce platform. It maintains simplicity, but features a great new interface and functionalities, including:

- Sales Channels function that links to social shopping platforms (e.g. Facebook, Instagram), and supports mobile apps and [POS](/glossaries/multisafepay-glossary/#point-of-sale-pos-terminal) systems
- Rule Builder that lets you set price rules per country, and supports multi-currency options, VAT rules, and delivery options, e.g. free delivery for orders above a specified amount
- Content management function that uses stylized blocks on Experience and Storytelling pages
- Text editor that is easier and more user-friendly

**Shopware 5 phase out**  

Support for Shopware 5 will be phased out as follows:

1. General support until mid-2024
2. Regular functional releases until mid-2021
3. Bug fixes and small releases until mid-2023
4. Security updates until mid-2024

MultiSafepay will continue to support Shopware 5 as long as it remains in the market.

**Migrating to Shopware 6**  

For instructions, see the [Shopware migration manual](https://docs.shopware.com/en/migration-en).

For questions, email <integration@multisafepay.com>

{{< /details >}}