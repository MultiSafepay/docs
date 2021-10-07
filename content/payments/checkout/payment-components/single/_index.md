---
title : "Integrating a single payment method"
breadcrumb_title : "Integrating a single payment method"
meta_title: "Payment Components - Integrating a single payment method step 1 - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: 'single'
read_more: '.'
url: '/payment-components/single/'
aliases:
    - /payment-components/integrating-single-payment-method
--- 

## Step 1: Add the elements

Add the following elements to your checkout page:

**1.** Add the component's CSS to the `<head>` of your checkout page:  
```
<link rel="stylesheet" href="https://testpay.multisafepay.com/sdk/components/v2/components.css">
```

**2.** Add the component's script to the bottom of the `<body>` of your checkout page:  
```
<script src="https://testpay.multisafepay.com/sdk/components/v2/components.js"></script>
```

**3.** Add the DOM element for the component's UI in the `<body>` of your checkout page:
```
<div id="MultiSafepayPayment"></div>
```

## Next steps

- Step 2: [Initialize the component](/payment-components/single/step-2)
- Step 3: [Create an order](/payment-components/single/step-3)
- Step 4: [Go live](/payment-components/single/step-4)

{{< two-buttons

href-1="/payment-components/" header-1="Back" text-1="Payment Components" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/payment-components/single/step-2" header-2="Next" text-2="Step 2: Initialize the component" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}



