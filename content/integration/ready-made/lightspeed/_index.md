---
title : "Lightspeed"
meta_title: "Lightspeed - MultiSafepay Docs"
changelog_url: '.'
changelog: https://lightspeed.multisafepay.com/changelog
layout: 'single'
type: 'App'
logo: "/logo/Integrations/Lightspeed.svg"
weight: 04
title_short: "Lightspeed"
url: '/lightspeed/'
description_short: "Free app to integrate MultiSafepay payment solutions with Lightspeed."
aliases: 
    - /integrations/hosted/lightspeed/
    - /integrations/hosted/lightspeedbeta/
    - /hosted/lightspeed_app
    - /integrations/hosted/lightspeed_app
    - /integrations/lightspeed_app
    - /integrations/ecommerce-integrations/lightspeed_app 
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/multiple-accounts/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/supported-payment-methods/
    - /ecommerce-platforms/lightspeed/
    - /lightspeed-core/
    - /integrations/hosted/lightspeed_app/faq/footer-icons
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/adding-payment-method-footer-icons/
    - /integrations/ecommerce-integrations/lightspeed_app/faq/missing-payment-method-logos/
    - /lightspeed/payment-method-icons/
    - /lightspeed/payment-method-logos/
    - /lightspeed/surcharges/
    - /integrations/ecommerce-integrations/lightspeed_app/faq/change-environment/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/changing-api-key-and-environment/
    - /lightspeed-app/api-key-environment/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/changing-internationalization/
    - /lightspeed-app/internationalization/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/deleting-multisafepay/
    - /lightspeed-app/deleting-multisafepay/
    - /integrations/ecommerce-integrations/lightspeed_app/faq/disable-payment-methods/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/disabling-payment-methods/
    - /lightspeed-app/disabling-payment-methods/
    - /integrations/ecommerce-integrations/lightspeed_app/faq/maximal-order-amount/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/setting-minimum-order-amount/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/setting-maximum-order-amount/
    - /lightspeed-app/displaying-payment-methods/
    - /hosted/lightspeed_app/faq/how-to-login
    - /integrations/hosted/lightspeed_app/faq/how-to-login
    - /integrations/lightspeed_app/faq/how-to-login
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/logging-in/
    - /lightspeed-app/login/
    - /integrations/ecommerce-integrations/lightspeed_app/faq/order-payment-methods/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/ordering-payment-methods/
    - /lightspeed-app/ordering-payment-methods/
    - /hosted/lightspeed_app/faq/refunding-lightspeed
    - /integrations/hosted/lightspeed_app/faq/refunding-lightspeed
    - /integrations/lightspeed_app/faq/refunding-lightspeed
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/processing-refunds/
    - /lightspeed-app/refunds/
    - /integrations/ecommerce-integrations/lightspeed_app/faq/payment-reminders/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/sending-payment-reminders/
    - /lightspeed-app/payment-reminders/
    - /integrations/ecommerce-integrations/lightspeed_app/faq/lightspeed-orderid/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/synchronizing-payment-links/
    - /lightspeed-app/synchronizing-payment-links/
    - /integrations/ecommerce-integrations/lightspeed_app/faq/migrate-to-app/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/upgrading-to-new-app/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/disabling-classic-lightspeed/
    - /ecommerce-platforms/lightspeed/disabling-core-integration/
    - /lightspeed/disabling-core-integration/
    - /lightspeed-app/upgrading/
    - /integrations/ecommerce-integrations/lightspeed_app/faq/shop_id/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/viewing-your-shop_id/
    - /lightspeed-app/shop-id/
