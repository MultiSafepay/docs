---
title : "Can I test with MultiSafepay?"
meta_title: "FAQ Getting Started - Testing - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---
In order to help you integrate your [website](/faq/general/glossary/#website) with MultiSafepay or test new features, we provide a separate test environment. In the test environment, no real transactions can take place, allowing you to test different payment methods and your website's transaction status handling.

Please start with [creating a test account](https://testmerchant.multisafepay.com/signup) for MultiSafepay Control. As soon as you have created your first website, you can use the test [API key](/faq/general/glossary/#api-key) found in the website settings, in order to authenticate. Alternatively, you can use the test Account ID, Secure Code and Site ID to configure your plugin. You can find these credentials too in the website settings.

{{< alert-notice >}} Outgoing payments and additional payment methods (e.g. American Express) are disabled by default in a test account of MultiSafepay. As a result, a refund cannot be processed successfully. Contact our Integration Team to enable outgoing payments or additional payment methods in your MultiSafepay Control.
{{< /alert-notice >}} 

Contact our Integration Team at <integration@multisafepay.com>

## Test API

`https://testapi.multisafepay.com/v1/json/`

Test Steps
----------

Every transaction processed by MultiSafepay goes through a number of standard steps. During testing, it is helpful to ensure that each step is being completed successfully.

1.  Initiate an order
2.  Customer completes the payment
3.  MultiSafepay sends a status change notification
4.  Client system updates transaction status.

See our [Diagnosing Errors](/faq/errors-explained/diagnosing-errors) guide for help addressing any issues during testing.

### 1\. Initiate an order

Before initiating an order, MultiSafepay checks the information contained in the request to ensure its validity. The majority of fields are optional, but these can have an impact on later stages of the payment process. In particular, you should try to include as much data about the customer as possible, as this data is used by our risk and fraud detection systems. The more data available to the system, the more accurate the results.

When initiating an order, you will receive a link which you should redirect your customer to. If you do not receive a payment link, something must have gone wrong and you will receive an error code.

### 2. Customer completes the payment

This part of the process requires no input from the client. However you should be aware that the result of this step is made available in the transaction status and that payments may not be successful for various reasons.

### 3. MultiSafepay sends a status change notification

The status of an order can change for many reasons. Payments being received or reversed and charge-backs are a few examples. Each time this happens, MultiSafepay will send a notification to your system with the _transaction ID_. The URL that MultiSafepay sends this notification to can be configured in two places. The first place checked is the request when initiating an order. If there is no Notification URL provided when initiating an order, the default Notification URL set in [MultiSafepay Control](https://merchant.multisafepay.com) will be used.

You can check within [MultiSafepay Control](https://merchant.multisafepay.com) to see if we were able to successfully connect and send a notification to your system in the **Offline Actions** section. This information is also available on the _Details_ screen for each transaction.

### 4. Client system updates transaction status

Once your system receives a notification, it must retrieve the transaction status from MultiSafepay. The transaction status will clearly show whether a payment was successful or not and give a reason why a transaction was not successful.

After your system has updated the transaction or order status, you can verify that the information displayed is correct by comparing it to the information displayed within [MultiSafepay Control](https://merchant.multisafepay.com)

## Refunds

It is possible to process refunds in your test account, although refunding any amount is by default disabled. Please contact our Integration team at <integration@multisafepay.com> if you would like to have this option enabled.


