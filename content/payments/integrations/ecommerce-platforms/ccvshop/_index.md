---
title : "MultiSafepay app for CCV Shop"
meta_title: "CCV Shop app - MultiSafepay Docs"
faq: "."
layout: 'single'
logo: "/logo/Integrations/CCVShop.svg"
weight: 29
title_short: "CCVShop"
description_short: "Free app to integrate MultiSafepay payment solutions into your CCV Shop webshop."
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
---
This technical manual is for installing and configuring our free app to integrate MultiSafepay payment solutions into your CCV Shop webshop.

{{< details title="Test environment" >}}
&nbsp;  
We recommend first installing the app in a test environment following the recommended CCV Shop installation procedure. Make sure you have made a backup.

{{< /details >}}

{{< details title="Requirements" >}}
&nbsp;  
You will need a MultiSafepay account. See [Getting started](/getting-started/).
{{< /details >}}

{{< details title="Support" >}}
&nbsp;  
For any technical queries about the app, email CCV Shop at <support@ccvshop.nl>

Contact MultiSafepay:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

{{< details title="Supported payment methods" >}}

**Credit and debit cards**
  
- [American Express](/payment-methods/american-express)
- [Mastercard](/payment-methods/mastercard)
- [Maestro](/payment-methods/maestro)
- [Visa](/payments/methods/credit-and-debit-cards/visa), including [Cartes Bancaires](/payment-methods/cartes-bancaires), [Dankort](/payment-methods/dankort), and [V Pay](/payment-methods/vpay/)

**Banking methods**

- [Bancontact](/payment-methods/bancontact)
- [Bank transfer](/payment-methods/bank-transfer)
- [Giropay](/payment-methods/giropay)
- [iDEAL](/payment-methods/ideal)
- [Sofort](/payment-methods/sofort)
- [Trustly](/payment-methods/trustly)

**Pay later methods**

- [AfterPay](/payments/methods/billing-suite/afterpay/)
- [Klarna](/payments/methods/billing-suite/klarna/)

**Wallets**

- [PayPal](/payment-methods/paypal)

{{< /details >}}

To install and configure the app, follow these steps:

1. Sign in to your CCV Shop [backend](/getting-started/glossary/#backend) and install the MultiSafepay app from the App Store.
2. Go to **Mijn Webshop** > **Instellingen** > **Bestelproces & Voorraad** > **Betaalmethoden**.
3. In the **Electronische betalingen** tab, select **MultiSafepay**.
4. Enter your account ID, [site ID and secure code](/set-up-your-account/site-id-api-key-secure-code).
5. If using your MultiSafepay test account, select **Test mode**.
6. Click **Synchroniseer betaalmethodes met MultiSafepay**, and then click **Save**.


