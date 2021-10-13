---
title : "Integrating the previous release"
breadcrumb_title : "Step 4"
meta_title: "Payment Components - Integrating the previous release step 4 - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: 'single'
read_more: '.'
url: '/payment-components/previous-release/step-4/'
--- 

## Step 4: Go live

When you're ready to process real payments, make the following changes:

**1.** In Step 2: [Construct the component object](/payment-components/previous-release/step-2/#construct-the-component-object), change the environment from `test` to `live`:
```
PaymentComponent = new MultiSafepay({
    env: 'live',
    apiToken: apiToken,
    order: orderData
});
```


**2.** In Step 3: [Create an order](/payment-components/previous-release/step-3), change the test endpoint to the live endpoint:  

`https://api.multisafepay.com/v1/json/orders`


{{< two-buttons

href-1="/payment-components/previous-release/step-3/" header-1="Back" text-1="Step 3: Create an order" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/payment-components/customization" header-2="Next" text-2="Customizing Payment Components" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}