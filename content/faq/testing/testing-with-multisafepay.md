---
title: 'Testing payment methods'
breadcrumb_title: 'Testing'
weight: 10
meta_title: "Testing - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: "."
logo: '/svgs/Getting started.svg'
layout: 'single'
weight: 10
short_description: "Testing"
aliases:
    - /faq/getting-started/getting-started
---

Before you start processing real transactions with MultiSafepay, we recommend testing each payment method in your MultiSafepay Test Control.<br>

This section assumes you have followed the steps on [Getting started](/guides/getting-started/#step-1-create-a-test-account).

If you encounter any issues during testing, see [Diagnosing errors](/faq/errors-explained/diagnosing-errors/).

To start testing, follow these steps:

{{< br >}}

### Step 1: Initiate a transaction

There are two ways to initiate a transaction:

- Creating a test payment through your [ecommerce integration](/integrations/)
- Sending a request using our [API](/api/)

#### Ecommerce integration

1. Enter your test API key in the backend of your ecommerce integration.
2. Place a test order and initiate a transaction using the payment method you want to test.

#### API

The test API endpoint is: `https://testapi.multisafepay.com/v1/json/`

1. In your API testing environment, enter your test API key.
2. Select a payment method request from the API - [Payment methods](/api/#payment-methods) page.
3. Include **all** required parameters in the request.

If you are using a [custom-built integration](/guides/getting-started/#custom-built-integrations), MultiSafepay checks the customer information in the request to ensure its validity. To minimize the chance of errors during the payment process, include as much identifying information about your test customer as possible.

### Step 2: Complete the payment

A unique URL is automatically generated to a [payment page](/tools/payment-pages/) where you can complete the payment.

1. Fill in the [test payment details](/faq/getting-started/test-payment-details/) if applicable. Payment methods such as iDEAL will let you select various test scenarios instead of filling in the fields. An overview and explanation of these scenarios are visible on the payment page. Read more about statuses per payment method

3. Submit the order by clicking **Test** or **Place Order**.

_Payments may not be successful for various reasons. See the [Diagnosing Errors](/faq/errors-explained/diagnosing-errors/) guide_

### Step 3: Check transaction details

After completing the payment, the transaction details are reflected in the MultiSafepay test environment. To check the status of a transaction:

1. Open your [MultiSafepay test environment](https://testmerchant.multisafepay.com/).
2. Go to **Transactions** → **Transactions overview**.
3. Click on the corresponding transaction from the list.
4. You are now be able to view the **Transaction details, Order summary, Customer details, Status history** and more.

### Step 5: Test to Live

After exploring the testing possibilities within the MultiSafepay test environment, you can [sign up for a live account](https://merchant.multisafepay.com/signup) to begin processing real transactions.

As a [payment service provider](/faq/general/glossary/#payment-service-provider-psp[) and [acquirer](/faq/general/glossary/#acquirer), we are legally required to check your account based on the **Know your customer** guidelines. You can supply the information needed to activate your account through your [MultiSafepay Control](https://merchant.multisafepay.com/) 

Read more about the [onboarding process](/faq/getting-started/onboarding/) 

**Once your live account is approved, remember to change your API key from the previously used test API key to the live API key in your MultiSafepay Control.**

_If you have any questions, feel free to email our [sales team](mailto:sales@multisafepay.com)_
