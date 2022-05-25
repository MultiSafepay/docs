---
title : "MultiSafepay plugin for Shopware 5"
download_url : "https://store.shopware.com/en/mltis39871819230f/multisafepay-online-payments-free-plugin-with-20-payment-methods.html"
github_url : "https://github.com/MultiSafepay/Shopware"
faq: "."
meta_title: "Shopware 5 plugin - MultiSafepay Docs"
logo: "https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Shopware_5.svg"
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
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Shopware 5 webshop.

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}

- MultiSafepay account – See [Getting started](/getting-started/).
- Shopware 5.6.x or 5.5.7 and above.
- Tested on PHP 7.0

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit cards**

- [American Express](/payment-methods/amex)
- [Maestro](/payment-methods/maestro)
- [Mastercard](/payment-methods/mastercard)
- [Visa](/payment-methods/visa), including [Cartes Bancaires](/payment-methods/cartes-bancaires), [Dankort](/payment-methods/dankort), and [V Pay](/payment-methods/vpay)

**Banking methods**

- [Bancontact](/payment-methods/bancontact)
- [Bank Transfer](/payment-methods/bank-transfer)
- [Belfius](/payment-methods/belfius)
- [CBC/KBC](/payment-methods/cbc-kbc)
- [Dotpay](/payment-methods/dotpay)
- [EPS](/payment-methods/eps)
- [Giropay](/payment-methods/giropay)
- [iDEAL and iDEAL QR](/payment-methods/ideal)
- [Request to Pay](/payment-methods/request-to-pay)
- [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
- [Sofort](/payment-methods/sofort)
- [Trustly](/payment-methods/trustly)
- [TrustPay](/payment-methods/trustpay)

**Pay later methods**

- [AfterPay](/payment-methods/afterpay)
- [Betaal per Maand](/payment-methods/betaal-per-maand)
- [E-Invoicing](/payment-methods/e-invoicing)
- [in3](/payment-methods/in3/)
- [Klarna](/payment-methods/klarna)
- [Pay After Delivery](/payment-methods/pay-after-delivery)

**Wallets**

- [Alipay](/payment-methods/alipay)
- [Apple Pay](/payment-methods/apple-pay)
- [PayPal](/payment-methods/paypal)

**Prepaid cards**

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

See also [MultiSafepay gateway](/developer/generic-gateways/#multisafepay-gateways).

{{< /details >}}

## Installation and configuration

{{< blue-notice >}} We recommend first installing the plugin in a test environment following, the recommended Shopware 5 installation procedure. Make sure you have made a backup. {{< /blue-notice >}}

1. Sign in to your Shopware 5 [backend](/glossaries/multisafepay-glossary/#backend).
2. Go to **Configuration** > **Plugin manager**.
3. Search for the MultiSafepay plugin and click **Download now**.
4. Go to **Configuration** > **Plugin manager** > **Installed**.
5. Search for the installed MultiSafepay plugin and click on the pencil icon.
6. In the **API key** field, enter your [API key](https://docs.multisafepay.com/tools/multisafepay-control/get-your-api-key).
7. Fill out the other fields as required.
8. Go to **Configuration** and select the required payment methods.


