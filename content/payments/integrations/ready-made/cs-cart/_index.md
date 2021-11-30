---
title : "MultiSafepay plugin for CS-Cart"
github_url : "https://github.com/MultiSafepay/CS-Cart"
download_url : "https://github.com/MultiSafepay/CS-Cart/releases/download/1.6.0/Plugin_CS-Cart_1.6.0.zip"
faq: "."
changelog: "https://github.com/MultiSafepay/CS-Cart/blob/master/CHANGELOG.md"
meta_title: "CS-Cart plugin - MultiSafepay Docs"
type: 'Plugin'
logo: "/logo/Plugins/CS-Cart.svg"
weight: 13
title_short: "CS-Cart"
layout: 'single'
description_short: "Free plugin to integrate MultiSafepay payment solutions into your CS-Cart webshop."
url: '/cs-cart/'
aliases: 
    - /plugins/cs-cart
    - /integrations/plugins/cs-cart
    - /integrations/cs-cart
    - /integrations/ecommerce-integrations/cs-cart
    - /payments/integrations/ecommerce-platforms/cs-cart/
    - /ecommerce-platforms/cs-cart/
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your CS-Cart webshop.

{{< details title="Test environment" >}}
&nbsp;  

We recommend first installing the plugin in a test environment following the recommended Shopware 6 installation procedure. Make sure you have made a backup.

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
- CS-Cart 4.x
- Tested on PHP 7.0

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit cards**

- [American Express](/payment-methods/american-express)
- [Mastercard](/payment-methods/mastercard)
- [Visa](/payments/methods/credit-and-debit-cards/visa), including [Cartes Bancaires](/payment-methods/cartes-bancaires) & [Dankort](/payments/methods/credit-and-debit-cards/dankort)

**Banking methods**

- [Bancontact](/payment-methods/bancontact)
- [Bank transfer](/payment-methods/bank-transfer)
- [Belfius](/payment-methods/belfius)
- [CBC](/payments/methods/banks/cbc)
- [Dotpay](/payment-methods/dotpay)
- [EPS](/payment-methods/eps)
- [Giropay](/payment-methods/giropay)
- [iDEAL](/payment-methods/ideal)
- [iDEAL QR](/payments/methods/banks/idealqr)
- [ING Home'Pay](/payment-methods/ing-home-pay)
- [CBC/KBC](/payment-methods/cbc-kbc)
- [Maestro](/payment-methods/maestro)
- [Request to Pay](/payments/methods/banks/request-to-pay)
- [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
- [Sofort](/payment-methods/sofort)
- [Trustly](/payment-methods/trustly)
- [TrustPay](/payment-methods/trustpay)
- [V PAY](/payment-methods/vpay)

**Pay later methods**

+ [AfterPay](/payments/methods/billing-suite/afterpay)
+ [Betaal per Maand](/payment-methods/betaal-per-maand)
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
+ [Fashioncheque](https://www.fashioncheque.com/nl)
+ [Fashion gift card](https://www.fashion-giftcard.nl)
+ Fietsenbon
+ [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
+ [Nationale tuinbon](https://www.nationale-tuinbon.nl)
+ [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
+ [Paysafecard](/payment-methods/paysafecard)
+ [Podium](https://www.podiumcadeaukaart.nl)
+ [Sport en Fit](https://www.sportenfitcadeau.nl)
+ [VVV gift card](https://www.vvvcadeaukaarten.nl)
+ [Webshop gift card](https://www.webshopgiftcard.nl)
+ [Wellness gift card](https://www.wellnessgiftcard.nl)
+ Wijncadeau
+ [Winkelcheque](https://www.winkelcheque.nl)
+ [Yourgift](https://www.yourgift.nl)

{{< /details >}}

## Installation
 1. Unpack the content of the .ZIP file in the root of your CS-Cart webshop.
 2. To trigger the installation, go to `yourdomain.com/msp_installer.php`. 
 3. Delete the `msp_installer.php` file.
 4. In your [MultiSafepay account](https://merchant.multisafepay.com), provide your [notification URL](/tools/multisafepay-control/set-your-notification-url).

## Configuration
1. Sign in to your CS-Cart [backend](/getting-started/glossary/#backend).
2. Go to **Administration** > **Payment methods**.
3. To add payment methods, click the **+** button.
4. In the next screen, enter a name for the payment method to display during checkout. 
5. In the **Processing unit** field, specify the payment method. 
6. Fill out the other fields as required.
7. Click **Create**.
8. In the **Configure** tab, enter your account ID, site ID, and site code. {{% account_info %}}
Your account ID appears in the top right corner of your MultiSafepay account.

Extra options such as **IP-Validation** and **debugmode** are intended for developers. Leave them unchanged.
