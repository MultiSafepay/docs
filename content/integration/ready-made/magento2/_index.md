---
title: "Magento 2 plugin"
breadcrumb_title: "Magento 2"
github_url : "https://github.com/MultiSafepay/Magento2"
changelog_url : "."
type: 'Plugin'
layout: 'single-old-button'
meta_title: "Magento 2 plugin - MultiSafepay Docs"		
meta_description: "Free plugin to integrate MultiSafepay payment solutions with Magento 2."
changelog: https://github.com/MultiSafepay/magento2/blob/master/CHANGELOG.md
weight: 01
logo: "/logo/Plugins/Magento_2.svg"
title_short: "Magento 2"
url: '/magento-2/'
aliases: 
    - /plugins/magento2
    - /integrations/plugins/magento2
    - /integrations/magento2
    - /support-tab/magento2/manual
    - /plugins/magento2/manual
    - /integrations/plugins/magento2/manual
    - /integrations/magento2/manual
    - /integrations/ecommerce-integrations/magento2
    - /integrations/plugins/magento2/beta
    - /integrations/ecommerce-integrations/magento2
    - /payments/integrations/ecommerce-platforms/magento2/
    - /ecommerce-platforms/magento-2/
    - /integrations/ecommerce-integrations/magento2/faq/does-the-magento-2-plugin-support-magento-vault/
    - /payments/integrations/ecommerce-platforms/magento2/faq/activating-magento-vault/
    - /magento-2/magento-vault/
    - /integrations/ecommerce-integrations/magento2/faq/does-the-magento-2-plugin-support-magento-vault/
    - /payments/integrations/ecommerce-platforms/magento2/faq/activating-credit-card-component/
    - /payments/integrations/ecommerce-platforms/magento2/faq/activating-payment-component/
    - /magento-2/payment-components/
    - /magento2/faq/payment-links-in-order-confirmation-for-backend-orders
    - /integrations/magento2/faq/payment-links-in-order-confirmation-for-backend-orders/
    - /payments/integrations/ecommerce-platforms/magento2/faq/adding-payment-links-in-order-confirmation-emails/
    - /magento-2/payment-links-in-emails/
    - /integrations/magento2/faq/payment-fee-surcharges/
    - /payments/integrations/ecommerce-platforms/magento2/faq/applying-surcharges/
    - /magento-2/surcharges/
    - /payments/integrations/ecommerce-platforms/magento2/faq/configuring-generic-gateways/
    - /magento-2/generic-gateways/
    - /magento-2/configuring-generic-gateways/
    - /integrations/ecommerce-integrations/magento2/faq/which-tax-settings-should-i-use/
    - /payments/integrations/ecommerce-platforms/magento2/faq/configuring-tax-settings/
    - /magento-2/tax-settings/
---

This technical manual is for installing and configuring MultiSafepay's free plugin for integrating with Magento 2.

