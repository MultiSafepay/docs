---
title : "Setting order lifetimes for Second Chance"
meta_title: "Magento 2 plugin FAQ - Setting order lifetimes for Second Chance - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
read_more: "."
---

[Second Chance](/payments/boost/second-chance/) emails are sent 1 hour and 24 hours after the order was created. By default, the status of Magento 2 orders changes from **Pending payment** to **Cancelled** after 8 hours (480 minutes).

If the customer pays via the **second** email (24 hours later), the payment is processed but the transaction update may not be handled correctly in Magento 2 because the order has expired. This may cause issues with external services (e.g. ERP/inventory management), if items are low in stock, or for one-off products like antiques.

To avoid this, you must match the order lifetime to the MultiSafepay payment link lifetime in your [backend](/getting-started/glossary/#backend).

We recommend setting the lifetimes to 2 days (2880 minutes) to allow enough time for the customer to pay, but to avoid issues with external services. 


## Setting the Magento 2 order lifetime

1. Sign in to your backend.
2. Go to **Stores** > **Configuration** > **Sales** > **Sales** > **Orders cron settings**.
3. Select **Pending payment order lifetime (minutes)** and set to **2880 minutes**.

## Setting the MultiSafepay payment link lifetime

1. From your Magento 2 admin panel, go to **Stores** > **Configuration** > **MultiSafepay** > **Payment gateways**.
2. Select the relevant gateway, and then go to **Custom payment link lifetime**.
3. Select **Pending payment order lifetime** and set to **2880 minutes**.

