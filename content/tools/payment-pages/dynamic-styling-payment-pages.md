---
title : "Dynamic styling payment pages"
weight: 41
meta_title: "Payment pages - Dynamic styling - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    -/tools/payment-pages/dynamic-templates
---
Merchants with a custom integration built using our [API](/api) can use dynamic styling to change the look and feel of V2 payment page templates for every transaction.

For more information about V2 payment pages, see FAQ – [Difference between V1 and V2](https://docs.multisafepay.com/tools/payment-pages/difference-between-v1-and-v2).

There are two ways of dynamically styling payment page templates:

## Load a saved template
If you have stored a template, you can request it in the first-level JSON object `"template_id": "value of the template"`.

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Navigate to the WYSIWYG editor, and use it to style the template.
3. Save the template with a unique name, e.g. "template_1". This is used as the `template_id`.
4. Add the `template_id` to your API request for **every** transaction.


## Provide template object structure in the transaction request
You can also style templates in real time. See the template code on API Reference - [Dynamic styling](https://docs.multisafepay.com/api/#dynamic-styling).

1. Sign in to your [MultiSafepay account](https://merchant.multisafepay.com).
2. Navigate to the WYSIWYG editor, and use it to style the template.
3. Go to **</> API view code** to retrieve the code.
4. Add the code to your API request for **every** transaction.

**Note:** Images can only be hosted on external HTTPS domains.
