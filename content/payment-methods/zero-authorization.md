---
title: Zero Authorization
category:
  uri: Payment methods
slug: zero-authorization
position: 9
privacy:
  view: public
parent:
  uri: cards
---
Zero Authorization is a MultiSafepay solution that lets you verify a card without charging the cardholder. Simply charge an amount of 0 EUR to the card (with or without [3D Secure](/docs/3ds2/) authentication).

MultiSafepay stores the sensitive payment details as a non-sensitive token, and then checks if the card is legitimate.

You can then also use tokens for [recurring payments](/docs/recurring-payments/).

# Activation

Email a request to activate Zero Authorization to [sales@multisafepay.com](mailto:sales@multisafepay.com)

# Integration

Zero Authorization supports Maestro, Mastercard, and Visa, and is available in all countries and currencies.

### Via our API

* API reference – [Create order](/reference/createorder/) > Card order
* API recipe – <a href="https://docs.multisafepay.com/recipes/verify-a-card-with-zero-authorization" target="_blank">Verify a card with Zero Authorization</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }}></i> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.

**Via ready-made integrations:** Zero Authorization is not supported in our [ready-made integrations](/docs/our-integrations/) by default, but you can customize it via our API.<br />

***

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)