{{< alert-notice>}} If you are still using the [deprecated plugin](https://github.com/MultiSafepay/Magento2Msp), we recommend migrating to this new version as soon as possible. {{< /alert-notice >}}

{{< details title="Features" >}}

The new plugin features code improvements, and unit and integration testing. It is built on top of the Magento payment provider gateway structure. Some payment methods now skip the MultiSafepay payment page, which increases [conversion](/glossaries/multisafepay-glossary/#conversion-rate).

We support most Magento functionalities. For any questions, email <integration@multisafepay.com>

### New features

- Improved:
    - Magento [backend](/glossaries/multisafepay-glossary/#backend) configuration
    - Translations
    - Error handling
    - Event and error logs
- Support information available in the Magento backend
- Clear explanation of each payment method with links to docs
- Modular setup, providing more installation flexibility
- PWA (GraphQL) endpoints

As of version 2.4.0, we also support [Magento Vault](https://devdocs.magento.com/guides/v2.4/payments-integrations/vault/vault-intro.html) and [Instant Purchase](https://docs.magento.com/user-guide/sales/checkout-instant-purchase.html). For more information, see MultiSafepay Blog - [Magento 2: Boost conversion through Magento Vault & Instant Purchase](https://www.multisafepay.com/blog/magento-2-boost-conversion-through-magento-vault-instant-purchase). 

These features are based on [recurring payments](/payments/recurring-payments/).

### Obsolete features
Features that are no longer available:

- Recurring Payments – replaced by Magento Vault and Instant Purchase
- FastCheckout – no longer supported

{{< /details >}}

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- Magento Open Source version 2.3.x & 2.4.x **or** Adobe Commerce version 2.3.x & 2.4.x (For GraphQL, only Magento Open Source versions 2.4.x are supported)
- PHP 7.1+

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue
- [Magento Slack channel](https://magentocommeng.slack.com) #multisafepay-payments

Our plugin is supported by a certified Magento 2 Solution Specialist and receives regular updates for the latest features from Magento and MultiSafepay.

{{< /details >}}

{{< details title="Payment methods" >}}

- Cards: All
- Banking methods: All
- Pay later methods: All
- Wallets: All
- Prepaid cards:
    - Baby gift card
    - Beauty and Wellness gift card
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Edenred](/payment-methods/edenred)
    - [Fashioncheque](https://www.fashioncheque.com/nl/)
    - [Fashion gift card](https://www.fashion-giftcard.nl/)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome/)
    - [Givacard](https://www.givacard.nl/)
    - [Good4fun](https://www.good4fun.nl/)
    - Goodcard
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl/)
    - [Paysafecard](/payment-methods/paysafecard)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl/)
    - [Podium](https://www.podiumcadeaukaart.nl/)
    - [Sport en Fit](https://www.sportenfitcadeau.nl/)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl/)
    - [Webshop gift card](https://www.webshopgiftcard.nl/)
    - [Wellness gift card](https://www.wellnessgiftcard.nl/)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl/)
    - [Yourgift](https://www.yourgift.nl)

See also [MultiSafepay gateway](/developer/generic-gateways/#multisafepay-gateways).

{{< /details >}}

## Modules

{{< details title="Magento modules" >}}
The plugin consists of several Magento modules:

| Module  | Description  |
|---|---|
| [Multisafepay-magento2-core](https://github.com/MultiSafepay/magento2-core)   | Provides core functionalities  |
| [Multisafepay-magento2-frontend](https://github.com/MultiSafepay/magento2-frontend)  | Enables payment gateways in the Magento checkout  |
| [Multisafepay-magento2-adminhtml](https://github.com/MultiSafepay/magento2-adminhtml)  | Enables/disables payment gateways, and changes settings in the Magento backend  |
| [Multisafepay-magento2-msi](https://github.com/MultiSafepay/magento2-msi)  | Handles stock when MSI is enabled  |
| [Multisafepay-magento2-catalog-inventory](https://github.com/MultiSafepay/magento2-catalog-inventory)  | Handles stock when MSI is disabled  |
| [Multisafepay-magento2](https://github.com/MultiSafepay/magento2)  | Meta package that installs all the above  |
| [Multisafepay-magento2-graphql](https://github.com/MultiSafepay/magento2-graphql)| For GraphQL support, extends and adds GraphQL queries and mutations |

{{< /details >}}

{{< details title="Module dependencies" >}}

The meta-package has a dependency on MSI. This means the MSI modules must be available (but not necessarily enabled) in your store. 

If you have removed MSI (e.g. with a composer-replace trick like [yireo/magento2-replace-inventory](https://github.com/yireo/magento2-replace-inventory)), you can't install the meta-package. To integrate with MultiSafepay, instead of installing the meta-package, install the magento2-frontend module and the magento2-catalog-inventory module.

The magento2-frontend module has a dependency on the magento2-core and magento2-adminhtml modules, so they are all installed together. In some cases, you also then need a stock-handling module. Since MSI is not available, you can install the magento2-catalog-inventory module instead.

The installation process is the same for the Adobe Commerce version.

{{< /details >}}

## Installation

**Note:** Make sure you finish processing all orders created in the deprecated plugin **before** you [delete it](/magento-2/deleting-deprecated-plugin/). Meanwhile, it can run in parallel with the new plugin. 

**1.** We recommend installing the meta-package using Composer:

``` 
composer require multisafepay/magento2
php bin/magento setup:upgrade
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy
```

**2.** To enable all the modules, use the following command in the Magento 2 root directory:
```
./bin/magento module:enable `./bin/magento module:status | grep MultiSafepay_`
```

### Stock handling

When you disable MSI in Magento 2, you must also disable the MultiSafepay MSI module using the following command:
```
php bin/magento module:disable MultiSafepay_ConnectMSI
```
If you have enabled MSI in Magento 2, to disable the MultiSafepay CatalogInventory module, use the following command:
```
php bin/magento module:disable MultiSafepay_ConnectCatalogInventory
```

## Configuration
Sign in to your Magento 2 backend, and go to **Stores** > **Configuration** > **MultiSafepay**. This section contains the following pages:

- **General information:** Contains all the main support information. We recommend reading this first.
- **General settings:** Contains all main settings.  
  - Here you can configure all gateways and gift cards.  
  - Enter your [account ID, site ID, site secure code](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).   
- **Payment methods:** Contains the configuration options for all MultiSafepay payment methods.  
    - Make sure you have activated your selected payment methods in your [MultiSafepay dashboard](https://merchant.multisafepay.com).
- **Gift cards:** Contains the configuration options for all gift cards supported by MultiSafepay.  
    - Make sure you have activated your selected gift cards in your [MultiSafepay dashboard](https://merchant.multisafepay.com).  
    - For more information, see [Gift cards](/payments/methods/prepaid-cards/gift-cards).

## User guide

### Magento Vault and Instant Purchase

Magento Vault enables you to use [Instant purchase](https://magento.com/innovations-lab/instant-purchase), a feature that helps make repeat payments faster and easier, increasing conversion. 

{{< details title="How it works" >}}

1. After filling out their credit card number, CVC, and expiry date at checkout, customers can give permission to store these details for future payments. 
2. MultiSafepay encrypts the sensitive payment details and stores the encrypted version on our secure, GDPR compliant servers. 
3. We return a non-sensitive identifier for the payment details, known as a token, which can only be used in your Magento webshop. 
4. The token is automatically stored in your Magento Vault. 
5. For subsequent payments, the customer can simply click **Instant purchase** at checkout. They don't need to re-provide any details. 

{{< /details >}}

{{< details title="Mastercard and Visa requirements" >}} 

You must:  

- Include a checkbox at checkout for customers to give permission to tokenize their payment details (provided as standard by Magento Vault).
- Explain in your terms and conditions how you use and store their details.
- Inform customers how they can delete stored payment details.

{{< /details >}}

{{< details title="Activating Magento Vault" >}} 
&nbsp;  
To activate Magento Vault, email a request to enable [recurring payments](/features/recurring-payments/) to <sales@multisafepay.com>

{{< /details >}}

{{< details title="Vault security" >}} 

If you host Magento yourself, the security of the vault depends on the security of your server. 

However, the vault only contains tokens valid in your webshop. If your server is compromised, no actual payment details are at risk, only stored customer data.   

{{< /details >}}

### Payment components

The plugin supports [Payment Components](/payment-components/), which:

- Provide a seamless checkout experience to increase [conversion](/glossaries/multisafepay-glossary/#conversion-rate).
- Encrypt customer payment details for secure processing.
- Shift responsibility for [PCI DSS compliance](/glossaries/multisafepay-glossary/#payment-card-industry-data-security-standard-pci-dss) to MultiSafepay.

{{< details title="Activating the payment component in your backend" >}}

1. Sign in to your Magento 2 backend.
2. Go to **Configuration** > **Credit card**, and then click **Configure**.
3. Click **Payment type** and select **Credit card component**.
4. Click **Save config**.

For questions, email <integration@multisafepay.com>

**Note:** If you have a custom checkout and encounter a conflict with the payment component, the Integration Team will do their best to provide support, but we can't guarantee compatibility in all cases.

{{< /details >}}

### Surcharges

[Surcharges](/security-and-legal/payment-regulations/about-surcharges/) are no longer supported.

{{< alert-notice >}} **Attention Dutch merchants** <br>  We strongly recommend that you do **not** apply surcharges to [pay later methods](/payment-methods/pay-later/). This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM). {{< /alert-notice >}}

{{< details title="Using Fooman for surcharges" >}}

To apply a surcharge or payment fee to a payment method, you can use the third-party [Fooman](https://store.fooman.co.nz/extensions/magento2) package.

**Refunds**

You can refund orders with a Fooman surcharge applied in your [MultiSafepay dashboard](https://merchant.multisafepay.com), but not from your Magento 2 backend. 

**Support**

The Integration Team will do their best to support you with installing Fooman, but bear in mind that it is a third-party package. We can't guarantee perfect compatibility.

**PSD2 implications**

See [Payment Services Directive 2](/security-and-legal/payment-regulations/about-payment-service-directive-2).

{{< /details >}}

### Generic gateways

The plugin supports [generic gateways](/developer/generic-gateways/), which you can filter by country, and minimum/maximum amount.

{{< details title="Configuring generic gateways" >}}

1. Sign in to your Magento 2 backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay** > **Payment methods** > **Generic gateway**.
3. Set the relevant [payment method gateway IDs](https://docs-api.multisafepay.com/reference/gateway-ids) and upload a custom gateway image.
4. For pay later methods, specify whether to include a shopping cart.

For support, email <integration@multisafepay.com>

{{< /details >}}

### Tax settings

{{< details title="Configuring Magento tax settings" >}}

To configure tax settings in Magento, go to **Stores** > **Configuration** > **Sales** > **Tax** > **Calculation settings**.

**Recommended tax settings**

To avoid discrepancies between item amounts in MultiSafepay transactions and Magento orders, we recommend using the following tax settings in Magento.

To show prices **excluding** tax, use the following settings:

- **Tax calculation method based on**: Row total
- **Catalog prices**: Excluding tax
- **Apply customer tax**: After discount
- **Apply discount on prices**: Excluding tax

To show prices **including** tax, use the following settings:

- **Tax calculation method based on**: Row total
- **Catalog prices**: Including tax
- **Apply customer tax**: After discount
- **Apply discount on prices**: Including tax

These recommended settings are based on Magento's standards. For more information, see Magento – [Warning messages](https://docs.magento.com/user-guide/tax/warning-messages.html).

{{< /details >}}


### Payment links in confirmation emails

{{< details title="Adding payment links to order confirmation emails" >}}

To add payment links to order confirmation emails and customize settings, follow these steps:

1. Sign in to your Magento 2 backend.
2. Go to **Marketing** > **Email templates**.
3. Under **New order**, import a template.
4. Add the following code snippet to the template:

```
{{depend order.getPayment().getAdditionalInformation('payment_link')}}
<a href="{{var order.getPayment().getAdditionalInformation('payment_link')}}">Pay now with {{var order.getPayment().getAdditionalInformation('method_title')}}</a>
{{/depend}}
```

**Magento 2.3.4+**

The email template syntax is different for Magento 2.3.4+. Add this code snippet instead:

```
{{depend order.payment.additional_information.payment_link}}
<a href="{{var order.payment.additional_information.payment_link}}">Pay now with {{var order.payment.additional_information.method_title}}</a>
{{/depend}}
```

**Backend emails**

To add payment links to order confirmation emails from your Magento **backend**, you can use the `payment_link` variable and an `if/else` statement in the template. 

**Frontend emails**

You cannot add payment links to order confirmation emails created in your **frontend**, but you can dispaly the name of the payment method:

`{{if payment_link}}`
`<a href="{{var payment_link}}">Pay now with {{var order.payment.additional_information.method_title}}</a>`
`{{else}}`
`<p>{{var order.payment.additional_information.method_title}}</p>`
`{{/if}}`

1. Go to **Stores** > **Configuration** > **Sales** > **Sales emails**.
2. Replace the **New order confirmation template** with your template.
3. Test the template to confirm it is working.

**Note:** You can also implement this directly in the email template files.

{{< /details >}}

### Order totals

From version 1.9.0 and higher, all order totals, including custom ones, are automatically read and displayed on MultiSafepay payment pages.

We read **all** custom totals in the cart. Sometimes this results in unwanted custom totals appearing on payment pages.

To exclude custom totals from payment pages, follow these steps:  

1. Sign in to your Magento 2 backend.
2. Go to **Stores** > **Configuration** > **MultiSafepay**.
3. Select **General settings** > **Advanced settings** > **Exclude custom totals**.

If you have included a custom total and it is **not** being read, make sure that it implements the following methods:

- getCode()
- getTitle() or getLabel()
- getValue() or getAmount() and getBaseAmount()
- getTaxRate() or getBaseTaxRate()
- getTaxAmount() or getBaseTaxAmount()

The base values are required if you have enabled the `use base currency` setting under **MultiSafepay** > **General settings**.




{{< blue-notice >}}MultiSafepay is an official partner of [OneStepCheckout.com](/payments/integrations/ecommerce-platforms/magento2/faq/supported-magento2-checkouts/). {{< /blue-notice >}}