---
title: 'MOTO'
category: 6298bd782d1cf4006032e765
order: 7
hidden: false
parentDoc: 62a727569e389a012f577acd
slug: 'moto'
---

Mail Order/Telephone Order (MOTO) is a MultiSafepay solution that lets you process card-not-present payments over the phone or by email. 

# How it works

The customer provides their card details to you over the phone or by email. 

Since MOTO skips [3D Secure](/docs/3ds2/) authentication, you bear the increased risk of fraud. To help ensure the customer is the cardholder, ask them to provide as much identifying information as possible, e.g.:

- Full name
- Address
- Phone numbers
- Email address
- Name of bank
- A copy of their signature on some correspondence, e.g. a scanned order confirmation

You handle the transaction via your MultiSafepay dashboard or our API. 

# Prerequisites

To handle MOTO transactions via our API, you must be PCI DSS compliant. 
See [Cardholder data](/docs/cardholder-data/).

# Activation
Email a request to activate MOTO to <sales@multisafepay.com>

The Risk Team assesses your request and, if approved, activates MOTO for your MultiSafepay account. 

Once activated, to process MOTO payments, follow these steps:

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Transactions** > **Mail & phone payments**.
3. Under **Order details**:  
    - From the **Currency** list, select the currency, and then fill out the **Amount** field.
    - From the **Website** list, select the relevant website. 
    - Optionally, in the **Order ID** field, enter an order ID.
    - In the **Description** text box, enter an order description.
4. Under **Card details**, enter the payment details provided by the customer by email or telephone. 
5. Under **Customer details**, enter the customer's name, address, and contact information. 
6. Click **Submit order**.  
The transaction appears in your **Transaction overview**.

# Integration

See API reference – [Create order](/reference/createorder/) > Card order.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** and select the **`Credit card` direct** example.

  <div style="text-align: center;">
  <img
    src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif"
    alt="MultiSafepay Sandbox Test Process GIF"
    style="width: 40%; height: auto;"
  />
  </div>

  </details>

See Recipes – <a href="https://docs.multisafepay.com/recipes/create-a-moto-order" target="_blank">Create a MOTO order</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Restrictions for MOTO

Only <<glossary:domestic transactions>>: can be processed for the following combinations of payment method and country:

| Card                                                                                                                                                                                        | Countries                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| <a href="https://www.multisafepay.com/solutions/payment-methods/maestro/" target="_blank">Maestro</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> (debit card) | Ireland, Turkey, and France |

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
