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

In our API, you can make direct and redirect requests.

{{< mermaid class="text-center" >}}

flowchart TD
    id1(Direct request)--> id3(Is further customer action required?)
    id2(Redirect request)--> id4(MultiSafepay payment page)
    id4(MultiSafepay payment page)--> id3(Is further customer action required?)
    id3(Is further customer action required?)--> id5(Yes) & id6(No)
    id5(Yes)--> id7(Redirects customer to payment method)
    id6(No)--> id8(Transaction completed)
    id7(Redirects customer to payment method)--> id8(Transaction completed)
    id8(Transaction completed)--> id9(Redirects customer to your success page)
    style id1 fill: #b4a7d6, stroke: #b4a7d6
    style id2 fill: #b6d7a8, stroke: #b6d7a8
    style id3 fill: #9fc5e8, stroke: #9fc5e8
    style id4 fill: #ffe599, stroke: #ffe599
    style id5 fill: #9fc5e8, stroke: #9fc5e8
    style id6 fill: #9fc5e8, stroke: #9fc5e8
    style id7 fill: #9fc5e8, stroke: #9fc5e8
    style id8 fill: #9fc5e8, stroke: #9fc5e8
    style id9 fill: #9fc5e8, stroke: #9fc5e8

{{< /mermaid >}}
&nbsp;  

Direct requests connect directly to the payment method, whereas redirect requests send the customer to a [MultiSafepay payment page](/payment-pages/).

If further customer action is:

- Required, they are redirected to complete payment, e.g. for iDEAL the customer is redirected to their online banking environment. 
- Not required, the transaction is completed automatically. 

If you provide a [redirect URL](/developer/api/redirect-url/), after completing payment, the customer is then directed to your success/thank you page.

For more information about the direct and redirect flows for a specific payment method, see the **Payment flow** section on the relevant [payment method](/payment-methods/) page.

