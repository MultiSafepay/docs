---
title : "MultiSafepay plugin for Zen Cart"
github_url : "https://github.com/MultiSafepay/Zencart"
download_url : "https://github.com/MultiSafepay/Zencart/releases/download/3.1.0/Plugin_ZenCart_3.1.0.zip"
changelog_url : "."
faq: "."
meta_title: "ZenCart plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
logo: "/logo/Plugins/Zen_Cart.svg"
weight: 20
title_short: "Zen Cart"
layout: 'single'
changelog : "https://github.com/MultiSafepay/Zencart/blob/master/CHANGELOG.md"
url: '/ecommerce-platforms/zen-cart/'
aliases: 
    - /plugins/zencart
    - /integrations/plugins/zencart
    - /integrations/zencart
    - /plugins/zencart/manual
    - /integrations/plugins/zencart/manual
    - /integrations/zencart/manual
    - /integrations/ecommerce-integrations/zencart
    - /payments/integrations/ecommerce-platforms/zencart/
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Zen Cart webshop.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended Zen Cart installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}

- MultiSafepay account – See [Getting started](/getting-started/).
- ZenCart 1.5.5
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
- [Dotpay](/payments/methods/banks/dotpay)
- [EPS](/payments/methods/banks/eps)
- [Giropay](/payments/methods/banks/giropay)
- [iDEAL](/payments/methods/banks/ideal)
- [ING Home'Pay](/payments/methods/banks/ing-home-pay)
- [KBC](/payments/methods/banks/kbc)
- [Maestro](/payments/methods/credit-and-debit-cards/maestro)
- [Request to Pay](/payments/methods/banks/request-to-pay)
+ [SEPA Direct Debit](/payments/methods/banks/sepa-direct-debit)
- [Sofort](/payments/methods/banks/sofort-banking)
- [Trustly](/payments/methods/banks/trustly)
+ [V PAY](/payments/methods/credit-and-debit-cards/vpay)

**Pay later methods**

+ [AfterPay](/payments/methods/billing-suite/afterpay)
+ [Betaal per Maand](/payments/methods/billing-suite/betaalpermaand)
+ [E-Invoicing](/payments/methods/billing-suite/e-invoicing)
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
1. In the root of your webshop, unpack the content of the .ZIP file.
2. Sign in to your Zen Cart [backend](/getting-started/glossary/#backend).
3. Go to **Modules** > **Payment**.
4. Select **MultiSafepay - Connect**, and then click **Install**.
5. Enter your [API key](/tools/multisafepay-control/get-your-api-key).
6. Click **Update**.
7. Disable the **MultiSafepay - Connect** module.
8. Enable the relevant payment methods.



