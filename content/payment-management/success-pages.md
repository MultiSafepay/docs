---
title: 'Success pages'
category: 6278c92bf4ad4a00361431b0
order: 70
hidden: false
slug: 'success-pages'
---

After completing payment, MultiSafepay redirects the customer to a success (or thank you) page. 

If `payment_options.redirect_url` in your [create order](/reference/createorder) request is:

- Set to your success page URL, we redirect the customer there
- **Not** set, we redirect the customer to a MultiSafepay success page

#### Example

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/SuccessPage.png" align ="center"/>

# Add order details to your success page

You can retrieve details about a transaction to include on your success page, e.g. payment details,`transaction_status`, `var1/2/3` content, `custom_info` content. 

1. In your [create order](/reference/createorder) request, set the URL to your success page in `payment_options.redirect_url`.
2. The `transaction_id` is appended as a query parameter to the URL.
3. To retrieve the order details, make a [get order](/reference/getorder) request from your server using the `transaction_id`.
4. Inject the details into your success page in your <<glossary:backend>>.

# Dynamically style a MultiSafepay success page

You can dynamically style the MultiSafepay success page in the create order request in the same way as a [payment page](/docs/payment-pages/). 

See:
- API reference – [Create order](/reference/createorder/) > Payment page/link > `payment_options` object
- Recipes – [Style the payment page](/recipes/style-the-payment-page)

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)

