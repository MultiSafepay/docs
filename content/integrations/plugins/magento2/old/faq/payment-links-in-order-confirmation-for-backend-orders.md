---
title : "Payment link in order confirmation email for backend orders"
meta_title: "Magento 2 plugin FAQ - Payment links - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
layout: "faqdetail"
summary: "As of version 1.7.0, we have added a feature to include the payment link in the order confirmation mail for orders created in the backend. This feature is customizable and can be changed to your liking."
read_more: "."
aliases:
    - /magento2/faq/payment-links-in-order-confirmation-for-backend-orders
---

As of version 1.7.0, we have added a feature to include the payment link in the order confirmation mail for orders created in the backend. This feature is customizable and can be changed to your liking. This feature can be implemented by the following steps:

1. Login into your Magento backend. Check how we do it [here](/integrations/plugins/magento2/old/) in step 3. 
2. Go to _Marketing_ -> _Email Templates_
3. Add a template (import from _new order_)
4. Add this sample code the template
</br>
`{{depend order.getPayment().getAdditionalInformation('payment_link')}}`
`<a href="{{var order.getPayment().getAdditionalInformation('payment_link')}}">Pay now with {{var order.getPayment().getAdditionalInformation('method_title')}}</a>`
`{{/depend}}`\
</br>\
The email template syntax is different for Magento 2.3.4+. For these versions you can add this sample code instead
</br>
`{{depend order.payment.additional_information.payment_link}}`
`<a href="{{var order.payment.additional_information.payment_link}}">Pay now with {{var order.payment.additional_information.method_title}}</a>`
`{{/depend}}`\
</br>
5. Go to _Stores -> Configuration → Sales → Sales Emails_
6. Change the "New Order Confirmation Template" with your template
7. After these changes, the template should be tested to confirm it is working.

_Note: This can also be implemented directly in the email template files._

