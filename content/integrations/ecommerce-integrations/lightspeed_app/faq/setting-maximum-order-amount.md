---
title : "Setting a maximum order value to display payment methods"
meta_title: "Lightspeed app - Setting a maximum order value to display payment method - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /integrations/ecommerce-integrations/lightspeed_app/faq/maximal-order-amount/
---
To set a maximum order amount for a payment method to display on your checkout page, follow these steps:

1. In the **Payment methods ordering** list, click the **+** button to open the relevant payment method.
2. In the **Maximum** field, enter an amount in EUR cents. If you **don't** want a maximum amount, enter **-1**.

**Example:** A maximum value of 1500 cents means the payment method only appears on the checkout page if the total order amount is **less** then 15 EUR.

### Setting a maximum order amount per language

To set different maximum order amounts for different languages, under the **Payment methods ordering** header > **Country** dropdown menu, select a country and set the maximum amount per language.

If no specific rule is set for a language, **Default** language is used.
