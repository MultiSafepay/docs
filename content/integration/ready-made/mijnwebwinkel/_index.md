---
title : "Mijnwebwinkel app for MultiSafepay"
meta_title: "Mijnwebwinkel app - MultiSafepay Docs"
faq: "."
logo: "/logo/Integrations/Mijnwebwinkel.svg"
weight: 25
type: 'App'
title_short: "Mijnwebwinkel"
layout: 'single'
url: '/mijnwebwinkel/'
aliases: 
    - /integrations/mijnwebwinkel/
    - /hosted/mijnwebwinkel
    - /integrations/hosted/mijnwebwinkel
    - /integrations/mijnwebwinkel
    - /hosted/mijnwebwinkel/manual
    - /integrations/hosted/mijnwebwinkel/manual
    - /integrations/mijnwebwinkel/manual
    - /integrations/ecommerce-integrations/mijnwebwinkel
    - /payments/integrations/ecommerce-platforms/mijnwebwinkel/
    - /ecommerce-platforms/mijnwebwinkel/
---
This technical manual is for installing and configuring Mijnwebwinkel's free app for integrating MultiSafepay payment solutions into your webshop. 

{{< details title="Support" >}}
&nbsp;  
The plugin is developed and supported by Mijnwebwinkel. See Mijnwebwinkel - [MultiSafepay](https://www.mijnwebwinkel.nl/partner/multisafepay).

For any technical queries about the plugin, see Mijnwebwinkel - [Contact form](https://www.mijnwebwinkel.nl/contactformulier).

For support documentation, see Mijnwebwinkel - [Support](https://www.mijnwebwinkel.nl/support).

Contact MultiSafepay:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}
&nbsp;  
You will need a MultiSafepay account. See [Getting started](/getting-started/).

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit cards**

- [Mastercard](/payment-methods/mastercard)
- [Visa](/payment-methods/visa)

**Banking methods**

- [Bancontact](/payment-methods/bancontact)
- [Bank Transfer](/payment-methods/bank-transfer)
- [Giropay](/payment-methods/giropay)
- [iDEAL](/payment-methods/ideal)
- [Maestro](/payment-methods/maestro)
- [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
- [Sofort](/payment-methods/sofort)

**Pay later methods**

+ [Klarna](/payment-methods/klarna)

**Wallets**

+ [PayPal](/payment-methods/paypal)

**Prepaid cards**

+ [Baby Cadeaubon](https://www.babycadeaubon.nl)
+ Beauty & Wellness
+ [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
+ [Fashion Cheque](https://www.fashioncheque.com/nl)
+ [Fashion gift card](https://www.fashion-giftcard.nl)
+ Fietsenbon
+ [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
+ [Good4fun](https://www.good4fun.nl)
+ [Nationale tuinbon](https://www.nationale-tuinbon.nl)
+ [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
+ [Podium](https://www.podiumcadeaukaart.nl)
+ [Sport en Fit](https://www.sportenfitcadeau.nl)
+ [VVV gift card](https://www.vvvcadeaukaarten.nl)
+ [Webshop gift card](https://www.webshopgiftcard.nl)
+ [Wellness gift card](https://www.wellnessgiftcard.nl)
+ Wijncadeau
+ [Winkelcheque](https://www.winkelcheque.nl)
+ [Yourgift](https://www.yourgift.nl)

{{< /details >}}

## Installation and configuration

{{< blue-notice >}} We recommend first installing the plugin in a test environment following, the recommended Mijnwebwinkel installation procedure. Make sure you have made a backup. {{< /blue-notice >}}

1. Sign in to your Mijwebwinkel [backend](/glossaries/multisafepay-glossary/#backend).
2. Go to **Online orders** > **Payment method** > **MultiSafepay**.
2. Add your MultiSafepay account ID, site ID, site security code, and [API key](/glossaries/multisafepay-glossary/#api-key).
6. Select the relevant payment methods.

**Note:** You can apply a [surcharge](/security-and-legal/payment-regulations/about-surcharges/) to payment methods.

{{< alert-notice >}} **For Dutch merchants** <br>  We strongly recommend that you do **not** apply surcharges to [pay later methods](/payment-methods/pay-later/). This is now considered providing credit under the Consumer Credit Act (Wet op het consumentenkrediet) and requires a permit from the Authority for Financial Markets (AFM). {{< /alert-notice >}}

