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

Before adding new payment methods to your integration with MultiSafepay, testing them will allow you to understand how transactions are processed while no real transactions take place. This can be performed in the MultiSafepay test environment that is designed for testing purposes as well as exploring new features or [tools](/tools/). To get started with testing, please follow the instructions below:

{{< br >}}

## How to test payment methods

### Step 1: Create a test account

By creating a test account, you will be able to build and test your payment integration, explore new features while no costs will be associated with the transactions.

To create a test account, follow these steps:

1. Fill out the signup form to [create a free test account](https://testmerchant.multisafepay.com/signup)
2. Open the email containing your **security code**
3. [Log in](https://testmerchant.multisafepay.com) using the **security code** provided in the email.

_Please contact our [support team](mailto:support@multisafepay.com) if you run into any issues during this process._

### Step 2: Initiate an order

The [MultiSafepay API](/api/) section contains the payment requests that can be sent to the MultiSafepay test API endpoint:

Test API endpoint: `https://testapi.multisafepay.com/v1/json/`

#### Prerequisites

1. [Add a website](/tools/multisafepay-control/add-website/#add-your-website-to-multisafepay-control) within your MultiSafepay test environment
2. Access your [API key](/tools/multisafepay-control/add-website/#accessing-your-api-key) to establish a connection with MultiSafepay

Before initiating an order, MultiSafepay checks the information contained in the request to ensure its validity. Please include as much information about the customer as possible to minimize the chance of errors occurring during the payment process. See our [Diagnosing Errors](/faq/errors-explained/diagnosing-errors/) guide for help addressing any issues during testing.

To initiate an order:

1. Enter the API key in the backend of your website or integration. You can find the instructions about where the API key can be entered on each [integration manual](/integrations/)
2. Place a test order of any payment method using the [API requests](/api/#payment-methods)
3. Ensure that all __required__ fields are filled in to avoid possible errors. Required fields are listed in the table to the left of the API requests
4. Submit the payment request.

### Step 3: Complete the payment

A payment URL based on the transaction will automatically be generated and can be used to complete the payment:

1. After the payment has been submitted, a payment link URL will be generated
2. Click on the generated payment link and fill in the [test payment details](/faq/getting-started/test-payment-details/) if applicable. Payment methods such as iDEAL will allow you to select various test scenarios. An overview and explanation of these scenarios are visible on the payment page. Read more about statuses per payment method
3. Submit the order by clicking _Test_ or *Place_Order*.

_Some payments may not be successful for various reasons. Please see the [Diagnosing Errors](/faq/errors-explained/diagnosing-errors/) guide_

### Step 4: Check transaction details

After completing the payment, the transaction details will be reflected in the MultiSafepay test environment. To check the status of a transaction:

1. Open your [MultiSafepay test environment](https://testmerchant.multisafepay.com/)
2. Go to _Transactions_ → _Transactions overview_
3. Click on the corresponding transaction from the list
4. You will now be able to view the _Transaction details, Order summary, Customer details, Status history_ and more.

### Step 5: Test to Live

After exploring the testing possibilities within the MultiSafepay test environment, you can [sign up for a live account](https://merchant.multisafepay.com/signup) to begin processing real transactions.

As a [payment service provider](/faq/general/glossary/#payment-service-provider-psp[) and [acquirer](/faq/general/glossary/#acquirer), we are legally required to check your account based on the 'Know your customer' guidelines. You can supply the information needed to activate your account through your [MultiSafepay Control](https://merchant.multisafepay.com/) 

Read more about the [onboarding process](/faq/getting-started/onboarding/)

_If you have any questions, our [sales team](mailto:sales@multisafepay.com) are ready to assit you_

## Status change notification

The status of an order can change for many reasons. Payments being received or reversed and chargebacks are a few examples. Each time this happens, MultiSafepay will send a notification to your system with the transaction ID. The URL that MultiSafepay sends this notification to can be configured in two places. The first place checked is the request when initiating an order. If there is no Notification URL provided when initiating an order, the default Notification URL set in [MultiSafepay Control](https://merchant.multisafepay.com/) will be used.

You can check within [MultiSafepay Control](https://merchant.multisafepay.com/) to see if we were able to successfully connect and send a notification to your system in the Offline Actions section. This information can be seen in the MultiSafepay test environment and MultiSafepay Control:

1. Log into the MultiSafepay test environment or MultiSafepay Control
2. Navigate to _Transactions_ → _Transaction overview_
3. Click on any transaction
4. Scroll to the bottom of the page to view the _Offline Actions_

## Client system updates transaction status

Once your system receives a notification, it must retrieve the transaction status from MultiSafepay. The transaction status will clearly show whether a payment was successful or not and give a reason why a transaction was not successful.

After your system has updated the transaction or order status, you can verify that the information displayed is correct by comparing it to the information displayed within [MultiSafepay Control](https://merchant.multisafepay.com/)

## Refunds

It is possible to process refunds in your test account, although refunding any amount is by default disabled. Please contact our Integration Team at <integration@multisafepay.com> if you would like to have this option enabled.