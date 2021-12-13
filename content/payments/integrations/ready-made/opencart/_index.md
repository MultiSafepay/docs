---
title : "MultiSafepay plugin for OpenCart"
github_url : "https://github.com/MultiSafepay/Opencart"
download_url : "https://www.opencart.com/index.php?route=marketplace/extension/info&extension_id=39960"
faq: "."
meta_title: "OpenCart plugin - MultiSafepay Docs"
logo: "/logo/Plugins/OpenCart.svg"
weight: 10
title_short: "OpenCart"
type: 'Plugin'
layout: 'single'
changelog : "https://github.com/MultiSafepay/Opencart/blob/master/CHANGELOG.md"
url: '/opencart/'
aliases: 
    - /plugins/opencart
    - /integrations/plugins/opencart
    - /integrations/opencart
    - /support-tab/opencart/manual
    - /plugins/opencart/manual
    - /integrations/plugins/opencart/manual
    - /integrations/opencart/manual
    - /integrations/ecommerce-integrations/opencart
    - /payments/integrations/ecommerce-platforms/opencart/
    - /ecommerce-platforms/opencart/
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your OpenCart webshop.

{{< details title="Test environment" >}}
&nbsp;  

We recommend first installing the plugin in a test environment following the recommended OpenCart installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support" >}}
&nbsp;  
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}
&nbsp;  
- MultiSafepay account – See [Getting started](/getting-started/).
- OpenCart 2.X, 3.X
- Tested on PHP 7.2, 7.3

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit and debit cards**

- [American Express](/payment-methods/american-express)
- [Maestro](/payment-methods/maestro)
- [Mastercard](/payment-methods/mastercard)
- [Visa](/payments/methods/credit-and-debit-cards/visa), including [Cartes Bancaires](/payment-methods/cartes-bancaires), [Dankort](/payment-methods/dankort), and [V Pay](/payment-methods/vpay/)

**Banking methods**

- [Bancontact](/payment-methods/bancontact)
- [Bank Transfer](/payment-methods/bank-transfer)
- [Belfius](/payment-methods/belfius)
- [CBC/KBC](/payment-methods/cbc-kbc)
- [Dotpay](/payment-methods/dotpay)
- [EPS](/payment-methods/eps)
- [Giropay](/payment-methods/giropay)
- [iDEAL and iDEAL QR](/payment-methods/ideal)
- [Request to Pay](/payments/methods/banks/request-to-pay)
- [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
- [Sofort](/payment-methods/sofort)
- [Trustly](/payment-methods/trustly)

**Pay later methods**

- [AfterPay](/payments/methods/billing-suite/afterpay)
- [Betaal per Maand](/payment-methods/betaal-per-maand)
- [E-Invoicing](/payment-methods/e-invoicing)
- [in3](/payment-methods/in3)
- [Klarna](/payment-methods/klarna)
- [Pay After Delivery](/payment-methods/pay-after-delivery)

**Wallets**

- [Alipay](/payment-methods/alipay)
- [Apple Pay](/payments/methods/wallet/applepay)
- [PayPal](/payment-methods/paypal)

**Prepaid cards**

- [Baby Cadeaubon](https://www.babycadeaubon.nl)
- Beauty & Wellness
- [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
- [Fashion Cheque](https://www.fashioncheque.com/nl)
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

## Installation
1. For security, always create backup of your OpenCart application.
2. Download the Plugin_OpenCart_3.x.x.ocmod.zip.
3. Sign in to your OpenCart [backend](/getting-started/glossary/#backend), and go to **Extensions** > **Installer**.
4. Click the **Upload** button, and then select the downloaded file.
5. Once installed, click the **Dashboard** menu.
7. To clear both caches, click the blue cog wheel button in the top-right corner, and then click the **Refresh** icon. 
8. Go to **Extensions** > **Modifications**, and then click the **Refresh** button.
9. Go to **Extensions** > **Payments** > **MultiSafepay**, and then click the **Install** button. 

## Configuration
1. Sign in to your backend and go to **Extensions** > **Extensions** > **Payments** > **MultiSafepay**.
2. On the **MultiSafepay configuration** page, fill out each tab.  
    To retrieve your API key, see [Get your API key](/tools/multisafepay-control/get-your-api-key).
3. On the **Payment methods** tab, enable and configure the relevant payment methods.
4. Configure the **Order status** tab, matching each possible MultiSafepay callback status with one of the order statuses in your OpenCart webshop.
5. Configure the **Options** tab. 



