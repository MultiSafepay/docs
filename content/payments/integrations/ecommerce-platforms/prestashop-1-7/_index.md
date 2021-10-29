---
title : "MultiSafepay plugin for PrestaShop 1.7"
github_url : "https://github.com/MultiSafepay/PrestaShop"
meta_title: "PrestaShop 1.7 plugin - MultiSafepay Docs"
download_url : "https://github.com/MultiSafepay/PrestaShop/releases/download/4.8.0/Plugin_PrestaShop_4.8.0.zip"
changelog_url : "."
faq: "."

logo: "/logo/Plugins/PrestaShop.svg"
weight: 09
title_short: "PrestaShop 1.7"
layout: 'single'
layout: 'single'
changelog: 'https://github.com/MultiSafepay/PrestaShop/blob/master/CHANGELOG.md'
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

{{< alert-notice >}}
**Important:** There is a new release candidate for our PrestaShop 1.7 plugin for version 1.7.6 or higher available to [download now](/payments/integrations/ecommerce-platforms/prestashop-1-7/releases/Plugin_PrestaShop_5.0.0-RC.zip). 
{{< /alert-notice>}}

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
- PrestaShop 1.7
- Tested on PHP 7.0

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit cards**

- [American Express](/payments/methods/credit-and-debit-cards/american-express)
- [Mastercard](/payments/methods/credit-and-debit-cards/mastercard)
- [Visa](/payments/methods/credit-and-debit-cards/visa), including [Cartes Bancaires](/payments/methods/credit-and-debit-cards/cartes-bancaires) and [Dankort](/payments/methods/credit-and-debit-cards/dankort)

**Banking methods**

- [Bancontact](/payments/methods/banks/bancontact)
- [Bank transfer](/payments/methods/banks/bank-transfer)
- [Belfius](/payments/methods/banks/belfius)
- [CBC](/payments/methods/banks/cbc)
- [Dotpay](/payments/methods/banks/dotpay)
- [EPS](/payments/methods/banks/eps)
- [Giropay](/payments/methods/banks/giropay)
- [iDEAL](/payments/methods/banks/ideal)
- [iDEAL QR](/payments/methods/banks/idealqr)
- [ING Home'Pay](/payments/methods/banks/ing-home-pay)
- [KBC](/payments/methods/banks/kbc)
- [Maestro](/payments/methods/credit-and-debit-cards/maestro)
- [Request to Pay](/payments/methods/banks/request-to-pay)
- [SEPA Direct Debit](/payments/methods/banks/sepa-direct-debit)
- [Sofort](/payments/methods/banks/sofort-banking)
- [Trustly](/payments/methods/banks/trustly)
- [TrustPay](/payments/methods/banks/trustpay)
- [V PAY](/payments/methods/credit-and-debit-cards/vpay)

**Pay later methods**

+ [AfterPay](/payments/methods/billing-suite/afterpay)
+ [Betaal per Maand](/payments/methods/billing-suite/betaalpermaand)
+ [E-Invoicing](/payments/methods/billing-suite/e-invoicing)
+ [in3](https://docs.multisafepay.com/payment-methods/billing-suite/in3)
+ [Klarna](/payments/methods/billing-suite/klarna)
+ [Pay After Delivery](/payments/methods/billing-suite/pay-after-delivery)

**Wallets**

+ [Alipay](/payments/methods/wallet/alipay)
+ [Apple Pay](/payments/methods/wallet/applepay)
+ [PayPal](/payments/methods/wallet/paypal)

**Prepaid cards**

+ Beauty and Wellness gift card
+ [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
+ [Degrotespeelgoedwinkel](https://www.degrotespeelgoedwinkel.nl/cadeaukaart)
+ [Fashioncheque](https://www.fashioncheque.com/nl)
+ [Fashion gift card](https://www.fashion-giftcard.nl)
+ Fietsenbon
+ [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
+ [Good4fun](https://www.good4fun.nl)
+ [Nationale tuinbon](https://www.nationale-tuinbon.nl)
+ [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
+ [Paysafecard](/payments/methods/prepaid-cards/paysafecard)
+ [Podium](https://www.podiumcadeaukaart.nl)
+ [Sport en Fit](https://www.sportenfitcadeau.nl)
+ [VVV gift card](https://www.vvvcadeaukaarten.nl)
+ [Webshop gift card](https://www.webshopgiftcard.nl)
+ [Wellness gift card](https://www.wellnessgiftcard.nl)
+ Wijncadeau
+ [Yourgift](https://www.yourgift.nl/)

{{< /details >}}

## Installation
1. Sign in to your PrestaShop 1.7 [backend](/getting-started/glossary/#backend).
2. Go to **Modules** > **Modules & services**.
3. Click **Upload a module**.
4. Select the Plugin_PrestaShop.zip file, and then click **Configure**.

## Configuration
1. Sign in to your PrestaShop 1.7 backend.
2. Go to **Modules & services**.
3. Search for MultiSafepay, and then click **Configure**.
4. Enter your [API key](/getting-started/glossary/#api-key). {{% account_info %}}
5. Click **Save**.
3. On the **Payments** tab, enable the relevant payment methods.




