---
title : "How can I style the payment pages?"
weight: 42
meta_title: "Payment pages - Styling Payment pages - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
MultiSafepay's payment pages provide the quickest, easiest and most secure way to accept online payments. By default, your payment pages use MultiSafepay's renowned brand and styling. However, we recommend that you personally tailor the payment pages in a manner that is consistent with your own website. This is very easy, and can be done via [MultiSafepay Control](https://merchant.multisafepay.com).

> MultiSafepay is unable to customize payment pages or email templates for you, although if you do encounter functionality issues, please contact us at <integration@multisafepay.com>

## Using the editor
In your [MultiSafepay Control](https://merchant.multisafepay.com), use the editor to easily change the look and feel of the payment page template. To adjust the template, please follow the following steps:

1. Login into your [MultiSafepay Control](https://merchant.multisafepay.com)
2. Navigate to _Settings / Website Settings_ and select _Website_
3. Click on the _Template_ button.

In the editor, you can style nearly all elements on the Payment pages. Via the left menu you can change the colour of e.g. the background, the footer, buttons (incl. mouseover) and cart details. For the header, you can choose to pick a logo and use either an image or color for the background.

### 1. Choosing colors
In the left menu, you will see a color chart when you click on the field of an element. You can also directly use a [Hex color](https://www.w3schools.com/colors/colors_picker.asp) in the input field next to it.

### 2. Selecting a logo or header image
Before you can select a file for the logo or header background, you need to upload it under Settings / Payment page Templates. After uploading, it will automatically appear in the dropdown list on the editor. The processing of an uploaded image might take up to 5 minutes. Go to the [upload page](https://merchant.multisafepay.com/payment-page-templates)

### 3. Loading and Saving template
Whenever you finished a template, you can save it for its corresponding website via the _Submit website_ button. If you have more than one template, use the _Set default_ option to make this the default template. You can also give this template a name (later referred to as <i>template_id</i>). Via the top left button _Edit template_ you can select previously saved templates.

If you wish to load a template from another website within your account, you can load this via the _Apply style from_ button in the top right corner. Don't forget to save this to the website you are currently editing.

## Dynamic templates
For merchants with a custom integration via [MultiSafepay API](/api/), MultiSafepay also offers [dynamic styling of the templates](/tools/payment-pages/dynamic-templates/). This means you can change the look and feel of a payment page per transaction. There are two options to dynamically style the Payment page:

1. Load a saved template via object _template_id_
2. Provide _template_ object structure within the transaction request.
You can still use the editor to generate the object structure for the transaction request. To do this, first generate your template and then switch to the tab </> Api view code. Next to the code you can also find the _template_id_ here.

For more information visit the [API Reference](/api/).
