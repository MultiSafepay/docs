---
title : "About 3D Secure"
weight: 10
meta_title: "Payment regulations - About 3D Secure - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: "."
url: '/features/3d-secure/about/'
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
---

3D Secure is an authentication protocol for online credit and debit card payments. It provides an extra layer of security and prevents [fraud-related chargebacks](/payments/chargebacks/minimizing/). After entering their credit card details, customers are redirected to the card scheme to verify their identity, before completing payment.

If a customer requests a [chargeback](/payments/chargebacks/) due to fraud after the transaction passed 3D&nbsp;Secure authentication, the card scheme is responsible for the costs instead of you.

MultiSafepay is required under the Payment Services Directive 2 ([PSD2](/payment-regulations/psd2/)) to apply 3D&nbsp;Secure to all Europe-based credit card payments.

## How it works

**1.** The customer provides their card information and is redirected to the card scheme to verify their identity:

- American Express Safekey
- Mastercard SecureCode
- Verified by Visa

**2.** Contextual information from the customer's device is also shared with you and the scheme to conduct a risk assessment, e.g.:

- Transaction value
- New or existing customer
- Customer's transaction history
- Customer's location

**3.** You and the scheme each make an informed decision about whether to request additional authentication:

- **Frictionless flow:** The transaction appears legitimate and is authorized without further user-side authentication. 
- **Challenge flow:** The transaction appears risky and the customer is asked to provide additional authentication, e.g. password, SMS code, fingerprint.

{{< responsive_svg src="/diagrams/svg/3DS-flow" alt="3D Secure Flow" align="center" title="3D Secure 2.0 flow">}}

## See also

- [Dynamic 3D Secure](/features/3d-secure/dynamic/)
- [Flexible 3D](/features/flexible-3d/)
