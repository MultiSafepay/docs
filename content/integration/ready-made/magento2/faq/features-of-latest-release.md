---
title : "Features of latest release"
meta_title: "Magento 2 plugin - Features of latest release  - MultiSafepay Docs"
layout: "faqdetail"
read_more: "."
url: '/magento-2/latest-release-features/'
aliases: 
    - /integrations/ecommerce-integrations/magento2/faq/migrating-to-new-plugin
    - /payments/integrations/ecommerce-platforms/magento2/faq/changes-to-new-plugin/
    - /payments/integrations/ecommerce-platforms/magento2/faq/features-of-latest-release/
---

## Refunds and shipping

Make sure you finish processing all orders created in the deprecated plugin before you delete it. The deprecated payment gateways are no longer available in Magento after deletion. 

You can refund transactions processed through the deprecated plugin in your [MultiSafepay dashboard](https://merchant.multisafepay.com), but **not** from your Magento 2 [backend](/glossaries/multisafepay-glossary/#backend).

**Note:** After deleting the deprecated plugin, shipment requests for orders created in it are not automatically sent to MultiSafepay. You must set the order status to **Shipped** manually in your [MultiSafepay dashboard](https://merchant.multisafepay.com).

## Configuration fields

Under **General settings**, we have changed the following configuration fields from the deprecated plugin.

If you want one of these features back, email <integration@multisafepay.com>

## Emailing invoices to customers

This feature is still supported in the new plugin, but it now uses the following Magento core configuration field: **Sales** > **Sales emails** > **Invoice** > **Enabled**.

## Order status

As of version 2.16, the following MultiSafepay statuses can be assigned to a Magento order status:

- **Cancelled**
- **Chargeback**
- **Declined**
- **Expired**
- **Initialized**
- **Partial refunded**
- **Refunded**
- **Reserved**
- **Uncleared**
- **Void**

## Order status flow  

We have updated the order status flow from version 2.5.0:

- All new orders first receive **Pending** status.
- When redirecting the customer, the status changes to **Pending payment**, until the customer reaches the 'Thank you' page. 
- If the payment is succesfully received at this point, the status changes to **Processing**. 
- Around the same time, the offline action is triggered and the invoice is created. The offline action sets the status to **Processing** if it isn't already. 
- For bank transfer payment methods, the status doesn't change to **Pending payment**, therefore the order isn't automatically cancelled after a set period of time to give the customer more time to pay.

## Create payment link  

We have removed this field. Payment links are now generated automatically. See [Retrieving payment links](/payments/integrations/ecommerce-platforms/magento2/faq/retrieving-payment-links/).

## Reset gateway  

We have removed this field. When creating an order in the Magento 2 backend, you can now select the MultiSafepay payment gateway instead. The payment gateway displays all active payment gateways to the customer based on the website settings in your MultiSafepay account. 

To enable or disable the gateway on your checkout page, we have added the **Can use checkout** configuration field.

## Keep cart alive  

We have removed this field. Now the cart is always kept alive when the customer clicks the back button on the MultiSafepay payment page.

## Checkout  

For the following payment methods, we have changed the default payment flow from [redirect to direct](https://multisafepay.readme.io/reference/introduction#direct-vs-redirect):

- Afterpay
- Request to Pay
- Direct Debit
- E-Invoicing
- in3 
- Pay After Delivery (Betaal na Ontvangst)

We have included extra fields in the checkout for these payment methods. If you use a custom checkout, you must account for the iDEAL issuers checkout field and the new checkout fields for these payment methods.

Alternatively, you can disable additional checkout fields for these payment methods and change the flow back to redirect. Go to **Stores** > **Configuration** > **MultiSafepay** > **Payment gateways** > **Gateway** > **Additional checkout fields**.

### Example
  
This example shows the differences between the Luma checkout for Afterpay in the deprecated plugin and the new one

Deprecated plugin:
{{< screen src="/payments/integrations/ecommerce-platforms/magento2/faq/screens/magento2-afterpay-checkout-deprecated.png" align="center" class="desktop-radius" >}}

Payment page in the deprecated plugin:
{{< screen src="/payments/integrations/ecommerce-platforms/magento2/faq/screens/magento2-afterpay-checkout-deprecated-2.png" align="center" class="small-image desktop-radius" >}}

New plugin:
{{< screen src="/payments/integrations/ecommerce-platforms/magento2/faq/screens/magento2-afterpay-checkout.png" align="center" class="desktop-radius" >}}
