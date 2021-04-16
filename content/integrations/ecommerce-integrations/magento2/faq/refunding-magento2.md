---
title : "Can I refund orders?"
meta_title: "Magento 2 plugin FAQ - Refund - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
layout: "faqdetail"
read_more: "."
aliases: [/integrations/magento2/faq/refunding-magento2/]
---
Yes, it is possible to refund orders or credit memos from within the Magento 2 backend.  

In the Magento backoffice, go to the _Invoices_ tab, click on the invoice that was created by MultiSafepay, and then click _Credit Memo_. Now you see 2 refund buttons:
* Offline refund: refund request will not be sent to MultiSafepay
* Refund: a refund request will be sent to MultiSafepay.

You can also refund from your [MultiSafepay Control](https://merchant.multisafepay.com)

{{< blue-notice >}}
If you have just upgraded from the deprecated plugin to the new one, please note that refunding the orders with a payment method from the deprecated plugin is not possible inside Magento, because the payment method is not available anymore. These orders can be refunded via [MultiSafepay Control](https://merchant.multisafepay.com) instead.
{{< /blue-notice >}}

{{< blue-notice >}}
Refunding from the Magento 2 backend is disabled when the order has a Fooman Surcharge. It is still possible to refund those orders through [MultiSafepay Control](https://merchant.multisafepay.com)
{{< /blue-notice >}}

If you have more questions about refunds, please check out our [FAQ on refunds](/faq/refunds).
