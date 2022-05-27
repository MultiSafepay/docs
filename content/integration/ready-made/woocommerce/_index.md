---
title : "MultiSafepay plugin for WooCommerce"
github_url : "https://github.com/MultiSafepay/WooCommerce"
download_url : "https://github.com/MultiSafepay/WooCommerce/releases/download/4.15.0/Plugin_WooCommerce_4.15.0.zip"
changelog_url : "."
faq: "."
repo_url : "MultiSafepay/WooCommerce"
meta_title: "WooCommerce plugin - MultiSafepay Docs"
meta_description: "Integrate MultiSafepay payment solutions into your Wordpress WooCommerce webshop. MultiSafepay Docs provides information about getting started, building and testing integrations."
logo: "https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/WooCommerce.svg"
weight: 03
title_short: "WooCommerce"
type: "Plugin"
url: "/woo-commerce/"
layout: "single"
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
    - /payments/integrations/ecommerce-platforms/woocommerce/
    - /ecommerce-platforms/woocommerce/
---

This technical manual is for installing and configuring our free plugin for WooCommerce. WooCommerce is a free, open-source ecommerce platform for Wordpress.

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

- [American Express](/payment-methods/american-express/)
- [Maestro](/payment-methods/maestro)
- [Mastercard](/payment-methods/mastercard)
- [Visa](/payment-methods/visa), including [Cartes Bancaires](/payments/methods/cartes-bancaires), [Dankort](/payments/methods/dankort), and [V Pay](/payment-methods/vpay/)

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

**Pay later methods**

- [AfterPay](/payment-methods/afterpay)
- [Betaal per Maand](/payment-methods/betaal-per-maand)
- [E-Invoicing](/payment-methods/e-invoicing)
- [in3](/payment-methods/in3)
- [Klarna](/payment-methods/klarna)
- [Pay After Delivery](/payment-methods/pay-after-delivery)

**Wallets**

- [Alipay](/payment-methods/alipay)
- [Apple Pay](/payment-methods/apple-pay)
- [PayPal](/payment-methods/paypal)

**Prepaid cards**

- Baby Cadeaubon
- Beauty and Wellness gift card
- [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
- [Fashioncheque](https://www.fashioncheque.com/nl)
- [Fashion gift card](https://www.fashion-giftcard.nl)
- Fietsenbon
- [Good4fun](https://www.good4fun.nl)
- Goodcard
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

## Installation

{{< blue-notice >}} We recommend first installing the plugin in a test environment following, the recommended WooCommerce installation procedure. Make sure you have made a backup. {{< /blue-notice >}}

There are two ways to install the plugin:

**Manual installation**

1. Click the **Download** button above.
2. Sign in to your WooCommerce [backend](/glossaries/multisafepay-glossary/#backend).
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
2. Go to **WooCommerce** > **MultiSafepay settings**
3. On the **Account** tab, enter your API key. For where to find your API key, see [API key](/tools/multisafepay-control/get-your-api-key).
4. On the **Order status** tab, confirm the match between WooCommerce order statuses and MultiSafepay order statuses, and then click **Save changes**.
4. On the **Options** tab, confirm your settings, and then click **Save changes**.
5. On the **WooCommerce** > **Settings** > **Payments**. Enable the relevant payment methods and confirm the settings.


