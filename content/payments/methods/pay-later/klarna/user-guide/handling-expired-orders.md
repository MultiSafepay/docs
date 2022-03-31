---
title : "Handling expired orders"
meta_title: "Klarna - Handling expired orders - MultiSafepay Docs"
read_more: "."
weight: 7
url: '/payment-methods/klarna/handling-expired-orders/'
---

If you have already shipped an order but it expired because you didn't change the order status to **Shipped** within 28 days, follow these steps: 

1. Sign in to your MultiSafepay dashboard.
2. Go to **Transactions** > **Transaction overview**, and then select the expired transaction.  
3. Click **Payment link**, and then click **Duplicate this order**.
4. On the **Payment link generator** page, click **Generate payment link**. 
5. Send the payment link to the customer. 

**Or**

1. [Create a new order](https://api-docs.multisafepay.com/reference/createorder) > Pay later order > Examples > Klarna redirect.
2. [Ship the order](https://api-docs.multisafepay.com/reference/updateorder) > Ship order.
3. Send the payment link to the customer.