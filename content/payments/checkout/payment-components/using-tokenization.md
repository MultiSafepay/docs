---
title : "Using tokenization"
meta_title: "Payment Components - Using tokenization - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: 'single'
read_more: '.'
weight: 4
---
Tokenization lets you store a customer's payment details as a secure, encrypted token to make subsequent payments faster and easier. 

- Reduce cost and risk by shifting responsibility for storing payment details and [PCI DSS compliance](/faq/general/multisafepay-glossary/#payment-card-industry-data-security-standard-pci-dss) to MultiSafepay.
- Improve checkout experience and increase conversion:
    - Customers don't need to re-provide payment details, which autofill at checkout.
    - Subsequent payments are exempt from [SCA requirements](/payment-regulations/sca/) and can skip two-factor authentication.

## How it works

{{< details title="First-time customer" >}}

{{< screen src="/img/First-timeCustomer.png" align="center" class="medium-img desktop-radius" >}}

{{< /details >}}

{{< details title="Returning customer" >}}
&nbsp;  
{{< /details >}}

## Creating tokenziation requests

To make a POST /orders request with tokenziation enabled, see API reference – [Payment Component order](/api/#payment-component-order).

{{< two-buttons href-1="/payments/checkout/payment-components/" header-1="Overview" text-1="Payment Components" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" >}}