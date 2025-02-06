---
title: 'Edenred'
category: 6298bd782d1cf4006032e765
order: 0
hidden: false
parentDoc: 62a32bf042021c00e1cd7e5c
slug: 'edenred'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/giftcards/edenred.svg" width="80" align="right" style="margin: 20px 20px 20px 30px; max-height: 75px"/>

<a href="https://www.edenred.be/nl" target="_blank">Edenred</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> lets employers gift employees a prepaid card loaded with Edenred vouchers:  

- Ticket Restaurant
- Ticket EcoCheques
- Ticket Compliments
- Ticket Sport & Culture

Read how Edenred can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/edenred" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

| Supports | Details |
|---|---|
| [Countries](/docs/payment-methods#payment-methods-by-country)  | Belgium  | 
| [Currencies](/docs/currencies/) | EUR  |  
| [Chargebacks](/docs/chargebacks/) | No |
| [Payment pages](/docs/payment-pages/) | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/) | No |
| [Second Chance](/docs/second-chance/) | Yes |

### Terms and conditions
  
- You must sign a contract with Edenred.
- For each voucher, you must comply with Edenred's rules on permitted products and services. 
- An Edenred prepaid card can contain multiple Edenred vouchers.
- Edenred vouchers can be used for partial payments in combination with another payment method.
- View all the Edenred transactions for your site in <a href="https://myedenred.be" target="_blank">My Edenred</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/edenred-payment-flow.svg" alt="Edenred payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

The table below sets out the <<glossary:order status>> and <<glossary:transaction status>> for payments and refunds.

| Description | Order status | Transaction status |
|---|---|---|
| For partial payment with another method: The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |

# Activation 

1. Fill out the Edenred – <a href="https://registreermijnwebsite.edenred.be/" target="_blank">Registreer mijn website</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i> form, selecting the relevant checkbox for each voucher you want to offer.
2. Sign a contract with Edenred. They'll give you an Edenred Merchant ID.
3. Email your Edenred Merchant ID to <sales@multisafepay.com>
4. We activate the payment method for your account.

# Integration

### API
- See API reference – [Create order](/reference/createorder/) > Prepaid card order.

  <details id="example-requests"> 
  <summary>Example requests</summary>
  <br>

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Gift card redirect**. 
  Set `gateway` to the [gateway ID](/reference/gateway-ids) of the relevant voucher.

  <img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/APIExamples.png" align ="center"/>

  </details>

- By default, all activated Edenred vouchers display at checkout, but you can also specify which Edenred vouchers to display per transaction.

### Ready-made integrations

- You can add Edenred [gateway ID](/reference/gateway-ids) using a generic gateway in several of our [ready-made integrations](/docs/our-integrations/).
- Supported in our [Magento 2](/docs/magento-2/) integration.

### Testing
To test Edenred payments, see Testing payment methods - [Prepaid cards](/docs/testing#prepaid-cards).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
