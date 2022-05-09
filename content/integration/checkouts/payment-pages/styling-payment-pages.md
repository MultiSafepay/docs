---
title : "Styling payment pages"
weight: 30
meta_title: "Payment pages - Styling payment pages - MultiSafepay Docs"
read_more: '.'
url: '/payment-pages/styling/'
aliases:
    - /tools/payment-pages/payment-page-templates/
    - /payments/checkout/payment-pages/dynamic-styling-payment-pages/
    - /payments/checkout/payment-pages/styling-payment-pages/
---
We recommend styling MultiSafepay payment pages to be consistent with the look and feel of your website.

You can do this via your MultiSafepay dashboard, or our API. 

## Dashboard

To style payment page templates from your MultiSafepay dashboard, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings** > **Website settings** > **Website**.
3. Click the **Template** button. 
4. Use the WYSIWYG editor to style the payment page template.  
    - Choosing colors: In the left menu, a color chart appears when you click on the field of a page element. You can also enter a [Hex color](https://www.w3schools.com/colors/colors_picker.asp) in the input field next to it.
    - Selecting a logo or header image: In **Settings** > **Payment page templates**, upload files for logos or header backgrounds. They may take up to 5 minutes to process, and then automatically appear in the dropdown list in the editor.
5. To save the finished template to the relevant website, click **Submit website**. 

{{< details title="Other tips" >}}

- If you have more than one template and want to set one as your default template, use the **Set default** option. You can also give this template a name, which is used as the `template_id`. 

- To edit saved templates, click the **Edit template** button in the top-left corner.

- To apply the style from one template to another website under your account, click the **Apply style from** button in the top-right corner. Save the template to the relevant website.

{{< /details >}}

## API

Dynamically style the payment page template for specific transaction requests via our API. See API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Payment page/link > `payment_options` object. 

For support, email <integration@multisafepay.com>