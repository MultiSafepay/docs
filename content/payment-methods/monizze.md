---
title: 'Monizze'
category: 6298bd782d1cf4006032e765
order: 4
hidden: false
parentDoc: 62a32bf042021c00e1cd7e5c
slug: 'monizze'
---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/giftcards/monizze.svg" width="80" align="right" style={{margin: '20px 20px 20px 30px', maxHeight: '75px'}} />

<a href="https://www.monizze.be/nl/" target="_blank">Monizze</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} /> lets employers gift employees a prepaid card loaded with Monizze vouchers:

* Meal vouchers (maaltijdcheques/chèque-repas)
* Eco vouchers (ecocheque/eco-chèque)
* Gift vouchers (cadeaucheque/chèque-cadeau)

Read how Monizze can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/monizze" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />

| Supports                                                      | Details                               |
| ------------------------------------------------------------- | ------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Belgium                               |
| [Currencies](/docs/currencies/)                               | EUR                                   |
| [Chargebacks](/docs/chargebacks/)                             | No                                    |
| [Payment pages](/docs/payment-pages/)                         | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/)                             | No                                    |
| [Second Chance](/docs/second-chance/)                         | Yes                                   |

### Terms and conditions

* You must sign a contract with Monizze.
* For each voucher, you must comply with Monizze's rules on permitted products and services. You cannot prevent customers from paying for ineligible products or services with a Monizze voucher.
* A Monizze prepaid card can contain multiple Monizze vouchers.
* Monizze vouchers can be used for partial payments in combination with another payment method.
* Customers cannot pay for a single transaction with vouchers of different types.
* To request an automated monthly transaction report, email [shop@monizze.be](mailto:shop@monizze.be)

# Payment flow

This diagram shows the flow of a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/monizze-payment-flow.svg" alt="Monizze payment flow" style={{display: 'block', marginLeft: 'auto', marginRight: 'auto', maxWidth: '750px', width: '100%'}} />

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                                                              | Order status | Transaction status |
| ---------------------------------------------------------------------------------------- | ------------ | ------------------ |
| For partial payment with another method: The customer has been redirected to their bank. | Initialized  | Initialized        |
| MultiSafepay has collected payment.                                                      | Completed    | Completed          |

# Activation

1. Fill out the Monizze <a href="https://hello.monizze.be/nl/merchant/e-commerce/" target="_blank">application form</a> <i class="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />, selecting the checkbox for each voucher you want to offer.
2. Monizze and MultiSafepay will communicate to complete onboarding.
3. Once the activation is completed, we will notify you.

# Integration

### API

* See API reference – [Create order](/reference/createorder/) > Prepaid card order.

  <details id="example-requests">
    <summary>Example requests</summary>

    <br />

    For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Monizze redirect**.

    <div style={{textAlign: 'center'}}>
      <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{width: '40%', height: 'auto'}} />
    </div>
  </details>

* By default, all activated Monizze vouchers display at checkout, but you can also specify which ones to display per transaction.

### Ready-made integrations

You can add Monizze [gateway ID](/reference/gateway-ids) using a generic gateway in several of our [ready-made integrations](/docs/our-integrations/).

### Testing

To test Monizze payments, see Testing payment methods - [Prepaid cards](/docs/testing#prepaid-cards).\ <br />

***

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)