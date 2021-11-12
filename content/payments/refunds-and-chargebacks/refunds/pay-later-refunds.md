---
title : "Pay later method refunds"
weight: 40
layout: 'single'
meta_title: "Pay later method refunds - MultiSafepay Docs"
short_description: "Process refunds for pay later payment methods"
read_more: "."
url: '/refunds/pay-later/'
---
## API

Pay later refunds require a `shopping_cart` object in the refund request. 

See API reference – [Refund with shopping cart](/api/#refund-with-shopping-cart).

## Multiple order rules

If you supply multiple order rules with the same `merchant-item-id` and the customer requests a partial refund, this creates a conflict. 

To successfully process partial refunds for the same product with different specifications (e.g. size, color) via the shopping cart, each `merchant-item-id` must be unique.

**Example:** For different-sized products, differentiate the `merchant-item-id` with `-size`: 1001311-xxl, 1001311-m, 1001311-s.