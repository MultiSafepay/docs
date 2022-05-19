---
title : "CCV Shop app"
meta_title: "CCV Shop app - MultiSafepay Docs"
type: 'App'
layout: 'single'
logo: "/logo/Integrations/CCVShop.svg"
weight: 29
title_short: "CCV Shop"
description_short: "Free app to integrate MultiSafepay payment solutions with CCV Shop."
layout: 'single'
url: '/ccv-shop/'
aliases: 
    - /plugins/ccvshop
    - /integrations/plugins/ccvshop
    - /integrations/ccvshop
    - /plugins/ccvshop/manual/
    - /integrations/plugins/ccvshop/manual/
    - /integrations/ecommerce-integrations/ccvshop
    - /payments/integrations/ecommerce-platforms/ccvshop/
    - /ecommerce-platforms/ccv-shop/
    - /integrations/ccvshop/faq/refunding-ccv-shop/
    - /payments/integrations/ecommerce-platforms/ccvshop/faq/processing-refunds/
    - /ccv-shop/refunds/
---
This technical manual is for installing and configuring MultiSafepay's free app for integrating with CCV Shop.

{{< details title="Requirements" >}}
&nbsp;  
You will need a [MultiSafepay account](/getting-started/guide/).
{{< /details >}}

{{< details title="Support" >}}
&nbsp;  
For any technical queries about the app, email CCV Shop at <support@ccvshop.nl>

Contact MultiSafepay:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Payment methods" >}}

- Cards: All
- Banking methods:
    - [Bancontact](/payment-methods/bancontact)
    - [Bank Transfer](/payment-methods/bank-transfer)
    - [Giropay](/payment-methods/giropay)
    - [iDEAL](/payment-methods/ideal)
    - [Sofort](/payment-methods/sofort)
    - [Trustly](/payment-methods/trustly)
- Pay later methods: [AfterPay](/payment-methods/afterpay/), [Klarna](/payment-methods/klarna/)
- Wallets: [PayPal](/payment-methods/paypal)

See also [MultiSafepay gateway](/developer/generic-gateways/#multisafepay-gateways).

{{< /details >}}

## Installation and configuration

1. Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.
2. Sign in to your CCV Shop backend and install the MultiSafepay app from the App Store.
3. Go to **Mijn webshop** > **Instellingen** > **Bestelproces & voorraad** > **Betaalmethoden**.
4. In the **Electronische betalingen** tab, select **MultiSafepay**.
5. Enter your account ID, [site ID and secure code](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).
6. If using your MultiSafepay test account, select **Test mode**.
7. Click **Synchroniseer betaalmethodes met MultiSafepay**, and then click **Save**.

## Refunds

You can process refunds from your [MultiSafepay dashboard](https://merchant.multisafepay.com), but refunds are **not** supported in the CCV Shop app.
