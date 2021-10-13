---
title : "MultiSafepay plugin for CS-Cart"
github_url : "https://github.com/MultiSafepay/CS-Cart"
download_url : "https://github.com/MultiSafepay/CS-Cart/releases/download/1.6.0/Plugin_CS-Cart_1.6.0.zip"
faq: "."
changelog: "https://github.com/MultiSafepay/CS-Cart/blob/master/CHANGELOG.md"
meta_title: "CS-Cart plugin integration - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
logo: "/logo/Plugins/CS-Cart.svg"
weight: 13
title_short: "CS-Cart"
layout: 'single'
description_short: "Free plugin to integrate MultiSafepay payment solutions into your CS-Cart webshop"
url: '/cs-cart/'
aliases: 
    - /plugins/cs-cart
    - /integrations/plugins/cs-cart
    - /integrations/cs-cart
    - /integrations/ecommerce-integrations/cs-cart
    - /payments/integrations/ecommerce-platforms/cs-cart/
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

- [American Express](/payments/methods/credit-and-debit-cards/american-express)
- [Mastercard](/payments/methods/credit-and-debit-cards/mastercard)
- [Visa](/payments/methods/credit-and-debit-cards/visa), including [Cartes Bancaires](/payments/methods/credit-and-debit-cards/cartes-bancaires) & [Dankort](/payments/methods/credit-and-debit-cards/dankort)

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
