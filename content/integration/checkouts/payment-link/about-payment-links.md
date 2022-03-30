---
title: 'About payment links'
weight: 10
meta_title: "About payment links - MultiSafepay Docs"
layout: 'single'
logo: '/svgs/External link.svg'
short_description: 'Generate payment links via our API or in your MultiSafepay dashboard.'
url: '/payment-links/about/'
read_more: "."
aliases:
    - /tools/payment-link/payment-link-api/
    - /payments/checkout/payment-link/
---

You can manually generate a link to a [payment page](/payment-pages/) to pass to a customer to complete payment. 

## Use cases 

- A customer wants to adjust an existing order and instead of starting over with a new order.
- You need to create a transaction for a manually generated order.
- MultiSafepay collects a payment for an amount that doesn't match any order. If you accept the payment, you need to manually generate a payment link and email it to <support@multisafepay.com>
- A [Bank Transfer](/payment-methods/bank-transfer/) transaction has expired.

## Payment methods

All payment methods are supported. 

The [payment page](/payment-pages/) displays **all** payment methods activated for the relevant website. If&nbsp;you want to display specific payment methods, you need to create a new website profile with only the relevant methods activated. 

## Lifetimes

The lifetime of a payment link is how long it remains active for the customer to access the payment page and complete payment. The default is 30 days. 

To set or adjust the lifetime, see API reference – [Create order](https://api-docs.multisafepay.com/reference/createorder): `days_active` parameter.

{{< blue-notice >}} **Note:** This is different to [transaction expiration times per payment method](/developer/transaction-expiration/). {{< /blue-notice >}} 

## Attempts 
The customer can open the link to the payment page up to 20 times, after which the link is disabled.

Each attempt creates a new transaction. If the customer completes payment in one of these transactions, the [status](/about-payments/multisafepay-statuses/) of the other transactions remains **Initialized** until they expire.

## Viewing payment links

For an overview of all payment links in your [MultiSafepay dashboard](https://merchant.multisafepay.com), go to **Tools** > **Payment link generator**.

### Payment link statuses

| Status | Description |
|---|---|
| Active | The link is generated, but the customer hasn't paid yet.  | 
| Completed | The customer has paid. | 
| Cancelled | You cancelled the link.| 
| Expired | The link has expired.  | 