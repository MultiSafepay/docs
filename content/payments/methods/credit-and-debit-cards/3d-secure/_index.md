---
title: '3D Secure 2.0'
weight: 40
meta_title: "3D Secure 2.0 - MultiSafepay Docs"
logo: '/svgs/Flexible 3D alt.svg'
layout: 'single'
short_description: "Manage 3D Secure authentication for card payments."
url: '/cards/3ds2/'
aliases: 
    - /faq/risk-and-fraud/
    - /features/3d-secure/
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
    - /tools/server2server/3d-dynamics
    - /features/3d-secure/flexible/
    - /features/3d-secure/dynamic/
---

3D Secure 2.0 (3DS2) is an authentication protocol card schemes use to verify cardholder identity for online credit and debit card payments. Under [PSD2](/payment-regulations/psd2/), MultiSafepay is required to apply it to **all** Europe-based card payments, and we enable it by default for non-EU payments as well. 

3DS2 provides an extra layer of security and helps reduce fraud-related [chargebacks](/chargebacks/). If a transaction is successfully authenticated using 3DS2, the card scheme is responsible for chargeback costs instead of you.

## How it works

**1.** The cardholder enters their payment details and is redirected to the card scheme to authenticate using their branded version of 3DS2: 

- American Express Safekey
- Mastercard SecureCode
- Verified by Visa

**2.** Contextual information from the customer's device (fingerprint) is shared with you and the scheme to conduct a risk assessment, e.g.:

- Transaction value
- New or existing customer
- Customer's location and/or transaction history

**3.** You and the scheme each decide whether to request additional authentication:

- **Frictionless flow:** The transaction appears legitimate and is authorized without further user-side authentication. 
- **Challenge flow:** The transaction appears risky and the cardholder is asked to provide additional authentication, e.g. password, SMS code, fingerprint.

## Exemptions

To help you optimize conversion and manage risk, MultiSafepay supports exemptions from 3DS2 and [strong customer authentication](/payment-regulations/psd2/) (SCA). Under the PSD2, some exemptions are only supported **outside** of Europe.

{{< alert-notice >}} Exemptions remove an important layer of security and increase the risk of fraud. You are then liable for any fraud-related chargebacks. {{< /alert-notice>}}

### Merchant-initiated transactions

Merchant-initiated transactions are [recurring payments](/features/recurring-payments) initiated by the merchant on behalf of the customer, based on a prior agreement. Examples of merchant-initiated transactions include subscription payments and automatic balance top-ups. 

Merchant-initiated transactions do not require 3D Secure 2.0 authentication.

### Mail Order/Telephone Order (MOTO)
 
For [MOTO](https://docs.multisafepay.com/features/moto/) payments, the customer provides their card details to the merchant over the phone or by email. These payments do not require 3D Secure 2.0 authentication. 
### Transaction risk analysis

MultiSafepay can conduct a transaction risk analysis (TRA) for specific transactions for amounts up to EUR&nbsp;500. The issuer may soft decline the exemption, in which case the customer is automatically redirected to authenticate. 

| | |
|---|---|
| **Scope** | All EU and non-EU cards  |
| **Pricing** | Free |
| **Activation** | Email <sales@multisafepay.com> |

### Low value payments

We will soon support exemptions for low value payments (LVP) under 30&nbsp;EUR.

## Solutions

### Disabling 3DS2
MultiSafepay can disable 3DS2 for all your card payments.   

| | |
|---|---|
| **Scope** | Non-EU cards only |
| **Pricing** | Free |
| **Activation** | Email risk@multisafepay.com |

### Dynamic 3D

Dynamic 3D is a MultiSafepay solution that lets you set rules to disable 3DS2 per transaction, e.g. based on amount, or card/customer/IP country.

| | |
|---|---|
| **Scope** | Non-EU cards only |
| **Pricing** | MultiSafepay applies a different fee to non-3DS2 transactions. We&nbsp;may also charge a fee to implement Dynamic 3D. <br>To confirm pricing, email <sales@multisafepay.com> |
| **Activation** | Email <sales@multisafepay.com> {{< details title="Provide required information" >}} - State why you want to use Dynamic 3D. {{< br >}} - Provide evidence of significant volumes of non-EU card payments. {{< br >}} - Specify which sites under your account this applies to. {{< br >}} - Demonstrate excellent processing performance, especially for chargebacks. {{< br >}} - Confirm that you understand the increased risk of chargebacks and accept liability for non-payment after shipment, and the pricing structure. {{< /details >}} |

### Flexible 3D 

Flexible 3D is a MultiSafepay solution that lets you enable and disable 3DS2 per transaction via our API. 

| | |
|---|---|
| **Scope** | Non-EU cards only |
| **Prerequisites** | You must be certified to [handle cardholder data](/features/handling-cardholder-data/). |
| **Activation** | Email risk@multisafepay.com |
| **Integration** | See API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Card order. <br> Set the `type` parameter to `direct`. <br> Include the customer fingerprint data. |

