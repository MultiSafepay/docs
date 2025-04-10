---
title: 'Multibanco'
category: 6298bd782d1cf4006032e765
order: 13
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'multibanco'
---

> ⚠️ Note:
> 
> We are currently in the pilot phase for this product in Portugal.
> 
> If you are interested in participating in the next stage of our pilot, email <sales@multisafepay.com>
>

<img src="https://media.multisafepay.com/img/methods/svg/multibanco.svg" width="100" align="right" style="margin: 20px; max-height: 75px"/>

<a href="https://www.multibanco.pt/" target="_blank">Multibanco</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> is a payment method in Portugal that allows the customer to complete payment through home banking, service payments, or on the ATM Network.

<!--Read how Multibanco can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/multibanco" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>-->

| Supports                                                      | Details                                              |
| ------------------------------------------------------------- | ---------------------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Portugal                                             |
| [Currencies](/docs/currencies/)                               | EUR                                                  |
| [Payment methods](/docs/payment-pages/)                       | Mastercard, Visa, Visa Electron, or Multibanco card. |
| [Chargebacks](/docs/chargebacks/)                             | No                                                   |
| [Payment pages](/docs/payment-pages/)                         | Yes (current version only)                           |
| [Payment components](/docs/payment-components/)               | Yes                                                  |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial                                |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/multibanco-flow.svg" alt="MBWAY payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description                                                         | Order status | Transaction status |
| ------------------------------------------------------------------- | ------------ | ------------------ |
| The customer has initiated a transaction. You can no longer cancel. | Initialized  | Initialized        |
| The customer has completed the payment using the reference number.  | Completed    | Uncleared          |
| The transaction is settled.                                         | Completed    | Completed          |
| The customer didn't complete payment within 72 hours.               | Expired      | Expired            |
| The reference number used is invalid.                               | Declined     | Declined           |
| **Refunds:** Refund reserved.                                       | Reserved     | Reserved           |
| **Refunds:** Refund complete.                                       | Completed    | Completed          |
| **Refunds: ** Refund declined.                                      | Declined     | Declined           |

# Activation

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. To activate the payment method for:

- All websites, go to **Settings** > **Payment methods**.
- A specific website, go to **Websites**, and then click the relevant website.

3. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email [support@multisafepay.com](mailto:integration@multisafepay.com)

# Integration

### API

- See API reference – [Create order](/reference/createorder/) > Banking order. 

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

   For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Multibanco direct/redirect**.  
   Set `gateway` to `MULTIBANCO`, and `type` to `direct` or `redirect`.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- For <<glossary:direct>> orders, you must provide the customer with [payment instructions](#payment-instructions) to proceed with the payment.

- Transactions expire after 72 hours.

<!--

### Testing

To test Multibanco payments, see Testing payment methods - [Banking methods](<>).--

\-->

# User guides

## Amount limits

- Minimum order amount: 1 EUR
- Maximum order amount: 99.999,99 EUR

## Cancellation

You can no longer cancel a transaction after the status changes to **Initialized**.

## Payment instructions

Email the customer the following payment details to include when completing the payments. 

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Multibanco.png" width="100%" />
<br>

## Refunds

You can process refunds in your dashboard.

The customer must provide you with their IBAN to process refunds via bank transfer.

**⚠️Note:** Refunds are only available within 3 months of a purchase. Requests made after this time cannot be processed.

<details id="how-to-refund-an-order">
<summary>How to refund an order</summary>
<br>

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>. 
2. Go to **Transactions** > **Transaction overview**, and then click the relevant transaction.
3. On the **Transaction details** page, click **Refund order**.
4. In the **Account Holder Name** field, enter the customer's full name.
5. In the **IBAN** field, enter the customer's IBAN.
6. In the **Reason / Description** field, enter the reason for the refund or a description of what happened with the order, and then click **Complete**.
7. In the **Comment** field, enter any additional information.
8. In the **Amount** fields, enter the amount to refund. 
9. Click **Continue**.
10. Review the **Refund confirmation**, and then click **Confirm**.

</details>
---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)