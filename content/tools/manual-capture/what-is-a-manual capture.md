---
title: "Manual Capture, How it works"
weight: 61
meta_title: "Manual Capture, How it works - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
---

MultiSafepay offers you the ability to capture credit card payments either [partially](/tools/manual-capture/partial-capture) or in [full](/tools/manual-capture/full-capture) from your customers. Thus, it is now possible to charge for a product or service once it has been shipped or consumed. This type of flexibility allows you to take control of your payments and match charges with shipments, whilst gaining trust from customers.

## What are the features of Manual Capture?
* **Control**: Greater control over authorization of payments, whereby funds can be collected at a later stage in full, partial or multiple captures.
* **Trust**: Customers will not be billed for goods or services immediately, but instead only be charged when they have received them. The payment(s) will also not appear until the amount has been captured, thus increasing trust in your brand.
* **Alignment**: It is now possible to align charges and shipments. Administration efforts are now minimalized, along with simplification of your finance flow.
* **Less chargebacks**: Un-shipped, delayed or denied orders will not have their payments captured, thus decreasing the likelihood of chargebacks and reimbursements.

## Transaction overview

* **Order status**: The order status indicates the status of the order such as _completed_ or _void_. The order status is independent of the incoming or outgoing payment of the transaction.

* **Transaction status**: The transaction status indicates the payment status of the transaction, such as _initialized_, _completed_ or _void_. Once the transaction status is _completed_, the amount of the transaction is added to your MultiSafepay balance.
See below for the transaction status actions:


The full [API documentation](/api/#manual-capture-authorization) on Manual Capture will assist in the implementation of the feature.

| Action                         | Order Status     | Transaction Status |   Description                                                      |
|--------------------------------|------------------|------------------|--------------------------------------------------------------------|
| Authorize Transaction          | Completed      | Initialized        | The transaction has been authorized an amount has been reserved.               |
| Partial Capture                | Completed        | Completed        | A partial amount is captured in relation to a previous order id and so both transaction and order status are set to _Completed_.            |
| Full Capture                   | Completed        | Completed        | The full amount is captured in relation to a previous order id and so both the transaction and order status are set to _Completed_.                                                                                                                | 
| Partial Cancel Reservation     | Void             | Void             | The reserved amount or remaining amount which was partially captured has been cancelled.                                                                                                                             |
| Full Cancel Reservation        | Void             | Void             | The fully captured reserved amount has been cancelled.                                                                                                                     |
| Partial Authorization Expiry   | Void             | Void             | The authorized amount or remaining authorized amount has expired without being captured.                                                                                                 |
| Full Authorization Expiry      | Void             | Void             | The fully authorized amount has expired without being captured.                                                                                      |

## Supported payment methods

The Manual Capture functionality is suitable for a number of payment methods:

* VISA
* Mastercard
* Maestro

## Expiry settings

For each payment method a different expiry date applies for capturing a payment. After this period, the issuer can cancel the authorization and the funds will be released back to the customer’s account:

* VISA: 7 days
* Mastercard / Maestro: 30 days


