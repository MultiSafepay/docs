---
title: 'Recurring Payments'
weight: 10
meta_title: "Recurring Payments - MultiSafepay Docs"
layout: 'single'
logo: '/svgs/Tokenization.svg'
short_description: 'Boost conversion and manage subscriptions using tokenization.'
url: '/features/recurring-payments/'
aliases: 
    - /tools/tokenization/how-do-i-get-tokenization/
    - /tools/tokenization/tokenization-api-level/
    - /tools/tokenization/tokenization-via-api/
    - /tools/tokenization/tokenization-available-for-plugins/
    - /tools/recurring-payments/what-is-recurring-payments/
    - /payments/features/tokenization/
---

To process recurring payments, MultiSafepay encrypts the customer's sensitive payment details for secure storage. The encrypted payment details can be referenced through a non-sensitive identifier, also called 'token'.

In subsequent payments, tokens can be used for:

- **One-click payments**: The customer selects stored details for a frictionless checkout.
- **Subscriptions**: The merchant uses the token to schedule payments periodically.
- **Unscheduled**: The merchant uses the token for event-triggered payments e.g. toppping up an in-app balance.

### Initial payment

During the initial payment, customers are always asked to verify their identity through 3D Secure. Upon processing the payment, we encrypt the payment details for secure storage on our own servers. We return a non-sensitive token which is linked to the encrypted payment details. You can use the token to process recurring payments without needing to handle or store sensitive payment details. 

Optionally, the amount for the initial payment can be set to `0`. In this case, no funds are transferred, but if the payment details are valid, a token is created. This is also called [Zero Authorization](/features/zero-authorization/).

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Me as Merchant
    participant Mu as MultiSafepay

    C->>Me: Enters payment details, <br> verifies identity with 3D Secure
    Me->>Mu: Forwards payment details
    Mu-->>Mu: Encrypts payment details <br> for secure storage
    Mu->>Me: Returns a token <br> for future payments
    Me->>C: Redirects to success page
    C-->>Me: Funds are transferred

{{< /mermaid >}}

{{< br >}}

### Subsequent payment: customer-initiated 

For subsequent payments, the merchant displays the customer's available tokens at checkout, e.g. MASTERCARD **43. The customer selects a token and confirms payment. The merchant includes the token in the request to MultiSafepay. MultiSafepay then decrypts the payment details to process the payment.

The customer doesn't need to provide any payment details, this is also called a 'one-click payment'.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Me as Merchant
    participant Mu as MultiSafepay

    C->>Me: Signs in to their customer account <br> and places order
    Me->>C: Displays token summary at checkout <br> e.g. MASTERCARD **43
    C->>Me: Selects token and <br> confirms payment
    Me->>Mu: Places order with token
    Mu-->>Mu: Decrypts relevant payment details <br> to process payment
    Mu->>Me: Confirms successful payment
    Me->>C: Redirects to success page
    C-->>Me: Funds are transferred

{{< /mermaid >}}

{{< br >}}
{{< br >}}

### Subsequent payment: merchant-initiated 

There are two common use-cases for merchant-initiated subsequent payments: 

- Subscriptions
- Unscheduled payments

Both subscriptions and unscheduled payments require a customer's consent, but no actions. In the request to MultiSafepay, the merchant includes the relevant token. MultiSafepay then decrypts the payment details to process the payment.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Me as Merchant
    participant Mu as MultiSafepay

    C-->>Me: Provides consent for <br> merchant-initiated payments
    Me->>Mu: Places order with token
    Mu-->>Mu: Decrypts relevant payment details <br> to process payment
    Mu->>Me: Confirms successful payment
    C-->>Me: Funds are transferred

{{< /mermaid >}}

{{< br >}}
{{< br >}}

**Benefits**

- Subsequent payments are exempt from [SCA and 2FA](/payment-regulations/sca/).
- MultiSafepay assumes responsibility for compliant storage of payment details. 
- Customers can store multiple tokens.

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

{{< blue-notice >}}
Tokens are stored on an account-level. If you operate multiple websites from a single MultiSafepay account, you can offer cross-domain recurring payments e.g. tokenize a customer's details on website A to offer one-click payments on website B.
{{< /blue-notice >}}

## Recurring models
MultiSafepay offers three recurring models:

- **Card on file (COF)**: The cardholder has authorized you to store their card details.
- **Subscription**: An agreement or services that are billed at the end of your billing cycle, e.g. weekly, monthly.
- **Unscheduled**: Event-triggered, e.g. mobile top-up when no credit left on the phone.

Our [SDKs](/developer/wrappers/) support all three models. Our [plugins](/payments/integrations/) use COF only. 

## Via our API
See API reference – [Recurring Payments](/api/#recurring-payments-orders).

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

Email a request to <sales@multisafepay.com>

{{< details title="Supported MultiSafepay plugins" >}}

We support recurring payments in our plugins for:

- [Magento 1](/payments/integrations/ecommerce-platforms/magento1)
- [Magento 2](/payments/integrations/ecommerce-platforms/magento2)
- [PrestaShop 1.6](/payments/integrations/ecommerce-platforms/prestashop-1-6)
- [PrestaShop 1.7](/payments/integrations/ecommerce-platforms/prestashop-1-7)
- [Shopware 6](/payments/integrations/ecommerce-platforms/shopware6) 
- [Woocommerce](/payments/integrations/ecommerce-platforms/woocommerce/) 

{{< /details >}}

