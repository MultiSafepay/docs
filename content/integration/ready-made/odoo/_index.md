---
title: "Odoo plugin"
github_url : "https://github.com/MultiSafepay/official-odoo-integration"
download_url : "https://github.com/MultiSafepay/official-odoo-integration/archive/13.0-develop.zip"
breadcrumb_title: "Odoo"
changelog: https://github.com/MultiSafepay/official-odoo-integration/blob/13.0-develop/CHANGELOG.md
changelog_url : "."
layout: 'single'
meta_title: "Odoo plugin - MultiSafepay Docs"		
meta_description: "Free plugin to integrate MultiSafepay payment solutions with Odoo."
weight: 11
logo: "/logo/Plugins/Odoo.svg"
title_short: "Odoo"
type: 'Plugin'
url: '/odoo/'
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
    - /payments/integrations/ecommerce-platforms/odoo/faq/generic-gateways/
    - /odoo/generic-gateways/
    - /odoo/configuring-generic-gateways/
    - /payments/integrations/ecommerce-platforms/odoo/faq/updating-the-plugin/
    - /odoo/updates/
---

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with Odoo. 

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- Odoo 13.0
- Tested on Python 3.6

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

The plugin receives regular updates from Odoo and MultiSafepay.

{{< /details >}}

## Installation

{{< blue-notice >}} We recommend first installing the plugin in a test environment, following the Odoo installation procedure. Always make a backup. {{< /blue-notice >}}

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
6. In your Odoo backend, activate developer mode.
7. Go to the **Apps menu** > **Update apps list**.
8. Search for and open the MultiSafepay payments module `payment_multisafepay_official`.
9. Click **Install**.

## Configuration
1. Sign in to your Odoo backend. 
2. Go to the **Invoicing** or **Website** menu > **Configuration** > **Payment acquirers**.
3. Select **MultiSafepay** payment acquirer. 
4. Go to **Edit** mode. 
5. To change the acquirer state, click **Enabled** or **Test**. (Default: Disabled)
6. Enter **Live** and/or **Test** **API key**.
7. On the **Configuration tab**, set **Journal**, and then click **Save**.
9. To get payment methods from your MultiSafepay account, go the **Configuration** tab, click **Pull payment methods**.  
    Make sure the relevant payment methods are activated for your account.
10. Configure each payment method separately
{{< details title="Payment method settings" >}} 

- Name  
- State  
- Country: Disabled for some payment methods  
- Customer group  
- Order amount: Disabled for some payment methods  
- Supported currency: Some payment methods process transactions only in EUR. Orders not created in EUR are converted to the required currency, using **Odoo platform currency rate**. This can only be configured by a system administrator.

{{< /details >}}

## User guide

### Generic gateways

The plugin supports generic gateways, which redirect customers from your checkout to a MultiSafepay [payment page](/payment-pages/). You can use them to integrate custom gift cards, or co-branded credit cards. 

{{< details title="Configuring generic gateways" >}}

1. Sign in to your Odoo backend. 
2. Go to **Invoicing** > **Payment method** > **Other payment acquirer** > **MultiSafepay**.
3. In the **Title** field, set the relevant [payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids). 
4. Set the gateway logo and name.

Generic gateways support:

- All payment methods (filter by country, and minimum/maximum amount)
- [Split payments](/payments/split-payments/), [Second Chance reminders](/features/second-chance/) and [virtual IBANs](/payments/virtual-ibans/)
- Refunds (completed orders only)
- [Redirect requests](https://docs-api.multisafepay.com/reference/introduction#direct-vs-redirect) only

**Gift cards**

Generic gateways are particularly useful for integrating [gift cards](/payment-methods/gift-cards/), including [custom gift cards](/payment-methods/gift-cards/custom-cards/). This is because we don't support all [open-loop gift cards](/payment-methods/gift-cards/open-loop-closed-loop/) in our ready-made integrations and *no* closed-loop gift cards.

**Co-branded credit cards**

You can integrate Visa co-branded credit cards ([Cartes Bancaires](/payment-methods/cartes-bancaires/), [Dankort](/payment-methods/dankort/), and [V Pay](/payment-methods/vpay/)), using the generic `VISA` gateway.

For the logo, see MultiSafepay GitHub – [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons/tree/master/methods).

{{< /details >}}

### Payment methods

{{< details title="Payment methods" >}}

- Cards: [All](/payment-methods/credit-debit-cards/)
- Pay later methods: [All](/payment-methods/pay-later/)
- Wallets: [Alipay](/payment-methods/alipay), [Apple Pay](/payment-methods/apple-pay), [PayPal](/payment-methods/paypal)
- Banking methods:
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

{{< /details >}}

### Updates

{{< details title="Updating the plugin" >}}

1. Sign in to your Odoo backend. 
2. Go to the **Apps** menu.
3. Search for and open the **MultiSafepay payments** module.
4. Click **Upgrade**.

{{< /details >}}