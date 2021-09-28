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

Make a POST [`/orders`](/api/#orders) request from your server:

- Append the `payment_data` collected from the Payment Component UI to the `orderData` collected during the checkout process.
- Replace the `<GATEWAY>` placeholder with the relevant gateway code, see Step 2: [Initialize the payment component](#initialize-the-payment-component).

```
curl -X POST "https://testapi.multisafepay.com/v2/json/orders" \
--header "accept: application/json" \
--header "Content-Type: application/json" \
--header "api_key: <your-website-API-key>" \
--data-raw '{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "<GATEWAY>",
    "currency": "EUR",
    "amount": 100,
    "description": "Test order description",
...
    "payment_data": {
       "payload": "{secure_payload}"
    },
}'
```

## Redirect the customer

**1.** From your server, pass the response to the `POST /orders` request to the customer's device. 

**2.** Check that `response.success` is `true`.

**3.** Handle the response:

{{< details title="Bank transfer payments" >}}

In the `gateway_info` object, you receive the bank account details for the customer to wire the funds to.

Then render the account details in the interface for the customer with clear instructions. (MultiSafepay also emails these details to the customer.)

**Example gateway_info object**
```
{
  "gateway_info":{
    "mtpinfo":"NL25DEUT7351811717",
    "reference":"9202124254788300",
    "issuer_name":"Sofortbank",
    "destination_account_id":"003001380000",
    "destination_holder_name":"MultiSafepay",
    "destination_holder_city":"Zurich",
    "destination_holder_country":"CH",
    "destination_holder_iban":"NL25DEUT7351811717",
    "destination_holder_swift":"DEUTCHZZ",
    "account_holder_name":"testperson-nl approved",
    "account_holder_city":"gravenhage",
    "account_holder_coutry":"NL"
  }
}
```
{{< /details >}}
{{< details title="Other payment methods" >}}
Call the `PaymentComponent.init()` method using the following arguments:
```
PaymentComponent.init('redirection', {
    order: response.data
});
```

If 3D Secure verification is:

- Required, the customer is first directed to 3D Secure. If successful, the customer is then redirected to the `redirect_url`. 
- Not required, the customer is redirected to the `redirect_url`.

{{< /details >}}

{{< two-buttons

href-1="/payments/checkout/payment-components/single/single-2" header-1="Back" text-1="Step 2: Initialize" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/payments/checkout/payment-components/single/single-4" header-2="Next" text-2="Step 4: Go live" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}

