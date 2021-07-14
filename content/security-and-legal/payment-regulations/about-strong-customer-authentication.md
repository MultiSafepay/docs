---
title : "About strong customer authentication"
weight: 20
meta_title: "Payment regulations - About strong customer authentication - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/payment-regulations/strong-customer-authentication
    - /faq/payment-regulations/about-strong-customer-authentication
---

### What is SCA?

Since September 2020, European regulation rules require __Strong Customer Authentication (SCA)__ for most European online payments. This translates to businesses and payment service providers being required to verify customer purchases for transactions through a process called __Two Factor Authentication (2FA)__. Three methods of authentication are recognized in SCA. Every SCA compliant transaction uses at least two out of three methods.

{{< responsive_svg src="/diagrams/svg/SCA" alt="Strong Customer Authetication methods" title="Strong Customer Authentication" align="center" >}}

If these measures are not taken, banks may be forced to decline transactions that do not implement this type of authentication. The impact of SCA will depend on _when_ your business charges customers. For businesses such as ecommerce stores that charge customers when they are in the checkout flow, customers can simply authenticate while completing a payment for a purchase.

A downside to this type of authentication may lead to lower conversion rates for example; hotels, crowd funding campaigns and subscription services who have built their checkout flow to save payment details for future use. In these scenarios, customers may have to re-authenticate purchases being made with a stored card by returning to a website or app.

### Why do I need SCA for my business?

Many businesses in today's world experience financial and data fraud, therefore data such as personal information is constantly under attack. Techniques such as phishing and keystroke logging are used to steal passwords and other sensitive data such as credit card information.

With the introduction of Strong Customer Authentication (SCA) and Two-factor Authentication (2FA), transactions can be completed easily, quickly and cost-effectively to ensure that a customers' identity is verified, thus reducing the risk of fraud.

### When will SCA come into effect?

The deadline to be SCA compliant is __01-01-2021__, whereby you are expected to have implemented the necessary authentication requirements for your business. MultiSafepay will provide support for this process.


### What impact does SCA have on my business?

There will be no significant changes or impact to your business. Your configuration within your MultiSafepay account will remain the same unless you have Server-to-Server enabled. Be rest assured that MultiSafepay will take care of the rest to ensure the process runs smoothly.

Customers may encounter 2FA for payment methods which do not already have it enabled during checkout, therefore an additional step will be required for a customer when completing a payment.

### What are the exemptions?

Subscriptions and recurring transactions will be exempt to the SCA requirements. Although, this is only possible after an initial transaction has been authenticated successfully by SCA.

Low value orders will also be exempt once 3D Secure 2.0 is widely adopted. For more information or to apply, email the Integration Team at <integration@multisafepay.com>

Read more about [3D Secure 2.0](/faq/payment-regulations/3d-secure)
