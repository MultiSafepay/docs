---
title: 'Bank Transfer'
weight: 60
meta_title: "Payment methods - Bank Transfer - MultiSafepay Docs"
layout: "single"
logo: "https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/banktransfer-en.svg" 
short_description: 'A secure, trusted, international payment method within the SEPA region.'
url: "/payment-methods/bank-transfer/"
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
| **Currencies** | EUR, CZK, GBP, HUF, PLN <br> (USD **not** supported due to high transaction and currency conversion fees for customers) |
| **Chargebacks**  | No  | 
| **Refunds** | [Full and partial](/refunds/full-partial/) |
| **Transactions expire after** | 60 days  |

To better manage Bank Transfer payments, see also [Virtual IBANs](/payments/virtual-ibans/).

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

For more information, see [Payment statuses](/account/payment-statuses/).

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

### Payment instructions

MultiSafepay emails the customer the following payment details to include when transfering the funds, or your can email them yourself.

{{< screen src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Bank-Transfer-Payment-Details.png" align="left" class="small-img desktop-radius" >}}

{{< details title= "Emailing payment instructions yourself" >}} 

You may prefer to email the customer the payment details yourself, e.g. for consistent, branded communications. Make sure you include clear instructions about what details the customer needs to provide and the required format (see&nbsp;[Transfer guidance for customers](/payment-methods/bank-transfer/#transfer-guidance-for-customers) below).

To prevent us from emailing the customer, see API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order. Set the `disable_send_email` parameter to `true`. 

{{< /details >}}

**Note:** Bank accounts are always displayed in IBAN format. See also [Unmasking IBANs](/account/unmasking-ibans/).

### Local MultiSafepay bank accounts

To simplify transfers for customers and avoid them incurring international transfer and currency conversion fees, MultiSafepay has a local bank account in several European countries in the local currency. Customers then only pay the standard fee charged by their bank.

To send a customer the details of a local MultiSafepay bank account, include the relevant [ISO 3166 country code](https://www.iso.org/iso-3166-country-codes.html) in your [create order](https://docs-api.multisafepay.com/reference/createorder) request in the `country` parameter, e.g. `"country": "DE"`.

{{< details title="Countries with a local MultiSafepay bank account" >}}

| Country | Currency |
|---|---|
| Austria | EUR |
| Belgium | EUR |
| Czech Republic | CZK |
| France | EUR |
| Germany | EUR |
| Hungary | HUF |
| Italy | EUR |
| Netherlands | EUR |
| Poland | PLN |
| Portugal | EUR |
| Spain | EUR |
| UK | GBP |

{{< /details >}}

### Transfer guidance for customers

The customer must only pay for **one** order per bank transfer. When transferring the funds, provide:  
    
- The amount
- Their bank account number
- The payment reference number (**not** the order number)  
    **Format:** 16 digits, numbers only, no words

{{< alert-notice >}} Customers **must** enter the details accurately to avoid unmatched payments (see below). {{< /alert-notice >}}

### Matching payments

When we receive payments, we automatically match them to the corresponding transaction in our system by the amount **and** payment reference/customer bank account number. 

Automatic matching can fail if:

{{< details title="Payment details are incorrect, missing, or incorrectly formatted" >}}

We may not be able to match a payment if the customer:  

- Transfers the wrong amount
- Pays for multiple orders in one transfer
- Enters the payment reference number incorrectly, or includes words, e.g. "Payment ID 5213 0452 1234 5670" 
- Provides the order number instead of the payment reference number

Sometimes, the customer's bank has added comments to the transfer.

{{< /details >}}

{{< details title="Transaction wasn't successfully created" >}}

The customer made a transfer but did not:
    
- Place their order with you, **or**
- Click **Confirm** on the [payment page](/payment-pages/) (redirect orders).  

This means the transaction was not created successfully in our system.

{{< /details >}}

We then try to match the payment manually. If that fails:

- For smaller amounts, we refund the customer.
- For larger amounts, we contact you for information to help identify the correct transaction.

### Resolving unmatched payments

To create the transaction again, check if a [payment link](/account/payment-links/) was created: 

{{< details title="Payment link created" >}}

1. Click the link to open the payment page. 
2. Click **Bank Transfer**.
3. If the customer didn't fill in the **Bank account number** field, enter their bank account number (if known) to help us match the payment.
4. Click **Confirm** to create the transaction in our system.

{{< /details >}}

{{< details title="Payment link not created" >}}

1. [Generate a link manually](/account/payment-links/). 
2. Include in the description the customer's name and the order number (for your records). 
3. Click **Bank Transfer**.
4. Add the customer's bank account number (if known) to help us match the payment.
5. Click **Confirm** to create the transaction in our system.

**Note:** The order ID must be unique for each payment link.

{{< /details >}}

For support, email <support@multisafepay.com>

See this guidance in [Dutch](/bank-transfer/ongematchte-bankoverschrijvingen/) or [German](/bank-transfer/unzugeordneten-banküberweisungen/).

## Activation and integration

| | |
|---|---|
| **Activation** | [Enable in your dashboard](/payments/activating-payment-methods/#enable-in-dashboard) |
| **Checkout options** | [Payment components](/payment-components/) <br> [Payment pages](/payment-pages/) <br> ([current](/payment-pages/activation/) and [deprecated](/payment-pages/deprecated/)) |
| **Testing** | [Test payment details](/testing/test-payment-details/#banking-methods) |
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Bank Transfer direct/redirect |
| **Ready-made integrations** | Supported in all [ready-made integrations](/integrations/ready-made/) |

## User guide

### Stock issues

To avoid stock-related issues if a customer fails to pay within 60 days, you can hold your inventory in your backend until they complete payment.  This&nbsp;depends on your ecommerce platform or integration, and your products and/or services.  

**Note:** MultiSafepay bears no responsibility for stock-related issues.

### Validating transfers

To change how bank transfers are validated, check whether this is possible in your backend.



