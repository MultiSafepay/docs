---
title : "Processing refunds"
meta_title: "Lightspeed app - Processing refunds - MultiSafepay Docs"

read_more: "."
url: '/lightspeed-app/refunds/'
aliases:
    - /hosted/lightspeed_app/faq/refunding-lightspeed
    - /integrations/hosted/lightspeed_app/faq/refunding-lightspeed
    - /integrations/lightspeed_app/faq/refunding-lightspeed
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/processing-refunds/
---
**Refund rules**  

- From your [MultiSafepay account](https://merchant.multisafepay.com): [Full and partial refunds](/payments/refunds/) and credit notes
- From your Lightspeed eCom [backend](/getting-started/glossary/#backend):  
    - Refunds and credit notes 
    - Refunding more than the original transaction is **not** supported

**Enabling refunds**

To enable refunds from your backend, follow these steps:

1. Sign in to your Lightspeed app.
2. Go to **Settings**.
3. In the sidebar, click **Enable refunds**.
4. Select the relevant setting:
    - Refunds disabled (default)
    - Refunds enabled:
        - Create a refund when the credit memo status is **Unpaid** (default when refunds are enabled).
        - Always create a refund, no matter the credit memo status.

**Notes**

- If you use Lightspeed eCom linked to [Lightspeed Retail](https://www.lightspeedhq.nl/kassasysteem/retail/), to process refunds via MultiSafepay, you must enable the **Always create a refund, no matter the status** setting.

- When creating a credit memo, set the status to **Not paid**. If the **Always create a refund, no matter the status** setting is not enabled, MultiSafepay ignores **Paid** status.

**Known issues**

- For refunds created in your Lightspeed backend, a short message appears in the **Notes** section of the order where any errors are explained.

- Refunds created in your MultiSafepay account are not reported back to Lightspeed. Under **Offline actions**, an error appears: "Already a completed transaction".

- Some [pay later](/payment-methods/billing-suite/) methods require product IDs for each refunded item. When using product variants, make sure each variant has a unique identifier. If you provide duplicate IDs, we cannot distinguish which items to refund.

- Some [pay later](/payment-methods/billing-suite/) payment methods do not let you refund a partial amount and a full item in a single request.  
Example: A shopping cart contains 3 items for a total of 1.70 EUR. If you refund 1 item and 0.40 EUR, it fails. Make sure you refund items and amounts separately.

- Some [pay later](/payment-methods/billing-suite/) payment methods do not let you refund a partial amount and a full item in a single request, e.g. a shopping cart contains 3 items for a total of 1.70 EUR. If you refund 1 item and 0.40 EUR, it fails. Make sure you refund items and amounts separately.

- You cannot issue multiple refunds for the same amount within 5 minutes of each other, even for different items. 

For any questions, email the Integration Team at <integration@multisafepay.com>
