---
title : "Generating payment links from your account"
weight: 20
meta_title: "Payment links - Generating payment links from your account - MultiSafepay Docs"
url: '/payment-links/generating-payment-links-from-account'
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
layout: 'faq'
aliases:
    - /tools/multisafepay-control/manually-generated-payment-link
---

You might need to manually generate a payment link if:

- A customer wants to adjust an existing order and instead of starting over with a new order, you generate an adjusted (new) payment link.
- You have created an order manually for a customer.
- MultiSafepay receives a payment from a customer with an unmatching amount. If you accept the payment, you need to manually generate a payment link and email it to MultiSafepay.
- A bank transfer payment link has expired.

{{< details title="Supported payment methods" >}}

Check specific [payment methods](/payments/methods/) to see if manually generated payment links are supported.

For example, post-payment methods such as AfterPay, Pay After Delivery, and Klarna do not support manually generated payment links, due to the insolvency process requirement which creates a different flow.

{{< /details >}}

## Generating manual payment links

To manually generate a payment link, follow these steps:

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

### Viewing manually generated payment links

To view all manually generated payment links, including the date of creation and status:

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to **Tools** > **Payment link generator**.

### Existing transactions

To send a payment link for an existing transaction, you can duplicate the link in the transaction itself. 

**Note:** The order ID must be unique.