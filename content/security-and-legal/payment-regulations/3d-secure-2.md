---
title : "3D Secure 2.0"
weight: 40
meta_title: "Payment regulations - 3D Secure 2.0 - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/payment-regulations/3D-secure
    - /payment-methods/credit-and-debit-cards/creditcards/what-is-3d-secure/
    - /faq/general/what-is-3d-secure
    - /faq/payment-regulations/about-3d-secure/
    - /faq/payment-regulations/3d-secure-2
---
We are working on supporting 3DS 2.0 and we expect to rollout the support in 2021. In the meantime, transactions use 3DS 1.0 and are fully PSD2 compliant.

3DS 2.0 aims to provide better security and greater customer experience than its predecessor. This is achieved through the collection of more contextual data from the customer. The contextual data is used 'behind-the-scenes' to verify the identity of the customer. This reduces the complexity of the check-out flow, resulting in higher conversion and lower cart abandonment.

Based on the risk level of the transaction, two flows can emerge: the *frictionless flow* and *challenge flow*. Both flows start after the customer has provided his or her card information. Along with the card information, contextual information from the customer's device is shared with the issuer and merchant to make an informed decision as to request additional authentication or not.

{{< responsive_svg src="/diagrams/svg/3DS-flow" alt="3D Secure Flow" align="center" title="3DS Flow">}}

Examples of data used for risk assessment include:

* The value of the transaction
* New or existing customer
* Transactional history
* Location of customer

If the contextual data indicates a legitimate transaction, the payment is verified without further user-side authentication. This is also called a frictionless flow. In case the contextual data include abnormalities, the customer is asked to provide additional authentication (e.g. through password, code via SMS or fingerprint).
