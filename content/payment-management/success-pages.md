---
title: 'Success pages'
category: 6278c92bf4ad4a00361431b0
order: 7
hidden: false
slug: 'success-pages'
---
After completing payment process, MultiSafepay redirects the customer to a success ("thank you") page, or to the next confirmation step where necessary.

If `payment_options.redirect_url` in your [create order](/reference/createorder) request is:

* Set to your success page URL, we redirect the customer there (or to the next step in the process)
* **Not** set, we redirect the customer to a MultiSafepay success page (or to the next step in the process)

**⚠️ Note:** redirection to the success page should not be taken as a guarantor of completed payment; To check the status of a payment, you can rely on the notification.

#### Example

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/SuccessPage.png" align="center" />

# Add order details to your success page

You can retrieve details about a transaction to include on your success page, e.g. payment details, `transaction_status`, `var1/2/3` content, `custom_info` content.

1. In your [create order](/reference/createorder) request, set the URL to your success page in `payment_options.redirect_url`.
2. The `transaction_id` is appended as a query parameter to the URL.
3. To retrieve the order details, make a [get order](/reference/getorder) request from your server using the `transaction_id`.
4. Inject the details into your success page in your <Glossary>backend</Glossary>.

**⚠️ Note:** Make sure your URL only contains a specific set of ASCII characters (alphanumeric, -, \_, ., :, /).

# Dynamically style a MultiSafepay success page

You can dynamically style the MultiSafepay success page in the create order request in the same way as a [payment page](/docs/payment-pages/).

See:

* API reference – [Create order](/reference/createorder/) > Payment page/link > `payment_options` object
* Recipes – <a href="https://docs.multisafepay.com/recipes/style-the-payment-page" target="_blank">Style the payment page</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />

<br />

***

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:integration@multisafepay.com">integration@multisafepay.com</a></p>
</blockquote>

[Top of page](#)