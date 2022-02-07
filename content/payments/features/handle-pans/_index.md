---
title: 'Handle PANs'
weight: 50
layout: single
meta_title: "Handle PANs - MultiSafepay Docs"
logo: '/svgs/Server to server.svg'
childlist: '.'
short_description: 'Handle credit card primary account numbers (PANs) on your own server.'
url: '/features/handle-pans/'
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
When you process credit card payments by redirecting to a [MultiSafepay payment page](/payment-pages/) or using a [Payment Component](/payment-components/), MultiSafepay handles the customer's primary account number (PAN) and other sensitive credit card data. We bear responsibility for [PCI DSS compliance](/payment-regulations/pci-dss/) and risk. 

If you are PCI DSS certified, you can self-host credit card payments and handle unencrypted card data on your own server before sending it to MultiSafepay to process payment. 

Certification is a complex, time-consuming, and expensive process. Consider carefully if this makes sense for your business model. You also bear the risk of handling sensitive data. You are responsible for arranging certification. Once certified, ask us to activate the Handle PANs feature. 

## Activation

**1.** To check your eligibility for this feature with MultiSafepay, email <sales@multisafepay.com>

**2.** Once you are PCI DSS certified, email a request to handle PANs to the Risk Team at <risk@multisafepay.com>

**3.** The Risk Team checks your account and company performance and, if approved, completes activation. 

## Supported payment methods and 3D Secure requirements

The table below sets out supported payment methods and [3D Secure](/features/3d-secure/about/) requirements:

| Card | Supports |
|---|---|
| American Express | American Express Safekey, which is mandatory except for transactions less than 30 EUR |
| Bancontact | 3D Secure only |
| Maestro | 3D Secure only |
| Mastercard | Mastercard SecureCode **and** non-3D Secure payments |
| Visa | Verified by Visa **and** non-3D Secure payments |

## Integration

See API reference – [Handle PANs](/api/#handle-pans).


