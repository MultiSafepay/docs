---
title : "How to use dynamic styling for a Payment page?"
weight: 41
meta_title: "Payment pages - Dynamic templates - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
For merchants with a custom integration via [JSON API MultiSafepay](/api/), we also offers dynamic styling of the templates. This means you can change the look and feel of a payment page per transaction.

There are two options to dynamically style the payment page:

## 1. Load a saved template
Whenever you have stored a template, you can call it through the first-level JSON object "template_id": "value of the template".

## 2. Provide 'template' object structure within the transaction request
MultiSafepay also offers real-time styling of the templates. This means you can change the look and feel of a payment page per transaction on the fly. See the template code on our [API documentation page](/api/#dynamic-styling)