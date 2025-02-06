---
title: 'Second Chance reminders'
category: 6278c92bf4ad4a00361431b0
order: 5
hidden: false
slug: 'second-chance'
excerpt: 'Boost conversion by sending customers reminders about abandoned payments.'
---
Second Chance is a MultiSafepay solution that automatically emails customers a payment link when they initiate but don't complete a transaction. This helps boost <<glossary:conversion>> and impulse purchases. 

# How it works

Second Chance emails are sent:

- 1 hour after the customer initiates the payment, and a second email after 24 hours.
- For manually generated [payment links](/docs/payment-links/) if the customer doesn't click the link to complete payment.
- For a transaction for the same customer, email address, merchant, and site as a previous transaction initiated **more than** 120 minutes ago, even if the amount is different.

Second Chance emails are **not** sent:

- While the status of the original transaction is **Uncleared**, **Shipped**, or **Completed**
- For [recurring payments](/docs/recurring-payments/)
- If you have another **Completed** transaction with the same `order_id` and/or `session_id`
- For each separate transaction for orders with multiple linked transactions (one email is sent per `order_id` and `session_id`
- For a transaction for the same customer, email address, merchant, and site as a previous transaction initiated **less than** 120 minutes ago, even if the amount is different.


# Prerequisites

- Under the [GDPR](/docs/gdpr/), you must obtain documented consent from the customer to send Second Chance emails.
- You must include the customer's email address in the transaction API request.

# Activation

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Go to **Sites**, and then click the relevant site.
3. On the **Site profile** page, under **Site functionality**, select the **Enable Second Chance** checkbox.
4. Click **Save**.

# Integration

To integrate, see Recipes – <a href="https://docs.multisafepay.com/recipes/send-payment-reminders" target="_blank">Send payment reminders</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

<br>

---

# User guide

## Languages

<details id="supported-languages">
<summary>Supported languages</summary>
<br>

- Dutch
- English
- French
- German
- Italian
- Spanish

</details>

To set the language of Second Chance emails, see [Email styling](/docs/email-styling/) > Step 6.

**⚠️ Note:** The language set in the dashboard is overridden by the `locale` parameter in the `customer` object in [create order](/reference/createorder/) API requests.

<details id="locale-codes">
<summary>Locale codes per language and country</summary>
<br>

| Code | Language & country |
|---|---|
| cs_CZ	| Czech |
| de_AT	| German (Austria) |
| de_DE	| German (Germany) |
| en_US	| American English |
| fi_FI	| Finnish |
| fr_BE	| French (Belgium) |
| fr_FR	| French (France) |
| it_IT	| Italian |
| nl_BE	| Dutch (Belgium) |
| nl_NL	| Dutch (Netherlands) |
| pl_PL	| Polish |
| es_ES	| Spanish |
| sv_SE	| Swedish |
| zh_CN	| Chinese |

</details>

<details id="locale-example">
<summary>Locale example</summary>
<br>

```json
{
  "customer": {
    "first_name": "John",
    "last_name": "Doe",
    "house_number": "39",
    "address1": "Kraanspoor",
    "address2": "",
    "city": "Amsterdam",
    "zip_code": "1033 SC",
    "state": "Noord-Holland",
    "country": "NL",
    "locale": "nl_NL", // Set the language and country code
    "phone": "0208500500",
    "email": "example@multisafepay.com",
    "gender": "M",
    "birthday": "1980-12-31",
    "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    "referrer": "http://test.com",
    "ip_address": "123.123.123.123",
    "forwarded_ip": "",
    "reference": ""
  }
}
```

</details>

## Styling

You can style Second Chance email templates to match your brand's look and feel.

See [Email styling](/docs/email-styling/) > Select the **Second Chance email (to customer)** template.

## Payment link lifetimes

Payment links in Second Chance emails have the same lifetime as the original payment link, which is set to 30 days by default.

<details id="how-to-adjust-link-lifetimes">
<summary>How to adjust link lifetimes</summary>
<br>

To set or adjust the lifetime of a payment link, see API reference – [Create order](/reference/createorder/): `days_active` parameter.

**⚠️ Note:** This is different to [transaction expiration times per payment method](/reference/transaction-expiration/). 

This only applies to certain payment methods:

| Adjustable | Non-adjustable |
|---|---|
| Banking methods, except direct debits | Direct debits |
| Gift cards | Edenred, Paysafecard |
| Wallets | PayPal – Links are valid for 14 days. The lifetime is set by PayPal. |

</details>

## Payment methods

<details id="supported-payment-methods">
<summary>Supported payment methods</summary>
<br>

Most payment methods are supported, **except for**: 

- [Bank transfer](/docs/bank-transfer/)
- [E-Invoicing](/docs/e-invoicing/)
- [PayPal](/docs/paypal/)
- [Direct debit](/docs/direct-debit/)
- [Pay After Delivery](/docs/pay-after-delivery/)

</details>

## Potential errors

- Second Chance emails can cause issues when running an enterprise resource planning (ERP) system.
- If you have another <<glossary:order>> for the same total amount with the same customer email address completed in the last 120 minutes, Second Chance emails are suppressed.

<details id="errors-in-external-plugins">
<summary>Errors in external plugins</summary>
<br>

Second Chance emails can create conflicts with external warehouse systems. In some cases, this can be resolved using a cron job. However, this is not always a stable solution.

For example, when a customer cancels an <<glossary:order>> in the webshop, they can still pay for it using Second Chance within 30 days or a specified time frame. For more information, see API reference – [Create order](/reference/createorder/) > `days_active` parameter.

If a cancelled order is subsequently paid for, MultiSafepay reopens the order in the webshop. A warehouse system may have already released the reservation on the order when it received **Cancelled** status, or may consider the **Cancelled** status permanent. As result, the items the customer ordered may no longer be available or in stock.

</details>

## Reports

For an overview of all Second Chance emails that resulted in successful payment, see [Second Chance report](/docs/reports#second-chance-report).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)