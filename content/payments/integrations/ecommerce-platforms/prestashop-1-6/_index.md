---
title : "MultiSafepay plugin for PrestaShop 1.6"
download_url : "/payments/integrations/ecommerce-platforms/prestashop-1-6/releases/Plugin_PrestaShop1.6_3.6.0.zip"
changelog_url : "."
changelog: https://docs.multisafepay.com/payments/integrations/ecommerce-platforms/prestashop-1-6/changelog/
faq: "."
meta_title: "PrestaShop 1.6 plugin - MultiSafepay Docs"

logo: "/logo/Plugins/PrestaShop.svg"
weight: 09
title_short: "PrestaShop 1.6"
layout: 'single'
url: '/prestashop-1-6/'
aliases: 
    - /plugins/prestashop-1-6
    - /integrations/plugins/prestashop-1-6
    - /integrations/prestashop-1-6
    - /plugins/prestashop-1-6/manual
    - /integrations/plugins/prestashop-1-6/manual
    - /integrations/prestashop-1-6/manual
    - /integrations/ecommerce-integrations/prestashop-1-6
    - /payments/integrations/ecommerce-platforms/prestashop-1-6/
    - /ecommerce-platforms/prestashop-1-6/
---

{{< alert-notice >}} **Note:** We are phasing out support for our Prestashop 1.6 plugin. We recommend migrating to our [Prestashop 1.7 plugin](/prestashop/) as soon as possible. {{< /alert-notice >}}

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Prestashop 1.6 webshop.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended PrestaShop 1.6 installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}

- MultiSafepay account – See [Getting started](/getting-started/).
- PrestaShop 1.6
- Tested on PHP 7.0

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit cards**

- [American Express](/payment-methods/american-express)
- [Mastercard](/payment-methods/mastercard)
- [Visa](/payments/methods/credit-and-debit-cards/visa), including [Cartes Bancaires](/payment-methods/cartes-bancaires), [Dankort](/payment-methods/dankort), and [V Pay](/payment-methods/vpay/)

**Banking methods**

- [Bancontact](/payment-methods/bancontact)
- [Bank transfer](/payment-methods/bank-transfer)
- [Belfius](/payment-methods/belfius)
- [CBC](/payments/methods/banks/cbc)
- [Dotpay](/payment-methods/dotpay)
- [EPS](/payment-methods/eps)
- [Giropay](/payment-methods/giropay)
- [iDEAL](/payment-methods/ideal)
- [ING Home'Pay](/payment-methods/ing-home-pay)
- [CBC/KBC](/payment-methods/cbc-kbc)
- [Maestro](/payment-methods/maestro)
- [Request to Pay](/payments/methods/banks/request-to-pay)
- [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
- [Sofort](/payment-methods/sofort)
- [V PAY](/payment-methods/vpay)

**Pay later methods**

+ [AfterPay](/payments/methods/billing-suite/afterpay)
+ [E-Invoicing](/payment-methods/e-invoicing)
+ [Klarna](/payment-methods/klarna)
+ [Pay After Delivery](/payment-methods/pay-after-delivery)

**Wallets**

+ [Alipay](/payment-methods/alipay)
+ [Apple Pay](/payments/methods/wallet/applepay)
+ [PayPal](/payment-methods/paypal)

**Prepaid cards**

+ Beauty and Wellness gift card
+ [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
+ [Degrotespeelgoedwinkel](https://www.degrotespeelgoedwinkel.nl/cadeaukaart)
+ [Fashioncheque](https://www.fashioncheque.com/nl)
+ [Fashion gift card](https://www.fashion-giftcard.nl)
+ Fietsenbon
+ [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
+ [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
+ [Paysafecard](/payment-methods/paysafecard)
+ [Sport en Fit](https://www.sportenfitcadeau.nl)
+ [VVV gift card](https://www.vvvcadeaukaarten.nl)
+ [Webshop gift card](https://www.webshopgiftcard.nl)
+ Wijncadeau
+ [Yourgift](https://www.yourgift.nl/)

{{< /details >}}

## Installation and configuration
1. Unpack the contents of the .zip archive and upload the **Modules** folder via SFTP to the PrestaShop root directoy, merging the two folders.
2. Sign in to your PrestaShop 1.6 [backend](/getting-started/glossary/#backend).
3. Go to **Modules and services** > **Payments and gateways**.  
    **Note:** You must install and configure the MultiSafepay Core Module (MultiSafepay) because all payment methods require certain settings and/or the API key in the core module.
4. In the next screen, proceed with the installation.
5. Enter your [API key](/getting-started/glossary/#api-key), and then click **Save**. {{% account_info %}}
6. On the **Payments** tab, enable the relevant payment methods.

**Note:** Payment links generated manually in your MultiSafepay account don't automatically create or update orders in your PrestaShop 1.6 backend.

