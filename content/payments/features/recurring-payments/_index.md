---
title: 'Recurring payments'
weight: 30
meta_title: "Recurring payments - MultiSafepay Docs"
layout: 'single'

logo: '/svgs/Tokenization.svg'
short_description: 'Tokenize payment details to make checkout more convenient.'
url: '/features/recurring-payments/'
aliases: 
    - /tools/tokenization/how-do-i-get-tokenization/
    - /tools/tokenization/tokenization-api-level/
    - /tools/tokenization/tokenization-via-api/
    - /tools/tokenization/tokenization-available-for-plugins/
    - /tools/recurring-payments/what-is-recurring-payments/
    - /payments/features/tokenization/
---

Recurring payments involves MultiSafepay encrypting customers' sensitive payment details for secure storage and providing merchants a non-sensitive identifier, known as a "token", to enable quick, easy repeat payments, e.g.:


- **One-click payments:** The customer selects stored details for faster checkout.
- **Subscriptions:** You use the token to collect payments at specific intervals, e.g. weekly, monthly.
- **Unscheduled payments:** You use the token for event-triggered payments, e.g. mobile top-up when no credit left on phone.

### Benefits

- Subsequent payments are exempt from [SCA and 2FA](/payment-regulations/sca/).
- MultiSafepay is responsible for [PCI DSS](/payment-regulations/pci-dss/) compliant storage of payment details. 
- Customers can save multiple tokens.

{{< blue-notice >}}
Tokens are stored at account level rather than website level. If you operate multiple websites from a single MultiSafepay account, you can also offer cross-domain recurring payments, i.e. tokenize a customer's details on Website A and offer one-click payments on Website B.
{{< /blue-notice >}}

## How it works

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

### Initial payment

1. The customer gives you consent to store their payment details and verifies their identity with 3D Secure. 
2. MultiSafepay encrypts the payment details during processing and stores them securely on our servers. We return to you a non-sensitive token that references the encrypted payment details. 
3. You can use the token to process recurring payments without needing to handle or store sensitive payment details.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Me as Merchant
    participant Mu as MultiSafepay

    C->>Me: Enters payment details, <br> and verifies identity with 3D Secure
    Me->>Mu: Forwards payment details
    Mu-->>Mu: Encrypts payment details <br> for secure storage
    Mu->>Me: Returns a token <br> for subsequent payments
    Me->>C: Redirects to success page
    Mu-->>Me: Collects funds

{{< /mermaid >}}

{{< br >}}
&nbsp;

#### Zero Authorization
Optionally, you can set the amount for the initial payment `0`. No funds are transferred but a token is created (if the payment details are valid). 

See [Zero Authorization](/features/zero-authorization/).

### Subsequent payments: Customer-initiated 

1. You display the customer's available tokens at checkout, e.g. `MASTERCARD **43`. 
2. The customer selects a token and confirms payment. They don't need to reprovide any payment details or pass 3D Secure authentication again. 
3. You include the token in the request to MultiSafepay. 
4. MultiSafepay decrypts the payment details and processes the payment. 

This is also known as "one-click payment".

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
    C-->>Me: Collects funds 


{{< /mermaid >}}

{{< br >}}
{{< br >}}

### Subsequent payments: Merchant-initiated 

There are two common use cases for merchant-initiated subsequent payments: 

- Subscriptions
- Unscheduled payments

1. The customer must give consent (once only). 
2. You include the token in the request to MultiSafepay. 
3. MultiSafepay decrypts the payment details and processes the payment.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Me as Merchant
    participant Mu as MultiSafepay

    C-->>Me: Consents to <br> merchant-initiated payments
    Me->>Mu: Places order with token
    Mu-->>Mu: Decrypts payment details <br> to process payment
    Mu->>Me: Confirms successful payment <br> and collects funds

{{< /mermaid >}}

{{< br >}}

## Activation

Email a request to activate Recurring Payments to <sales@multisafepay.com>

## Integration

### Recurring models
MultiSafepay offers three recurring models:

- `COF` (card on file)
- `Subscription`
- `Unscheduled` (event-triggered)

Our [SDKs](/developer/wrappers/) support all three models. Our [ready-made integrations](/payments/integrations/) use `COF` only. 

### Via our API
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

### Via ready-made integrations

You must have **both** credit card payments and recurring payments enabled for your MultiSafepay account.

{{< details title="Supported MultiSafepay plugins" >}}

We support recurring payments in our plugins for:

- [Magento 1](/payments/integrations/ecommerce-platforms/magento1)
- [Magento 2](/payments/integrations/ecommerce-platforms/magento2)
- [PrestaShop 1.6](/payments/integrations/ecommerce-platforms/prestashop-1-6)
- [PrestaShop 1.7](/payments/integrations/ecommerce-platforms/prestashop-1-7)
- [Shopware 6](/payments/integrations/ecommerce-platforms/shopware6) 
- [Woocommerce](/payments/integrations/ecommerce-platforms/woocommerce/) 

{{< /details >}}

