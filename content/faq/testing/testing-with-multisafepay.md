---
title: 'How to test'
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

Before adding new payment methods to your integration with MultiSafepay, testing them will let you to understand how transactions are processed while no real transactions take place. This can be performed in the MultiSafepay test environment that is designed for testing purposes as well as exploring new features or [tools](/tools/). To get started with testing, follow the instructions below:

{{< br >}}

## How to test payment methods

### Step 1: Create a test account

By creating a test account, you can build and test payments for both an ecommerce integration as well as a custom-built integration. The test environment will also let you to explore new features while no costs will be associated with the transactions.

To create a test account, follow these steps:

1. Fill out the signup form to [create a free test account](https://testmerchant.multisafepay.com/signup)
2. Open the email containing your **security code** (6-digit number).
3. [Log in](https://testmerchant.multisafepay.com) using the **security code** provided in the email.

_Email our [support team](mailto:support@multisafepay.com) if you run into any issues during this process._

### Step 2: Initiate an order

The [MultiSafepay API](/api/) section contains the payment requests that can be sent to the MultiSafepay test API endpoint:

Test API endpoint: `https://testapi.multisafepay.com/v1/json/`

#### Prerequisites

1. [Add a website](/tools/multisafepay-control/add-website/#add-your-website-to-multisafepay-control) in your MultiSafepay test environment.
2. Access your [API key](/tools/multisafepay-control/add-website/#accessing-your-api-key) to establish a connection with MultiSafepay.

If you are using a [custom-built integration](/guides/getting-started/#custom-built-integrations), MultiSafepay checks the information contained in the request to ensure its validity. You should include as much information about the customer as possible to minimize the chance of errors occurring during the payment process. See our [Diagnosing Errors](/faq/errors-explained/diagnosing-errors/) guide for help addressing any issues during testing.

To initiate an order:

1. Enter the API key in the backend of your [ecommerce integration](/integrations/) or enter the **API key** in your custom-built integration.
2. Place an order on your website using any payment method or by using the [API requests](/api/#payment-methods)
3. If you are using a custom-built integration, ensure that all **required fields** are filled in to avoid possible errors. Required fields are listed in the table to the left of the [API requests](/api/#payment-methods)


### Step 3: Complete the payment

When placing an order on your website, a payment URL based on the transaction can automatically be generated and can be used to complete the payment:

1. After the payment has been submitted, a payment link URL will be generated and you will be redirected to MultiSafepay's [hosted payment page](/tools/payment-pages/).
2. Fill in the [test payment details](/faq/getting-started/test-payment-details/) if applicable. Payment methods such as iDEAL will let you select various test scenarios instead of filling in the fields. An overview and explanation of these scenarios are visible on the payment page. Read more about statuses per payment method
3. Submit the order by clicking **Test** or **Place Order**.

_Payments may not be successful for various reasons. See the [Diagnosing Errors](/faq/errors-explained/diagnosing-errors/) guide_

### Step 4: Check transaction details

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
