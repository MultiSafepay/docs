---
title : "MultiSafepay plugin for Shopware 6"
meta_title: "Shopware 6 plugin - MultiSafepay Docs"
github_url : "https://github.com/MultiSafepay/shopware6/"
download_url : "https://github.com/MultiSafepay/shopware6/releases/download/2.5.3/Plugin_Shopware6_2.5.3.zip"
faq: "."
logo: "/logo/Plugins/Shopware_6.svg"
weight: 06
title_short: "Shopware 6"
type: 'Plugin'
layout: 'single'
changelog : "https://github.com/MultiSafepay/shopware6/blob/master/CHANGELOG.md"
url: '/shopware-6/'
aliases: 
    - /plugins/shopware6
    - /integrations/plugins/shopware6
    - /integrations/shopware6
    - /plugins/shopware6/manual
    - /integrations/plugins/shopware6/manual
    - /integrations/shopware6/manual
    - /integrations/ecommerce-integrations/shopware6
    - /payments/integrations/ecommerce-platforms/shopware6/
    - /ecommerce-platforms/shopware-6/
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Shopware 6 webshop.

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue
- Join the official [Shopware 6 Slack channel](https://join.slack.com/t/shopwarenederland/shared_invite/zt-61exftia-TFYlw5LzmIBnz7Epq07goQ) 
- Join the private MultiSafepays [Shopware 6 Slack channel](https://shopwarenederland.slack.com/archives/G0146NKFJTT)

For support for Shopware 6 Professional/Enterprise, email <sales@multisafepay.com>

{{< /details >}}

{{< details title="Requirements" >}}

- MultiSafepay account – See [Getting started](/getting-started/).
- Shopware 6.3.x, 6.4.x _([Starter Edition](https://www.shopware.com/en/pricing) supported)_*
- Tested on PHP 7.2.0

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit and debit cards**

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
- [iDEAL](/payment-methods/ideal)
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

{{< blue-notice >}} We recommend first installing the plugin in a test environment following, the recommended Shopware 6 installation procedure. Make sure you have made a backup. {{< /blue-notice >}}

1. Navigate to our [Shopware 6 GitHub repository](https://github.com/MultiSafepay/shopware6/releases).
2. Under **Assets**, download the latest release, which starts with Plugin_Shopware6_x.x.x.zip.
3. Sign in to your Shopware 6 [backend](/glossaries/multisafepay-glossary/#backend).
4. Go to **Settings** > **System** on the left hand side.
5. Select **Plugins**.
6. Click **Upload plugin** at the top of the page, and then select the file you downloaded in step 2.
7. When the plugin appears, make sure the **Activated** button is toggled.
8. Click the **...** (more) button, and then select **Config**.
9. In the drop-down menu, select **Test**.
10. In the **API key** field, enter your [API key](https://docs.multisafepay.com/tools/multisafepay-control/get-your-api-key).
11. Fill out the other fields as required.

### Marketplace installation
Get the free MultiSafepay plugin from the [Shopware 6 marketplace](https://store.shopware.com/en/mltis59465832976f/multisafepay-online-payments-for-shopware-ideal-cards-klarna-alipay-etc..html) and connect your webshop with your Shopware account.

### Composer installation
Run the following command in the root of your Shopware root directory. Make sure the composer is installed on your hosting server.

```
composer require multisafepay/shopware6
```


