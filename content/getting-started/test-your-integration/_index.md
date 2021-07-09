---
title: 'Test your integration'
breadcrumb_title: 'Test your integration'
weight: 10
meta_title: "Getting Started - Test your integration - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
logo: '/svgs/Testing.svg'
layout: 'single'
weight: 40
short_description: "Test payments and resolve common issues."
aliases:
    - /faq/getting-started/testing-with-multisafepay/
    - /faq/getting-started/test-orders-overview/
    - /tools/multisafepay-test-environment/multisafepay-test-environment/
    - /faq/testing/testing-payments/
    - /faq/testing/testing-with-multisafepay/
---

Before you start processing real transactions with MultiSafepay, we recommend testing each payment method in your [MultiSafepay test account](https://testmerchant.multisafepay.com/).

If you encounter any issues during testing, see [Diagnosing errors](/faq/errors-explained/diagnosing-errors/).

For support, email the Integration Team at <integration@multisafepay.com>

## 1. Initiate a transaction

There are two ways to initiate a transaction:

- Create a test payment through your [ecommerce integration](/integrations/).
- Send a request using our [API](/api/).

### Ecommerce integration

1. Enter the [API key](/getting-started/set-up-your-account/user-guide/viewing-your-api-key/) from your test account in the backend of your ecommerce integration.
2. Place a test order, and then initiate a transaction using the payment method you want to test.

### API

The test API endpoint is: `https://testapi.multisafepay.com/v1/json/`

1. In your API testing environment, enter your test API key.
2. For the payment method you want to test, on the API Reference - [Payment methods](/api/#payment-methods) page, make a POST `/orders` request. Make sure you include __all__ required parameters in the request.

## 2. Complete the payment

A unique payment link is returned for you to complete the payment.

1. Enter relevant [test payment details](/faq/getting-started/test-payment-details/) for the payment method you are testing, or select a payment scenario.
2. Complete the test payment.

## 3. Check the transaction details

To check the transaction details in your MultiSafepay test account:

1. Go to **Transactions** > **Transactions overview**.
2. In the **Transactions overview** list, select the transaction to view the **Transaction details** page. 

For information about transaction statuses, see [Test payment details](/faq/getting-started/test-payment-details/).

## 4. Set the notification URL

MultiSafepay uses the notification URL as a webhook to send transaction status updates to your integration.

For custom-built integrations, first create a webhook listener that listens at the notification URL. For more information, see [Notification URL](/faq/api/notification-url/).

For all integrations, to set the notification URL in your MultiSafepay test account, follow these steps:

1. Go to __Settings__ > __Website settings__.
2. Select the relevant website.
3. In the __Notification URL__ field, enter your [notification URL](/tools/multisafepay-control/setting-your-notification-url/).
4. Click __Save__.

__Note:__ If you provide a `notification_url` in your POST `/orders` request, it overides the notification URL in your MultiSafepay test account. 

## 5. Check your connection with MultiSafepay

To check that you have succesfully connected to our system, follow these steps:

1. Sign in to your [MultiSafepay test account](https://testmerchant.multisafepay.com/).
2. Go to **Transactions** > **Transactions overview**.
3. Select the transaction to view the **Transaction details** page.
4. Under __Offline actions__, in the __Status__ field, check that you correctly received the MultiSafepay request. For information about errors, see [HTTP errors](/faq/errors-explained/http-errors/).

**Note:** Once your live account is approved, ensure you use the API key from your live account instead of your test account.

## Read more

{{< two-buttons href-2="/getting-started/test-your-integration/test-payment-details" header-2="Read more" text-2="Test payment details" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

{{< two-buttons href-2="/getting-started/test-your-integration/testing-refunds" header-2="Read more" text-2="Testing refunds" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

## Next steps

{{< two-buttons
href-1="/getting-started/build-your-integration" header-1="Previous" text-1="Build your integration" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/getting-started/go-live" header-2="Next" text-2="Onboard and go live" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}