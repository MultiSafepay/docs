---
title: 'Generating payment links'
weight: 30
meta_title: "Generating payment links - MultiSafepay Docs"
layout: 'single'
logo: '/svgs/External link.svg'
short_description: 'Generate payment links via our API or in your MultiSafepay dashboard.'
url: '/payment-links/generating-links/'
read_more: "."
aliases:
    - /tools/payment-link/manually-generating-a-payment-link/
    - /tools/payment-link/payment-link-api/
    - /tools/multisafepay-control/manually-generated-payment-link
    - /tools/multisafepay-control/generating-and-disabling-payment-links
    - /account/multisafepay-account/generating-and-disabling-payment-links/
    - /payments/checkout/payment-link/
---
You can generate payment links in:

- Your MultiSafepay dashboard
- The MultiSafepay app
- Some ready-made integrations
- Via our API

## Dashboard

### New transactions

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.
3. Click **New payment link**.
4. From the **Site** list, select the relevant website.
5. Under **Amount**, select the currency from the list, and then enter the whole value and cents.
6. In the **Order ID** field, enter the order ID from your webshop.  
**Note:** The order ID for every payment link must be unique.
7. In the **Description** field, enter a description of the order. 
8. In the **Link expiration (days)** field, enter the number of days for the link to remain active. Default: 30 days.
9. To send [Second Chance emails](/features/second-chance/), select the **Second chance email** check box. 
10. Optionally, enter the customer's:  
    - **First name** and **Last name**
    - **Email address**
    - **Country**
    - **Language**
11. To include additional information, in the top-right corner, click **Advanced mode** to display more fields. 
12. Click **Generate payment link**.
13. In the green bar that appears, copy the link from the green bar and pass it to the customer.

### Existing transactions

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Transactions** > **Transaction overview**.
3. Click on the relevant transaction.
4. In the **Transaction details** page, under **Order summary**, click **Payment link** > **Duplicate this order**.

**Note:** The order ID must be unique.

## MultiSafepay app

To generate a payment link from your MultiSafepay app, follow these steps:

1. Go to **Tools** > **Payment link generator**.
2. Fill in the required fields.
3. Click **Generate payment link**.
4. Save the QR code generated to your device, and then send it to the customer.   
When the customer scans the QR code, they are directed to a pre-filled [payment page](/payment-pages/) to complete payment.

## Ready-made integrations

You can generate payment links in the [backend](/glossaries/multisafepay-glossary/#backend) of the following [ready-made integrations](/integrations/ready-made/):

- [Magento 1](/magento-1/)
- [Magento 2](/magento-2)
- [OpenCart](/opencart/)
- [Shopware 5](/shopware-5/)
- [WooCommerce](/woo-commerce/)

## API

See API reference – [Create order](https://api-docs.multisafepay.com/reference/createorder). In the `type` parameter, enter `paymentlink`. 
