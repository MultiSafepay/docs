---
title : "MultiSafepay app for Mijnwebwinkel"
meta_title: "Mijnwebwinkel app - MultiSafepay Docs"
faq: "."
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
logo: "/logo/Integrations/Mijnwebwinkel.svg"
weight: 25
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
This technical manual is for installing and configuring our free app for integrating MultiSafepay payment solutions into your Mijnwebwinkel webshop. This app is managed by our partner Mijnwebwinkel (MyOnlineStore).

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the app in a test environment following the recommended Mijnwebwinkel installation procedure. Make sure you have made a backup.
{{< /details >}}

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

- [Mastercard](/payments/methods/credit-and-debit-cards/mastercard)
- [Visa](/payments/methods/credit-and-debit-cards/mastercard/visa)

**Banking methods**

- [Bancontact](/payments/methods/banks/bancontact)
- [Bank transfer](/payments/methods/banks/bank-transfer)
- [Giropay](/payments/methods/banks/giropay)
- [iDEAL](/payments/methods/banks/ideal)
- [Maestro](/payments/methods/credit-and-debit-cards/maestro)
- [SEPA Direct Debit](/payments/methods/banks/sepa-direct-debit)
- [Sofort](/payments/methods/banks/sofort-banking)

**Pay later methods**

+ [Klarna](/payments/methods/billing-suite/klarna)

**Wallets**

+ [PayPal](/payments/methods/wallet/paypal)

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

1. Sign in to your Mijwebwinkel [backend](/getting-started/glossary/#backend).
2. Go to **Online orders** > **Payment method** > **MultiSafepay**.
2. Add your MultiSafepay account ID, site ID, site security code, and [API key](/faq/general/multisafepay-glossary/#api-key).
6. Select the relevant payment methods.

**Note:** You can apply a [surcharge](/security-and-legal/payment-regulations/about-surcharges/) to payment methods.

