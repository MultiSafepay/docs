---
title : "MultiSafepay plugin for WooCommerce"
github_url : "https://github.com/MultiSafepay/WooCommerce"
download_url : "https://github.com/MultiSafepay/WooCommerce/releases/download/4.8.3/Plugin_WooCommerce_4.8.3.zip"
changelog_url : "."
faq: "."
repo_url : "MultiSafepay/WooCommerce"
meta_title: "WooCommerce plugin - MultiSafepay Docs"
meta_description: "Integrate MultiSafepay payment solutions into your Wordpress WooCommerce webshop. MultiSafepay Docs provides information about getting started, building and testing integrations."
logo: "/logo/Plugins/WooCommerce.svg"
weight: 03
title_short: "WooCommerce"
url: '/ecommerce-platforms/woo-commerce/'
layout: 'single'
changelog : "https://github.com/MultiSafepay/WooCommerce/blob/master/CHANGELOG.md"
aliases: 
    - /plugins/woocommerce
    - /integrations/plugins/woocommerce
    - /integrations/woocommerce
    - /plugins/woocommerce/manual
    - /integrations/plugins/woocommerce/manual
    - /integrations/woocommerce/manual
    - /integrations/ecommerce-integrations/woocommerce
    - /payments/integrations/ecommerce-platforms/woocommerce/manual
    - /payments/integrations/ecommerce-platforms/woocommerce/faq/supported-payment-methods/
---

This technical manual is for installing and configuring the MultiSafepay plugin for WooCommerce. WooCommerce is a free, open-source ecommerce platform for Wordpress.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the plugin in a test environment following the recommended WooCommerce installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Requirements" >}}

- MultiSafepay account – See [Getting started](/getting-started/).
- Wordpress 5.0
- PHP 7.2

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
- [V PAY](/payments/methods/credit-and-debit-cards/vpay)

**Pay later methods**

+ [AfterPay](/payments/methods/billing-suite/afterpay)
+ [Betaal per Maand](/payments/methods/billing-suite/betaalpermaand/)
+ [E-Invoicing](/payments/methods/billing-suite/e-invoicing)
+ [in3](/payments/methods/billing-suite/in3)
+ [Klarna](/payments/methods/billing-suite/klarna)
+ [Pay After Delivery](/payments/methods/billing-suite/pay-after-delivery)

**Wallets**

+ [Alipay](/payments/methods/wallet/alipay)
+ [Apple Pay](/payments/methods/wallet/applepay)
+ [PayPal](/payments/methods/wallet/paypal)

**Prepaid cards**

+ Baby Cadeaubon
+ Beauty and Wellness gift card
+ [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
+ [Fashioncheque](https://www.fashioncheque.com/nl)
+ [Fashion gift card](https://www.fashion-giftcard.nl)
+ Fietsenbon
+ [Good4fun](https://www.good4fun.nl)
+ Goodcard
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

There are two ways to install the plugin:

**Manual installation**

1. Click the **Download** button above.
2. Sign in to your WooCommerce [backend](/getting-started/glossary/#backend).
3. Go to **Plugins** > **Add new**. 
4. Click **Browse file**.
5. Upload the Plugin_WooCommerce_x.x.x.zip file.

**Wordpress installation**

1. Sign in to your WooCommerce backend.
2. Go to **Plugins** > **Add new**.
3. Search for **MultiSafepay**. 
4. For the **MultiSafepay plugin for WooCommerce**, click the **Install now** button.

## Configuration
1. Sign in to your WooCommerce backend.
2. Go to **WooCommerce** > **MultiSafepay Settings**
3. On the **Account** tab, enter your API key. For where to find your API key, see [API key](/tools/multisafepay-control/get-your-api-key).
4. On the **Order status** tab, confirm the match between WooCommerce order statuses and MultiSafepay order statuses, and then click **Save changes**.
4. On the **Options** tab, confirm your settings, and then click **Save changes**.
5. On the **WooCommerce** > **Settings** > **Payments**. Enable the relevant payment methods and confirm the settings.


