---
title: 'Self-hosted credit card payments'
weight: 50
layout: single
meta_title: "Self-hosted credit card payments - MultiSafepay Docs"
logo: '/svgs/Server to server.svg'
childlist: '.'
short_description: 'Accept credit card payments in your checkout.'
url: '/features/self-hosted-credit-card-payments/'
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

The usual way of processing credit card payments is to redirect customers to a [MultiSafepay payment page](/payment-pages/). In this case, MultiSafepay is responsible for handling customers' sensitive credit card payment details. Our server is fully [PCI DSS compliant](/payment-regulations/pci-dss/). 

If you want to avoid redirecting customers to a MultiSafepay payment page to reduce friction and increase conversion, you can:

- Use a [payment component](/payment-components/), where MultiSafepay remains responsible for PCI DSS compliance.
- Host credit card payments yourself. 

Self-hosting means the customer enters their sensitive payment details in a form in your checkout. You handle the unencrypted sensitive data on your own server before sending it to MultiSafepay to process payment. Therefore, your server must also be PCI DSS certified. You are responsible for arranging certification and bear the risk of handling sensitive data.

## Supported payment methods and 3D Secure requirements

The table below sets out supported payment methods and [3D Secure](/features/3d-secure/about/) requirements:

| Card | Supports |
|---|---|
| American Express | American Express Safekey, which is mandatory except for transactions less than 30 EUR |
| Bancontact | 3D Secure only |
| Maestro | 3D Secure only |
| Mastercard | Mastercard SecureCode **and** non-3D Secure payments |
| Visa | Verified by Visa **and** non-3D Secure payments |

## Activation

**1.** To check your eligibility with MultiSafepay, email <sales@multisafepay.com>

**2.** Once you are PCI DSS certified, email a request to activate self-hosted credit card payments to the Risk Team at <risk@multisafepay.com>

**3.** The Risk Team checks your account and company performance and, if approved, completes activation. 

## Integration

See API reference – [Self-hosted credit card payments](/api/#self-hosted-credit-card-payments).

Once the customer has successfully passed 3D Secure authentication and completed payment, we send **Completed** [transaction status](/about-payments/multisafepay-statuses/) to your [backend](/glossaries/multisafepay-glossary/#backend) via the [notification_url](/developer/api/notification-url/).

