---
title : "Providing track-and-trace codes"
meta_title: "Betaal per Maand - Providing track-and-trace codes - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
read_more: "."
weight: 
---

You can provide track-and-trace codes to MultiSafepay:

- In your [MultiSafepay account](https://merchant.multisafepay.com) when you [change the order status to Shipped](/payments/methods/billing-suite/betaalpermaand/faq/changing-order-status-to-shipped/)  

  **or**  

- Via our API. Make a `PATCH /orders` request to change the order status to **Shipped** and provide the track-and-trace code. For more information, see API reference – [Update an order](https://docs.multisafepay.com/api/#update-an-order).