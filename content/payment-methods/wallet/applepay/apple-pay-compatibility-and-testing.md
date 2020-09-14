---
title: "Apple Pay Compatibility and Testing"
weight: 25
meta_title: "Apple Pay Compatibility and Testing - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

## Compatibility and Testing
#### Testing with supported devices

It is possible to carry out testing with Apple Pay. Please follow these instructions:

1. Contact <integration@multisafepay.com> to activate Apple Pay
2. Activate Apple Pay in your backend environment
3. During checkout, select Apple Pay as a payment method.
4. The payment screen will appear with payment details. Click on the Apple Pay button (_You can ignore the 'Device is not supported' text_)
5. Complete the payment using real card data. (_No actual payment will be taken_)
6. The transaction is completed

It is important to note that Apple Pay is only compaible with a select number of [Apple devices](https://support.apple.com/en-us/HT208531)

It is worthy to mention testing with Apple Pay can only be conducted when the following requirements are met:

1. A [compatible](https://support.apple.com/en-us/HT208531) device is being used
2. A Safari browser is being used
3. The website is using HTTPS

If one of these requirments is not met, Apple Pay will not appear on the checkout page.

Instructions on how to use Apple Pay can be found directly on the offical [Apple website](https://support.apple.com/en-us/HT201239)

#### Testing without an Apple device

If you do not own an Apple device and would still like to test Apple Pay, we would reccomend using [Appetize.io](https://appetize.io)

This emulator allows the pretransaction to be created when ordering and using the payment method Apple Pay. When attempting to complete the order, you will be blocked on the MultiSafepay payment page with the error "this device is not supported" but the pretransaction with Apple Pay as a gateway will be created to check whether a connection to our server exists. However, it is not possible to fully complete the test transaction.