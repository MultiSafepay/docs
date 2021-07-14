---
title : "About 3D Secure"
weight: 30
meta_title: "Payment regulations - About 3D Secure - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/payment-regulations/3D-secure
    - /payment-methods/credit-and-debit-cards/creditcards/what-is-3d-secure/
    - /faq/general/what-is-3d-secure
    - /faq/payment-regulations/about-3d-secure/
---

3D Secure is an authentication protocol for online credit and debit card payments. It provides an extra layer of security and prevents [fraud-related chargebacks](/payments/methods/credit-and-debit-cards/user-guide/minimizing-chargebacks/). After entering their credit card details, customers are redirected to the card scheme to verify their identity, before completing payment.

The major credit card schemes each offer their own branded version of 3D Secure:

- American Express Safekey
- Mastercard SecureCode
- Verified by Visa

If a customer requests a [chargeback](/faq/chargebacks/about-chargebacks/) due to fraud and the transaction passed 3D Secure authentication, the acquirer is then responsible for the costs instead of the merchant.

## PSD2 requirements

Under the Payment Services Directive 2 ([PSD2]((/faq/payment-regulations/payment-service-directive-2))), MultiSafepay is required to apply the 3D Secure protocol to all Europe-based credit card payments we process.

The PSD2 is a set of laws and regulations that aims to improve European consumer rights while promoting competition within the financial industry. 

One of the requirements of PSD2 is Strong Customer Authentication [(SCA)](/faq/payment-regulations/strong-customer-authentication). SCA combines two forms of authentication to reduce the risk of fraud. 3D Secure is a widely implemented form of SCA that complies with PSD2 regulations.