---
title : "Providing track-and-trace codes"
meta_title: "Betaal per Maand - Providing track-and-trace codes - MultiSafepay Docs"
read_more: "."
weight: 
url: '/payment-methods/betaal-per-maand/track-and-trace/'
aliases:
    - /payments/methods/billing-suite/betaalpermaand/user-guide/providing-track-and-trace/
---

You can provide track-and-trace codes to MultiSafepay:

- In your [MultiSafepay account](https://merchant.multisafepay.com) when you [change the order status to Shipped](/payments/methods/billing-suite/betaalpermaand/faq/changing-order-status-to-shipped/)  

  **or**  

- Via our API. Make a `PATCH /orders` request to change the order status to **Shipped** and provide the track-and-trace code. For more information, see API reference – [Update an order](https://docs.multisafepay.com/api/#update-an-order).