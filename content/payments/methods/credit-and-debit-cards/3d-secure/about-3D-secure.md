---
title : "About 3D Secure 2.0"
weight: 10
meta_title: "3D Secure 2.0 - MultiSafepay Docs"
read_more: "."
url: '/cards/3ds2/about/'
aliases:
    - /faq/payment-regulations/3D-secure
    - /payment-methods/credit-and-debit-cards/creditcards/what-is-3d-secure/
    - /faq/general/what-is-3d-secure
    - /faq/payment-regulations/about-3d-secure/
    - /security-and-legal/payment-regulations/about-3d-secure/
    - /faq/payment-regulations/3D-secure
    - /payment-methods/credit-and-debit-cards/creditcards/what-is-3d-secure/
    - /faq/general/what-is-3d-secure
    - /faq/payment-regulations/about-3d-secure/
    - /faq/payment-regulations/3d-secure-2
    - /features/3d-secure/versions/
    - /features/3d-secure/about/
    - /features/3d-secure/about/
---

3D Secure 2.0 (3DS2) is an authentication protocol card schemes use to verify a cardholder's identity for online credit and debit card payments. It is enabled by default for all (EU and non-EU) card payments. 

Under [PSD2](/payment-regulations/psd2/), MultiSafepay is required to apply 3DS2 authentication to all Europe-based credit card payments.

3DS2 provides an extra layer of security and helps reduce [fraud-related chargebacks](/chargebacks/minimizing/). If a customer requests a [chargeback](/chargebacks/) due to fraud after the transaction passed 3DS2 authentication, the card scheme is responsible for the costs instead of you.

## How it works

**1.** The cardholder provides their cardholder data and is redirected to the card scheme to authenticate using their branded version of 3DS2:

- American Express Safekey
- Mastercard SecureCode
- Verified by Visa

**2.** Contextual information from the customer's device (fingerprint) is also shared with you and the scheme to conduct a risk assessment, e.g.:

- Transaction value
- New or existing customer
- Customer's location and/or transaction history

**3.** You and the scheme each make an informed decision about whether to request additional authentication:

- **Frictionless flow:** The transaction appears legitimate and is authorized without further user-side authentication. 
- **Challenge flow:** The transaction appears risky and the customer is asked to provide additional authentication, e.g. password, SMS code, fingerprint.

{{< responsive_svg src="/diagrams/svg/3DS-flow" alt="3D Secure Flow" align="center" title="3D Secure 2.0 flow">}}

