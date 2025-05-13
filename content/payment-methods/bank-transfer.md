---
title: 'Bank transfer'
category: 6298bd782d1cf4006032e765
parentDoc: 62a728d48b97080046c1d220
order: 3
hidden: false
slug: 'bank-transfer'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/banktransfer-en.svg" width="90" align="right" style="margin: 20px; max-height: 75px"/>

Bank transfers (also known as SEPA Credit Transfer) are a secure, trusted, international banking method. Customers can make any type of online payment in euros within the SEPA area. 

Read how bank transfers can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/bank-transfer" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details | 
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country) | Europe (SEPA area) | 
| [Currencies](/docs/currencies/) | AUD, CAD, CHF, CZK, DKK, EUR, GBP, HKD, HUF, JPY, NOK, PLN, SEK, USD |
| [Payment components](/docs/payment-components/) | Yes |
| [Payment pages](/docs/payment-pages/) | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/) | Yes: Full and partial |
| [Virtual IBANs](/docs/virtual-ibans/) | Yes, to better manage bank transfer payments |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/bank-transfer-payment-flow.svg" alt="Bank transfer payment flow" style="display: block;
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

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. To activate the payment method for:
- All websites, go to **Settings** > **Payment methods**.
- A specific website, go to **Websites**, and then click the relevant website.
3. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <support@multisafepay.com>

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > Banking order.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Bank transfer direct/redirect**.
  Set `type` to `direct` or `redirect`.

  <div style="text-align: center;">
  <img
    src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif"
    alt="MultiSafepay Sandbox Test Process GIF"
    style="width: 40%; height: auto;"
  />
  </div>

  </details>

- Transactions expire after 60 days.

### Ready-made integrations
Supported in all [ready-made integrations](/docs/our-integrations/).

### Testing
To test bank transfers, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).
<br>

---

# User guide

## Local MultiSafepay bank accounts

To simplify transfers for customers and avoid them incurring international transfer and currency conversion fees, MultiSafepay has a local bank account in several European countries in the local currency. Customers then only pay the standard fee charged by their bank.

To send a customer the details of a local MultiSafepay bank account, include the relevant <a href="https://www.iso.org/iso-3166-country-codes.html" target="_blank">ISO 3166 country code</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> in your [create order](/reference/createorder/) request in the `country` parameter, e.g. `"country": "DE"`.

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

---

</details>

## Payment instructions

MultiSafepay emails the customer the following payment details to include when transferring the funds, or your can email them yourself.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/bank-transfer.png" width="100%" align="left"/>
<br>

**⚠️ Note:** Bank accounts are always displayed in IBAN format. See also [Unmasking IBANs](/docs/ibans/).

<details id="how-to-email-payment-instructions-yourself"> 
<summary>How to email payment instructions yourself</summary>
<br>

You may prefer to email the customer the payment details yourself, e.g. for consistent, branded communications. Make sure you include clear instructions about what details the customer needs to provide, and the required format (see [Transfer guidance for customers](#transfer-guidance-for-customers) below).

To prevent us from emailing the customer:
- See API reference – [Create order](/reference/createorder/), under **Body params** > select **Banking order** 
- Click **customer object**, and set the `disable_send_email` parameter to `true`

</details>

### Transfer guidance for customers

The customer must only pay for **one** <<glossary:order>> per bank transfer. When transferring the funds, provide:  
    
- The amount
- Their bank account number
- The payment reference number (**not** the order number)  
    **Format:** 16 digits, numbers only, no words

>❗ Note
>
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

---

</details>

<details id="transaction-not-successfully-created">
<summary>Transaction wasn't successfully created</summary>
<br>

The customer made a transfer but did not:
    
- Place their order with you, **or**
- Click **Confirm** on the [payment page](/docs/payment-pages/) (<<glossary:redirect>> orders).  

This means the transaction was not created successfully in our system.

---

</details>

We then try to match the payment manually. If that fails:

- For smaller amounts, we refund the customer.
- For larger amounts, we contact you for information to help identify the correct transaction.

### Resolving unmatched payments

To resolve unmatched payments, check if a [transaction](/docs/payment-links#integration) was created: 

<details id="transaction-created">
<summary>Transaction created</summary>
<br>

1. Click the link to open the payment page. 
2. Click **Bank transfer**.
3. If the customer didn't fill in the **Bank account number** field, enter their bank account number (if known) to help us match the payment.
4. Click **Confirm** to create the transaction in our system.

---

</details>

<details id="transaction -not-created">
<summary>Transaction not created</summary>
<br>

1. [Generate a link manually](/docs/payment-links/#integration). 
2. Include in the description the customer's name and the order number (for your records). 
3. Click **Bank transfer**.
4. Add the customer's bank account number (if known) to help us match the payment.
5. Click **Confirm** to create the transaction in our system.

&nbsp; **💡 Tip!** The order ID must be unique for each payment link.

---

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
