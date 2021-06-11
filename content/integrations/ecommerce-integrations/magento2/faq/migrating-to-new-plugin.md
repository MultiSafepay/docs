---
title : "Migrating to the new plugin"
meta_title: "Magento 2 plugin - Migrating to the new plugin  - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
aliases:
    - /integrations/ecommerce-integrations/magento2/faq/changes-to-new-plugin/
---

This page describes the most important differences between the old plugin and the new one to help you avoid unexpected behaviour.

## Changes to refunds
After deleting the deprecated plugin and installing the new one, the payment gateways from the deprecated plugin are no longer available in Magento.

You can refund transactions processed through these gateways in your [MultiSafepay Control](https://merchant.multisafepay.com), but **not** from your Magento 2 backend.

## Changes to configuration fields
Under **General settings**, we have changed the following configuration fields from the deprecated plugin.

If you want one of these features back, email the Integration Team at <integration@multisafepay.com>

### Email invoice to customer
This feature is still supported in the new plugin, but it now uses the following Magento core configuration field: **Sales** > **Sales emails** > **Invoice** > **Enabled**.

### Order status

We have removed the following **Order status** fields:

- **Declined**
- **Canceled**
- **Expired** 
- **Chargeback**

All MultiSafepay statuses now set the order to the default **Canceled** status via the offline action.

### Create payment link
We have removed this field. Payment links are now generated automatically. See [Retrieving payment links](/integrations/ecommerce-integrations/magento2/faq/retrieving-payment-links/).

### Reset gateway
We have removed this field. When creating an order in the Magento 2 backend, you can now select the MultiSafepay payment gateway instead. The payment gateway displays all active payment gateways to the customer based on the website settings in your MultiSafepay Control. 

To enable or disable the gateway on your checkout page, we have added the **Can use checkout** configuration field.

### Keep cart alive
We have removed this field. Now the cart is always kept alive when the customer clicks the back button on the MultiSafepay payment page.

## Changes to order status flow
We have updated the order status flow from version 2.5.0:

- All new orders first receive **Pending** status.
- When redirecting the customer, the status changes to **Pending payment**, until the customer reaches the 'Thank you' page. 
- If the payment is succesfully received at this point, the status changes to **Processing**. 
- Around the same time, the offline action is triggered and the invoice is created. The offline action sets the status to **Processing** if it isn't already. 
- For bank transfer payment methods, the status doesn't change to **Pending payment**, therefore the order isn't automatically canceled after a set period of time to give the customer more time to pay.

## Changes to the checkout
For the following payment methods, we have changed the payment flow from [redirect to direct](/faq/api/difference-between-direct-and-redirect/):

- Afterpay
- Request to Pay
- Direct Debit
- E-invoicing
- in3 
- Pay After Delivery (Betaal na Ontvangst)

We have included extra fields in the checkout for these payment methods. If you use a custom checkout, you must account for the iDEAL issuers checkout field and the new checkout fields for these payment methods.

### Example 
This example shows the differences between the Luma checkout for Afterpay in the deprecated plugin and the new one

Deprecated plugin:
{{< screen src="/integrations/ecommerce-integrations/magento2/faq/screens/magento2-afterpay-checkout-deprecated.png" align="center" class="desktop-radius" >}}

Payment page in the deprecated plugin:
{{< screen src="/integrations/ecommerce-integrations/magento2/faq/screens/magento2-afterpay-checkout-deprecated-2.png" align="center" class="small-image desktop-radius" >}}

AfterPay in the new plugin:
{{< screen src="/integrations/ecommerce-integrations/magento2/faq/screens/magento2-afterpay-checkout.png" align="center" class="desktop-radius" >}}
