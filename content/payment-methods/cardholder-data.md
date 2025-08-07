---
title: Cardholder data
category:
  uri: Payment methods
slug: cardholder-data
position: 5
privacy:
  view: public
parent:
  uri: cards
content:
  excerpt: Handle sensitive cardholder data on your PCI DSS compliant server.
---
When you accept credit and debit card payments using a [payment page](/docs/payment-pages/) or [payment component](/docs/payment-components/), MultiSafepay handles the sensitive cardholder data, including:

* Primary account number (PAN)
* Cardholder name
* Service code
* Expiry date

We bear the risk and responsibility for [PCI DSS compliance](/docs/pci-dss/).

Alternatively, you can collect cardholder data through other means. Because you will then handle sensitive data on your own server before sending it to MultiSafepay, you must also have PCI DSS certification.

You are responsible for arranging certification, which is a complex, time-consuming, and expensive process. Consider carefully if this makes sense for your business model.

# Activation

1. To check your eligibility to use this feature, email [sales@multisafepay.com](mailto:sales@multisafepay.com)\
   Specify in your request:
   * The payment methods you want to integrate
   * The sites under your account this applies to
   * The type of products you will sell
   * Your average order values and volumes, and any available processing statements.
2. We check your account and company performance.
3. Email proof of your PCI DSS certification and an activation request to [risk@multisafepay.com](mailto:risk@multisafepay.com)
4. If approved, we complete activation.

# Integration

See API reference – [Create order](/reference/createorder/) > Card order.\
Set `type` to `direct`.

## 3DS2

When you collect cardholder data, you must also collect the contextual information about the customer's device (fingerprint) required for [3DS2](/docs/3ds2) authentication. The fingerprint can be created through JavaScript interfaces and methods in the customer's browser.\
**⚠️ Note:** Some details are required to comply with scheme regulations. For example, transactions created with payment method VISA must include correct information in the `email` or `phone` parameter.

To learn how to create a fingerprint, see Recipe – <a href="https://docs.multisafepay.com/recipes/create-a-customerbrowser-object" target="_blank">Create a customer.browser object</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }}></i> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.

***

# User guide

## Maintenance

You must provide us with your:

* Attestation of Compliance each year
* Approved Scanning Vendor reports every 3 months

## Payment methods

The table below sets out supported payment methods and their respective [3D Secure](/docs/3ds2/) authentication requirements:

| Card             | Authentication protocol                                            |
| ---------------- | ------------------------------------------------------------------ |
| American Express | American Express Safekey – mandatory for transactions above 30 EUR |
| Bancontact       | 3D Secure only                                                     |
| Maestro          | 3D Secure only                                                     |
| Mastercard       | Mastercard SecureCode **and** non-3D Secure payments               |
| Visa             | Verified by Visa **and** non-3D Secure payments                    |

<br />

***

<blockquote class="callout callout_info">
  <h3 class="callout-heading false">
    <span class="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a></p>
</blockquote>

[Top of page](#)