---
title: 'Testing payments'
breadcrumb_title: 'Testing payments'
weight: 10
meta_title: "Testing - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
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

### Step 1: Initiate a transaction

There are two ways to initiate a transaction:

- Creating a test payment through your [ecommerce integration](/integrations/)
- Sending a request using our [API](/api/)

### Ecommerce integration

1. Enter your test [API key](/tools/multisafepay-control/get-your-api-key/) in the backend of your ecommerce integration.
2. Place a test order and initiate a transaction using the payment method you want to test.

### API

The test API endpoint is: `https://testapi.multisafepay.com/v1/json/`

1. In your API testing environment, enter your test API key.
2. On the API - [Payment methods](/api/#payment-methods) page, select a request for the payment method you want to test.
3. Include **all** required parameters in the request.

If you are using a [custom-built integration](/guides/getting-started/#custom-built-integrations), MultiSafepay checks the customer information in the request to ensure its validity. To minimize the chance of errors during the payment process, include as much identifying information about your test customer as possible.

### Step 2: Complete the payment

A unique payment URL is automatically generated where it is then possible for you to complete the payment.

1. Enter test payment details or select a payment scenario for the payment method you are testing. See [Test payment details](/faq/getting-started/test-payment-details/). 
2. Complete the test payment.

### Step 3: Check transaction details

After completing the payment, the transaction details appear in your MultiSafepay Test Control. To check the status of a transaction:

1. Go to **Transactions** > **Transactions overview**.
2. In the **Transactions overview** list, select the transaction to view the **Transaction details** page.

For information about payment statuses, see [Test payment details](/faq/getting-started/test-payment-details/)

### Step 4: Setting the notification URL

The notification URL is used for sending transaction status updates to your integration.

To set the notification URL in your MultiSafepay Test Control, follow these steps:

1. Navigate to __Settings__ > __Website settings__.
2. Select your website.
3. Fill in the __notification URL__, and then click __Save__.

If the notification URL field is empty, the notification URL from the transaction will be used. For more information, see [Notification URL](/faq/api/notification-url/)

### Step 5: Checking the status

The transaction status must correspond in both the Offline actions in your MultiSafepay Test Control and your system.

To check that we have successfully connected to your system and sent the status change notification, see __Offline actions__ section at the bottom of the page of any transaction.

Once your system receives a notification, it must retrieve the __transaction status__ from MultiSafepay. The transaction status states whether the payment succeeded or failed, and provides the reason for failure.

After your system has updated the transaction or order status, you can compare the information displayed within your MultiSafepay Test Control and your system for verification. If no error appears in the __Offline actions__ section, you have successfully established a connection between both environments.

## Go live

To start processing real transactions, sign up for a live account. See [Onboarding](/faq/getting-started/onboarding/).

**Note:** Once your live account is approved, ensure you use the new live API key from your MultiSafepay Control instead of your test API key.

For any questions about this process, email the Integration Team at <integration@multisafepay.com>
