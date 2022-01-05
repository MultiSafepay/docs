---
title: "Direct vs redirect API requests"
weight: 1
meta_title: "Direct vs redirect API requests - MultiSafepay Docs"
read_more: "."
url: '/developer/direct-vs-redirect/'
aliases:
    - /faq/api/difference-between-direct-and-redirect
    - /developer/api/difference-between-direct-and-redirect/
---
With our API, you can make requests to create direct transactions and redirect transactions.

{{< mermaid class="text-center" >}}

flowchart LR
    id1(Redirect request)--> id2{Is the gateway <br> specified?}
    id2{Is the gateway <br> specified?}-- Yes --> id4(Customer is redirected to <br> MultiSafepay payment page <br> tailored to payment method)
    id2{Is the gateway <br> specified?}-- No --> id5(Customer is redirected to <br> MultiSafepay payment page <br> displaying all activated <br> payment methods)
    id4(Customer is redirected to <br> MultiSafepay payment page <br> tailored to payment method)--> id6{Is further customer <br> action required?}
    id5(Customer is redirected to <br> MultiSafepay payment page <br> displaying all activated <br> payment methods)--> id9[/Customer selects <br> payment method/]
    id9[/Customer selects <br> payment method/]--> id6{Is further customer <br> action required?}
    id10(Direct request: <br> Gateway required )--> id6{Is further customer <br> action required?}
    id6{Is further customer <br> action required?}-- No --> id7(Customer is redirected to <br> success page)
    id6{Is further customer <br> action required?}-- Yes --> id8(Customer is redirected to <br> payment method)
    id8(Customer is redirected to <br> payment method)--> id7(Customer is redirected to <br> success page)

    style id1 fill: #ffe599, stroke: #ffe599
    style id2 fill: #9fc5e8, stroke: #9fc5e8
    style id4 fill: #9fc5e8, stroke: #9fc5e8
    style id5 fill: #9fc5e8, stroke: #9fc5e8
    style id6 fill: #9fc5e8, stroke: #9fc5e8
    style id7 fill: #9fc5e8, stroke: #9fc5e8
    style id8 fill: #9fc5e8, stroke: #9fc5e8
    style id9 fill: #9fc5e8, stroke: #9fc5e8
    style id10 fill: #ffe599, stroke: #ffe599

{{< /mermaid >}}

&nbsp;  

Direct requests connect directly to the payment method, whereas redirect requests first send the customer to a [MultiSafepay payment page](/payment-pages/).

For redirect requests, if the gateway for a specific payment method is:

- Provided, the payment page is tailored for that payment method, e.g. for Visa, the page includes fields for the customer to enter their credit card details. 
- Not provided, the payment page displays all payment methods 

Then, if further customer action is:

- Required, they are redirected to complete payment, e.g. for iDEAL the customer is redirected to their online banking environment. 
- Not required, the transaction is completed automatically. 

If you provide a [redirect URL](/developer/api/redirect-url/), after completing payment, the customer is then directed to your success/thank you page.

For more information about the direct and redirect flows for a specific payment method, see the **Payment flow** section on the relevant [payment method](/payment-methods/) page.

