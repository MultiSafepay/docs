---
title: 'Bank Transfer'
weight: 60
meta_title: "Payment methods - Bank Transfer - MultiSafepay Docs"
layout: 'single'
faq: '.'
logo: '/logo/Payment_methods/banktransfer-en.svg' 
short_description: 'A secure, trusted, international payment method within the SEPA region.'
url: '/payment-methods/bank-transfer/'
aliases: 
    - /support-tab/magento2/payment-methods/bank-transfer
    - /payment-methods/banks/bank-transfer
    - /payments/methods/banks/bank-transfer/
    - /payment-methods/bank-transfer/what-is-bank-transfer/
    - /payments/methods/banks/bank-transfer/about/
    - /payments/methods/bank-transfer/product-rules/
    - /payment-methods/bank-transfer/product-rules/
    - /payment-methods/bank-transfer/overview/
    - /payment-methods/bank-transfer/how-does-bank-transfer-work/
    - /payments/methods/banks/bank-transfer/payment-flow/
    - /payment-methods/bank-transfer/payment-flow/
    - /payment-methods/bancontact/bank-transfer-testing
    - /payments/methods/banks/bank-transfer/integration-and-testing/
    - /payment-methods/bank-transfer/integration-testing/
    - /bank-transfer/ongematchte-bankoverschrijvingen/
    - /bank-transfer/unzugeordneten-banküberweisungen/
    - /bank-transfer/unmatched-payments/
---
Bank Transfer (also known as SEPA Credit Transfer) is a secure, trusted, international banking method. Customers can make any type of online payment in euros within the SEPA area. 

[See how Bank Transfer can help your business!](https://www.multisafepay.com/solutions/payment-methods/bank-transfer)

## Overview
|   |   |   
|---|---|
| **Countries** | Europe (SEPA area) | 
| **Currencies** | EUR, CZK, GBP, HUF, PLN {{< br >}} USD is **not** supported due to extremely high transaction and currency conversion fees for customers. |
| **Chargebacks**  | No  | 
| **Refunds** | [Full and partial](/refunds/full-partial/) |
| **Transactions expire after** | 60 days  |

## Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant Me as Merchant

    C->>Mu: Selects Bank Transfer at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page to confirm <br> their bank account number and (optionally) bank country, <br> then displays payment instructions
    else Direct flow
    Mu->>C: Redirects to your success page, <br> then emails payment instructions <br> (or email the instructions yourself)
    end
    C->>Mu: Transfers funds (online or with teller) <br> (takes 1–3 business days) 
    Mu->>Me: Matches payment and settles funds
    
{{< /mermaid >}}
&nbsp;  
{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

| Payments | Order status | Transaction status |
|---|---|---|
| Awaiting the customer to transfer the funds. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| You cancelled the transaction. | Void   | Void/Cancelled   |
| The customer didn't complete  payment within 60 days. | Expired | Expired |
|**Refunds**|||
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |

{{< /details >}}

## How it works

MultiSafepay emails the customer the following payment details to include when transfering the funds, or your can email them yourself.

{{< screen src="/img/Bank-Transfer-Payment-Details.png" align="left" class="small-img desktop-radius" >}}

{{< details title= "Emailing payment instructions yourself" >}} 

You may prefer to email the customer the payment details yourself, e.g. for consistent, branded communications. Make sure you include clear instructions about what details the customer needs to provide and the required format (see&nbsp;2.&nbsp;below).

To prevent us from emailing the customer, see API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order. Set the `disable_send_email` parameter to `true`. 

{{< /details >}}

**Note:** Bank accounts are always displayed in IBAN format. See also [Unmasking IBAN numbers](/developer/unmasking-ibans/).

You can view the payment details for a transaction in your MultiSafepay dashboard, in the relevant **Transaction details** page under **Offline actions**.

### Transfer guidance for customers

The customer must only pay for **one** order per bank transfer. When transferring the funds, they must correctly input:  
    
- The amount
- Their bank account number
- The payment reference number (**not** the order number)  
    **Format:** 16 digits, numbers only, no words

### Matching payments

When we receive payment from the customer (1–3 business days later), we automatically match it to the corresponding transaction in our system based on the payment details provided. If auto-matching fails, we try to match the payment manually.

If we cannot match the payment:

- For smaller amounts, we refund the customer.
- For larger amounts, we contact you for information to help identify the correct transaction.

This costs all parties time and effort, and creates a negative customer experience. To avoid this, see [Resolving unmatched payments](/bank-transfer/unmatched-payments/).

## Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payments/activating-payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment pages](/payment-pages/) <br> ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/)s) {{< br >}} [Payment components](/payment-components/) |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> **Examples** > Bank Transfer direct/redirect |
| **Ready-made integrations** | Supported in all our [ready-made integrations](/integrations/ready-made/) |

## Notes

- To avoid stock-related issues if a customer fails to pay within 60 days, you can hold your inventory in your [backend](/glossaries/multisafepay-glossary/#backend) until they complete the payment.  This&nbsp;depends on your ecommerce platform or integration, and your products and/or services.  
**Note:** MultiSafepay bears no responsibility for stock-related issues.

- To change how bank transfers are validated, check whether this is possible in your backend.

### MultiSafepay local bank accounts

To simplify transfers for customers and avoid them incurring international transfer and currency conversion fees, MultiSafepay has a local bank account in several European countries in the local currency. Customers then only pay the standard fee charged by their bank.

To send a customer the details of a local MultiSafepay bank account, include the relevant [ISO 3166 country code](https://www.iso.org/iso-3166-country-codes.html) in your [create order](https://docs-api.multisafepay.com/reference/createorder) request in the `country` parameter, e.g. `"country": "DE",`.

{{< details title="Countries with a local MultiSafepay bank account" >}}


- Austria (EUR)
- Belgium (EUR)
- Czech Republic (CZK)
- France (EUR)
- Germany (EUR)
- Hungary (HUF)
- Italy (EUR)
- Netherlands (EUR)
- Poland (PLN)
- Portugal (EUR)
- Spain (EUR)
- UK (GBP)

{{< /details >}}

