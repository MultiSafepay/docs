---
title : "Processing refunds"
meta_title: "Lightspeed app - Processing refunds - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /hosted/lightspeed_app/faq/refunding-lightspeed
    - /integrations/hosted/lightspeed_app/faq/refunding-lightspeed
    - /integrations/lightspeed_app/faq/refunding-lightspeed
---
Refund rules:

- From your [MultiSafepay account](https://merchant.multisafepay.com): [Full and partial refunds](/payments/refunds/) and credit notes
- From your Lightspeed [backend](/getting-started/glossary/#backend):  
    - Refunds and credit notes 
    - Refunding more than the original transaction is **not** supported

To enable refunds from your Lightspeed backend, follow these steps:

1. Sign in to your Lightspeed app.
2. Go to **Settings**.
3. In the sidebar, click **Enable refunds**.

**Known issues**

- If you use Lightspeed [Retail](https://www.lightspeedhq.nl/kassasysteem/retail/), you cannot process refunds via MultiSafepay.

- When creating a credit memo for a refund, set the status to **Not paid**. MultiSafepay ignores **Paid** status.

- When a refund is created in your Lightspeed backend, a short message appears in the notes section of the order. Any errors are explained here.

- Refunds created in your MultiSafepay account are not reported back to Lightspeed. Under **Offline actions**, an error appears: "Already a completed transaction".

- Some [billing suite](https://docs.multisafepay.com/payment-methods/billing-suite/) payment methods do not let you refund a partial amount and a full item in a single request, e.g.: a shopping cart contains 3 items for a total of 1.70 EUR. If you refund 1 item and 0.40 EUR, it fails. Make sure you refund items and amounts separately.

- You cannot issue multiple refunds for the same amount within 5 minutes of each other, even for different items. 

- Some [billing suite](https://docs.multisafepay.com/payment-methods/billing-suite/) payment methods require us to provide product ids related to the refunded items. When using product variants make sure the variants have different ids from each other and the default product. With duplicate ids we cannot distinguish what items need to be refunded.

For any questions, email the Integration Team at <integration@multisafepay.com>
