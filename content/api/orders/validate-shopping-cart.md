---
weight: 210
meta_title: "API Reference - Validate shopping cart - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#validate-the-shopping-cart
---
{{< code-block >}}

```json 
{
  "checkout_options":{
    "validate_cart":true
  }
}
```

{{< /code-block >}}

{{< description >}}

### Validate shopping cart

Applies to non-[post payment](/payments/methods/billing-suite/) methods.

**Parameters**

----------------
`checkout_options` | object | required

Contains:  

`validate_cart` | boolean | required

If set to `true`, the value of `amount` is compared with the calculated total value of the shopping cart.  

Returned as `order_total`.

If the values match, the request is submitted.

If the values don't match, the request is not submitted and `error_code` **1027** is returned.

----------------

{{< /description >}}