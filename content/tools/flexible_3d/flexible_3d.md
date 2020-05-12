---
title: "Flexible 3D"
weight: 11
meta_title: "Flexible 3D - MultiSafepay Support"
meta_description: "Flexible 3D is a feature that allows you to enable/disable 3D secure at an API level. The Flexible 3D forces whether or not to complete a transaction with the 3D secure verification."
read_more: '.'
---

## What it is

Flexible 3D is a feature that allows you to enable/disable 3D Secure at an API level. The Flexible 3D forces whether or not to complete a transaction with the 3D secure verification.

[3D secure, What it is](/faq/general/what-is-3d-secure/)

## How it works

[Fraud related chargebacks](/faq/chargebacks/what-is-a-chargeback/) can be avoided altogether by using 3D Secure, given the extra layer of security imposed by the cardholder needing to identify him or herself. Fraud-based chargebacks are no longer possible when using the 3D secure.

**Example 1:**  
Credit card transactions which are processed with the 3D Secure verification, require a form of authentication of the customer during a payment process. When the 3D secure is required upon releasing a payment, setting the Flexible 3D to _false_, will disable the 3D secure verification process. Resulting in releasing a payment that is **"Not Enrolled, Liability".**

**Example 2:**   
When Flexible 3D is set on _true_, the verification is mandatory to finalize and release a successful payment. Credit card transactions which were originally processed without the 3D Secure protocol are now required to complete the 3D Secure verification too. By enforcing this measure - finalizing the payment only upon completing the 3D Secure verification - all released payments will be enrolled with the 3D authentication. **3D Secure Result: Enrolled Liability**

**Flexible 3D Secure and Dynamic 3D Secure settings**
Activating Flexible 3D secure will override the rules of the Dynamic 3D settings. For more information about Dynamic 3D Secure, please refer to the page, [Dynamic 3D, What it is](/tools/server2server/3d-dynamics/)

## Available for?

Flexible 3D is a feature that allows you to enable/disable 3D secure at an API level. 

For Full API calls on [Flexible 3D](/api/#flexible-3d), please refer to the API section on our documentation.

| Parameter                      | Type      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| type               | string |  Specifies the payment flow for the checkout process. Options: redirect and direct. |
| gateway            | string | The unique gateway_id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Option: VISA and MASTERCARD. |
| 

An extra step is required when processing a direct credit card transactions. Because a direct "server to server" credit card payment takes place on the checkout page of the webshop instead of on the payment page of MultiSafepay, it is up to the merchant to refer the customer to the verification page to complete the payment.

#### Complete callback

| Parameter                      | Type      | Description |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| reference_id      | string | Authorise 3D response reference_id |
| MD                | string | Authorise 3D response MD  |
|








