---
title : "MOTO"
weight: 80
meta_title: "MOTO - MultiSafepay Docs"
layout: "single"
read_more: "."
logo: "/svgs/MOTO.svg"
short_description: 'Accept credit card payments securely by mail or telephone.'
url: "/features/moto/"
aliases: 
    - /tools/mail-order-telephone-order/
    - /tools/moto/moto
    - /payments/features/moto/
---

Mail Order/Telephone Order (MOTO) is a MultiSafepay solution that lets you process card-not-present payments over the phone or by email. 

## How it works

The customer provides their card details to you over the phone or by email. 

Since MOTO skips [3D Secure](/features/3d-secure/about) authentication, you bear the increased risk of fraud. To&nbsp;help ensure the customer is the cardholder, ask them to provide as much identifying information as possible, e.g.:

- Full name
- Address
- Phone numbers
- Email address
- Name of bank
- A copy of their signature on some correspondence, e.g. a scanned order confirmation

You handle the transaction via your MultiSafepay dashboard or our API. 

{{< details title="Supported payment methods" >}}

- American Express
- Generic credit card gateway
- Maestro, **except for** non-domestic transactions in France, Ireland, and Turkey
- Mastercard
- Visa

{{< /details >}}

## Activating MOTO
Email a request to activate MOTO to <sales@multisafepay.com>

The Risk Team assesses your request and, if approved, activates MOTO for your MultiSafepay account. 

## Dashboard

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

## API

See API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Card order.

In the `gateway_info` object, include the `moto` parameter.

