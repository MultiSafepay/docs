---
title: Introduction
category: 623dacddb0cbdd0394b9f5a9
slug: 'introduction'
order: 1
hidden: false
---

Welcome to the MultiSafepay API reference (JSON gateway)!

To test using the API sandbox, you need to [create a test account](/docs/create-account/).

Direct vs redirect
------------------

With our API, you can create transactions through direct and redirect requests.

Direct requests connect directly to the payment method, whereas redirect requests first send the customer to a [payment page](/docs/payment-pages/).

For redirect requests, if the gateway for a specific payment method is:

- Provided: The payment page is tailored for that payment method, e.g. for Visa, the page includes fields for the customer to enter their credit card details. 
- Not provided: The payment page displays **all** payment methods.

Then, if further customer action is:

- Required: The customer is redirected to complete payment, e.g. for iDEAL, they are redirected to their online banking environment. 
- Not required: The transaction is completed automatically. 

If you provide a `redirect_url`, after completing payment the customer is directed to your success/thank you page.

For more information about the direct and redirect flows for a specific payment method, see the payment method page.

### Flow

Click to magnify.

![](https://files.readme.io/c702a54-DirectVsRedirectFlowchart.png "DirectVsRedirectFlowchart.png")

Wrappers and SDKs
-----------------

We provide the following SDKs and wrappers to facilitate integrating via our API:

- [Django wrapper](https://github.com/edoburu/django-multisafepay)
- [Go wrapper](https://github.com/kurt-stolle/go-multisafepay)
- [Java wrapper](https://github.com/MultiSafepay/Java)
- [Laravel wrapper](https://github.com/MultiSafepay/laravel-api)
- [.NET wrapper](https://github.com/MultiSafepay/.Net)
- [NodeJS wrapper](https://github.com/MultiSafepay/multisafepay-node-wrapper)
- [PHP SDK](https://github.com/MultiSafepay/php-sdk)
- [Python wrapper](https://github.com/MultiSafepay/multisafepay-python-wrapper)

Deprecated XML API
------------------

Our XML API was superseded by the JSON API.

You can still use the XML endpoint to process transaction requests, but new payment methods, features, and tools are only supported by the JSON API.

<br>

***

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>