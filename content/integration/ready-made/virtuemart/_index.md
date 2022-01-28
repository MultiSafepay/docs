---
title : "MultiSafepay plugin for VirtueMart"
github_url : "https://github.com/MultiSafepay/Virtuemart"
download_url : "https://github.com/MultiSafepay/VirtueMart/releases/download/2.2.2/Plugin_VirtueMart_2.2.2.zip"
changelog_url : "."
faq: "."
meta_title: "VirtueMart plugin - MultiSafepay Docs"
logo: "/logo/Plugins/VirtueMart.svg"
weight: 18
title_short: "VirtueMart"
type: 'Plugin'
layout: 'single'
changelog : "https://github.com/MultiSafepay/VirtueMart/blob/master/CHANGELOG.md"
url: '/virtuemart/'
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
    - /ecommerce-platforms/virtuemart/
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your VirtueMart webshop.

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

**Credit and debit cards**

- [American Express](/payment-methods/american-express)
- [Maestro](/payment-methods/maestro/)
- [Mastercard](/payment-methods/mastercard)
- [Visa](/payment-methods/visa), including [Cartes Bancaires](/payment-methods/cartes-bancaires), [Dankort](/payment-methods/dankort), and [V Pay](/payment-methods/vpay/)

**Banking methods**

- [Bancontact](/payment-methods/bancontact)
- [Bank Transfer](/payment-methods/bank-transfer)
- [Belfius](/payment-methods/belfius)
- [CBC/KBC](/payment-methods/cbc-kbc)
- [Dotpay](/payment-methods/dotpay)
- [EPS](/payment-methods/eps)
- [Giropay](/payment-methods/giropay)
- [iDEAL and iDEAL QR](/payment-methods/ideal)
- [Request to Pay](/payment-methods/request-to-pay/)
- [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
- [Sofort](/payment-methods/sofort)
- [Trustly](/payment-methods/trustly)
- [TrustPay](/payment-methods/trustpay)

**Pay later methods**

- [AfterPay](/payment-methods/afterpay/)
- [Betaal per Maand](/payment-methods/betaal-per-maand)
- [E-Invoicing](/payment-methods/e-invoicing)
- [in3](/payment-methods/in3/)
- [Klarna](/payment-methods/klarna)
- [Pay After Delivery](/payment-methods/pay-after-delivery)

**Wallets**

- [Alipay](/payment-methods/alipay)
- [Apple Pay](/payment-methods/apple-pay/) – **Note:** If a customer selects Apple Pay at checkout but isn't on an Apple device, they receive a notification to select another payment method. 
- [PayPal](/payment-methods/paypal)
- [Google Pay](/payment-methods/google-pay/)
- [WeChat Pay](/payment-methods/wechat-pay/)

**Prepaid cards**

- Beauty and Wellness gift card
- [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
- [Edenred](/payment-methods/edenred/)
- [Fashioncheque](https://www.fashioncheque.com/nl)
- [Fashion gift card](https://www.fashion-giftcard.nl)
- Fietsenbon
- [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
- [Nationale tuinbon](https://www.nationale-tuinbon.nl)
- [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl)
- [Paysafecard](/payment-methods/paysafecard)
- [Podium](https://www.podiumcadeaukaart.nl)
- [Postepay](/payment-methods/postepay/)
- [Sport en Fit](https://www.sportenfitcadeau.nl)
- [VVV gift card](https://www.vvvcadeaukaarten.nl)
- [Webshop gift card](https://www.webshopgiftcard.nl)
- [Wellness gift card](https://www.wellnessgiftcard.nl)
- Wijncadeau
- [Winkelcheque](https://www.winkelcheque.nl)
- [Yourgift](https://www.yourgift.nl/)

See also [MultiSafepay gateway](/developer/generic-gateways/#multisafepay-gateways).

{{< /details >}}

## Installation

{{< blue-notice >}} We recommend first installing the plugin in a test environment following, the recommended VirtueMart installation procedure. Make sure you have made a backup. {{< /blue-notice >}}

1. Sign in to your VirtueMart [backend](/glossaries/multisafepay-glossary/#backend).
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


