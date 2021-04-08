---
title: 'Testing'
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

Before adding new payment methods to your integration with MultiSafepay, testing them will allow you to understand how transactions are processed while no real transactions take place. This can be performed in the MultiSafepay Test environment that is designed for testing purposes as well as exploring new features or [tools](/tools/). To get started with testing, please follow the instructions below:

{{< br >}}

## Step 1: Create a test account

By creating a test account, you will be able to build and test your payment integration, explore new features while no costs will be associated with the transactions.

To create a test account, follow these steps:

1. Fill out the signup form to [create a free test account](https://testmerchant.multisafepay.com/signup)
2. Open the email containing your **security code**
3. [Log in](https://testmerchant.multisafepay.com) using the **security code** provided in the email

_Please contact our [support team](mailto:support@multisafepay.com) if you run into any issues during this process._

## Step 2: Initiate an order

The [MultiSafepay API](/api/) section contains the payment requests that can be sent to the MultiSafepay Test API endpoint:

Test API endpoint: `https://testapi.multisafepay.com/v1/json/`

### Prerequisites

1. [Add a website](/tools/multisafepay-control/add-website/#add-your-website-to-multisafepay-control) within your MultiSafepay Test environment
2. Access your [API key](/tools/multisafepay-control/add-website/#accessing-your-api-key) to establish a connection with MultiSafepay

Before initiating an order, MultiSafepay checks the information contained in the request to ensure its validity. Please include as much information about the customer as possible to ensure no errors are encountered during the payment process. See our [Diagnosing Errors](/faq/errors-explained/diagnosing-errors/) guide for help addressing any issues during testing.

To initiate an order:

1. Enter the API key retrieved above in the backend of your website
2. Place a test order of any payment method using the [API requests](/api/#payment-methods)
3. Ensure that all __required__ fields are filled in to avoid errors
4. Submit the request

## Step 3: Complete the payment

A payment URL based on the transaction will automatically be generated and can be used to _complete the payment:_

1. After the payment has been submitted, a payment link will be generated
2. Click on the generated payment link and fill in the [test payment details](/faq/getting-started/test-payment-details/) if applicable
3. Some payments may not be successful for various reasons. Please see the [Diagnosing Errors](/faq/errors-explained/diagnosing-errors/) guide
