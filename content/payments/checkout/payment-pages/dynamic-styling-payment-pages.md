---
title : "Dynamic styling payment pages"
weight: 50
meta_title: "Payment pages - Dynamic styling - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    -/payments/checkout/payment-pages/dynamic-styling-payment-pages/
---
Merchants with a custom integration built using our [API](/api) can use dynamic styling to change the look and feel of V2 payment page templates for every transaction.

For more information about V2 payment pages, see [Classic payment page](/checkout/payment-pages/classic-payment-page).

There are two ways of dynamically styling payment page templates:

## Saved templates
If you have stored a template, you can request it in the first-level JSON object `"template_id": "value of the template"`.

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to the WYSIWYG editor, and use it to style the template.
3. Save the template with a unique name, e.g. Template 1. This is used as the `template_id`.
4. Add the `template_id` to your `POST /orders` request for **every** transaction.

## Template object 
You can also style templates in real time. See API Reference – [Apply dynamic templates](https://docs.multisafepay.com/api/#dynamic-styling).

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Go to the WYSIWYG editor, and use it to style the template.
3. Go to **</> API view code** to retrieve the code.
4. Add the code to your `POST /orders` request for **every** transaction.

**Note:** Images can only be hosted on external HTTPS domains.
