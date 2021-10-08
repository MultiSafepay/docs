---
title : "Generating payment links"
weight: 20
meta_title: "Payment links - Generating payment links - MultiSafepay Docs"
url: '/payment-links/generating-payment-links'
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: '.'
layout: 'single'
aliases:
    - /tools/multisafepay-control/manually-generated-payment-link
    - /payment-links/generating-payment-links-from-account
    - /payment-links/generating-payment-links-from-app/
    - /payment-links/generating-payment-links-from-backend/
---

You might need to manually generate a payment link if:

- A customer wants to adjust an existing order and instead of starting over with a new order, you generate an adjusted (new) payment link.
- You have created an order manually for a customer.
- MultiSafepay receives a payment from a customer for an amount that doesn't match any order. If you accept the payment, you need to manually generate a payment link and email it to MultiSafepay.
- A [Bank Transfer](/payments/methods/banks/bank-transfer/) payment link has expired.

## Payment methods

Check specific [payment methods](/payments/methods/) to see if manually generated payment links are supported.

**Note:** [Pay later methods](/payments/methods/billing-suite/) do **not** support manually generated payment links.

## Generating payment links

You can generate payment links:

{{< details title="From your MultiSafepay account" >}}

To manually generate a payment link from your account, follow these steps:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.
3. Click the **New payment link** button.
4. From the **Site** dropdown menu, select the relevant website.
5. Under **Amount**, select the currency from the dropdown menu, and then enter the whole value and cents.
6. In the **Order ID** field, enter the order ID from your webshop. The Order ID in every payment link must be unique.
7. In the **Description** field, enter a description of the order. 
8. In the **Link expiration (days)** field, enter the number of days the link remains active. The default is 30 days.
9. If needed, select the **Second chance email** check box. 
10. Optionally, enter the customer's:  
    - **First name**
    - **Last name**
    - **Email address**
    - **Country**
    - **Language**
11. Click **Generate payment link**.
12. Copy the newly generated link from the green bar and email it to the customer.

To view all manually generated payment links, including date of creation and status:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.

To send a payment link for an existing transaction:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Click on the relevant transaction.
4. In the **Transaction details** page, under **Order summary**, click **Payment link** > **Duplicate this order**.

**Note:** The order ID must be unique.

{{< /details >}}

{{< details title="From your backend" >}}

For some ecommerce integrations, you can generate payment links in your [backend](/getting-started/glossary/#backend).

To use the `POST /orders` request, see API reference – [Create an order](https://docs.multisafepay.com/api/#create-an-order). In the `type` parameter, enter `paymentlink`. 

Or, see API reference – [Generating a payment link](/api/#generate-payment-links).

For support, email the Integration Team at <integration@multisafepay.com>

{{< /details >}}

{{< details title="From your MultiSafepay app" >}}

To generate a payment link from your MultiSafepay app, follow these steps:

1. Go to **Tools** > **Payment link generator**.
2. Fill in the required fields.
3. Click **Generate payment link**.
4. Save the QR code generated to your device and then send it to the customer. 
5. Use the QR code that is generated to complete the payment.
6. When the customer scans the QR code, they are directed to a pre-filled MultiSafepay payment page to complete payment.

{{< /details >}}
