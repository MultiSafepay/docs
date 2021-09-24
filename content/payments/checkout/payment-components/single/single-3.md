---
title : "Step 3: Redirect to pay"
breadcrumb_title : "Step 3"
meta_title: "Payment Components - Integrating a single payment method step 3 - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: 'single'
read_more: '.'
--- 

## Collect payment data
**1.** To collect the customer's payment details from the Payment Component UI, call the `PaymentComponent.getPaymentData()` method:

```
PaymentComponent.getPaymentData()
```

**2.** Pass the `payment_data` to your server.

## Create an order

Make a `POST /orders` request from your server, appending the `payment_data` collected from the Payment Component UI to the `orderData` collected during the checkout process.

See API reference – [Payment Component order](/api/#payment-component-order).

## Redirect the customer

**1.** From your server, pass the response to the `POST /orders` request to the customer's device. 

**2.** Check that `response.success` is `true`.

**3.** Call the `PaymentComponent.init()` method using the following arguments:
```
PaymentComponent.init('redirection', {
    order: response.data
});
```
If the customer needs to perform additional actions, they are redirected to the relevant page, e.g. the `payment_url` or 3D Secure. Then, if successful, they are redirected to the `redirect_url`.

If no further action is required, the customer is redirected to the `redirect_url`.



{{< two-buttons

href-1="/payments/checkout/payment-components/single/single-2" header-1="Back" text-1="Step 2: Initialize" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/payments/checkout/payment-components/single/single-4" header-2="Next" text-2="Step 4: Go live" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

