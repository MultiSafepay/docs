---
title : "MultiSafepay plugin for Drupal 7"
github_url : "https://github.com/MultiSafepay/Drupal-Commerce"
download_url : "https://github.com/MultiSafepay/Drupal-Commerce/releases/download/2.2.0/Plugin_Drupal_2.2.0.zip"
changelog: https://docs.multisafepay.com/payments/integrations/ecommerce-platforms/drupal7/changelog/
faq: "."
meta_title: "Drupal 7 plugin - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
logo: "/logo/Plugins/Drupal_7.svg"
weight: 15
title_short: "Drupal 7"
description_short: "Free plugin to integrate MultiSafepay payment solutions into your Drupal 7 webshop"
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

**Credit cards**

- [American Express](/payments/methods/credit-and-debit-cards/american-express)
- [Mastercard](/payments/methods/credit-and-debit-cards/mastercard)
- [Visa](/payments/methods/credit-and-debit-cards/visa), including [Cartes Bancaires](/payments/methods/credit-and-debit-cards/cartes-bancaires) & [Dankort](/payments/methods/credit-and-debit-cards/dankort)

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
- [SEPA Direct Debit](/payments/methods/banks/sepa-direct-debit)
- [Sofort](/payments/methods/banks/sofort-banking)
- [TrustPay](/payments/methods/banks/trustpay)
- [V PAY](/payments/methods/credit-and-debit-cards/vpay)

**Pay later methods**

+ [E-Invoicing](/payments/methods/billing-suite/e-invoicing)
+ [Klarna](/payments/methods/billing-suite/klarna)
+ [Pay After Delivery](/payments/methods/billing-suite/pay-after-delivery)

**Wallets**

+ [Alipay](/payments/methods/wallet/alipay)
+ [Apple Pay](/payments/methods/wallet/applepay)
+ [PayPal](/payments/methods/wallet/paypal)

**Prepaid cards**

+ [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
+ [Fashioncheque](https://www.fashioncheque.com/nl)
+ [Fashion gift card](https://www.fashion-giftcard.nl)
+ [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome)
+ [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl
+ [Paysafecard](/payments/methods/prepaid-cards/paysafecard)
+ Wijn cadeau
+ [Yourgift](https://www.yourgift.nl)

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
