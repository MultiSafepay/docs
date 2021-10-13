---
title: 'Recurring payments'
weight: 30
meta_title: "Recurring payments - MultiSafepay Docs"
layout: 'single'
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
logo: '/svgs/Tokenization.svg'
short_description: 'Store payment details to make checkout more convenient.'
url: '/features/recurring-payments/'
aliases: 
    - /tools/tokenization/how-do-i-get-tokenization/
    - /tools/tokenization/tokenization-api-level/
    - /tools/tokenization/tokenization-via-api/
    - /tools/tokenization/tokenization-available-for-plugins/
    - /payments/features/tokenization/
---

To process recurring payments, MultiSafepay encrypts the customer's sensitive payment details from an initial transaction as a secure, non-sensitive token. For subsequent payments, the customer can select stored details for faster and easier checkout. This is also known as tokenization. 

**Benefits**

- Subsequent payments are exempt from [SCA and 2FA](/payment-regulations/sca/).
- MultiSafepay assumes responsibility for compliant storage of payment details. 
- Customers can store multiple tokens.

**Uses** 

- Easily manage recurring payments and subscriptions. 
- Payment details can autofill at checkout.

{{< details title="Supported payment methods" >}}

- American Express
- Bancontact
- iDEAL
- Maestro
- Mastercard
- SEPA Direct Debit
- Sofort
- Visa

{{< /details >}}

## Recurring models
MultiSafepay offers three recurring models:

- **Card on file (COF)**: The cardholder has authorized you to store their card details.
- **Subscription**: An agreement or services that are billed at the end of your billing cycle, e.g. weekly, monthly.
- **Unscheduled**: Event-triggered, e.g. mobile top-up when no credit left on the phone.

Our [SDKs](/developer/wrappers/) support all three models. Our [plugins](/payments/integrations/) use COF only. 

## Via our API
See API reference – [Recurring payments](/api/#recurring-payments-orders).

**Note:** Tokens for SEPA Direct Debit "DIRDEB" transactions are originally received as iDEAL or Sofort transactions. 

{{< details title="Additional parameters" >}}

| Parameter | Type | Description |
|---|---|---|
| `type` | string | The payment flow for the checkout process. Options: `direct`, `redirect`. |
| `gateway` | string | The unique `gateway_id` to redirect the customer to the specific payment method. Retrieve gateways using a `GET /gateway` request. {{< br >}} Options: `AMEX`, `VISA`, `MASTERCARD`, `DIRDEB`. |
| `recurring_id` | string | A randomly generated recurring ID for the customer. |
| `reference` | string | The customer's reference number for the token. |
| `recurring_model` | string | The type of recurring model to use. Options: `unscheduled`, `cardOnFile`, `subscription`.  |

{{< /details >}}

## Via plugins

Make sure you have enabled credit card payments and recurring payments in your MultiSafepay account.

Email requests to your account manager at <sales@multisafepay.com>

{{< details title="Supported MultiSafepay plugins" >}}

We support recurring payments in our plugins for:

- [Magento 1](/payments/integrations/ecommerce-platforms/magento1)
- [Magento 2](/payments/integrations/ecommerce-platforms/magento2)
- [PrestaShop 1.6](/payments/integrations/ecommerce-platforms/prestashop-1-6)
- [PrestaShop 1.7](/payments/integrations/ecommerce-platforms/prestashop-1-7)
- [Shopware 6](/payments/integrations/ecommerce-platforms/shopware6) 
- [Woocommerce](/payments/integrations/ecommerce-platforms/woocommerce/) 

{{< /details >}}

