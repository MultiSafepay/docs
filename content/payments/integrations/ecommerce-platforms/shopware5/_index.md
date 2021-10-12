---
title : "MultiSafepay plugin for Shopware 5"
download_url : "https://store.shopware.com/en/mltis39871819230f/multisafepay-online-payments-free-plugin-with-20-payment-methods.html"
github_url : "https://github.com/MultiSafepay/Shopware"
faq: "."
meta_title: "Shopware 5 plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
logo: "/logo/Plugins/Shopware_5.svg"
weight: 07
title_short: "Shopware 5"
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
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Shopware 5 webshop.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended Shopware 5 installation procedure. Make sure you have made a backup.

{{< /details >}}

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

- [American Express](/payments/methods/credit-and-debit-cards/american-express)
- [Mastercard](/payments/methods/credit-and-debit-cards/mastercard)
- [Visa](/payments/methods/credit-and-debit-cards/visa), including [Cartes Bancaires](/payments/methods/credit-and-debit-cards/cartes-bancaires) & [Dankort](/payments/methods/credit-and-debit-cards/dankort)

**Banking methods**

- [Bancontact](/payments/methods/banks/bancontact)
- [Bank transfer](/payments/methods/banks/bank-transfer)
- [Belfius](/payments/methods/banks/belfius)
+ [CBC](/payments/methods/banks/cbc)
- [Dotpay](/payments/methods/banks/dotpay)
- [EPS](/payments/methods/banks/eps)
- [Giropay](/payments/methods/banks/giropay)
- [iDEAL](/payments/methods/banks/ideal)
- [iDEAL QR](/payments/methods/banks/idealqr)
- [ING Home'Pay](/payments/methods/banks/ing-home-pay)
- [KBC](/payments/methods/banks/kbc)
- [Maestro](/payments/methods/credit-and-debit-cards/maestro)
- [Request to Pay](/payments/methods/banks/request-to-pay)
+ [SEPA Direct Debit](/payments/methods/banks/sepa-direct-debit)
- [Sofort](/payments/methods/banks/sofort-banking)
- [Trustly](/payments/methods/banks/trustly)
+ [TrustPay](/payments/methods/banks/trustpay)
+ [V PAY](/payments/methods/credit-and-debit-cards/vpay)

**Pay later methods**

+ [AfterPay](/payments/methods/billing-suite/afterpay)
+ [Betaal per Maand](/payments/methods/billing-suite/betaalpermaand)
+ [E-Invoicing](/payments/methods/billing-suite/e-invoicing)
+ [in3](/payments/methods/billing-suite/in3/)
+ [Klarna](/payments/methods/billing-suite/klarna)
+ [Pay After Delivery](/payments/methods/billing-suite/pay-after-delivery)

**Wallets**

+ [Alipay](/payments/methods/wallet/alipay)
+ [Apple Pay](/payments/methods/wallet/applepay)
+ [PayPal](/payments/methods/wallet/paypal)

**Prepaid cards**

+ Beauty and Wellness gift card
+ [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
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
+ [Winkelcheque](https://www.winkelcheque.nl)
+ [Yourgift](https://www.yourgift.nl/)

{{< /details >}}

## Installation and configuration
1. Sign in to your Shopware 5 [backend](/getting-started/glossary/#backend).
2. Go to **Configuration** > **Plugin manager**.
3. Search for the MultiSafepay plugin and click **Download now**.
4. Go to **Configuration** > **Plugin manager** > **Installed**.
5. Search for the installed MultiSafepay plugin and click on the pencil icon.
6. In the **API key** field, enter your [API key](https://docs.multisafepay.com/tools/multisafepay-control/get-your-api-key).
7. Fill out the other fields as required.
8. Go to **Configuration** and select the required payment methods.


