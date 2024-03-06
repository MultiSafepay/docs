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

# Changelog

<details id="changelog">
<summary>Changelog</summary>
<br>

**1.0.0-RC1**
Release date: Feb. 26th, 2024

### Added
- Endpoints for CCV Shop app installation: Handshake, Install, Uninstall.
- Localization for Install view based on `language` query variable (Dutch, English, German and French).
- Payment Service Provider (PSP) configuration based on MultiSafepay merchant data: API key, selected payment methods.
- Ability to update payment methods during CCV Shop app installation edit.
- Scheduled monitoring and updating of the payment methods.
- Endpoints for CCV Shop transactions creation and updating.
- Possibility to enable/disable refunds while installing CCV Shop app/editing CCV Shop app installation.
- Support for CCV Shop webhook events: `invoices.updated.status`, `orders.deleted`, `orders.updated.status`, `orders.updated.trackandtrace`.
- `invoices.updated.status` webhook event handler to create a MultiSafepay refund after CCV Shop invoice status is changed to `Refunded.
- `orders.deleted` webhook event handler to create a MultiSafepay refund after CCV Shop order is deleted.
- `orders.updated.status` webhook event handler to update MultiSafepay order status to `Shipped` after CCV Shop order status is changed to `Sent`.
- `orders.updated.trackandtrace` webhook event handler to update MultiSafepay order status to `Shipped` and populate track and trace information after CCV Shop order gets updated in **Shipment** section.
- Created artisan command: `ccv:register-webhooks`.
- CCV Shop **Order ID** as **Order ID** for MultiSafepay orders, which is used as **Transaction ID** for CCV Shop payments.

</details>

# Prerequisites

You will need a [MultiSafepay account](/docs/getting-started-guide/).

# Installation and configuration

1. Sign in to your CCV Shop <<glossary:backend>>.
2. Go to **App store** and search for **MultiSafepay** app.
3. Once found, select the app and click in **Install** button.
4. Review and accept the permissions required by the app.
5. Follow the instructions and fill the required fields to configure the app. 
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

---

[block:html]
{
"html": "<blockquote class=\"callout callout_info\">\n<h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n  <p>Contact MultiSafepay:</p>\n  <ul>\n    <li>Telephone: <a href=\"tel:+310208500500\">+31 (0)20 8500 500</a></li>\n    <li>Email: <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></li>\n    <li>GitHub: <a href=\"https://github.com/MultiSafepay/CS-Cart/issues\" target=\"_blank\"> create a technical issue</a></li>\n  </ul>  \n</blockquote>"
}
[/block]

[Top of page](#)