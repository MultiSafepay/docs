---
title : "Processing refunds"
meta_title: "Lightspeed app - Processing refunds - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /hosted/lightspeed_app/faq/refunding-lightspeed
    - /integrations/hosted/lightspeed_app/faq/refunding-lightspeed
    - /integrations/lightspeed_app/faq/refunding-lightspeed
---

You can refund orders and issue credit notes in your [MultiSafepay Control](https://merchant.multisafepay.com) and from your Lightspeed backend.

To enable refunds from your Lightspeed backend, follow these steps:

1. Log in to lightspeed.multisafepay.com.
2. Go to **Settings**.
3. In the sidebar, click **Enable refunds**.

## Known issues

- When creating a credit memo for a refund, set the status to **Not paid**. MultiSafepay ignores **Paid** status.

- When a refund is created in your lightspeed backend, a short message appears in the notes section of the order. Any errors are explained here.

- Some [billing suite](https://docs.multisafepay.com/payment-methods/billing-suite/) payment methods do not let you refund a partial amount and a full item in a single request, e.g.: a shopping cart contains 3 items for a total of 1.70 EUR. If you refund 1 item and 0.40 EUR, it fails. Make sure you refund items and amounts separately.

- You cannot issue multiple refunds for the same amount within 5 minutes of each other, even for different items. 

For any questions, email the Integration Team at <integration@multisafepay.com>
