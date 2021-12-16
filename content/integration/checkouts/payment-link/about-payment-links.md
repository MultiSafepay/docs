---
title : "About payment links"
weight: 10
meta_title: "Payments - About payment links - MultiSafepay Docs"
url: '/payment-links/about'

read_more: '.'
url: '/payment-links/about/'
layout: 'faq'
---

Payment links create a unique transaction in your [MultiSafepay account](https://merchant.multisafepay.com/) to match to a payment.

## Lifetimes

The lifetime of a payment link is how long it remains valid for the customer to complete payment. The default is 30 days. 

To set or adjust lifetimes, see API reference – [Adjust payment link lifetimes](/api/#adjust-payment-link-lifetimes).

You can adjust lifetimes for all payment methods except for:  

- [Pay later methods](/payments/methods/pay-later/)
- PayPal: Links are valid for 14 days. The lifetime is set by PayPal.
- Prepaid cards: Edenred, Paysafecard
- SEPA Direct Debit

## Attempts 
The customer can click a payment link to attempt payment up to 20 times, after which the link is disabled.

Each attempt is registered as a separate transaction (`PSP ID`). If payment for one of the transactions is successfully completed, all the others remain open until they expire.

## Simple mode and advanced mode

Simple mode is the default payment link mode, which contains the minimum necessary information. 

In advanced mode, you can enter the order items and add extra information about the customer, e.g. birthday, full address, phone number. 

## Payment link statuses

|  Status      | Description |
|-----|----|
| Active      | A payment link has been generated, but the payment has not yet been completed.  | 
| Completed   | The customer has completed the payment. | 
| Cancelled   | The merchant has cancelled the payment link.| 
| Expired     | The link has expired.  | 

