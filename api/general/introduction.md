---
title: Introduction
category: 623dacddb0cbdd0394b9f5a9
slug: 'introduction'
order: 1
hidden: false
---

Welcome to the MultiSafepay API reference (JSON gateway)!

To test using the API sandbox, you need to [create a test account](/docs/create-account/).

# Direct vs redirect


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

#### Flow

Click to magnify.

![](https://files.readme.io/c702a54-DirectVsRedirectFlowchart.png "DirectVsRedirectFlowchart.png")

# Pagination

Some requests can return a lot of results. To make responses easier to handle, we paginate the results. You can specify how many results to return using the `limit` parameter.

To view the **next** page of the response, use the `after` cursor from the pager object in the response. 
When you make subsequent requests, use the most recently returned `after` cursor to refresh all pages. 
The last page containing data returns an `after` cursor to an empty page. 
Further requests to this page are successful, but won’t return any data or new cursors.

To view the **previous** page of the response, use the `before` cursor from the `pager` object.

Results are sorted from newest to oldest, e.g. for `GET /transactions` requests, the `after` cursor points to older transactions.

# Wrappers and SDKs

We provide the following SDKs and wrappers to facilitate integrating via our API:

- <a href="https://github.com/edoburu/django-multisafepay" target="_blank">Django wrapper</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://github.com/kurt-stolle/go-multisafepay" target="_blank">Go wrapper</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://github.com/MultiSafepay/Java" target="_blank">Java wrapper</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://github.com/MultiSafepay/laravel-api" target="_blank">Laravel wrapper</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://github.com/MultiSafepay/.Net" target="_blank">.NET wrapper</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://github.com/MultiSafepay/multisafepay-node-wrapper" target="_blank">NodeJS wrapper</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://github.com/MultiSafepay/php-sdk" target="_blank">PHP SDK</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>
- <a href="https://github.com/MultiSafepay/multisafepay-python-wrapper" target="_blank">Python wrapper</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

# Deprecated XML API

Our XML API was superseded by the JSON API.

You can still use the XML endpoint to process transaction requests, but new payment methods, features, and tools are only supported by the JSON API.

<br>

---

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>