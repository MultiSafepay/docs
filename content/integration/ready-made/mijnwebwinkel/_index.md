---
title : "Mijnwebwinkel app "
meta_title: "Mijnwebwinkel app - MultiSafepay Docs"
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
    - /integrations/ecommerce-integrations/mijnwebwinkel/faq/change-order-of-payment-methods/
    - /payments/integrations/ecommerce-platforms/mijnwebwinkel/faq/changing-order-of-payment-methods/
    - /mijnwebwinkel/payment-method-order/
---
This technical manual is for installing and configuring Mijnwebwinkel's free app for MultiSafepay. 

{{< details title="Requirements" >}}
&nbsp;  
You will need a [MultiSafepay account](/getting-started/guide/).

{{< /details >}}

{{< details title="Support" >}}
&nbsp;  
See Mijnwebwinkel:

- General information about the plugin - [MultiSafepay](https://www.mijnwebwinkel.nl/partner/multisafepay).
- Technical queries about the plugin - [Contact form](https://www.mijnwebwinkel.nl/contactformulier).
- Support documentation - [Support](https://www.mijnwebwinkel.nl/support).

Contact MultiSafepay:

- Telephone: -31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

## Installation and configuration

{{< blue-notice >}} We recommend first installing the plugin in a test environment, following the Mijnwebwinkel installation procedure. Always make a backup. {{< /blue-notice >}}

1. Sign in to your Mijwebwinkel backend.
2. Go to **Online orders** > **Payment method** > **MultiSafepay**.
2. Add your MultiSafepay account ID, [site ID, site security code, and API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).
6. Select the relevant payment methods.

## User guide

### Payment methods

{{< details title="Payment methods" >}}

- Cards: [Mastercard](/payment-methods/mastercard) and [Visa](/payment-methods/visa)
- Pay later methods: [Klarna](/payment-methods/klarna)
- Wallets: [PayPal](/payment-methods/paypal)
- Banking methods: 
    - [Bancontact](/payment-methods/bancontact)
    - [Bank Transfer](/payment-methods/bank-transfer)
    - [Giropay](/payment-methods/giropay)
    - [iDEAL](/payment-methods/ideal)
    - [Maestro](/payment-methods/maestro)
    - [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
    - [Sofort](/payment-methods/sofort)
- Prepaid cards:
    - [Baby Cadeaubon](https://www.babycadeaubon.nl)
    - Beauty & Wellness
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Fashion Cheque](https://www.fashioncheque.com/nl)
    - [Fashion gift card](https://www.fashion-giftcard.nl)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
    - [Good4fun](https://www.good4fun.nl)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
    - [Podium](https://www.podiumcadeaukaart.nl)
    - [Sport en Fit](https://www.sportenfitcadeau.nl)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl)
    - [Webshop gift card](https://www.webshopgiftcard.nl)
    - [Wellness gift card](https://www.wellnessgiftcard.nl)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl)
    - [Yourgift](https://www.yourgift.nl)

{{< /details >}}

{{< details title="Changing payment method order in checkout">}} 

To change the order of payment methods in your checkout, follow these steps:

1. Go to Mijnwebwinkel - [Sorting](https://www.mijnwebwinkel.nl/beheer/payment/sorting).
2. Select **Sort manually, defined below**.
3. Drag and drop the active payment methods to change the order.

{{< /details >}}

### Surcharges

[Surcharges](/surcharges/) are supported.

{{< alert-notice >}} **For Dutch merchants** <br>  We strongly recommend **not** applying surcharges to [pay later methods](/payment-methods/pay-later/). This is now considered providing credit under the Consumer Credit Act (Wet op het consumentenkrediet) and requires a permit from the Authority for Financial Markets (AFM). {{< /alert-notice >}}
