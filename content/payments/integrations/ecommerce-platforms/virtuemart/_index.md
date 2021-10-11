---
title : "MultiSafepay plugin for VirtueMart"
github_url : "https://github.com/MultiSafepay/Virtuemart"
download_url : "https://github.com/MultiSafepay/VirtueMart/releases/download/2.2.2/Plugin_VirtueMart_2.2.2.zip"
changelog_url : "."
faq: "."
meta_title: "VirtueMart plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
logo: "/logo/Plugins/VirtueMart.svg"
weight: 18
title_short: "VirtueMart"
layout: 'single'
changelog : "https://github.com/MultiSafepay/VirtueMart/blob/master/CHANGELOG.md"
url: '/ecommerce-platforms/virtuemart/'
aliases:
    - /integrations/virtuemart/
    - /plugins/virtuemart
    - /integrations/plugins/virtuemart
    - /integrations/virtuemart
    - /plugins/virtuemart/manual
    - /integrations/plugins/virtuemart/manual
    - /integrations/virtuemart/manual
    - /integrations/ecommerce-integrations/virtuemart
    - /payments/integrations/ecommerce-platforms/virtuemart/
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your VirtueMart webshop.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended VirtueMart installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support" >}}
&nbsp; 
Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}

- MultiSafepay account – See [Getting started](/getting-started/).
- Joomla 2.5 & 3.x + Virtuemart 2.x & 3.x
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
- [iDEAL QR](/payments/methods/banks/idealqr)
- [ING Home'Pay](/payments/methods/banks/ing-home-pay)
- [KBC](/payments/methods/banks/kbc)
- [Maestro](/payments/methods/credit-and-debit-cards/maestro)
+ [SEPA Direct Debit](/payments/methods/banks/sepa-direct-debit)
- [Sofort](/payments/methods/banks/sofort-banking)
- [Trustly](/payments/methods/banks/trustly)
+ [TrustPay](/payments/methods/banks/trustpay)
+ [V PAY](/payments/methods/credit-and-debit-cards/vpay)

**Pay later methods**

+ [Betaal per Maand](/payments/methods/billing-suite/betaalpermaand)
+ [E-Invoicing](/payments/methods/billing-suite/e-invoicing)
+ [Klarna](/payments/methods/billing-suite/klarna)
+ [Pay After Delivery](/payments/methods/billing-suite/pay-after-delivery)

**Wallets**

+ [Alipay](/payments/methods/wallet/alipay)
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

## Installation
1. Sign in to your VirtueMart [backend](/getting-started/glossary/#backend).
2. Go to **Extensions** > **Extension manager**.
3. Install the Plugin_VirtueMart_x.x.x.zip file using **Drag and drop** or **Browse for file**. 
4. Click **Upload & install**.

## Configuration
1. Sign in to your VirtueMart backend.
2. Go to **Extensions** > **Plugins**.
3. In the search box, enter **MultiSafepay**, and then set the plugin status to **Enabled**.
4. Go to **Components** > **VirtueMart**. 
5. Click **Shop** > **Payment methods**. 
6. To install and configure each payment method separately:  
    - Click **New**.
    - Set the payment method to **VirtueMart – Payment, MultiSafepay**.
    - To install, save the **Payment method name**.
7. On the **Configuration** tab, enter your:
    - Account ID
    - [Site ID, API key, and secure code](/set-up-your-account/site-id-api-key-secure-code)
    - Gateway ID  


