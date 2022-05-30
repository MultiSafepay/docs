---
title : "OsCommerce plugin"
github_url : "https://github.com/MultiSafepay/OsCommerce"
download_url : "https://github.com/MultiSafepay/OsCommerce/archive/3.0.0.zip"
changelog: https://docs.multisafepay.com/integration/ready-made/oscommerce/changelog/
meta_title: "OsCommerce plugin - MultiSafepay Docs"
meta_description: "Free plugin to integrate MultiSafepay payment solutions with OsCommerce."
logo: "/logo/Plugins/OsCommerce.svg"
weight: 17
title_short: "OsCommerce"
type: 'Plugin'
description_short: "For support, contact OsCommerce."
layout: 'single'
url: '/oscommerce/'
aliases: 
    - /plugins/oscommerce
    - /integrations/plugins/oscommerce
    - /integrations/oscommerce
    - /plugins/oscommerce/manual
    - /integrations/plugins/oscommerce/manual
    - /integrations/oscommerce/manual
    - /integrations/ecommerce-integrations/oscommerce
    - /payments/integrations/ecommerce-platforms/oscommerce/
    - /ecommerce-platforms/oscommerce/
    - /integrations/oscommerce/faq/refunding-oscommerce/
    - /payments/integrations/ecommerce-platforms/oscommerce/faq/processing-refunds/
    - /oscommerce/refunds/
    - /integrations/oscommerce/faq/how-can-i-update-the-plugin-for-oscommerce/
    - /payments/integrations/ecommerce-platforms/oscommerce/faq/updating-the-plugin/
    - /oscommerce/updates/
---

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with OsCommerce.

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- OsCommerce 2.3
- Tested on PHP 7.0

**Note:** Version 3.0.0 is tested on PHP 5.6. Previous versions are no longer tested for compatibility. For more information, email <sales@multisafepay.com>

{{< /details >}}

{{< details title="Support" >}}

For support, contact OsCommerce.

Contact MultiSafepay:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

## Installation and configuration

{{< blue-notice >}} We recommend first installing the plugin in a test environment, following the OsCommerce installation procedure. Always make a backup.

{{< /blue-notice >}}

1. Unpack the content of the .ZIP file in the root of your webshop.
2. Sign in to your OsCommerce backend.
3. Go to **Modules** > **Payment**.
4. Click **Install modules** in the top-right corner.
5. Enter your [API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code), and then complete the other fields as required.

## User guide

### Payment methods

{{< details title="Payment methods" >}}

- Cards: [All](/payment-methods/credit-debit-cards/)
- Pay later methods: [E-Invoicing](/payment-methods/e-invoicing), [Klarna](/payment-methods/klarna), [Pay After Delivery](/payment-methods/pay-after-delivery)
- Wallets: [PayPal](/payment-methods/paypal)
- Banking methods:
    - [Bancontact](/payment-methods/bancontact)
    - [Bank Transfer](/payment-methods/bank-transfer)
    - [CBC/KBC](/payment-methods/cbc-kbc)
    - [Dotpay](/payment-methods/dotpay)
    - [EPS](/payment-methods/eps)
    - [Giropay](/payment-methods/giropay)
    - [iDEAL](/payment-methods/ideal)
    - [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
    - [Sofort](/payment-methods/sofort)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/payments/methods/prepaid-cards/paysafecard)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl/)

See also [MultiSafepay gateway](/developer/generic-gateways/#multisafepay-gateways).

{{< /details >}}

### Refunds

[Full refunds](/refunds/full-partial/) are supported in your MultiSafepay dashboard and backend.  
You can't refund more than the original amount in your backend.

### Updates

You can update the plugin in your backend or the CMS marketplace, or via SFTP.

{{< details title="Updating via SFTP" >}}

1. Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.
2. Download the plugin again above.
3. Follow the Installation and configuration instructions from step 2.

{{< /details >}}