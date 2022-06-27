---
title: 'Bank Transfer'
category: 6298bd782d1cf4006032e765
parentDoc: 62a728d48b97080046c1d220
order: 102
hidden: false
slug: 'bank-transfer'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/banktransfer-en.svg" width="90" align="right" style="margin: 20px; max-height: 75px"/>

Bank Transfer (also known as SEPA Credit Transfer) is a secure, trusted, international banking method. Customers can make any type of online payment in euros within the SEPA area. 

Read how Bank Transfer can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/bank-transfer)

| Supports | Details | 
|---|---|
| **Chargebacks**  | No  | 
| **Countries** | Europe (SEPA area) | 
| **Currencies** | EUR, CZK, GBP, HUF, PLN <br> (USD **not** supported due to high transaction and currency conversion fees for customers) |
| **Payment components** | [Yes](/docs/payment-components/) |
| **Payment pages** | [Yes](/docs/payment-pages/) (current and deprecated versions) |
| **Refunds** | [Yes](/docs/refund-payments/): Full and partial |
| **Virtual IBANs** | [Yes](/docs/virtual-ibans/) to better manage Bank Transfer payments |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/bank-transfer-payment-flow.svg" alt="Bank transfer payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;width: 100%;">

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| Awaiting the customer to transfer the funds. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |
| You cancelled the transaction. | Void   | Void/Cancelled   |
| The customer didn't complete  payment within 60 days. | Expired | Expired |
| **Refunds:** Refund initiated. | Reserved | Reserved |
| **Refunds:** Refund complete. | Completed | Completed |

# Activation 

You can activate Bank Transfer yourself in your dashboard. 

<details id="how-to-activate-bank-transfer"> 
<summary>How to activate in your Bank Transfer</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings**. 
3. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
4. Select the checkbox for the relevant payment method, and then click **Save changes**.

> 💬  Support
> If the payment method isn't visible in your dashboard, email <integration@multisafepay.com> 

</details>

# Integration

### API
- [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order.
- Examples > Bank Transfer direct/redirect.
- Transactions expire after 60 days.

### Ready-made integrations
Supported in all [ready-made integrations](/docs/our-integrations/).

### Testing
To test Bank Transfer payments, see [Testing](/docs/testing#banking-methods).
<br>

---

# User guide

## Local MultiSafepay bank accounts

To simplify transfers for customers and avoid them incurring international transfer and currency conversion fees, MultiSafepay has a local bank account in several European countries in the local currency. Customers then only pay the standard fee charged by their bank.

To send a customer the details of a local MultiSafepay bank account, include the relevant [ISO 3166 country code](https://www.iso.org/iso-3166-country-codes.html) in your [create order](https://docs-api.multisafepay.com/reference/createorder) request in the `country` parameter, e.g. `"country": "DE"`.

<details id="countries-with-a-local-MultiSafepay-bank-account">
<summary>Countries with a local MultiSafepay bank account</summary>
<br>

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

</details>

## Payment instructions

MultiSafepay emails the customer the following payment details to include when transfering the funds, or your can email them yourself.

{{< screen src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Bank-Transfer-Payment-Details.png" align="left" class="small-img desktop-radius">

<details id="how-to-email-payment-instructions-yourself"> 
<summary>How to email payment instructions yourself</summary>
<br>

You may prefer to email the customer the payment details yourself, e.g. for consistent, branded communications. Make sure you include clear instructions about what details the customer needs to provide and the required format (see [Transfer guidance for customers](#transfer-guidance-for-customers) below).

To prevent us from emailing the customer, see API reference – [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order. Set the `disable_send_email` parameter to `true`. 

</details>

**Note:** Bank accounts are always displayed in IBAN format. See also [Unmasking IBANs](/docs/ibans/).

### Transfer guidance for customers

The customer must only pay for **one** order per bank transfer. When transferring the funds, provide:  
    
- The amount
- Their bank account number
- The payment reference number (**not** the order number)  
    **Format:** 16 digits, numbers only, no words

>❗ Note
> Customers **must** enter the details accurately to avoid unmatched payments (see below).

## Matching payments

When we receive payments, we automatically match them to the corresponding transaction in our system by the amount **and** payment reference/customer bank account number. 

Automatic matching can fail if the:

<details id="payment-details-are-incorrect,-missing,-or-incorrectly-formatted">
<summary>Payment details are incorrect, missing, or incorrectly formatted</summary>
<br>

We may not be able to match a payment if the customer:  

- Transfers the wrong amount
- Pays for multiple orders in one transfer
- Enters the payment reference number incorrectly, or includes words, e.g. "Payment ID 5213 0452 1234 5670" 
- Provides the order number instead of the payment reference number

Sometimes, the customer's bank has added comments to the transfer.

</details>

<details id="transaction-not-successfully-created">
<summary>Transaction wasn't successfully created</summary>
<br>

The customer made a transfer but did not:
    
- Place their order with you, **or**
- Click **Confirm** on the [payment page](/docs/payment-pages/) (redirect orders).  

This means the transaction was not created successfully in our system.

</details>

We then try to match the payment manually. If that fails:

- For smaller amounts, we refund the customer.
- For larger amounts, we contact you for information to help identify the correct transaction.

### Resolving unmatched payments

To create the transaction again, check if a [payment link](/docs/payment-links/) was created: 

<details id="payment-link-created">
<summary>Payment link created</summary>
<br>

1. Click the link to open the payment page. 
2. Click **Bank Transfer**.
3. If the customer didn't fill in the **Bank account number** field, enter their bank account number (if known) to help us match the payment.
4. Click **Confirm** to create the transaction in our system.

</details>

<details id="payment-link-not-created">
<summary>Payment link not created</summary>
<br>

1. [Generate a link manually](/docs/payment-links/). 
2. Include in the description the customer's name and the order number (for your records). 
3. Click **Bank Transfer**.
4. Add the customer's bank account number (if known) to help us match the payment.
5. Click **Confirm** to create the transaction in our system.

**Note:** The order ID must be unique for each payment link.

</details>

See this guidance in [Dutch](/docs/ongematchte-bankoverschrijvingen) or [German](/docs/unzugeordneten-banküberweisungen).

## Stock issues

To avoid stock-related issues if a customer fails to pay within 60 days, you can hold your inventory in your <<glossary:backend>> until they complete payment. This depends on your ecommerce platform or integration, and your products and/or services.  

❗ MultiSafepay bears no responsibility for stock-related issues.

## Validation

To change how bank transfers are validated, check whether this is possible in your backend.
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)

