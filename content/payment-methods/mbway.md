---
title: MB WAY
category:
  uri: Payment methods
slug: mb-way
position: 12
privacy:
  view: public
parent:
  uri: banking-methods
---
> ⚠️ Note:
>
> We are currently in the pilot phase for this product in Portugal.
>
> If you are interested in participating in the next stage of our pilot, email [sales@multisafepay.com](mailto:sales@multisafepay.com)

<img src="https://media.multisafepay.com/img/methods/svg/mbway.svg" width="100" align="right" style={{margin: '20px', maxHeight: '75px'}} />

<a href="https://www.mbway.pt/" target="_blank">MB WAY</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> is a popular payment method in Portugal that lets customers make payments, send or request money, and manage funds using their mobile application.

{/*Read how Multibanco can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/mbway" target="_blank">multisafepay.com</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}}></i>*/}

| Supports                                                      | Details                                             |
| ------------------------------------------------------------- | --------------------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Portugal                                            |
| [Currencies](/docs/currencies/)                               | EUR                                                 |
| [Payment methods](doc:payment-methods)                        | Mastercard, Visa, Visa Electron or Multibanco card. |
| [Chargebacks](/docs/chargebacks/)                             | No                                                  |
| [Payment pages](/docs/payment-pages/)                         | Yes (current version only)                          |
| [Payment components](/docs/payment-components/)               | Yes                                                 |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial                               |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/MB-WAY-flow.svg" alt="MBWAY payment flow" style={{display: 'block', marginLeft: 'auto', marginRight: 'auto', maxWidth: '750px', width: '100%'}} />

# Payment statutes

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                                         | Order status | Transaction status |
| ------------------------------------------------------------------- | ------------ | ------------------ |
| The customer has initiated a transaction. You can no longer cancel. | Initialized  | Initialized        |
| The customer has completed the payment using the reference number.  | Completed    | Uncleared          |
| The transaction is settled.                                         | Completed    | Completed          |
| The customer didn't complete payment within 4 minutes.              | Expired      | Expired            |
| The reference number used is invalid.                               | Declined     | Declined           |
| **Refunds:** Refund reserved.                                       | Reserved     | Reserved           |
| **Refunds:** Refund complete.                                       | Completed    | Completed          |
| **Refunds:** Refund declined.                                       | Declined     | Declined           |

# Activation

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
2. To activate the payment method for:

* All websites, go to **Settings** > **Payment methods**.
* A specific website, go to **Websites**, and then click the relevant website.

3. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email [support@multisafepay.com](mailto:integration@multisafepay.com)

# Integration

* See API reference – [Create order](/reference/createorder/) > Wallet order.

<details id="example-requests">
  <summary>Example requests</summary>

  <br />

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **MB WAY direct/redirect**.\
  Set `gateway` to `MBWAY`, and `type` to `direct` or `redirect`.

  <div style={{textAlign: 'center'}}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{width: '40%', height: 'auto'}} />
  </div>
</details>

* A `phone` number is required in the `customer` object, and must be in a 9-digit number format excluding +351 <a href="https://en.wikipedia.org/wiki/List_of_country_calling_codes#Overview" target="_blank">Portugal calling code</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
* For <Glossary>direct</Glossary> orders, you must provide the customer with [payment instructions](#payment-instructions) to proceed with the payment.
* Transactions expire after 4 minutes.

# User guides

## Amount limits

* Minimum order amount: 1 EUR
* Maximum order amount: 99.999,99 EUR

## Cancellation

You can no longer cancel a transaction after the status changes to **Initialized**.

## Payment instructions

Email the customer the following payment details to include when completing the payments.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/MB-WAY.png" width="100%" align="left" />

<br />

You can still update the customer's phone number on the [payment pages](/docs/payment-pages).

## Refunds

You can process refunds in your dashboard.

The customer must provide you with their IBAN to process refunds via bank transfer.

**⚠️Note:** Refunds are only available within 3 months of a purchase. Requests made after this time cannot be processed.

<details id="how-to-refund-an-order">
  <summary>How to refund an order</summary>

  <br />

  1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
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

<blockquote className="callout callout_info">
  <h3 className="callout-heading false">
    <span className="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)
