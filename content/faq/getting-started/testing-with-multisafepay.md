---
title : "Testing with MultiSafepay"
weight: 5
meta_title: "FAQ Getting Started - Testing - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
aliases:
    - /faq/getting-started/can-i-test-with-multisafepay
---
In the MultiSafepay Test Environment, you can test your [website](/faq/general/glossary/#website) integration with MultiSafepay or try out new features, without processing real transactions. You can test different payment methods and your website's transaction status handling.

Start by [creating a test account](https://testmerchant.multisafepay.com/signup). For authentication, see the test environment settings and use either:
* the test [API key](/faq/general/glossary/#api-key) provided, or 
* the test Account ID, Secure Code, and Site ID.

{{< alert-notice >}} Outgoing payments and additional payment methods (e.g. American Express) are disabled by default in test accounts, therefore refunds cannot be processed. To enable outgoing payments or additional payment methods in your test account, email the Integration Team at <integration@multisafepay.com>.
{{< /alert-notice >}} 

## Test API

`https://testapi.multisafepay.com/v1/json/`

Using the MultiSafepay Test Environment
----------

Every transaction MultiSafepay processes goes through a number of standard steps. During testing, it is worth checking that each step was completed successfully.

1.  Merchant initiates an order.
2.  Customer completes the payment.
3.  MultiSafepay sends a status change notification.
4.  Client system updates the transaction status.

For help with testing, see [Diagnosing errors](/faq/errors-explained/diagnosing-errors).

### 1. The merchant initiates an order

Provide as much information in the order request as possible. MultiSafepay checks that all this information is valid before initiating the order. Most fields are optional, but leaving them blank may have an impact at later stages of the payment process. Try to include as much data about the customer as possible to help the MultiSafepay risk and fraud detection systems. The more data you provide the system, the more accurate the results.

Once you have initiated the order, we send you a payment link to redirect your customer to. If you don't receive a link, you will receive an error code.

### 2. The customer completes the payment

This part of the process requires no input from the client. The result is displayed in the transaction status. Note that payments may not be successful for various reasons.

### 3. MultiSafepay sends a status change notification

Order status may change for many reasons, e.g. received or reversed payments, or chargebacks. Each time this happens, we send you a status change notification for the _transaction ID_. You can specify the URL you want us to send this notification to in the order request. Otherwise, we will send the notification to the default URL in [MultiSafepay Control](https://merchant.multisafepay.com).

To check that we have successfully connected to your system and sent the status change notification, see [MultiSafepay Control](https://merchant.multisafepay.com) in the **Offline Actions** section, or the _Details_ screen for the transaction.

### 4. Client server updates transaction status

After you receive the status change notification, retrieve the transaction status from MultiSafepay. The transaction status states whether the payment succeeded or failed, and provides the reason for failure.

When the client server has updated the transaction or order status, you can verify the information displayed by comparing it against your [MultiSafepay Control](https://merchant.multisafepay.com).

## Refunds

You can process refunds in your test account, but this is disabled by default. To enable refunds in your test account, email the Integration Team at <integration@multisafepay.com>.
