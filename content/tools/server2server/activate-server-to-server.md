---
title: "Activate Server to Server credit card payments"
weight: 72
meta_title: "Server to Server, how to active it? - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
---

>_Before you proceed with processing direct credit card transactions, check with your account manager at MultiSafepay if you are eligible for the payment method_. 

## Activation and requirements

In order to process direct credit card transactions, the following is required of the merchant:

1. Register for a [MultiSafepay Control](https://merchant.multisafepay.com/signup) account.
2. Make sure you are [PCI](/faq/risk-and-fraud/what-do-i-need-to-know-about-credit-card-payments) compliant. To request approval and enable this feature, email the Risk Team at <risk@multisafepay.com>
3. We will check your merchant file and company performance. If approved, the Integration Team will integrate Server to Server.
4. Once activated, integrate with MultiSafepay via JSON [API](/api/#server-to-server) following these instructions.
5. Credit card payments are [3D Secure](/faq/general/glossary/#3d-secure) enabled by default, in line with PSD2 regulations. If you operate outside of Europe and require a more flexible setup, email your account manager at <sales@multisafepay.com>

>_All options require approval and enabling by our Risk Team_.

## 3D Secure Processing

3D Secure is a protocol designed to reduce fraud and chargebacks during ecommerce Internet transactions. Cardholders are redirected during the payment process to their issuing bank in order to identify themselves before the purchase can be completed. This usually means entering a PIN or a password after entering their card details. In the event of a dispute with the transaction at a later date, the card issuer will usually take responsibility of the chargeback instead of the merchant. This only applies for charges with no authorization and/or fraud, not for situations where the product is not delivered or where customer is dissatisfied with the quality of the order.

The liability issues involved with 3D Secure transactions are outside of the scope of this document. For a detailed indication of the liabilities involved, contact our Risk Team at <risk@multisafepay.com>

>_MultiSafepay only supports Mastercard Secure Code, Verified by Visa, American Express Safekey and Bancontact 3D_.
