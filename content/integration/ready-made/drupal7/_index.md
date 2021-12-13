---
title: "MultiSafepay plugin for Drupal 7"
github_url: "https://github.com/MultiSafepay/Drupal-Commerce"
download_url: "https://github.com/MultiSafepay/Drupal-Commerce/releases/download/2.2.0/Plugin_Drupal_2.2.0.zip"
changelog: https://github.com/MultiSafepay/Drupal-Commerce/blob/master/CHANGELOG.md
faq: "."
type: 'Plugin'
meta_title: "Drupal 7 plugin - MultiSafepay Docs"
logo: "/logo/Plugins/Drupal_7.svg"
weight: 15
title_short: "Drupal 7"
description_short: "Free plugin to integrate MultiSafepay payment solutions into your Drupal 7 webshop."
layout: 'single'
url: '/drupal-7/'
aliases: 
    - /plugins/drupal7
    - /integrations/plugins/drupal7
    - /integrations/drupal7
    - /integrations/ecommerce-integrations/drupal7
    - /payments/integrations/ecommerce-platforms/drupal7/
    - /ecommerce-platforms/drupal-7/
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Drupal 7 webshop.

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
- Drupal 7.x
- Tested on PHP 7.0

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit and debit cards**

- [American Express](/payment-methods/american-express)
- [Mastercard](/payment-methods/mastercard)
- [Maestro](/payment-methods/maestro)
- [Visa](/payments/methods/credit-and-debit-cards/visa), including [Cartes Bancaires](/payment-methods/cartes-bancaires), [Dankort](/payments/methods/credit-and-debit-cards/dankort), and [V Pay](/payment-methods/vpay)

**Banking methods**

- [Bancontact](/payment-methods/bancontact)
- [Bank Transfer](/payment-methods/bank-transfer)
- [Belfius](/payment-methods/belfius)
- [CBC/KBC](/payment-methods/cbc-kbc)
- [Dotpay](/payment-methods/dotpay)
- [EPS](/payment-methods/eps)
- [Giropay](/payment-methods/giropay)
- [iDEAL](/payment-methods/ideal)
- [Request to Pay](/payments/methods/banks/request-to-pay)
- [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
- [Sofort](/payment-methods/sofort)
- [TrustPay](/payment-methods/trustpay)

**Pay later methods**

- [E-Invoicing](/payment-methods/e-invoicing)
- [Klarna](/payment-methods/klarna)
- [Pay After Delivery](/payment-methods/pay-after-delivery)

**Wallets**

- [Alipay](/payment-methods/alipay)
- [Apple Pay](/payments/methods/wallet/applepay)
- [PayPal](/payment-methods/paypal)

**Prepaid cards**

- [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
- [Fashioncheque](https://www.fashioncheque.com/nl)
- [Fashion gift card](https://www.fashion-giftcard.nl)
- [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
- [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl
- [Paysafecard](/payment-methods/paysafecard)
- Wijn cadeau
- [Yourgift](https://www.yourgift.nl)

{{< /details >}}

## Installation and configuration
1. Unpack the content of the .ZIP file in the root of your Drupal 7 webshop.
2. Sign in to your Drupal 7 [backend](/getting-started/glossary/#backend).
3. Go to **Site settings** > **Modules**. 
4. Enable the Commerce MultiSafepay JSON module, and your selected payment method modules. 
5. Click **Save configuration**.
6. Go to **Store settings** > **Advanced store settings** > **Payment methods**.
7. **Enable** the `multisafepay` core module.
8. **Enable** the modules for each payment method.
9. To configure each payment method, under **Actions**, click the **Edit** button.
10. When the main module is installed, two rules are created but disabled by default:  
    * MultiSafepay order paid in full: Order state to `processing`  
This rule sets the order to `processing` when the order is paid in full.  

    * MultiSafepay order complete: Shipped at MultiSafepay  
This rule updates the [transaction status](/payments/multisafepay-statuses/) to **Shipped** at MultiSafepay. For Pay After Delivery, Klarna, and E-Invoicing, this triggers the invoicing process.
