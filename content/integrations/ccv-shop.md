---
title: "CCV Shop"
category: 62962dd7e272a6002ebbbbc5
order: 0
hidden: false
parentDoc: 62a9a54abde254065ee92a5c
slug: 'ccv-shop'
excerpt: "Technical manual for MultiSafepay's free app."
---
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/a87cfe4f49a0fd17e939bc70f53b23900421f524/static/logo/Integrations/ccv-shop.svg" width="50" align="right" style="margin: 20px; max-height: 75px"/>

# Prerequisites

- [MultiSafepay account](/docs/getting-started-guide/)
- A MultiSafepay [site API key](/docs/sites#site-id-api-key-and-security-code)

# Installation and configuration

1. Sign in to your CCV Shop <<glossary:backend>>.
2. Go to **App store** and search for **MultiSafepay** app.
3. Once found, select the app and click in **Install** button.
4. Review and accept the permissions required by the app.
5. Enter your [Site API key](/docs/sites#site-id-api-key-and-security-code), and fill the required fields to configure the app. 
6. Click the **Install** button to complete the installation.
7. Go to **My web shop** > **Settings** > **Ordering process & stock** > **Payment methods** and confirm your payments are enabled in the section **MultiSafepay Payment Service provider**

# Configuration

1. Sign in to your CCV Shop <<glossary:backend>>.
2. Go to **App store** and search for **MultiSafepay** app.
3. Once found, select the app and click in **Edit** button.
4. Modify the settings according your preferences.

___

# User guide

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

The activated payment methods from your MultiSafepay account appear will be registered in CCV Shop as a payment method.
To keep the payment methods synchronized, ensure to toggle the "update payment methods" setting before pressing "update". 

</details>

## Refunds

You can process full refunds for all payment methods, from your MultiSafepay dashboard, and from the CCV Shop <<glossary:backend>>.

<details id="refund-rules">
<summary>Refund rules</summary>
<br>
To process backend refunds:

- In the configuration of the MultiSafepay app, **Automatic refunds** needs to be enabled.
- To process a refund, the invoice status must be **Paid**.
- The refund amount cannot exceed the original transaction amount.
- The refund amount cannot exceed the available funds in your MultiSafepay account.
<br>
</details>

<details id="how-to-process-backend-refunds">
<summary>How to process refunds</summary>
<br>
To process backend refunds:

1. Sign in to your CCV Shop <<glossary:backend>>.
2. Go to **My orders** > **Order management**.
3. Select the order, and click on the **Invoices** tab.
4. Change the **Invoice status** from **Paid** to **Refunded**.
5. A refund request will be processed in MultiSafepay.
<br>
</details>

## Sorting Payment Methods

To sort the payment methods on the checkout page, you can change the order in the MultiSafepay app configuration.

<details id="sorting-payment-methods">
<summary>How to sort payment methods</summary>
<br>

1. Sign in to your CCV Shop <<glossary:backend>>.
2. Go to **App Store** > **MultiSafepay**.
3. Click on **Edit** button.
4. Turn on the switch field **Payment methods order**.
5. A list of the installed payment methods will be shown.
6. Use the arrow icons to sort the payment methods.
7. Click on **Update** button to save the changes.
<br>

**⚠️ Note:** Only payment methods provided by MultiSafepay can be reordered. CCV Shop does not support ordering of payment methods not provided by our app, so the order of other payment methods cannot be adjusted.

<br>
</details>

---

[block:html]
{
"html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)