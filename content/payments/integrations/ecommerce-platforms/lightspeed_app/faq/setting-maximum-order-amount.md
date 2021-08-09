---
title : "Setting a max/min order value to display payment methods"
meta_title: "Lightspeed app - Setting a max/min order value to display payment method - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /integrations/ecommerce-integrations/lightspeed_app/faq/maximal-order-amount/
    - /payments/integrations/ecommerce-platforms/lightspeed_app/faq/setting-minimum-order-amount/
---
To set a maximum/minimum order amount for a payment method to display on your checkout page, follow these steps:

1. In the **Payment methods ordering** list, click the **+** button to open the relevant payment method.
2. Enter an amount in EUR cents in the:  
    - **Maximum** field. E.g. A maximum value of 1500 cents means the payment method only appears on the checkout page if the total order amount is **less** then 15 EUR. If you **don't** want a maximum amount, enter **-1**.
    **OR**
    - **Minimum** field. E.g. A minimum value of 1500 cents means the payment method only appears on the checkout page if the total order amount is **more** then 15 EUR.

### Setting a maximum/minimum order amount per language

To set different maximum/minimum order amounts for different languages, under the **Payment methods ordering** header > **Country** dropdown menu, select a country and set the maximum/minimum amount per language.

If no specific rule is set for a language, **Default** language is used.