---
{{< alert-notice >}} We recommend [upgrading to the latest version](/lightspeed/#upgrading-to-the-new-app) as soon as possible. {{< /alert-notice >}}

This technical manual is for installing and configuring MultiSafepay's free app for integrating with Lightspeed.  

{{< details title="Requirements" >}}

- [MultiSafepay account](/getting-started/guide/)
- A MultiSafepay [API key](/tools/multisafepay-control/get-your-api-key)
- The app only supports one account per webshop

{{< /details >}}

{{< details title="Support" >}}

Contact us:

- Telephone: +31 (0)20 8500 500
- Email: <integration@multisafepay.com>
- GitHub: Create a technical issue

{{< /details >}}

## Installation 

{{< blue-notice >}} Make sure you have a backup of your production environment, and that you test the plugin in a staging environment. {{< /blue-notice >}}

1. Sign in to your Lightspeed backend.
2. Go to **Apps** on the left-hand side of the dashboard.
3. Search for the **MultiSafepay payments app**.
4. Click on the app, and then on **Install app** in the top-right corner.  
5. In the dialog, approve the permissions required for the app.  
   You are redirected to Lightspeed – [MultiSafepay: How to log in](https://lightspeed.multisafepay.com/install).
6. In the **Setup** page:  
    - Enter your email address, [account ID and site API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code).
    - Select **Test** or **Live** environment, and click **Save and continue**.  
You are redirected to the **Settings** page.
7. We recommend enabling:
    - Refunds
    - MultiSafepay checkout scripts – Creates a list of iDEAL issuers, and suppresses Apple Pay for non-Apple devices.
8. Verify the other settings, and then click **Save**.  

## User guide

### API keys and environments

{{< details title="Changing API keys and environments" >}}

To change your [API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code) or environment (live or test) after installation, follow these steps:

1. Sign in to the app.
2. Tap the hamburger menu and go to **Environment**.
3. Edit your **API key** and/or the **Environment**.

{{< /details >}}

### Checkouts

This app is tested using the default 1-step and 1-page checkout using the default theme.

{{< details title="Ordering payment methods in your checkout" >}}

To change the order in which payment methods appear on your checkout page, follow these steps:

1. Go to **Settings** > **Payment method settings**. 
2. Drag and drop the payment methods to the preferred order.
3. Click **Save**.

**Setting payment method order per language**

To set the payment method order for different languages, under the **Payment method settings** select a country / store language and set the order per language.

If no specific rule is set for a country, the **Default** order is used.

{{< /details >}}

### Internationalization

{{< details title="Changing internationalization" >}}

When changing internationalization in your Lightspeed eCom backend, do **not** change the primary language setting while installing the app.  

Lightspeed eCom requires a language, an API key, and a cluster to validate API requests. 

If you remove the language used during installation instead of deactivating it, the app cannot communicate with Lightspeed eCom services.

{{< /details >}}

### Lightspeed shop ID

{{< details title="Viewing your shop ID" >}}

To view your shop ID, follow these steps:

1. Sign in to the **/admin** area of your Lightspeed app.
2. Click **Help** in the bottom-left corner.
3. A popup appears containing your shop ID (also known as the store ID).

{{< /details >}}

### Order amounts

{{< details title="Setting maximum/minimum order amounts" >}}

**Setting a maximum/minimum order amount per payment method**

To set a maximum/minimum order amount for a payment method to display on your checkout page, follow these steps:

1. In the **Payment methods ordering** list, click the **+** button to open the relevant payment method.
2. Enter an amount in EUR cents in the:  
    - **Maximum** field, e.g. A maximum value of 1500 cents means the payment method only appears on the checkout page if the total order amount is **less** then 15 EUR. If you **don't** want a maximum amount, enter **-1**.
    **OR**
    - **Minimum** field, e.g. A minimum value of 1500 cents means the payment method only appears on the checkout page if the total order amount is **more** then 15 EUR.

**Setting a maximum/minimum order amount per language**

To set different maximum/minimum order amounts for different languages, under the **Payment methods ordering** header > **Country** list, select a country and set the maximum/minimum amount per language.

If no specific rule is set for a language, **Default** language is used.

{{< /details >}}

### Payment links

When you generate a payment link in your MultiSafepay dashboard, you cannot update the [transaction status](/payments/payment-statuses/) or link it to a transaction in Lightspeed via our app. This&nbsp;is by design in Lightspeed. 

### Payment methods

{{< details title="Payment methods" >}}

- Cards: [All](/payment-methods/credit-debit-cards/)
- Banking methods: [All](/payment-methods/banks/), **except** iDEAL QR and TrustPay
- Pay later methods: [All](/payment-methods/pay-later/)
- Wallets: [All](/payment-methods/wallets/) 
- Prepaid cards: 
    - Baby gift card
    - Beauty and Wellness gift card
    - [Bloemencadeaukaart](https://www.bloemen-cadeaukaart.nl)
    - [Boekenbon](https://www.cadeaubon.nl/cadeaubonnen/nederlandse-boekenbon)
    - [Degrotespeelgoedwinkel](https://www.degrotespeelgoedwinkel.nl/cadeaukaart)
    - [Fashion Cheque](https://www.fashioncheque.com/nl/)
    - [Fashion gift card](https://www.fashion-giftcard.nl/)
    - Fietsenbon
    - [Gezondheidsbon](https://www.gezondheidsbon.nl/mhome/)
    - Goodcard
    - [Nationale bioscoopbon](https://www.bioscoopbon.nl)
    - [Nationale tuinbon](https://www.nationale-tuinbon.nl/)
    - [Parfumcadeaukaart](https://www.parfumcadeaukaart.nl/)
    - [Sport en Fit](https://www.sportenfitcadeau.nl/)
    - [VVV gift card](https://www.vvvcadeaukaarten.nl/)
    - [Webshop gift card](https://www.webshopgiftcard.nl/)
    - Wijncadeau
    - [Winkelcheque](https://www.winkelcheque.nl/)
    - [Yourgift](https://www.yourgift.nl)  

To use MultiSafepay payment method icons, see GitHub [MultiSafepay icons](https://github.com/MultiSafepay/MultiSafepay-icons).

{{< /details >}}

{{< details title="Payment methods logos in your website footer" >}}

By default, the app does **not** support adding payment methods logos to your website footer. We provide a script for this, or you can ask your developer to add the logos to your theme. Themes can differ and you may need to make some changes for it to function.

**Adding logos via our script**

1. Sign in to your Lightspeed app.
2. Go to **Settings** > **Storefront payment icons**.
3. Click **Copy to clipboard**. 
5. In your **Lightspeed admin area**, go to **Settings** > **Web extras and custom Javascript**. 
6. Paste the script into the **Javascript textbox**, and set the status to **Enable**.
7. Click **Save**. The logos appear in the footer.

**Display order**  

Depending on the storefront, the display order of the logos is determined by the settings at the time of generation. If you update these settings, you must update the script as well.

**Size**  

By default the logos are 16 px high. In most themes, footer logos are found in the "div.payment-methods p". If needed, you can change the selector based on the theme.

**Resizing logos**

1. In the JavaScript for displaying the logos, locate the following `img` element near the end of the script:
    ```<img src="${msplt[e]}" alt="${e}" />```
2. Specify the height and width in pixels as required, e.g.:
    ```<img height="16" width="37" src="${msplt[e]}" alt="${e}" />```

**Adding missing logos**  

Logos may be missing due to your website theme settings. 

To add missing payment method logos, follow these steps:

1. Download the logos from our [Github repo](https://github.com/MultiSafepay/MultiSafepay-icons).
2. Rename the file with upper case formatting, e.g applepay.png > APPLEPAY.png.
3. Sign in to your Lightspeed app.
4. Go to **Design** > **Theme editor** > **Advanced** > **Edit code** > **Assets**, and drop in the logos.  

The logos won't appear instantly. It takes a little time.

**JavaScript**

For the best user experience, we provide some Javascript and images, e.g. to add a dropdown for iDEAL and MultiSafepay icons for other payment methods. 

Some user-added themes or scripts may cause issues, e.g. missing images for payment methods. 

For assistance, ask your developer. 

All payment methods still work if you don't use the Javascript files. 

{{< /details >}}

{{< details title="Ordering payment methods in your checkout" >}}

To change the order in which payment methods appear on your checkout page, follow these steps:

1. Go to **Settings** > **Payment method settings**. 
2. Drag and drop the payment methods to the preferred order.
3. Click **Save**.

**Setting payment method order per language**

To set the payment method order for different languages, under the **Payment method settings** select a country / store language and set the order per language.

If no specific rule is set for a country, the **Default** order is used.

{{< /details >}}

{{< details title="Disabling payment methods" >}}

You can disable payment methods in the **Payment method settings list**. The dot next to the payment methods is green when enabled, and grey when disabled.

To disable payment methods for specific languages, follow these steps:

1. Sign in to your Lightspeed app.
2. Select the relevant storefont.
4. For each language, disable the relevant payment methods. 

If no specific language rule-set is found, **Default** is used.

**Missing payment methods**

By default, newly activated payment methods for your MultiSafepay account are disabled in the Lightspeed app's MultiSafepay payments settings. You need to enable them in both environments.

If a payment method is missing:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com/) and check that the payment method is enabled.
2. Sign in to your Lightspeed app, go to **Settings**, and then enable the payment method again. 

{{< /details >}}

{{< details title="Removing payment methods" >}}

After terminating your contract with MultiSafepay, our payment methods may still be visible in your checkout.

1. Sign in to your Lightspeed app.
2. Go to **Apps** > **Purchased apps** > **MultiSafepay payments**.
3. Click **Go to app**.
4. Sign in to the MultiSafepay app.
5. Click **Disable all payment methods**.

{{< /details >}}

### Payment reminders

The Lightspeed app doesn't support [Second Chance](/features/second-chance/) emails because Lightspeed orders expire after 12 hours. 

Lightspeed offers a functionality that lets you configure payment reminders and emails for orders with **Pending** status. For more information and instructions, see Lightspeed - [Configuring payment reminders](https://ecom-support.lightspeedhq.com/hc/en-us/articles/220661507-Configuring-payment-reminders)

### Refunds

[Full and partial refunds](/refunds/full-partial/) and credit notes are supported in your MultiSafepay dashboard and backend.  
You can't refund more than the original amount in your backend.

{{< details title="Enabling refunds in your backend" >}}

1. Sign in to your Lightspeed app.
2. Go to **Settings**.
3. In the sidebar, click **Enable refunds**.
4. Select the relevant setting:
    - Refunds disabled (default)
    - Refunds enabled:
        - Create a refund when the credit memo status is **Unpaid** (default when refunds are enabled).
        - Always create a refund, no matter the credit memo status.

**Notes**

- If you use Lightspeed eCom linked to [Lightspeed Retail](https://www.lightspeedhq.nl/kassasysteem/retail/) to process refunds via MultiSafepay, you must enable the **Always create a refund, no matter the status** setting.

- When creating a credit memo, set the status to **Not paid**. If the **Always create a refund, no matter the status** setting is not enabled, MultiSafepay ignores **Paid** status.

**Known issues**

- For refunds created in your Lightspeed backend, a short message appears in the **Notes** section of the order where any errors are explained.

- Refunds created in your MultiSafepay dashboard are not reported back to Lightspeed. Under **Offline actions**, an error appears: "Already a completed transaction".

- Some [pay later](/payment-methods/pay-later/) methods:
    - Require product IDs for each refunded item. When using product variants, make sure each variant has a unique identifier. If you provide duplicate IDs, we cannot distinguish which items to refund.
    - Do not let you refund a partial amount and a full item in a single request, e.g. a shopping cart contains 3 items for a total of 1.70 EUR. If you refund 1 item and 0.40 EUR, it fails. Make sure you refund items and amounts separately.

- You cannot issue multiple refunds for the same amount within 5 minutes of each other, even for different items. 

For any questions, email <integration@multisafepay.com>

{{< /details >}}

### Single sign-on

Lightspeed single sign-on lets you sign in to the app's **Settings** directly from the Lightspeed eCom store. You don't need to click or tap the **Login** button.

{{< details title="Signing in with Lightspeed single sign-on" >}}

1. Sign in to the **Admin** section of your Lightspeed store.
2. In the sidebar, click **Apps**.
3. Click **Purchased apps**.
4. In the sidebar, click **Apps**.
5. Click **MultiSafepay Payments**, **or** to take you straight to the store page, paste **/admin/store/apps/1517** after the base URL of your store.
6. On the store page, click **Go to app** / **Ga naar app**. 

{{< /details >}}

### Surcharges

{{< details title="Applying surcharges" >}}

1. Sign in to your Lightspeed app.
2. Go to **App** > **Purchased app** > **MultiSafepay app**.
3. Select the payment method you want to apply a surcharge to. 
4. Enter the surcharge amount as a:
    - Fixed amount under **Flat payment fee**, **or**
    - Percentage under **Dynamic payment fee**.
5. Click **Save**.

**Attention Dutch merchants** 

We strongly recommend **not** applying surcharges to [pay later methods](/payment-methods/pay-later/). This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

{{< /details >}}

### Updates

You don't need to manually update the app. 

### Upgrading to the new app

{{< details title="Upgrading to the new app" >}}

**Upgrading to the new app**

To upgrade from our deprecated core integration to the Lightspeed app, follow these steps:

1. In the [Lightspeed app manual](/lightspeed/#installation), follow the steps to install the app.
2. Place a test order to make sure it's working properly.
3. Open the core integration, and then [disable the payment provider](/lightspeed-app/upgrading/#disabling-the-core-integration).

To access the MultiSafepay Payments app **Settings** page:

- You are automatically redirected after installing the app, or 
- Select the MultiSafepay Payments app, and then click **Go to app**.

**Disabling the core integration**

To disable the core integration after migrating to the new app, follow these steps:

1. Sign in to your Lightspeed backend.
2. Go to **Settings** > **Payment providers** > **MultiSafepay**.
2. At the top of the screen, click **Disable this payment provider**.

For any questions about the app, email <integration@multisafepay.com>

{{< /details >}}