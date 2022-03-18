---
title: 'Handling cardholder data'
weight: 90
read_more: "."
layout: single
meta_title: "Handling cardholder data - MultiSafepay Docs"
logo: '/svgs/Server to server.svg'
short_description: 'Handle sensitive cardholder data on your own PCI DSS compliant server.'
url: '/features/handling-cardholder-data/'
aliases:
    - /payments/features/server-to-server/
    - /payments/features/server-to-server/payment-flow/
    - /features/server-to-server/payment-flow/
    - /features/server-to-server/about/
    - /payments/features/server-to-server/about/
    - /payments/features/server-to-server/activation/
    - /features/server-to-server/activation/
    - /payments/features/server-to-server/integration/
    - /features/server-to-server/integration/
    - /features/server-to-server/
---
When you accept credit and debit card payments using a [MultiSafepay payment page](/payment-pages/) or [Payment Component](/payment-components/), MultiSafepay handles the sensitive cardholder data, including:

- Primary account number (PAN)
- Cardholder name
- Service code
- Expiry date

We bear the risk and responsibility for [PCI&nbsp;DSS compliance](/payment-regulations/pci-dss/). 

Alternatively, you can collect cardholder data through other means. Because you will then handle sensitive data on your own server before sending it to MultiSafepay, you must also have PCI DSS certification. 

You are responsible for arranging certification, which is a complex, time-consuming, and expensive process. Consider carefully if this makes sense for your business model. 

For more information and advice, email <sales@multisafepay.com>

## Activation

**1.** To check your eligibility to use this feature, email <sales@multisafepay.com>

**2.** We check your account and company performance.

**3.** Email proof of your PCI DSS certification and an activation request to <risk@multisafepay.com>

**4.** If approved, we complete activation. 

## Supported payment methods and 3D Secure requirements

The table below sets out supported payment methods and [3D Secure](/features/3d-secure/about/) requirements:

| Card | Authentication protocol |
|---|---|
| American Express | American Express Safekey – mandatory except for transactions less than 30 EUR |
| Bancontact | 3D Secure only |
| Maestro | 3D Secure only |
| Mastercard | Mastercard SecureCode **and** non-3D Secure payments |
| Visa | Verified by Visa **and** non-3D Secure payments |

## Integration

See API reference – [Credit card: Direct](/api/#credit-card--direct).


