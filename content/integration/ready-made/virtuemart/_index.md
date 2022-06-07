---
title : "VirtueMart plugin"
github_url : "https://github.com/MultiSafepay/Virtuemart"
download_url : "https://github.com/MultiSafepay/VirtueMart/releases/download/2.2.2/Plugin_VirtueMart_2.2.2.zip"
changelog_url : "."
meta_title: "VirtueMart plugin - MultiSafepay Docs"
logo: "/logo/Plugins/VirtueMart.svg"
weight: 18
title_short: "VirtueMart"
type: 'Plugin'
layout: 'single'
changelog : "https://github.com/MultiSafepay/VirtueMart/blob/master/CHANGELOG.md"
url: '/virtuemart/'
aliases:
    - /integrations/virtuemart/
    - /plugins/virtuemart
    - /integrations/plugins/virtuemart
    - /integrations/virtuemart
    - /plugins/virtuemart/manual
    - /integrations/plugins/virtuemart/manual
    - /integrations/virtuemart/manual
    - /integrations/ecommerce-integrations/virtuemart
    - /payments/integrations/ecommerce-platforms/virtuemart/
    - /ecommerce-platforms/virtuemart/
    - /integrations/virtuemart/faq/refunding-virtuemart/
    - /payments/integrations/ecommerce-platforms/virtuemart/faq/processing-refunds/
    - /virtuemart/refunds/
    - /integrations/virtuemart/faq/how-can-i-update-the-plugin-for-virtuemart/
    - /payments/integrations/ecommerce-platforms/virtuemart/faq/updating-the-plugin/
    - /virtuemart/updates/
---

This technical manual is for installing and configuring MultiSafepay free plugin for integrating with VirtueMart.

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- Joomla 2.5 & 3.x + Virtuemart 2.x & 3.x
- Tested on PHP 7.0

{{< /details >}}

{{< details title="Support" >}}
&nbsp; 
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

## Installation

{{< blue-notice >}} We recommend first installing the plugin in a test environment, following the VirtueMart installation procedure. Always make a backup. {{< /blue-notice >}}

1. Sign in to your VirtueMart backend.
2. Go to **Extensions** > **Extension manager**.
3. Install the Plugin_VirtueMart_x.x.x.zip file using **Drag and drop** or **Browse for file**. 
4. Click **Upload & install**.

## Configuration
1. Sign in to your VirtueMart backend.
2. Go to **Extensions** > **Plugins**.
3. In the search box, enter **MultiSafepay**, and then set the plugin status to **Enabled**.
4. Go to **Components** > **VirtueMart**. 
5. Click **Shop** > **Payment methods**. 
6. To install and configure each payment method separately:  
    - Click **New**.
    - Set the payment method to **VirtueMart – Payment, MultiSafepay**.
    - To install, save the **Payment method name**.
7. On the **Configuration** tab, enter your:
    - Account ID (top-right corner of your dashboard)
    - [Site ID, API key, and secure code](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code)
    - [Gateway ID](https://docs-api.multisafepay.com/reference/gateway-ids)

## User guide

### Checkouts

If a customer selects Apple Pay at checkout but isn't on an Apple device, they receive a notification to select another payment method. 

### Payment methods

{{< details title="Payment methods" >}}

- Cards: [All](/payment-methods/credit-debit-cards/)
- Banking methods: [All](/payment-methods/banks/)
- Pay later methods: [All](/payment-methods/pay-later/)
- Wallets: [All](/payment-methods/wallets/)
- Prepaid cards:
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Edenred](/payment-methods/edenred/)
    - [Fashioncheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Paysafecard](/payment-methods/paysafecard)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Postepay](/payment-methods/postepay/)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl/)

{{< /details >}}

### Refunds

[Full refunds](/refunds/#full-and-partial-refunds) are supported in your MultiSafepay dashboard and your backend.  
You cannot refund more than the original amount in your backend.

### Updates

You can update the plugin in your backend and the CMS marketplace, via SFTP.

{{< details title="Updating in your backend" >}}

**Note:** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Download the plugin again above.
2. Follow the Installation and configuration instructions from step 2.

{{< /details >}}