---
title: 'Tokenization'
weight: 90
meta_title: "Tokenization - MultiSafepay Docs"
layout: 'single'
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: '/svgs/Tokenization.svg'
short_description: 'Store credit card information as a token allowing customers for a more convenient checkout.'
aliases: 
    - /tools/tokenization/how-do-i-get-tokenization/
    - /tools/tokenization/tokenization-api-level/
    - /tools/tokenization/tokenization-via-api/
    - /tools/tokenization/tokenization-available-for-plugins/
---

Tokenization is substituting sensitive customer payment details with a non-sensitive token to reduce risk. For example, a unique recurring ID is created to replace credit card details, which is encrypted as a unique string of numbers that is automatically issued in real-time. The token is used online in approved environments to complete the payment. 

Customers can complete payments in one step by selecting the stored token in their account. Customers may have multiple tokens.

Tokenization is mainly used for credit card, recurring, and subscription payments, but is also available for bank payment methods. 

{{< details title="Supported payment methods" >}}

- Visa
- Mastecard
- Maestro
- Amex
- iDEAL
- SOFORT Banking
- Direct debit

{{< /details >}}

## Via API
To use tokenization via our API, see API Reference – [Tokenization and recurring model](/api/#recurring-payment).

**Note:** Tokens for SEPA Direct Debit "DIRDEB" transactions are originally received as iDEAL or SOFORT Banking transactions. 

{{< details title="Additional request parameters" >}}

| Parameter | Type | Description |
|---|---|---|
| `type` | String | Specifies the payment flow for the checkout process. Options: Direct, Redirect |
| `gateway` | String | The unique `gateway_id` to redirect the customer to the specific payment method. Retrieve gateways using a GET `/gateway` request. {{< br >}} Options: AMEX, VISA, MASTERCARD and DIRDEB |
| `recurring_id` | String | A randomly generated recurring ID for the customer. |
| `reference` | String | The customer's reference number for the token. |
| `recurring_model` | String | The type of recurring model to use. {{< br >}} Options: unscheduled, cardOnFile, subscription  |

{{< /details >}}

## Via plugins

Make sure you have enabled credit card payments and Recurring Payments in your MultiSafepay account.

Email your request to enable tokenization to your account manager at <sales@multisafepay.com>

{{< details title="Supported MultiSafepay plugins" >}}

We support tokenization in our plugins for:

- [Magento 1](/integrations/ecommerce-integrations/magento1)
- [Magento 2](/integrations/ecommerce-integrations/magento2)
- [PrestaShop 1.6](/integrations/ecommerce-integrations/prestashop-1-6)
- [PrestaShop 1.7](/integrations/ecommerce-integrations/prestashop-1-7)
- [Shopware 6](/integrations/ecommerce-integrations/shopware6) 
- [Woocommerce](/integrations/ecommerce-integrations/woocommerce/) 

{{< /details >}}

