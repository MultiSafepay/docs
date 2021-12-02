---
title : "MultiSafepay plugin for X-Cart"
github_url : "https://github.com/MultiSafepay/X-Cart"
download_url : "https://github.com/MultiSafepay/X-Cart/releases/download/2.3.0/Plugin_X-Cart_2.3.0.zip"
changelog_url : "."
faq: "."
meta_title: "X-Cart plugin - MultiSafepay Docs"
logo: "/logo/Plugins/X-Cart.svg"
weight: 14
title_short: "X-Cart"
type: 'Plugin'
layout: 'single'
changelog : "https://github.com/MultiSafepay/X-Cart/blob/master/CHANGELOG.md"
url: '/x-cart/'
aliases:
    - /integrations/x-cart/
    - /plugins/x-cart
    - /integrations/plugins/x-cart
    - /integrations/x-cart
    - /plugins/x-cart/manual
    - /integrations/plugins/x-cart/manual
    - /integrations/x-cart/manual
    - /integrations/ecommerce-integrations/x-cart
    - /payments/integrations/ecommerce-platforms/x-cart/
    - /ecommerce-platforms/x-cart/
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your X-Cart webshop.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended X-Cart installation procedure. Make sure you have made a backup.

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
- X-Cart 5.x        
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
- [Dotpay](/payment-methods/dotpay)
- [EPS](/payment-methods/eps)
- [Giropay](/payment-methods/giropay)
- [iDEAL](/payment-methods/ideal)
- [iDEAL QR](/payments/methods/banks/idealqr)
- [ING Home'Pay](/payment-methods/ing-home-pay)
- [CBC/KBC](/payment-methods/cbc-kbc)
- [Maestro](/payment-methods/maestro)
+ [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
- [Sofort](/payment-methods/sofort)
- [Trustly](/payment-methods/trustly)
+ [TrustPay](/payment-methods/trustpay)
+ [V PAY](/payment-methods/vpay)

**Pay later methods**

+ [AfterPay](/payments/methods/billing-suite/afterpay)
+ [Betaal per Maand](/payment-methods/betaal-per-maand)
+ [E-Invoicing](/payment-methods/e-invoicing)
+ [Klarna](/payment-methods/klarna)
+ [Pay After Delivery](/payment-methods/pay-after-delivery)

**Wallets**

+ [Alipay](/payment-methods/alipay)
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
+ [Yourgift](https://www.yourgift.nl/)

{{< /details >}}

## Installation
1. In the root of your webshop, unzip the content of the .ZIP file.
2. Sign in to your X-Cart [backend](/getting-started/glossary/#backend).
3. Go to **System tools** > **Cache management** > **Re-deploy the store**.
4. Click **Start**.

## Configuration
1. Sign in to your X-Cart backend.
2. Go to **My Addons**, and search for **MultiSafepay**.
3. Locate and enable **MultiSafepay Connect**. This is required to enter your [API key](/getting-started/glossary/#api-key) in a later step.
4. Select the relevant payment methods, and then click **Save changes**.
5. Go to **Store setup** > **Payment methods**.
6. Locate and activate your enabled payment methods.
7. For **MultiSafepay Connect**, click **Configure**.
8. For **Account type**, you have two options: **Live** and **Test**.  
    - Enter your account ID, site ID, site secure code, and your API key.
    - Make sure you enter the correct API key for the account type you want to use. 
    - For where to find your account ID, site ID, site secure code, see [API key](/tools/multisafepay-control/get-your-api-key).
9. Click **Save changes**.  

