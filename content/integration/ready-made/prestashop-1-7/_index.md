---
title : "MultiSafepay plugin for PrestaShop 1.7"
github_url : "https://github.com/MultiSafepay/prestashop-official"
meta_title: "PrestaShop 1.7 plugin - MultiSafepay Docs"
download_url : "https://github.com/MultiSafepay/prestashop-official/releases/download/5.1.1/Plugin_PrestaShop_5.1.1.zip"
changelog_url : "."
faq: "."
logo: "/logo/Plugins/PrestaShop.svg"
weight: 09
title_short: "PrestaShop 1.7"
type: 'Plugin'
layout: 'single'
layout: 'single'
changelog: 'https://github.com/MultiSafepay/prestashop-official/blob/main/CHANGELOG.md'
url: '/prestashop/'
aliases: 
    - /plugins/prestashop-1-7
    - /integrations/plugins/prestashop-1-7
    - /integrations/prestashop-1-7
    - /plugins/prestashop-1-7/manual
    - /integrations/plugins/prestashop-1-7/manual
    - /integrations/prestashop-1-7/manual
    - /integrations/ecommerce-integrations/prestashop-1-7
    - /payments/integrations/ecommerce-platforms/prestashop-1-7/
    - /ecommerce-platforms/prestashop-1-7/
---
This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions with your Prestashop 1.7 webshop.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended PrestaShop 1.7 installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}

- MultiSafepay account – See [Getting started](/getting-started/).
- PrestaShop 1.7.6 or higher
- Tested on PHP 7.2

If you're on PrestaShop 1.7.5 or lower, consider updating PrestaShop or use an older version (4.x) of our plugin which can be found in our [PrestaShop GitHub repository](https://github.com/MultiSafepay/prestashop/releases). 

{{< /details >}}

{{< details title="Supported versions" >}}

- 1.7.6
- 1.7.7
- 1.7.8

To use an older version of the plugin, see MultiSafepay GitHub – [PrestaShop releases](https://github.com/MultiSafepay/prestashop/releases).

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit cards**

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
- [TrustPay](/payment-methods/trustpay)

**Pay later methods**

- [AfterPay](/payments/methods/billing-suite/afterpay)
- [Betaal per Maand](/payment-methods/betaal-per-maand)
- [E-Invoicing](/payment-methods/e-invoicing)
- [in3](/payment-methods/in3)
- [Klarna](/payment-methods/klarna)
- [Pay After Delivery](/payment-methods/pay-after-delivery)

**Wallets**

- [Alipay](/payment-methods/alipay)
- [Apple Pay](/payment-methods/apple-pay/)
- [Google Pay](/payment-methods/google-pay/)
- [WeChat Pay](/payment-methods/wechat-pay/)
- [PayPal](/payment-methods/paypal)

**Prepaid cards**

- Baby Giftcard
- Beauty and wellness
- [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
- [Degrotespeelgoedwinkel](https://www.degrotespeelgoedwinkel.nl/cadeaukaart)
- [Fashioncheque](https://www.fashioncheque.com/nl)
- [Fashion gift card](https://www.fashion-giftcard.nl)
- Fietsenbon
- [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
- Givacard
- [Good4fun](https://www.good4fun.nl)
- Goodcard
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

See also [MultiSafepay gateway](/integrations/multisafepay-gateway/).

{{< /details >}}

{{< details title="Upgrading to version 5.x from an older version" >}}

When you update from an older version of the plugin to 5.x, keep the older version installed until you are sure that orders created with the new plugin are successfully processed.

## Switching to the new plugin

1. Go to **Modules** > **Module Manager** > **MultiSafepay** > **Configure**.
2. Open the **Payment Methods** tab.
3. Set all Payment Methods to **off**.
4. Open the **Giftcards** tab.
5. Set all gift cards to **off**.
6. Install and configure the new plugin following the instructions below.
7. Don't uninstall the older plugin until you are sure that orders created with the new plugin are successfully processed 

{{< /details >}}

## Installation
1. Sign in to your PrestaShop 1.7 [backend](/glossaries/multisafepay-glossary/#backend).
2. Go to **Modules** > **Module Manager**.
3. Click **Upload a module**.
4. Select the Plugin_PrestaShop.zip file, and then click **Configure**.

## Configuration
1. Sign in to your PrestaShop 1.7 backend.
2. Go to **IMPROVE** > **MultiSafepay**.
3. Enter your [API key](/glossaries/multisafepay-glossary/#api-key). {{% account_info %}}
4. On the **Payment methods** tab, enable the relevant payment methods.
5. Click **Save**.




