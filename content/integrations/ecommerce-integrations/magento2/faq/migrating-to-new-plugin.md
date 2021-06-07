---
title : "What should I do when migrating to the new plugin?"
meta_title: "Magento 2 plugin FAQ - Migration to the new plugin  - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "Version 2 of our plugin is a different plugin and has been built from the ground up. This also means that there are some differences, compared to the deprecated plugin. This article will describe in detail all of the most important differences, to prevent you running in to unexpected behaviour."
---
Our new plugin has been built from the ground up. This also means that there are some differences, compared to the deprecated plugin. This article will describe in detail all of the most important differences, to prevent you running in to unexpected behaviour.

### 1. Installation of the new plugin
We recommend to completely remove the deprecated plugin, before installing the new one. If you need help with removing the deprecated plugin, please take a look at our dedicated [FAQ article](/integrations/ecommerce-integrations/magento2/faq/how-to-delete-deprecated-plugin/) for this.

#### 1.1 Refunding orders that have a payment method from the deprecated plugin
After removing the deprecated plugin and installing the new plugin, the payment gateways from the deprecated plugin are not available inside Magento.

Orders made with payment gateways that are unavailable in Magento cannot be refunded directly from Magento. Instead, these orders can be refunded via your [MultiSafepay Control](https://merchant.multisafepay.com).

### 2. Configuration field changes in General Settings
Some configuration fields are now changed as well. Below you can find all the configuration fields that were available in the deprecated plugin that have changed in some way:

#### E-mail invoice to customer
The feature for sending invoices is still present in the new plugin, but instead of a separate configuration field for enabling/disabling sending the invoice, the plugin now decides to send a invoice based on the following Magento core configuration field:

_Sales_ > _Sales E-mails_ > _Invoice_ > _Enabled_

#### Declined Order Status, Canceled Order Status, Expired Order Status and Chargeback Order Status
These fields have been removed and all of these MultiSafepay statusses will now set the order to the default 'Canceled' status via the offline action.

#### Create Payment link
This configuration field has been removed and a payment link will always be generated and available in the order notes for all MultiSafepay orders that are created.

#### Reset Gateway
This configuration field has been removed, because when creating an order in the Magento backend, you can now select the MultiSafepay payment gateway instead. This payment gateway will show all the active payment gateways to the customer based on the website settings inside the merchant control panel. To make sure this gateway is only available inside the backend and not on the frontend checkout of the store, we have added an extra configuration field 'Can Use Checkout' to the MultiSafepay gateway to enable or disable the gateway in the frontend checkout.

#### Keep cart alive
This configuration field has been removed, because the cart will always be kept alive when a customer uses the back button on the payment page.

{{< blue-notice >}}
_Want one of these features back? Email us at <integration@multisafepay.com> and we will look into the possibility of bringing the desired feature(s) back._
{{< /blue-notice >}}

### 3. Changes in order status flow
The order status flow has been changed a bit. In the new plugin from version 2.5.0, all new orders will start with the state 'Pending'. When redirecting the customer, the order will get the 'Pending Payment' state, until the customer has reached the 'Thank you' page. If the payment has been succesfully received by then, the status will then be changed to 'Processing'. Around the same time the offline action will be triggered and the invoice will get created. If the state has not been set to 'Processing' yet by then, the offline action will set the state 'Processing' instead. For 'Bank Transfer' payments, the state will not be changed to 'Pending Payment' so the order will not get automatically canceled after a set period of time, to give the customer more time to pay.

### 4. Changes in the checkout
For the following payment methods, the payment flow has been changed from [Redirect to Direct](/faq/api/difference-between-direct-and-redirect/). This applies to the following payment methods: AfterPay, Request to Pay, Direct Debit, Einvoicing, in3 and Pay After Delivery (Betaal na Ontvangst).

**For these payment methods, we have included extra fields in the checkout. This means that if you are using a customised checkout, you now not only have to account for the iDEAL issuers checkout field, but also other checkout fields for the other payment methods mentioned above.**

#### An example of differences in the Luma checkout between AfterPay in the deprecated and the new plugin

AfterPay in the deprecated plugin:
{{< screen src="/integrations/ecommerce-integrations/magento2/faq/screens/magento2-afterpay-checkout-deprecated.png" align="center" class="desktop-radius" >}}

AfterPay payment page in the deprecated plugin:
{{< screen src="/integrations/ecommerce-integrations/magento2/faq/screens/magento2-afterpay-checkout-deprecated-2.png" align="center" class="small-image desktop-radius" >}}

AfterPay in the new plugin:
{{< screen src="/integrations/ecommerce-integrations/magento2/faq/screens/magento2-afterpay-checkout.png" align="center" class="desktop-radius" >}}