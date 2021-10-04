---
title : "Using tokenization"
meta_title: "Payment Components - Using tokenization - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: 'single'
draft: 'true'
read_more: '.'
weight: 4
url: '/payment-components/tokenization/'
---

### New customer

{{< mermaid class="text-center" caption="How it works: New customer" >}}
sequenceDiagram
    autonumber
    participant C as Customer
    participant EI as Your ecommerce integration
    participant PC as Payment Component
    participant S as Your server
    Participant M as MultiSafepay
    
    EI->>PC: Passes the customer reference in the preOrder object
    PC->>M: Requests tokens
    M->>PC: Responds: no tokens found
    C->>PC: Provides payment details
    PC->>S: Passes payment details
    S->>M: Creates order
    opt If two-factor authentication is required
        C->>M: Provides authentication
    end
    M->>S: Returns recurring_id
    S->>EI: Returns redirect_url
    EI->>C: Redirects customer to success page

{{< /mermaid >}}

### Returning customer

{{< mermaid class="text-center" caption="How it works: Returning customer" >}}
sequenceDiagram
    autonumber
    participant C as Customer
    participant EI as Your ecommerce integration
    participant PC as Payment Component
    participant S as Your server
    Participant M as MultiSafepay
    
    EI->>PC: Passes the customer reference in the preOrder object
    PC->>M: Requests tokens
    M->>PC: Provides tokens with recurring_ids
    C->>PC: Selects a tokenized payment method to pay with
    PC->>S: Passes token
    S->>M: Creates order
    M->>S: Returns response
    S->>C: Returns redirect_url
    EI->>C: Redirects customer to success page

{{< /mermaid >}}

{{< two-buttons href-1="/payment-components/" header-1="Overview" text-1="Payment Components" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" >}}