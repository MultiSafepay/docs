---
title : "Step 1: Add the elements"
breadcrumb_title : "Step 1"
meta_title: "Payment Components - Integrating a single payment method step 1 - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: 'single'
read_more: '.'
aliases:
    - /payments/checkout/payment-components/integrating-single-payment-method
--- 

Add the following elements to your checkout page:

**1.** Add the Payment Component CSS to the `<head>` of your checkout page:  
```
<link rel="stylesheet" href="https://pay.multisafepay.com/sdk/components/v2/components.css">
```

**2.** Add the Payment Component script to the bottom of the `<body>` of your checkout page:  
```
<script src="https://pay.multisafepay.com/sdk/components/v2/components.js"></script>
```

**3.** Add the DOM element for the Payment Component UI in the `<body>` of your checkout page:
```
<div id="MultiSafepayPayment"></div>
```

## Next steps

- Step 2: [Initialize the component](/payments/checkout/payment-components/single/single-2)
- Step 3: [Create an order](/payments/checkout/payment-components/single/single-3)
- Step 4: [Go live](/payments/checkout/payment-components/single/single-4)

{{< two-buttons

href-1="/payments/checkout/payment-components/single" header-1="Back" text-1="Integrating a single payment method" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/payments/checkout/payment-components/single/single-2" header-2="Next" text-2="Step 2: Initialize the component" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}



