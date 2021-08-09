---
title : "Adding payment links to order confirmation emails"
meta_title: "Magento 2 plugin FAQ - Adding payment links - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: "faqdetail"
summary: "We have added a feature to include the payment link in the order confirmation mail. This feature is customizable and can be changed to your liking."
read_more: "."
aliases:
    - /magento2/faq/payment-links-in-order-confirmation-for-backend-orders
    - /integrations/magento2/faq/payment-links-in-order-confirmation-for-backend-orders/
---

To add payment links to order confirmation emails and customize settings, follow these steps:

1. Sign in to your Magento 2 backend.
2. Go to **Marketing** > **Email templates**.
3. Under **New order**, import a template.
4. Add the following code snippet to the template:

```
{{depend order.getPayment().getAdditionalInformation('payment_link')}}
<a href="{{var order.getPayment().getAdditionalInformation('payment_link')}}">Pay now with {{var order.getPayment().getAdditionalInformation('method_title')}}</a>
{{/depend}}
```

### Magento 2.3.4+
The email template syntax is different for Magento 2.3.4+. Add this code snippet instead:

```
{{depend order.payment.additional_information.payment_link}}
<a href="{{var order.payment.additional_information.payment_link}}">Pay now with {{var order.payment.additional_information.method_title}}</a>
{{/depend}}
```
### Backend emails
To add payment links to order confirmation emails from your Magento **backend**, you can use the `payment_link` variable and an `if/else` statement in the template. 

### Frontend emails
You cannot add payment links to order confirmation emails created in your **frontend**, but you can dispaly the name of the payment method:

`{{if payment_link}}`
`<a href="{{var payment_link}}">Pay now with {{var order.payment.additional_information.method_title}}</a>`
`{{else}}`
`<p>{{var order.payment.additional_information.method_title}}</p>`
`{{/if}}`

1. Go to **Stores** > **Configuration** > **Sales** > **Sales emails**.
2. Replace the **New order confirmation template** with your template.
3. Test the template to confirm it is working.

**Note:** You can also implement this directly in the email template files.

