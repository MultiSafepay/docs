---
title : "Payment link in order confirmation email for backend orders"
meta_title: "Magento 2 plugin FAQ - Checkouts - MultiSafepay support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
layout: "faqdetail"
---

As of version 1.7.0 we have added a feature to include the payment link in the order confirmation mail for orders created in the backend. This feature is customizable and can be changed to your liking. This feature can be implemented by the following steps:

1. Login at your Magento backend. Check how we do it [here](https://docs.multisafepay.com/integrations/magento2/manual/) in step 3. 
2. Go to _Marketing -> Email Templates_
3. Add a template (import from _new order_)
4. Add this sample code the template
</br>
`{{depend order.getPayment().getAdditionalInformation('payment_link')}}`
`<a href="{{var order.getPayment().getAdditionalInformation('payment_link')}}">Pay now with {{var order.getPayment().getAdditionalInformation('method_title')}}</a>`
`{{/depend}}`
</br>
5. Go to _Stores -> Configuration → Sales → Sales Emails_
6. Change the "New Order Confirmation Template" with your template
7. After these changes, the template should be tested to confirm it is working.

_Note: This can also be implemented directly in the email template files._
