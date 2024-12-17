---
title: "Lightspeed"
category: 62962dd7e272a6002ebbbbc5
order: 4
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
excerpt: "Technical manual for MultiSafepay's free app."
slug: 'lightspeed'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Integrations/Lightspeed.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

<a class="suggestEdits" style="display: inline-flex; border-radius: 5px; padding: 10px 20px; margin: 10px; font-size: 1rem; background-color: #DFEBF6; color: #0a59a1; text-decoration: none;" href="https://lightspeed.multisafepay.com/changelog" target="_self"><span>Changelog</span></a>
<br>

</details>

> ⚠️ Action required
>
> We recommend [upgrading to the latest version](/docs/lightspeed#how-to-upgrade-to-the-new-app) as soon as possible.

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- A MultiSafepay [site API key](/docs/sites#site-id-api-key-and-security-code)
- The app only supports one account per webshop

# Installation 

&nbsp; **💡 Tip!** Make sure you have a backup of your production environment, and that you test the plugin in a staging environment.

1. Sign in to your Lightspeed <<glossary:backend>>.
2. Go to **Apps** on the left-hand side of the dashboard.
3. Search for the **MultiSafepay payments app**.
4. Click the app, and then **Install app** in the top-right corner.  
5. In the dialog, approve the permissions required for the app.  
   You are redirected to Lightspeed – <a href="https://lightspeed.multisafepay.com/install" target="_blank">MultiSafepay: How to log in</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
6. In the **Setup** page:
  - Enter your email address, [account ID and site API key](/docs/sites#site-id-api-key-and-security-code).
  - Select **Test** or **Live** environment, and then click **Save and continue**.  
You are redirected to the **Settings** page.
7. We recommend enabling:
  - Refunds
  - MultiSafepay checkout scripts – Creates a list of iDEAL <<glossary:issuers>>, and suppresses Apple Pay for non-Apple devices.
8. Verify the other settings, and then click **Save**.  
<br>

---

# User guide

## API keys and environments

You can change your [site API key](/docs/sites/#site-id-api-key-and-security-code) or environment (live or test) after installation.

<details id="how-to-change-api-keys-and-environments">
<summary>How to change API keys and environments</summary>
<br>

1. Sign in to the app.
2. Tap the hamburger menu and go to **Environment**.
3. Edit your **API key** and/or the **Environment**.

</details>

## Checkouts

This app is tested using the default 1-step and 1-page checkout using the default theme.

<details id="how-to-order-payment-methods-in-your-checkout">
<summary>How to order payment methods in your checkout</summary>
<br>

To change the order in which payment methods appear on your checkout page, follow these steps:

1. Go to **Settings** > **Payment method settings**. 
2. Drag and drop the payment methods to the preferred order.
3. Click **Save**.

**How to set the payment method order per language**

To set the payment method order for different languages, under the **Payment method settings** select a country / store language and set the order per language.

If no specific rule is set for a country, the **Default** order is used.

</details>

## Internationalization

<details id="how-to-change-internationalization">
<summary>How to change internationalization</summary>
<br>

When changing internationalization in your Lightspeed eCom backend, do **not** change the primary language setting while installing the app.  

Lightspeed eCom requires a language, an API key, and a cluster to validate API requests. 

If you remove the language used during installation instead of deactivating it, the app cannot communicate with Lightspeed eCom services.

</details>

## Lightspeed shop ID

<details id="how-to-view-your-shop-id">
<summary>How to view your shop ID</summary>
<br>

To view your shop ID, follow these steps:

1. Sign in to the **/admin** area of your Lightspeed app.
2. Click **Help** in the bottom-left corner.
3. A popup appears containing your shop ID (also known as the store ID).

</details>

## Order amounts

<details id="how-to-set-maximum-minimum-order-amounts">
<summary>How to set maximum/minimum order amounts</summary>
<br>

**Per payment method**

To set a maximum/minimum order amount for a payment method to display on your checkout page, follow these steps:

1. In the **Payment methods ordering** list, click the **+** button to open the relevant payment method.
2. Enter an amount in EUR cents in the:  
    - **Maximum** field, e.g. A maximum value of 1500 cents means the payment method only appears on the checkout page if the total order amount is **less** then 15 EUR. If you **don't** want a maximum amount, enter **-1**.
    **OR**
    - **Minimum** field, e.g. A minimum value of 1500 cents means the payment method only appears on the checkout page if the total order amount is **more** then 15 EUR.

**Per language**

To set different maximum/minimum order amounts for different languages, under the **Payment methods ordering** header > **Country** list, select a country and set the maximum/minimum amount per language.

If no specific rule is set for a language, **Default** language is used.

</details>

## Payment components

Lightspeed supports [Payment Components](/docs/payment-components/), which:

- Provide a seamless checkout experience to increase <<glossary:conversion>>.
- Encrypt customer payment details for secure processing.
- Shift responsibility for [PCI DSS compliance](/docs/pci-dss/) to MultiSafepay.

<details id="how-to-activate-payment-component-in-backend">
<summary>How to activate the payment component in your backend</summary>
<br>

1. Sign in to your Lightspeed app.
2. Go to **Apps** > **Purchased apps** > **MultiSafepay payments**.
3. Click **Go to app**.
4. In the **Setup** page:
  - Enter your email address, [account ID and site API key](/docs/sites#site-id-api-key-and-security-code).
  - Select **Test** or **Live** environment, and then click **Save and continue**.  
You are redirected to the **Settings** page.
5. On the **Payment method settings** tab:
- Select the relevant **Payment method settings**.
- To expand the payment method, click on the tab.
- On the **Enable MultiSafepay Components** and select the **Enabled** checkbox. 
6. On the **Enable MultiSafepay checkout scripts** tab, select the **Enabled script** checkbox.
7. Click **Save**.

</details>

## Payment links

When you generate a payment link in your MultiSafepay dashboard, you cannot update the <<glossary:transaction status>> or link it to a transaction in Lightspeed via our app. This is by design in Lightspeed. 

## Payment methods

By default, activated payment methods from your MultiSafepay account appear on the payment method list. However, any newly activated payment methods for your MultiSafepay account must be enabled manually in your Lightspeed <<glossary:backend>> under MultiSafepay payment settings.

To use MultiSafepay payment method icons, see GitHub <a href="https://github.com/MultiSafepay/MultiSafepay-icons" target="_blank">MultiSafepay icons</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

<details id="payment-methods-logos-in-your-site-footer">
<summary>Payment methods logos in your site footer</summary>
<br>

By default, the app does **not** support adding payment methods logos to your site footer. We provide a script for this, or you can ask your developer to add the logos to your theme. Themes can differ and you may need to make some changes for it to function.

**How to add logos via our script**

1. Sign in to your Lightspeed app.
2. Go to **Apps** > **Purchased apps** > **MultiSafepay payments**.
3. Click **Go to app**.
4. In the **Setup** page:
  - Enter your email address, [account ID and site API key](/docs/sites#site-id-api-key-and-security-code).
  - Select **Test** or **Live** environment, and then click **Save and continue**.  
You are redirected to the **Settings** page.
5. On the **Storefront payment icons** tab, click **Copy to clipboard**. 
6. In your **Lightspeed admin area**, go to **Settings** > **Web extras and custom Javascript**. 
7. Paste the script into the **Javascript textbox**, and set the status to **Enable**.
8. Click **Save**. 
The logos appear in the footer.

**Display order**  

Depending on the storefront, the display order of the logos is determined by the settings at the time of generation. If you update these settings, you must update the script as well.

**Size**  

By default the logos are 16 px high. In most themes, footer logos are found in the "div.payment-methods p". If needed, you can change the selector based on the theme.

**How to resize logos**

1. In the JavaScript for displaying the logos, locate the following `img` element near the end of the script:
    ```
    <img src="${msplt[e]}" alt="${e}" />
    ```
2. Specify the height and width in pixels as required, e.g.:
    ```
    <img height="16" width="37" src="${msplt[e]}" alt="${e}" />
    ```

**How to add missing logos**  

Logos may be missing due to your site theme settings. 

To add missing payment method logos, follow these steps:

1. Download the logos from our <a href="https://github.com/MultiSafepay/MultiSafepay-icons" target="_blank">Github repo</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Rename the file with upper case formatting, e.g applepay.png > APPLEPAY.png.
3. Sign in to your Lightspeed app.
4. Go to **Design** > **Theme editor** > **Advanced** > **Edit code** > **Assets**, and drop in the logos.  

The logos won't appear instantly. It takes a little time.

**JavaScript**

For the best user experience, we provide some Javascript and images, e.g. to add a dropdown for iDEAL and MultiSafepay icons for other payment methods. 

Some user-added themes or scripts may cause issues, e.g. missing images for payment methods. 

For assistance, ask your developer. 

All payment methods still work if you don't use the Javascript files. 

</details>

<details id="how-to-order-payment-methods-in-your-checkout">
<summary>How to order payment methods in your checkout</summary>
<br>

To change the order in which payment methods appear on your checkout page, follow these steps:

1. Go to **Settings** > **Payment method settings**. 
2. Drag and drop the payment methods to the preferred order.
3. Click **Save**.

**Setting payment method order per language**

To set the payment method order for different languages, under the **Payment method settings** select a country / store language and set the order per language.

If no specific rule is set for a country, the **Default** order is used.

</details>

<details id="how-to-enable-payment-methods">
<summary>How to enable payment methods</summary>
<br>

You can enable and disable payment methods in the **Payment method settings list**. The dot next to the payment methods is green when enabled, and grey when disabled.

To disable payment methods for specific languages, follow these steps:

1. Sign in to your Lightspeed app.
2. Select the relevant storefont.
4. For each language, disable the relevant payment methods. 

If no specific language rule-set is found, **Default** is used.

**Missing payment methods**

By default, newly activated payment methods for your MultiSafepay account are disabled in the Lightspeed app's MultiSafepay payments settings. You need to enable them in both environments.

If a payment method is missing:

1. Sign in to your <a href="https://merchant.multisafepay.com/" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Settings** > **Payment methods**, and check that the payment method is enabled.
3. Sign in to your Lightspeed app, go to **Settings**, and then enable the payment method again. 

</details>

<details id="how-to-remove-payment-methods">
<summary>How to remove payment methods</summary>
<br>

After terminating your contract with MultiSafepay, our payment methods may still be visible in your checkout.

1. Sign in to your Lightspeed app.
2. Go to **Apps** > **Purchased apps** > **MultiSafepay payments**.
3. Click **Go to app**.
4. Sign in to the MultiSafepay app.
5. Click **Disable all payment methods**.

</details>

## Payment reminders

The Lightspeed app doesn't support [Second Chance](/docs/second-chance/) emails because Lightspeed orders expire after 12 hours. 

Lightspeed offers a functionality that lets you configure payment reminders and emails for orders with **Pending** status. For more information and instructions, see Lightspeed – <a href="https://ecom-support.lightspeedhq.com/hc/en-us/articles/220661507-Configuring-payment-reminders" target="_blank">Configuring payment reminders</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

## Refunds

[Full and partial refunds](/docs/refund-payments/) and credit notes are supported in your MultiSafepay dashboard and backend.  
You can't refund more than the original amount in your backend.

<details id="how-to-enable-refunds-in-your-backend">
<summary>How to enable refunds in your backend</summary>
<br>

1. Sign in to your Lightspeed app.
2. Go to **Apps** > **Purchased apps** > **MultiSafepay payments**.
3. Click **Go to app**.
4. In the **Setup** page:
  - Enter your email address, [account ID and site API key](/docs/sites#site-id-api-key-and-security-code).
  - Select **Test** or **Live** environment, and then click **Save and continue**.  
You are redirected to the **Settings** page.
3. On the **Allow refunds** tab, select the **Refunds enabled** checkbox.
4. Select the relevant setting:
    - Refunds disabled (default)
    - Refunds enabled:
        - Create a refund when the credit memo status is **Unpaid** (default when refunds are enabled).
        - Always create a refund, no matter the credit memo status.

**Notes**

- If you use Lightspeed eCom linked to <a href="https://www.lightspeedhq.nl/kassasysteem/retail/" target="_blank">Lightspeed Retail</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> to process refunds via MultiSafepay, you must enable the **Always create a refund, no matter the status** setting.

- When creating a credit memo, set the status to **Not paid**. If the **Always create a refund, no matter the status** setting is not enabled, MultiSafepay ignores **Paid** status.

</details>

<details id="known-issues">
<summary>Known issues</summary>
<br>

- For refunds created in your Lightspeed backend, a short message appears in the **Notes** section of the order where any errors are explained.
- Refunds created in your MultiSafepay dashboard are not reported back to Lightspeed. Under **Notification history**, an error appears: "Already a completed transaction".
- Some <<glossary:BNPL>> orders:
    - Require product IDs for each refunded item. When using product variants, make sure each variant has a unique identifier. If you provide duplicate IDs, we cannot distinguish which items to refund.
    - Do not let you refund a partial amount and a full item in a single request, e.g. a shopping cart contains 3 items for a total of 1.70 EUR. If you refund 1 item and 0.40 EUR, it fails. Make sure you refund items and amounts separately.
- You cannot issue multiple refunds for the same amount within 5 minutes of each other, even for different items. 

</details>

## Single sign-on

Lightspeed single sign-on lets you sign in to the app's **Settings** directly from the Lightspeed eCom store. You don't need to click or tap the **Login** button.

<details id="how-to-use-lightspeed-single-sign-on">
<summary>How to use Lightspeed single sign-on</summary>
<br>

1. Sign in to the **Admin** section of your Lightspeed store.
2. In the sidebar, click **Apps**.
3. Click **Purchased apps**.
4. In the sidebar, click **Apps**.
5. Click **MultiSafepay Payments**, **or** to take you straight to the store page, paste **/admin/store/apps/1517** after the base URL of your store.
6. On the store page, click **Go to app** / **Ga naar app**. 

</details>

## Surcharges

<details id="how-to-apply-surcharges">
<summary>How to apply surcharges</summary>
<br>

1. Sign in to your Lightspeed app.
2. Go to **App** > **Purchased app** > **MultiSafepay app**.
3. Select the payment method you want to apply a surcharge to. 
4. Enter the surcharge amount as a:
    - Fixed amount under **Flat payment fee**, **or**
    - Percentage under **Dynamic payment fee**.
5. Click **Save**.

> ⚠️ **Attention Dutch merchants** 
> We strongly recommend **not** applying surcharges to <<glossary:BNPL>> orders. This is now considered providing credit under the Wet op het consumentenkrediet and article 7:57 of the Burgerlijk Wetboek, and requires a permit from the Authority for Financial Markets (AFM).

</details>

## Updates

You don't need to manually update the app. 

## Upgrades

We recommend upgrading from our deprecated core integration to the Lightspeed app.

<details id="how-to-upgrade-to-the-new-app">
<summary>How to upgrade to the new app</summary>
<br>

1. In the [Lightspeed app manual](/docs/lightspeed#how-to-install), follow the steps to install the app.
2. Place a test order to make sure it's working properly.
3. Open the core integration, and then [disable the payment provider](/docs/lightspeed#how-to-disable-core-integration).

To access the MultiSafepay Payments app **Settings** page:

- You are automatically redirected after installing the app, or 
- Select the MultiSafepay Payments app, and then click **Go to app**.

</details>

<details id="how-to-disable-core-integration">
<summary>How to disable the core integration</summary>
<br>

1. Sign in to your Lightspeed backend.
2. Go to **Settings** > **Payment providers** > **MultiSafepay**.
2. At the top of the screen, click **Disable this payment provider**.

</details>
<br>


# Troubleshooting 

## Payment methods not displayed correctly

Checks you can do:

- are you using the correct API key and environment combination?
- are the payment methods activated for your account? 
- in **Payment method settings**, check that you have modified your preferences for the correct / all store languages. Check also: current setting is set to **enabled**.

</details>
---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)