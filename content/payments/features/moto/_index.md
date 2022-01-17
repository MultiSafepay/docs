---
title : "MOTO"
weight: 80
meta_title: "MOTO - MultiSafepay Docs"
layout: 'single'
read_more: "."
logo: '/svgs/MOTO.svg'
short_description: 'Accept credit card payments by mail or telephone using MOTO'
url: '/features/moto/'
aliases: 
    - /tools/mail-order-telephone-order/
    - /tools/moto/moto
    - /payments/features/moto/
---

Mail Order/Telephone Order (MOTO) is a feature that lets you process credit card payments with card details provided by phone or email. You can create the transaction via your MultiSafepay dashboard or our API. 

Supported payment methods:

- American Express
- Mastercard
- Visa

{{< alert-notice >}} **Note:** Using MOTO skips [3D Secure](/security-and-legal/payment-regulations/about-3d-secure) verification. {{< /alert-notice >}}

## Activating MOTO
Email a request to activate MOTO to <sales@multisafepay.com>

The Risk Team assesses your request and, if approved, activates MOTO for your MultiSafepay account. 

## Via your MultiSafepay dashboard

Once activated, to process MOTO payments, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Tools** > **Mail & phone payments**.
3. Under **Payment details**:  
    - From the **Currency** list, select the currency, and then enter the amount.
    - From the **Site** list, select the relevant website. 
    - Enter an order ID, if relevant.
    - Enter an order description.
4. Under **Credit card details**, enter the payment details provided by the customer by email or telephone. 
5. Under **Customer details**, enter the customer's name, address, and contact information. 
6. Click **Submit order**.  
The transaction appears in your **Transaction overview**.

## Via our API

See API reference – Server to Server: [Credit card and MOTO requests](/api/#credit-card-and-moto-requests).

In the `gateway_info` object, include the `moto` parameter.

