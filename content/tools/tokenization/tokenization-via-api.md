---
title : "Tokenization via API"
weight: 91
meta_title: "Tokenization via API Reference - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
aliases:
    - /tools/tokenization/tokenization-api-level/
---

To use tokenization via our API, see API Reference – [Tokenization and recurring model](/api/#tokenization-recurring-model).

| Parameter | Type | Description |
|---|---|---|
| `type` | String | Specifies the payment flow for the checkout process. Options: Direct, Redirect |
| `gateway` | String | The unique `gateway_id` to redirect the customer to the specific payment method. Retrieve gateways using a GET `/gateway` request. {{< br >}} Options: AMEX, VISA, MASTERCARD and DIRDEB |
| `recurring_id` | String | A randomly generated recurring ID for the customer. |
| `reference` | String | The customer's reference number for the token. |
| `recurring_model` | String | The type of recurring model to use. {{< br >}} Options: unscheduled, cardOnFile, subscription  |

**Note:** Tokens for SEPA Direct Debit "DIRDEB" transactions are originally received as iDEAL or SOFORT Banking transactions. 




