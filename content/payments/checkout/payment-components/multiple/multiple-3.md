---
title : "Step 3: Redirect to pay"
breadcrumb_title : "Step 3"
meta_title: "Payment Components - Integrating multiple payment methods step 3 - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
layout: 'single'
read_more: '.'
--- 

## Handle the interaction

{{< blue-notice >}} This step only applies if using your own or an existing payment button. {{< /blue-notice >}}

**1.** Assign the button element to a variable:

```
const paymentButton = document.querySelector('#payment-button');
```

**2.** Create an event handler for the payment button:

- When the customer clicks the payment button, call the `getPaymentData()` method.
- Send the response to the call to your server (`createOrder`) to create an order (see [Create an order](#create-an-order)).
- Return the reponse from your server to the client-side to redirect the customer.

```
paymentButton.addEventListener('click', e => {
    paymentButton.addAttribute('disabled');
    if (PaymentComponent.hasErrors()) {
        let errors = PaymentComponent.getErrors();
        console.log(errors);
        return false;
    }
    createOrder(PaymentComponent.getPaymentData()).then(response => {
        if(!response || !response.success) {
            paymentButton.removeAttribute('disabled');
            console.log(response);
        } else {
            PaymentComponent.init('redirection', {
                order: response.data
            });
        }
    });
});
```

**Note:** When using your own payment button, if the customer clicks it again during the latency before redirection, this creates duplicate orders. 

To avoid duplicate orders, disable the button until you have attempted to create an order. Then, check `response.success`:

- If `true`, don't re-enable the button and proceed to the redirect.
- If `false`, re-enable the button for the customer to try again. 

{{< details title="Redirect to 3D verification" >}}

The `init('redirection')` method redirects customers that pay with credit card to the relevant page.

If 3D Secure verification is:

- Required, the customer is first directed to 3D Secure. If successful, they are then redirected to the `redirect_url`. 

- Not required, the customer is redirected to the `redirect_url`.

{{< /details >}}

{{< details title="Redirect bank transfer payments" >}}

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

## Create an order

Make a POST [`/orders`](/api/#orders) request from your server:

- Append the `payment_data` collected from the Payment Component UI to the `orderData` collected during the checkout process.
- Replace the `<GATEWAY>` placeholder with the relevant gateway code, see Step 2: [Initialize the payment component](#initialize-the-payment-component).

```
curl -X POST "https://testapi.multisafepay.com/2/json/orders" \
--header "accept: application/json" \
--header "Content-Type: application/json" \
--header "api_key: <your-website-API-key>" \
--data-raw '{
    "type": "direct",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 10000,
    "description": "Test order description",
...
    "payment_data": {
       "payload": "{secure_payload}"
    },
}'
```

{{< two-buttons

href-1="/payments/checkout/payment-components/multiple/multiple-2" header-1="Back" text-1="Step 2: Initialize" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/payments/checkout/payment-components/multiple/multiple-4" header-2="Next" text-2="Step 4: Go live" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}


