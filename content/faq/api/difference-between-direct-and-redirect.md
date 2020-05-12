---
title: "What is the difference between a Direct and Redirect API call?"
weight:
meta_title: "FAQ API - What is the difference between a Direct and Redirect API call? - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

On our API section, you will often see the terms 'Direct' and 'Redirect' being used. In this section, we will explain the difference between the two API calls.

### Direct

A Direct transaction will simply connect you directly to the chosen payment method and will either provide a direct link to the payment method or perform the transaction immediately without the customer having to do anything. Direct transactions can also be carried out on a continuous basis with automated payments, such as [Recurring payments](/tools/recurring-payments/)

_For example, pre-selecting 'iDEAL' as the gateway will take you directly to the respective bank page (a valid IssuerID must also be provided only for an iDEAL transaction)_

### Redirect

A Redirect transaction will redirect the consumer to the MultiSafepay payment page, where they will be presented with the payment method based on what has been pre-selected in the gateway of the API call. 

_For example, pre-selecting 'Visa' as the gateway will present the consumer with the fields to fill in their Visa credit card information. The consumer will not leave the MultiSafepay payment page._

It is also possible to leave the 'gateway' field empty, this will present the customer with all payment methods from MultiSafepay (subject to the payment methods that are actually enabled for your webshop).
