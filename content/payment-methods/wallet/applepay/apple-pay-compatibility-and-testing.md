---
title: "Apple Pay Compatibility and Testing"
weight: 25
meta_title: "Apple Pay Compatibility and Testing - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: '.'
---

## Compatibility and Testing
#### Testing with supported devices

It is important to note that Apple Pay is only compaible with a select number of [Apple devices](https://support.apple.com/en-us/HT208531)

It is worthy to mention that Apple Pay is also only compatible with the Safari browser. Other browsers such as Chrome and Firefox are not supported due to security reasons. Apple Pay testing can only therefore be carried out on supported devices and the Safari browser.

Instructions on how to use Apple Pay can be found directly on the offical [Apple website](https://support.apple.com/en-us/HT201239)

#### Testing without an Apple device

If you do not own an Apple device and would still like to test Apple Pay, we would reccomend using [Appetize.io](https://appetize.io/)

This emulator allows the pretransaction to be created when ordering and using the payment method Apple Pay. When attempting to complete the order, you will be blocked on the MultiSafepay payment page with the error "this device is not supported" but the pretransaction with Apple Pay as a gateway will be created to check whether a connection to our server exists. However, it is not possible to fully complete the test transaction.