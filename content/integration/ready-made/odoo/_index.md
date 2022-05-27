---
title: "MultiSafepay plugin for Odoo"
github_url : "https://github.com/MultiSafepay/official-odoo-integration"
download_url : "https://github.com/MultiSafepay/official-odoo-integration/archive/13.0-develop.zip"
breadcrumb_title: "Odoo"
changelog: https://github.com/MultiSafepay/official-odoo-integration/blob/13.0-develop/CHANGELOG.md
changelog_url : "."
faq: "."
layout: "single"
meta_title: "Odoo plugin - MultiSafepay Docs"		
meta_description: "MultiSafepay plugin for Odoo. Easily integrate MultiSafepay payment solutions into your Odoo platform with the free plugin."
weight: 11
logo: "https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Odoo.svg"
title_short: "Odoo"
type: "Plugin"
url: "/odoo/"
aliases: 
    - /plugins/odoo
    - /integrations/plugins/odoo
    - /integrations/odoo
    - /support-tab/odoo/manual
    - /plugins/odoo/manual
    - /integrations/plugins/odoo/manual
    - /integrations/odoo/manual
    - /integrations/ecommerce-integrations/odoo
    - /payments/integrations/ecommerce-platforms/odoo/
    - /ecommerce-platforms/odoo/
---

This technical manual is for installing and configuring our free plugin for integrating MultiSafepay payment solutions into your Odoo webshop. Our plugin receives regular updates from Odoo and MultiSafepay.

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
- Odoo 13.0
- Tested on Python 3.6

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit cards**

- [American Express](/payment-methods/amex)
- [Maestro](/payment-methods/maestro)
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
- [iDEAL](/payment-methods/ideal)
- [SEPA Direct Debit](/payment-methods/sepa-direct-debit)
- [Sofort](/payment-methods/sofort)
- [Trustly](/payment-methods/trustly)

**Pay later methods**

- [AfterPay](/payment-methods/afterpay)
- [Betaal per Maand](/payment-methods/betaal-per-maand/)
- [E-Invoicing](/payment-methods/e-invoicing)
- [in3](/payment-methods/in3)
- [Klarna](/payment-methods/klarna)
- [Pay After Delivery](/payment-methods/pay-after-delivery)

**Wallets**

- [Alipay](/payment-methods/alipay)
- [Apple Pay](/payment-methods/apple-pay)
- [PayPal](/payment-methods/paypal)

See also [MultiSafepay gateway](/developer/generic-gateways/#multisafepay-gateways).

{{< /details >}}

## Installation

{{< blue-notice >}} We recommend first installing the plugin in a test environment following, the recommended Odoo installation procedure. Make sure you have made a backup. {{< /blue-notice >}}

1. Download the ZIP archive with module.
2. Unpack the content of the .ZIP file.
3. In your Odoo server (`/mnt/extra-addons/`), under **Custom apps**, add the **payment_multisafepay_official** folder. 
4. Install the required Python dependencies:
    ```
    pip3 install -r requirements.txt
    ```
    Alternatively, you can install them manually:
    ```
    pip3 install multisafepay==0.2.0
    ```
    For more information about dependencies, see Python - [MultiSafepay](https://pypi.org/project/multisafepay).
5. Restart your Odoo server.
6. In your Odoo [backend](/glossaries/multisafepay-glossary/#backend), activate developer mode.
7. Go to the **Apps menu** > **Update apps list**.
8. Search for and open the MultiSafepay payments module `payment_multisafepay_official`.
9. Click **Install**.

## Configuration
1. Sign in to your Odoo backend. 
2. Go to the **Invoicing** or **Website** menu > **Configuration** > **Payment acquirers**.
3. Select **MultiSafepay** payment acquirer. 
4. Go to **Edit** mode. 
5. By default, acquirer state is disabled. To change the state, click **Enabled** or **Test**.
6. Enter **Live** and/or **Test** **API key**.
7. On the **Configuration tab**, set **Journal**.
8. Click **Save**.
9. To get payment methods from your MultiSafepay account, go the **Configuration** tab, click **Pull payment methods**.  
    Make sure the relevant payment methods are activated for your account.
10.  Configure for each payment method separately:  
    - Name  
    - State  
    - Country: Disabled for some payment methods  
    - Customer group  
    - Order amount: Disabled for some payment methods  
    - Supported currency: Some payment methods process transactions only in EUR. Orders not created in EUR are converted to the required currency, using **Odoo platform currency rate**. This can only be configured by a system administrator.

