---
title : "Generating and disabling payment links"
weight: 2
meta_title: "MultiSafepay Control- Generating and disabling payment links - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/multisafepay-control/manually-generated-payment-link
---

Payment links create a unique transaction in your [MultiSafepay Control](https://merchant.multisafepay.com/) to match to a payment.

### Supported payment methods and payment links 

Check specific [payment methods](/payment-methods/) to see if manually generated payment links are supported.

For example, post-payment methods such as AfterPay, Pay After Delivery, and Klarna do not support manually generated payment links, due to the insolvency process requirement which creates a different flow.

## Manually generating payment links

You might need to manually generate a payment link if:

- A customer wants to adjust an existing order and instead of starting over with a new order, you generate an adjusted (new) payment link.
- You have created an order manually for a customer.
- MultiSafepay receives a payment from a customer with an unmatching amount. If you accept the payment, you need to manually generate a payment link and email it to MultiSafepay.
- A bank transfer payment link has expired.

To manually generate a payment link, follow these steps:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).

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
&nbsp;
11. Click **Generate payment link**.

12. Copy the newly generated link from the green bar and email it to the customer.

### Payment links for existing transactions

To send a payment link for an existing transaction, you can duplicate the transaction in the transaction itself. 

**Note:** The order ID must be unique.

### Simple mode and advanced mode

Simple mode is the default payment link mode, which contains the minimum necessary information. 

In advanced mode, you can enter the order items and add extra information about the customer, e.g. birthday, full address, phone number. 

### Viewing manually generated payment links

To view all manually generated payment links, including the date of creation and status:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).

2. Go to **Tools** > **Payment link generator**.

## Cancelling payment links

To cancel a payment link:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com).

2. Go to **Tools** > **Payment link generator**.

3. Next to the relevant payment link, click the red circle button. The status changes to **Cancelled**. 

|  Status      | Description |
|-------------|---------------------------------------------------------------------------|
| Active      | A payment link has been generated, but the payment has not yet been completed.  | 
| Completed   | The customer has completed the payment. | 
| Cancelled   | The merchant has cancelled the payment link.| 
| Expired     | The link has expired.  | 

## Disabling payment links for a payment method

You can only disable a payment link in the website settings. You will need a separate site ID where only the desired payment methods are available. For more information, email the Integration Team at <integration@multisafepay.com>

## Generating payment links in your backend 

For some ecommerce integrations, you can generate payment links in your backend. 

For example, for Magento 1 or a custom integration, you can make a create an order request to our API. See API Reference - [Create an order](https://docs.multisafepay.com/api/#create-an-order). In parameter `type`,  enter `'payment link'`. 

For support, email the Integration Team at <integration@multisafepay.com>

For more information about manually creating payment links using our API, see API Reference - [Generating a payment link](/api/#generating-a-payment-link).
