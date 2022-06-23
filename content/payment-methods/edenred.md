---
title: 'Edenred'
category: 6298bd782d1cf4006032e765
order: 401
hidden: false
parentDoc: 62a32bf042021c00e1cd7e5c
slug: 'edenred'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/edenred.svg" width="80" align="right" style="margin: 20px 20px 20px 30px; max-height: 75px"/>

[Edenred](https://www.edenred.be/nl) lets employers provide their employees with a prepaid card loaded with Edenred vouchers:  

- Ticket Restaurant
- Ticket EcoCheques
- Ticket Compliments
- Ticket Sport & Culture

Read how Edenred can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/edenred)

| Overview | Details |
|---|---|
| **Chargebacks** | No |
| **Countries**  | Belgium  | 
| **Currencies** | EUR  |  
| **Payment pages** | [Yes](/payment-pages/) (current and deprecated versions) |
| **Refunds** | No |
| **Second Chance** | [Yes](/second-chance/) |

### Terms and conditions
  
- You must sign a contract with Edenred.
- For each voucher, you must comply with Edenred's rules regarding permitted products and services. 
- An Edenred prepaid card can contain multiple Edenred vouchers.
- Edenred vouchers can be used for partial payments in combination with another payment method.
- View all the Edenred transactions for your site in [My Edenred](https://myedenred.be).

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/readmedocs-staging/static/diagrams/svg/edenred-payment-flow.svg" alt="Edenred payment flow" style="display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 750px;
  width: 100%;">

# Payment statuses  

- **Order status:** Changes as the customer's order with you progresses towards shipment 
- **Transaction status:** Changes as the funds progress towards settlement in your account balance

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| For partial payment with another method: The customer has been redirected to their bank. | Initialized | Initialized |
| MultiSafepay has collected payment. | Completed | Completed |

</details>

# Activation 

<details id="how-to-activate-edenred">
<summary>How to activate Edenred</summary>
<br>

1. Fill out the Edenred – [Registreer mijn website](https://registreermijnwebsite.edenred.be/) form, selecting the relevant checkbox for each voucher you want to offer.
2. Sign a contract with Edenred. They'll give you an Edenred Merchant ID.
3. Email your Edenred Merchant ID to <sales@multisafepay.com>
4. We activate the payment method for your account.
</details >

# Integration

To test 

| Integration | Details |
|---|---|
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Prepaid card order <br> Examples > Edenred redirect <br> By default, all activated Edenred vouchers display at checkout, but you can also specify which Edenred vouchers to display per transaction. |
| **Ready-made integrations** | Only supported in our [Magento 2](/magento-2/) integration. |
<br>

> ℹ️ Testing
> To test Edenred payments, see [Testing](/testing/#prepaid-cards).
<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)
