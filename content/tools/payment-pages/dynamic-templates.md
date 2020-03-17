---
title : "How to use dynamic styling for a Payment page?"
weight: 41
meta_title: "Payment pages - Dynamic templates - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
For merchants with a __custom integration__ via [JSON API MultiSafepay](/api/), we also offers dynamic styling of the templates. This means you can change the look and feel of a payment page per transaction.

There are two options to dynamically style the payment page:

## 1. Load a saved template
Whenever you have stored a template, you can call it through the first-level JSON object "template_id": "value of the template".

1. Login to your [MultiSafepay Control](https://merchant.multisafepay.com/)
2. Navigate to the WYSIWYG editor
3. Style the template with the editor
4. Save the template you created with a unique name e.g. "template_1". This will be the template_id
5. Add the template_id to the API call __per transaction__


## 2. Provide 'template' object structure within the transaction request
MultiSafepay also offers real-time styling of the templates. This means you can change the look and feel of a payment page per transaction on the fly. See the template code on our [API documentation page](https://docs.multisafepay.com/api/#dynamic-styling)

1. Login to your [MultiSafepay Control](https://merchant.multisafepay.com/)
2. Style the template via the editor
3. Go to __</> Api view code__ to retrieve the code
4. Add the code to the API call __per transaction__

_Please note:_ 

* The styling on template pages can only be carried out on the V2 payment pages. Read more about the [difference between V1 and V2](https://docs.multisafepay.com/tools/payment-pages/difference-between-v1-and-v2/)
* This only works for custom integrations (JSON API), not for plugins or hosted solutions
* Images can be hosted on external domains (only HTTPS)