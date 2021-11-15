---
title : "Hiding shopping cart details on payment pages"
weight: 50
meta_title: "Hiding shopping cart details on payment pages - MultiSafepay Docs"
read_more: '.'
url: '/payment-pages/hiding-shopping-cart/'
---

For payment methods that include a shopping_cart object in the `POST /orders` request, the cart details are displayed on the payment page by default. That is, all items in the customer's order, with the price and VAT for each. 

{{< details title="Applicable payment methods" >}}

- AfterPay
- E-Invoicing
- In3
- Klarna
- Pay After Delivery

{{< /details >}}

To hide shopping cart details on payment pages:

**1.** Request the Integration Team to enable **Advanced website templates** in your MultiSafepay account. Email <integration@multisafepay.com>

**2.** Sign in to your [MultiSafepay account](https://merchant.multisafepay.com/). 

**3.** Go to **Settings** > **New payment pages**.

**4.** Next to the relevant website, click **Template**.

**5.** Under **Configure page style**, click **Settings**, and then select the **Hide cart details** checkbox. 

For support, email the Integration Team at <integration@multisafepay.com>