---
title : "Manually generating a payment link"
weight: 34
meta_title: "MultiSafepay Control- Manually generate a payment link - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

## What is a manually generated payment link and what do merchants use it for?

For several scenarios, it can be useful for our merchants to generate a payment link. The payment link allows MultiSafepay Control to create a unique transaction that the payment can be matched with.

Examples:

* A customer wants to adjust an existing order and instead of starting over with a new one, the merchant can generate an adjusted (new) payment link

* A merchant creates an order manually for a customer

* When MultiSafepay receives a payment with an unmatching amount from a customer, if the merchant accepts it, a payment link needs to be generated manually and emailed to MultiSafepay

* In case of an expired bank transfer payment link.

## How can a Merchant generate a payment link? 

In order to manually generate a payment link, please follow these steps:

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com)
2. Click on _Tools_ → _Payment link generator_
3. Click on the blue _New payment link_ button
4. Fill in the required information and click on _generate payment link_
5. Copy the newly generated link from the green bar and send it by email to the customer.

The left side field must be completed with the order information, whereas the right side field can be optionally completed with the contact information of the customer. 

> Please keep in mind that the Order ID filled in every payment link must be unique, otherwise an error notification will show up.

### Creating a payment link by duplicating an order

Should you want to send a payment link for an existing transaction, you can duplicate the transaction via the transaction itself. The Order ID must also be unique! 

### “Simple Mode” or “Advanced Mode”

The 'Simple Mode' is the default payment link mode with the minimum necessary information. 

In the 'Advanced Mode' you are able to fill in the order items and add extra information related to the customer such as articles, birthday, full address and phone number. 

## How long is a manually generated payment link valid? 

The default validity of a manually generated payment link is 30 days. However, you can adjust this to a shorter or longer period depending on your preference. 

## Where can a merchant find a summary of all the generated payment links? 

1. Log in to your [MultiSafepay Control](https://merchant.multisafepay.com)
2. Click on _Tools_ → _Payment link generator_.

You will now be able to see a history of all the generated payment links, the date of their creation creation and their status. 

### Cancelling a payment link
In the summary page of the payment links, there is a red circle button next to each payment link.  After clicking on the button, the status will be changed to _Cancelled_. 

|  Status      | Description |
|-------------|---------------------------------------------------------------------------|
| Active      | A payment link has been generated, but the payment has not yet been fulfilled.  | 
| Completed   | The payment link has been successfully received. | 
| Cancelled   | The payment has been cancelled by the merchant.| 
| Expired     | The link has automatically expired after a predefined period.  | 

## Which payment methods can use a payment link? 

In theory, for every payment method it's possible to add a manually generated payment link, depending on the availability of the payment methods in MultiSafepay Control. Moreover, it is important to check your webshop's requirements in relation to a certain payment method and its support.

For example, post-payment methods such as AfterPay, Pay After Delivery and Klarna do not support manually generated payment links, due to the insolvency process requirement that creates a different flow and dynamics around these payment methods.

## Can a payment link be disabled for a certain payment method? 
Disabling is only possible in the site profile. In this case, as a merchant you will need a separate Site ID in which only the desired payment methods are available. For more information you can contact the Integration Team at <integration@multisafepay.com>

## Can a payment link be generated in the backend of a webshop?

The short answer is yes. However, this depends on the webshop you are using.

For example, for Magento 1 or own integration, a payment link can be created in the backend of the webshop using our [API tool](https://docs.multisafepay.com/api/#create-an-order). The parameter _type_ must be filled with 'payment link'. 

For more information on this topic, please contact the Integration Team at <integration@multisafepay.com>

For the full API reference on manually creating a payment link, please refer to the [generating a payment link page](/api/#generating-a-payment-link).