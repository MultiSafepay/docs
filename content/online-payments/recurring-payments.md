---
title: 'Recurring payments'
category: 6278c92bf4ad4a00361431b0
order: 600
hidden: false
slug: 'recurring-payments'
excerpt: 'Boost conversion and manage subscriptions using tokenization.'
---
Recurring payments is a MultiSafepay solution that securely stores payment details to enable quick, easy repeat payments.

# How it works

- **One-click payments:** The customer selects stored details for faster checkout.
- **Subscriptions:** You use the token to collect payments at specific intervals, e.g. weekly, monthly.
- **Unscheduled payments:** You use the token for event-triggered payments, e.g. mobile top-up when no credit left on phone.

MultiSafepay encrypts customers' sensitive payment details during an initial payment for secure storage, and provides you with a non-sensitive identifier for the details known as a "token". Customers can save multiple tokens.

Subsequent payments are exempt from [SCA and 2FA](/pds2/).
MultiSafepay is responsible for [PCI DSS](/pci-dss/) compliant storage of payment details. 

Tokens are stored at account level rather than site level. If you operate multiple sites from a single MultiSafepay account, you can also offer cross-domain recurring payments, i.e. tokenize a customer's details on Site A and offer one-click payments on Site B.

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

- American Express
- [Bancontact WIP](/payment-methods/bancontact/overview/#bancontact-wip-service)
- iDEAL
- Maestro
- Mastercard
- SEPA Direct Debit – First you need to provide us with some information. See SEPA Direct Debit – [Activation](/sepa-direct-debit/#activation).
- Sofort
- Visa

</details>

## Initial payment

1. The customer gives you consent to store their payment details and verifies their identity with 3D Secure. 
2. MultiSafepay encrypts the payment details during processing and stores them securely on our servers. We return to you a non-sensitive token that references the encrypted payment details. 
3. You can use the token to process recurring payments without needing to handle or store sensitive payment details.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/recurring-payments-initial.svg" alt="Sequence diagram for request to tokenize cardholder data" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

### Zero Authorization
Optionally, you can set the amount for the initial payment `0`. No funds are transferred but a token is created (if the payment details are valid). 

See [Zero Authorization](/zero-authorization/).

## Subsequent payments: Customer-initiated 

1. You display the customer's available tokens at checkout, e.g. `MASTERCARD **43`. 
2. The customer selects a token and confirms payment. They don't need to reprovide any payment details or pass 3D Secure authentication again. 
3. You include the token in the request to MultiSafepay. 
4. MultiSafepay decrypts the payment details and processes the payment. 

This is also known as "one-click payment".

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/recurring-payments-cit.svg" alt="Sequence diagram for customer-initiated recurring payments" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

## Subsequent payments: Merchant-initiated 

There are two common use cases for merchant-initiated subsequent payments: 

    - Subscriptions
    - Unscheduled payments

1. The customer must give consent (once only). 
2. You include the token in the request to MultiSafepay. 
3. MultiSafepay decrypts the payment details and processes the payment.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/recurring-payments-mit.svg" alt="Sequence diagram for merchant-initiated recurring payments" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Activation

Email a request to activate recurring payments to <sales@multisafepay.com>

Specify in your request which tokenization model(s) you want to use:

- One-click payments
- Subscriptions
- Unscheduled payments

We send you an agreement to sign, including terms and conditions for data usage. 

# Integration

## Recurring models
MultiSafepay offers three recurring models:

- `cardOnFile` (one-click payments)
- `subscription`
- `unscheduled` (event-triggered)

Our API and [PHP SDK](https://github.com/MultiSafepay/php-sdk) support all three models.  
Our [ready-made integrations](/integrations/ready-made/) use `cardOnFile` only. 

## Ready-made integrations

You must have **both** credit card payments and recurring payments enabled for your MultiSafepay account.

<details id="supported-integrations">
<summary>Supported integrations</summary>
<br>

We support recurring payments in our plugins for:

- [Magento 1](/magento-1)
- [Magento 2](/magento-2)
- [PrestaShop 1.6](/prestashop-1-6)
- [PrestaShop 1.7](/prestashop-1-7)
- [Shopware 6](/shopware-6) 
- [WooCommerce](/woo-commerce/) 

</details>

## API

See API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > `customer.reference`.

**Note:** Tokens for SEPA Direct Debit transactions are originally received as iDEAL or Sofort transactions. 

<details id="additional-parameters">
<summary>Additional parameters</summary>
<br>

| Parameter | Type | Description |
|---|---|---|
| `type` | string | The payment flow for the checkout process. Options: `direct`, `redirect`. |
| `gateway` | string | The unique `gateway_id` to redirect the customer to the specific payment method. Make a [get gateway](https://docs-api.multisafepay.com/reference/getgateway) request. {{< br >}} Options: `AMEX`, `VISA`, `MASTERCARD`, `DIRDEB`. |
| `recurring_id` | string | A randomly generated recurring ID for the customer. |
| `reference` | string | The customer's reference number for the token. |
| `recurring_model` | string | The type of recurring model to use. Options: `unscheduled`, `cardOnFile`, `subscription`.  |

</details>

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)