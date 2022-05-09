---
title : "Exemptions from 3DS2 and SCA"
weight: 20
meta_title: "Exemptions from 3DS2 and SCA - MultiSafepay Docs"
read_more: "."
url: '/features/3ds2/exemptions/'
aliases:
    - /tools/server2server/3d-dynamics
    - /features/3d-secure/flexible/
    - /features/3d-secure/dynamic/
---

To help you optimize conversion and manage risk, MultiSafepay supports several exemptions from [3D Secure 2.0](/features/3d-secure/about/) (3DS2) and [strong customer authentication](/payment-regulations/psd2/) (SCA).

Under the [PSD2](/payment-regulations/psd2/), some exemptions are only supported **outside** of Europe.

{{< alert-notice >}} **Important:** Exemptions remove an important layer of security and increase the risk of fraud. You bear the risk and become liable for any [fraud-related chargebacks](/chargebacks/). {{< /alert-notice>}}

## Transaction risk analysis

MultiSafepay can conduct a transaction risk analysis (TRA) for specific transactions for amounts up to EUR&nbsp;500. The issuer may soft decline the exemption, in which case the customer is automatically redirected to authenticate. 

| | |
|---|---|
| **Scope** | All cards within and outside EU  |
| **Pricing** | Free |
| **Activation** | Email <sales@multisafepay.com> |

## Disabling 3DS2
MultiSafepay can disable 3DS2 for all your card payments.   

| | |
|---|---|
| **Scope** | **Non-EU cards** only |
| **Pricing** | Free |
| **Activation** | Email risk@multisafepay.com |

## Dynamic 3D

Dynamic 3D is a MultiSafepay solution that lets you set rules to disable 3DS2 per transaction, e.g. based on amount, or card/customer/IP country.

| | |
|---|---|
| **Scope** | **Non-EU cards** only. |
| **Pricing** | MultiSafepay applies a different fee to non-3DS2 transactions. We&nbsp;may also charge a fee to implement Dynamic 3D. <br>To confirm pricing, email <sales@multisafepay.com> |
| **Activation** | Email <sales@multisafepay.com> |
| | - State why you want to use Dynamic 3D. |
| | - Provide evidence of significant volumes of non-EU card payments. |
| | - Specify which sites under your account this applies to. |
| | - Demonstrate excellent processing performance, especially for chargebacks. |
| | - Confirm that you understand the increased fraud risk, and the pricing structure. |

## Flexible 3D 

Flexible 3D is a MultiSafepay solution that lets you enable and disable 3DS2 per transaction via our API. 

| | |
|---|---|
| **Scope** | **Non-EU cards** only. |
| **Prerequisites** | You **must** be certified to [handle cardholder data](/features/handling-cardholder-data/). |
| **Activation** | Email risk@multisafepay.com |
| **Integration** | See API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Card order. <br> Set the `type` parameter to `direct`. <br> Include the customer fingerprint data. |

## Coming soon

MultiSafepay will soon support exemptions for low value payments (LVP) under 30&nbsp;EUR.