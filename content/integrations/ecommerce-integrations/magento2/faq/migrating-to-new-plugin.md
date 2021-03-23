---
title : "What should I do when migrating to the new plugin?"
meta_title: "Magento 2 plugin FAQ - Migration to the new plugin  - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
layout: "faqdetail"
read_more: "Version 2 of our plugin is a different plugin and has been built from the ground up. This also means that there are some differences, compared to the deprecated plugin. This article will describe in detail all of the most important differences, to prevent you running in to unexpected behaviour."
---
Our new plugin has been built from the ground up. This also means that there are some differences, compared to the deprecated plugin. This article will describe in detail all of the most important differences, to prevent you running in to unexpected behaviour.

### 1. Installation of the new plugin
We recommend to completely remove the deprecated plugin, before installing the new one. If you need help with removing the deprecated plugin, please take a look at our dedicated [FAQ article](/integrations/ecommerce-integrations/magento2/faq/how-to-delete-deprecated-plugin/) for this.
The payment gateways that were in the deprecated plugin will now not be available anymore, which means that online refunds for orders with these gateways can not be done anymore. These orders can be refunded via the MultiSafepay merchant control panel instead.

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
_Want one of these feature back? Please send us an e-mail at integration@multisafepay.com and we will look into the possibility of bringing the desired feature(s) back._
{{< /blue-notice >}}

### 3. Changes in order status flow
The order status flow has been changed a bit. In the new plugin from version 2.5.0, all new orders will start with the state 'Pending'. When redirecting the customer, the order will get the 'Pending Payment' state, until the customer has reached the 'Thank you' page. If the payment has been succesfully received by then, the status will then be changed to 'Processing'. Around the same time the offline action will be triggered and the invoice will get created. If the state has not been set to 'Processing' yet by then, the offline action will set the state 'Processing' instead. For 'Bank Transfer' payments, the state will not be changed to 'Pending Payment' so the order will not get automatically canceled after a set period of time, to give the customer more time to pay.

### 4. Changes in the checkout
For the following payment methods, the payment flow has been changed from [Redirect to Direct](/faq/api/difference-between-direct-and-redirect/). This applies to the following payment methods: Afterpay, Request to Pay, Direct Debit, Einvoicing, in3 and Pay After Delivery (Betaal na Ontvangst).

**For these payment methods, we have included extra fields in the checkout. This means that if you are using a customised checkout, you now not only have to account for the iDEAL issuers checkout field, but also other checkout fields for the other payment methods mentioned above.**

#### An example of differences in the Luma checkout between Afterpay in the deprecated and the new plugin

Afterpay in the deprecated plugin:
{{< screen src="/integrations/ecommerce-integrations/magento2/faq/screens/magento2-afterpay-checkout-deprecated.png" align="center" class="desktop-radius" >}}

Afterpay payment page in the deprecated plugin:
{{< screen src="/integrations/ecommerce-integrations/magento2/faq/screens/magento2-afterpay-checkout-deprecated-2.png" align="center" class="small-image desktop-radius" >}}

Afterpay in the new plugin:
{{< screen src="/integrations/ecommerce-integrations/magento2/faq/screens/magento2-afterpay-checkout.png" align="center" class="desktop-radius" >}}