---
title : "Dynamic 3D Secure"
weight: 60
meta_title: "Payment regulations - Dynamic 3D Secure - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
url: '/payment-regulations/dynamic-3d'
aliases:
    - /tools/server2server/3d-dynamics
---

[3D Secure](/security-and-legal/payment-regulations/about-3d-secure/) is enabled by default for all credit card payments. 

Dynamic 3D Secure lets you set rules to disable 3D Secure authentication for certain credit card payments, e.g. based on:

- Transaction amount
- Country, e.g. card country, IP country, customer country

The most common reason for disabling 3D Secure is if you have lots of customers outside Europe who don't have access to it. Consider setting a rule for transactions with a non-European card and a billing address outside of Europe.

## Increased risk of fraud

Removing the layer of security provided by 3D Secure increases the risk of fraud. Liability doesn't change for payments processed without 3D Secure. Also, banks don't accept liability for fraudulent transactions so you bear the risk of chargebacks.

## Fees
A different fee applies to non-3D Secure transactions. We may also charge a fee for implementing Dynamic 3D Secure. 

## Applying for Dynamic 3D Secure
To apply to use Dynamic 3D Secure, email sales@multisafepay.com

You must:

- State why you want to use Dynamic 3D Secure.
- Provide evidence that you process a significant volume of transactions for customers outside of Europe.
- Confirm that you understand the increased fraud risk and the fee structure.
- Specify which sites in your MultiSafepay Control to apply the rule to.
- Confirm you have excellent processing performance, especially for chargebacks.