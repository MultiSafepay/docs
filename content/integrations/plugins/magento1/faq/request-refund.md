---
title : "Issue a refund"
meta_title: "Magento 1 plugin refunding - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---
Yes, it is possible to refund order or process a credit memo from the backend. Follow these steps:

1. Please ensure an API key has been provided under _System_ -> _Connect Settings_ and that the option Credit Memo has been enabled
2. Go to the order in the Magento backend for which you’d like to issue a refund
3. Click the _Invoices_ tab on the left of the _Order Overview_
4. Open the invoice, and click on _Credit memo_ located at the top right of the overview
5. Once the desired refunds/adjustments have been provided and made, click on _Refund Online_ so we can receive the request.

Further information on issuing a refund available in the [Magento 1](https://docs.magento.com/m1/ce/user_guide/order-processing/credit-memo-create.html) user guide. 

> Issuing a refund for AfterPay, Klarna, Pay After Delivery, Betaal per Maand or E-Invoicing in the Magento 1 ecommerce platform is possible. However, this can only be processed by selecting an item. It is not possible to credit an amount from the Magento 1 backend.

**Warning: If an amount is specified instead of an item selected, the entire order will be refunded.**
 





