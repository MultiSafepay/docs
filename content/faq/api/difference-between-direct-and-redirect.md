---
title: "What is the difference between a Direct and Redirect API call?"
weight:
meta_title: "FAQ API - What is the difference between a Direct and Redirect API call? - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: "."
---

On our API section, you will often see the terms 'Direct' and 'Redirect' being used. In this section, we will explain the difference between the two API calls.

### What is a Direct transaction?

A Direct transaction will simply skip the MultiSafepay payment page and take you directly to the payment page of the payment method selected. Therefore the payment will be also completed directly through the selected payment method.

_For example, pre-selecting 'IDEAL' as the gateway will take you directly to the payment page of iDEAL, where you will be then able to select the bank you wish to pay with._

### What is a Redirect transaction?

A Redirect transaction will take you to the MultiSafepay payment page where you be presented with the payment method based on what you have pre-selected in the gateway of the API call. 

_For example, pre-selecting iDEAL as the gateway will present the visitor with the banks to select from directly on the MultiSafepay payment page. The customer will then be redirected to the bank they selected to complete the payment._

It is also possile to leave the 'gateway' field empty, this will present the customer with all payment methods from MultiSafepay (subject to the payment methods that are actually enabled for your webshop).
