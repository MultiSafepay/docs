---
title: 'Testing payments'
breadcrumb_title: 'Testing payments'
weight: 10
meta_title: "Testing - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
logo: '/svgs/Testing.svg'
layout: 'single'
weight: 10
short_description: "Testing"
aliases:
    - /faq/getting-started/testing-with-multisafepay/
    - /faq/getting-started/test-orders-overview/
    - /tools/multisafepay-test-environment/multisafepay-test-environment/
---

Before you start processing real transactions with MultiSafepay, we recommend testing each payment method in your [MultiSafepay Test Control](https://testmerchant.multisafepay.com/).<br>

This page assumes you have followed the steps on [Getting started](/guides/getting-started/#step-1-create-a-test-account).

If you encounter any issues during testing, see [Diagnosing errors](/faq/errors-explained/diagnosing-errors/).

To start testing, follow these steps:

## Step 1: Initiate a transaction

There are two ways to initiate a transaction:

- Creating a test payment through your [ecommerce integration](/integrations/)
- Sending a request using our [API](/api/)

### Ecommerce integration

1. Enter your test [API key](/tools/multisafepay-control/get-your-api-key/) in the backend of your ecommerce integration.
2. Place a test order, and then initiate a transaction using the payment method you want to test.

### API

The test API endpoint is: `https://testapi.multisafepay.com/v1/json/`

1. In your API testing environment, enter your test API key.
2. For the payment method you want to test, on the API - [Payment methods](/api/#payment-methods) page, make a POST `/orders` request. Make sure you include __all__ required parameters in the request.

## Step 2: Complete the payment

A unique payment link is returned for you to complete the payment.

1. Enter relevant [test payment details](/faq/getting-started/test-payment-details/) for the payment method you are testing, or select a payment scenario.
2. Complete the test payment.

## Step 3: Check the transaction details

To check the transaction details in your MultiSafepay Test Control:

1. Go to **Transactions** > **Transactions overview**.
2. In the **Transactions overview** list, select the transaction to view the **Transaction details** page. 

For information about transaction statuses, see [Test payment details](/faq/getting-started/test-payment-details/).

## Step 4: Set the notification URL

MultiSafepay uses the notification URL as a webhook to send transaction status updates to your integration.

For custom-built integrations, first create a webhook listener that listens at the notification URL. For more information, see [Notification URL](/faq/api/notification-url/).

For all integrations, to set the notification URL in your MultiSafepay Test Control, follow these steps:

1. Go to __Settings__ > __Website settings__.
2. Select the relevant website.
3. In the __Notification URL__ field, enter your [notification URL](/tools/multisafepay-control/setting-your-notification-url/).
4. Click __Save__.

__Note:__ If you provide a `notification_url` in your POST `/orders` request, it overides the notification URL in your MultiSafepay Test Control. 

## Step 5: Check your connection with MultiSafepay

To check that you have succesfully connected to our system, follow these steps:

1. Log in to your [MultiSafepay Test Control](https://testmerchant.multisafepay.com/).
2. Go to **Transactions** > **Transactions overview**.
3. Select the transaction to view the **Transaction details** page.
4. Under __Offline actions__, in the __Status__ field, check that you correctly received the MultiSafepay request. For information about errors, see [HTTP errors](/faq/errors-explained/http-errors/).

## Go live

To start processing real transactions, sign up for a live account. See [Onboarding](/faq/getting-started/onboarding/).

**Note:** Once your live account is approved, ensure you use the new __live__ API key from your MultiSafepay Control instead of your test API key.

For any questions, email the Integration Team at <integration@multisafepay.com>
