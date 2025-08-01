---
title: Sodexo
category:
  uri: Payment methods
slug: sodexo
position: 3
privacy:
  view: public
parent:
  uri: prepaid-cards
---
<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/giftcards/sodexo-sportculturepass.svg" width="80" align="right" alt="Sodexo" style={{ margin:'20px 20px 20px 30px', maxHeight:'75px' }} />

<a href="https://www.sodexo.be/nl" target="_blank">Sodexo</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i><i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} /> lets employers gift their employees with prepaid card sport and culture voucher.

Read how Sodexo can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/sodexo" target="_blank">multisafepay.com</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i><i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />

| Supports                                                      | Details                               |
| ------------------------------------------------------------- | ------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Belgium                               |
| [Currencies](/docs/currencies/)                               | EUR                                   |
| [Chargebacks](/docs/chargebacks/)                             | No                                    |
| [Payment pages](/docs/payment-pages/)                         | Yes (current and deprecated versions) |
| [Refunds](/docs/refund-payments/)                             | No                                    |
| [Second Chance](/docs/second-chance/)                         | Yes                                   |

**Terms and conditions**

* You must sign a contract with Sodexo.
* For each voucher, you must comply with Sodexo rules regarding permitted products and services.
* Sodexo voucher can be used for partial payments with another payment method.

# Payment flow

This diagram shows the flow of a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/sodexo-payment-flow.svg" alt="Sodexo payment flow" style={{ display: "block", marginLeft: "auto", marginRight: "auto", maxWidth: "750px", width: "100%" }} />

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                                                              | Order status | Transaction status |
| ---------------------------------------------------------------------------------------- | ------------ | ------------------ |
| For partial payment with another method: The customer has been redirected to their bank. | Initialized  | Initialized        |
| MultiSafepay has collected payment.                                                      | Completed    | Completed          |

# Activation

1. Fill out the Sodexo <a href="https://sportculture.sodexo.be/nl/" target="_blank">application form</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i><i className="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.

   * Under **Bank details**, select the checkbox to accept the sport & culture pass on your webshop.
   * Select MultiSafepay your payment service provider.

2. Sign a contract with Sodexo. They'll give you a Sodexo Merchant ID.<br /> The <Glossary>issuer</Glossary> communicates your **Merchant ID** to us.

3. We activate the payment method for your account.

# Integration

### API

* See API reference – [Create order](/reference/createorder/) > Prepaid card order.

<details id="example-requests">
  <summary>Example requests</summary>

  <br />

  For example requests, on the [Create order](/reference/createorder/) page, in the black sandbox, see **Examples** > **Gift card redirect**.\
  Set `gateway` to the [gateway ID](/reference/gateway-ids) of the relevant voucher.

  <div style={{ textAlign: "center" }}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{ width: "40%", height: "auto" }} />
  </div>
</details>

{/* By default, all activated Sodexo vouchers display at checkout, but you can also specify which Sodexo vouchers to display per transaction. */}

### Ready-made integrations

* You can add Sodexo [gateway ID](/reference/gateway-ids) using a generic gateway in several of our [ready-made integrations](/docs/our-integrations/).

### Testing

To test Sodexo payments, see Testing payment methods - [Prepaid cards](/docs/testing#prepaid-cards).<br />

***

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)
