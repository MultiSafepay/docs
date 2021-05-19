---
title : "Status change notification and Offline actions"
meta_title: "Status change notification and Offline actions - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

The status of a transaction can change for many reasons. Payments being received or reversed and chargebacks are a few examples. Each time this happens, MultiSafepay will send a notification to your system with the **transaction ID**. The URL that MultiSafepay sends this notification to can be configured in two places.

The first check occurs when initiating an order. If there is no notification URL provided when initiating an order, the default **notification URL** set in [MultiSafepay Control](https://merchant.multisafepay.com/) will be used.

## Offline actions

You can check in your [MultiSafepay Control](https://merchant.multisafepay.com/) to see if we were able to successfully connect and send a notification to your system in the **Offline Actions** section. This information can be seen in the MultiSafepay Control or the MultiSafepay test environment. To access the **Offline Actions** section, follow these steps:

1. Log into the **MultiSafepay test environment** or **MultiSafepay Control**.
2. Navigate to **Transactions** → **Transaction overview**.
3. Click on any transaction.
4. Scroll to the bottom of the page to view the **Offline Actions**.

## Transaction status

Once your system receives a notification, it must retrieve the transaction status from MultiSafepay. The transaction status will clearly show whether a payment was successful or not and give a reason why a transaction was not successful.

After your system has updated the transaction or order status, you can verify that the information displayed is correct by comparing it to the information displayed within the MultiSafepay Control or MultiSafepay test environment.