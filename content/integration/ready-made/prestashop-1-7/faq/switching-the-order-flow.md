---
title : "Switching the order flow"
meta_title: "PrestaShop 1.7 - Switching the order flow - MultiSafepay Docs"
read_more: "."
url: "/prestashop-1-7/order-flow/"
---

Because PrestaShop does not give any guidelines about an order needing to be created before or after a transaction has been completed, we give you the option to switch between two flows:
1. Creating the order before the actual payment has been finalized.
2. Creating the order after the payment has been finalized. 

Both of these flows have their upsides and downsides.

In the first flow, the order confirmation emails are sent before the payment is finalized, unless you disable this. Also orders that are initialized by a customer but not completed will eventually receive the status: "Cancelled".

In the second flow, the order is being created through a notification send by MultiSafepay. After payment the customer will be redirected to the order confirmation page, and if the notification has not been processed yet, it will show a waiting page with a loader, while the order is being created. Also because the order does not exist yet we are using the cart id instead of order reference to create the order within MultiSafepay.

To change the flow you are using, follow these steps:

1. Sign in to your PrestaShop 1.7 [backend](/glossaries/multisafepay-glossary/#backend).
2. Go to **Improve** > **Module manager** > **MultiSafepay**.
3. In the MultiSafepay module, go to the **General settings** tab.
4. Change the **Create order before payment** field to your desired flow.
5. Click **Save**.
