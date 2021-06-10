---
title : "Processing refunds"
meta_title: "Magento 1 plugin - Processing refunds - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases: 
    - /integrations/magento1/faq/request-refund/
---
To process a refund or a credit memo from your backend, follow these steps:

1. Log in to your Magento 1 backend. 
2. Go to **System** > **Connect settings**.
3. Check that you have:
    - Entered an [API key](/faq/general/multisafepay-glossary/#api-key)
    - Enabled the **Credit Memo** option
4. Search for and open the order you want to refund.
5. Click the **Invoices** tab on the left of the **Order overview**.
6. Open the invoice, and click **Credit memo** at the top right of the overview.
7. Enter the refund amount, and then click **Refund online** to send the request to MultiSafepay.

For more information, see Magento - [Create a credit memo](https://docs.magento.com/m1/ce/user_guide/order-processing/credit-memo-create.html). 

For AfterPay, Klarna, Pay After Delivery, Betaal per Maand, and E-invoicing, you can only refund a selected item from the order, not a set amount. If you enter an amount instead of selecting an item, the entire order is refunded.
 





