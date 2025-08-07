---
title: Edenred
category:
  uri: Payment methods
slug: edenred
position: 0
privacy:
  view: public
parent:
  uri: prepaid-cards
---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/giftcards/edenred.svg" width="80" align="right" style={{margin: '20px 20px 20px 30px', maxHeight: '75px'}} />

<a href="https://www.edenred.be/nl" target="_blank">Edenred</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> lets employers gift employees a prepaid card loaded with Edenred vouchers:

* Ticket Restaurant
* Ticket EcoCheques
* Ticket Compliments
* Ticket Sport & Culture

Read how Edenred can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/edenred" target="_blank">multisafepay.com</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />

| Supports                                                      | Details                               |
| ------------------------------------------------------------- | ------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Belgium                               |
| [Currencies](/docs/currencies/)                               | EUR                                   |
| [Chargebacks](/docs/chargebacks/)                             | No                                    |
| [Payment pages](/docs/payment-pages/)                         | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/)                             | No                                    |
| [Second Chance](/docs/second-chance/)                         | Yes                                   |

### Terms and conditions

* You must sign a contract with Edenred.
* For each voucher, you must comply with Edenred's rules on permitted products and services.
* An Edenred prepaid card can contain multiple Edenred vouchers.
* Edenred vouchers can be used for partial payments in combination with another payment method.
* View all the Edenred transactions for your website in <a href="https://myedenred.be" target="_blank">My Edenred</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/edenred-payment-flow.svg" alt="Edenred payment flow" style={{display: 'block', marginLeft: 'auto', marginRight: 'auto', maxWidth: '750px', width: '100%'}} />

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                                                              | Order status | Transaction status |
| ---------------------------------------------------------------------------------------- | ------------ | ------------------ |
| For partial payment with another method: The customer has been redirected to their bank. | Initialized  | Initialized        |
| MultiSafepay has collected payment.                                                      | Completed    | Completed          |

# Activation

1. Fill out the Edenred – <a href="https://registreermijnwebsite.edenred.be/" target="_blank">Registreer mijn website</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> form, selecting the relevant checkbox for each voucher you want to offer.
2. Sign a contract with Edenred. They'll give you an Edenred Merchant ID.
3. Email your Edenred Merchant ID to [sales@multisafepay.com](mailto:sales@multisafepay.com)
4. We activate the payment method for your account.

# Integration

### API

* See API reference – [Create order](/reference/createorder/) > Prepaid card order.

  <details id="example-requests">
    <summary>Example requests</summary>

    <br />

    For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Gift card redirect**.\
    Set `gateway` to the [gateway ID](/reference/gateway-ids) of the relevant voucher.

    <div style={{textAlign: 'center'}}>
      <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{width: '40%', height: 'auto'}} />
    </div>
  </details>

* By default, all activated Edenred vouchers display at checkout, but you can also specify which Edenred vouchers to display per transaction.

### Ready-made integrations

* You can add Edenred [gateway ID](/reference/gateway-ids) using a generic gateway in several of our [ready-made integrations](/docs/our-integrations/).
* Supported in our [Magento 2](/docs/magento-2/) integration.

### Testing

To test Edenred payments, see Testing payment methods - [Prepaid cards](/docs/testing#prepaid-cards).\ <br />

***

<blockquote className="callout callout_info">
  <h3 className="callout-heading false">
    <span className="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)
