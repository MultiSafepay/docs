---
title: 'Handling cardholder data'
category: 6298bd782d1cf4006032e765
order: 202
hidden: false
parentDoc: 62a727569e389a012f577acd
excerpt: Handle sensitive cardholder data on your PCI DSS compliant server.
slug: handling-cardholder-data
---
When you accept credit and debit card payments using a [payment page](/payment-pages/) or [payment component](/payment-components/), MultiSafepay handles the sensitive cardholder data, including:

- Primary account number (PAN)
- Cardholder name
- Service code
- Expiry date

We bear the risk and responsibility for [PCI DSS compliance](/payment-regulations/pci-dss/). 

Alternatively, you can collect cardholder data through other means. Because you will then handle sensitive data on your own server before sending it to MultiSafepay, you must also have PCI DSS certification. 

You are responsible for arranging certification, which is a complex, time-consuming, and expensive process. Consider carefully if this makes sense for your business model. 

# Activation

1. To check your eligibility to use this feature, email <sales@multisafepay.com>
Specify in your request:
    - The payment methods you want to integrate
    - The websites under your account this applies to
    - The type of products you will sell  
    - Your average order values and volumes, and any available processing statements. 
2. We check your account and company performance.
3. Email proof of your PCI DSS certification and an activation request to <risk@multisafepay.com>
4. If approved, we complete activation.

# Integration

See API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Card order.
Set `type` to `direct`.

#### Supported payment methods 

The table below sets out supported payment methods and their respective [3D Secure](/cards/3ds2/) authentication requirements:

| Card | Authentication protocol |
|---|---|
| American Express | American Express Safekey – mandatory for transactions above 30 EUR |
| Bancontact | 3D Secure only |
| Maestro | 3D Secure only |
| Mastercard | Mastercard SecureCode **and** non-3D Secure payments |
| Visa | Verified by Visa **and** non-3D Secure payments |

# Maintenance

You must provide us with your:

- Attestation of Compliance each year
- Approved Scanning Vendor reports every 3 months
<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>
