---
title: "FastCheckout iOS SDK"
category: 62962df622e99600810c117d
order: 3
hidden: true
slug: 'fastcheckout-ios'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/1281f9320696f2d256d0859421ec2cfa2350e644/static/logo/Integrations/Fastcheckout_iOS.svg" width="100" align ="right"/>

The FastCheckout iOS SDK enables a fast, frictionless, native checkout experience by storing and reusing customer data.

<a href="https://github.com/MultiSafepay/fastcheckout-ios-sdk" target="_blank">View on GitHub</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>

# How it works

Simply provide a valid transaction ID or [create an order](/reference/createorder/). The SDK generates the checkout automatically and sends status updates for each transaction.

The checkout flow includes:

1. Shipping: Select a saved address, or add new shipping details.
2. Billing: Select saved payment details or a gift card, or add new payment details.
3. Confirmation: Confirm the order.

The SDK provides the following features:

- Secure sign up and sign in functionality
- Open seamless support tickets for specific orders

For more information, see the documentation in the SDK, which contains all classes, methods, and troubleshooting.

For how to create, update and retrieve orders, see the [API reference](/reference/introduction/).

# Preview

See how to:

<details id="sign-in-with-registered-email">
<summary>Sign in with registered email address</summary>
<br> 

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-ios-1.png" width="300">

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-ios-2.png" width="300">

</details>

<details id="sign-in-with-unregistered-email">
<summary>Sign in with unregistered email address</summary>
<br> 

The customer is automatically redirected to the **Register** screen: 

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-ios-3.png" width="300">

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-ios-4.png" width="300">

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-ios-5.png" width="300">

</details>

<details id="change-email">
<summary>Change an email address</summary>
<br> 

1. If a registered customer changes their email address, the SDK automatically sends a new security code to the email provided: 

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-ios-6.png" width="300">
    
<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-ios-7.png" width="300">

2. If the security code is received via SMS, it is automatically added to the appropriate field, or the customer enters the code. 

3. The customer enters a new PIN. 

4. The SDK provides biometric options, including face recognition:

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-ios-8.png" width="300">

</details>

<details id="place-order">
<summary>Place an order</summary>
<br> 

1. The **Delivery** screen contains available shipping options. 

2. When the customer clicks **Continue**, the SDK moves to the **Payment** screen.  

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-ios-9.png" width="300">

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-ios-10.png" width="300">

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-ios-11.png" width="300">
    
3. Once payment is complete, the SDK proceeds to the **Transaction complete** screen. The SDK callback notifies the client app of the <<glossary:transaction status>>. 

4. The customer clicks **Back to shop**.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/fastcheckout-ios-12.png" width="300">

</details>

# Requirements

- Xcode 12.0 and iOS 15 SDK
- iOS 9+ target
- Swift 5.3 or Objective-C

# Installation

1. Copy your [site API key](/docs/sites#site-id-api-key-and-security-code) to get the SDK from our <a href="https://github.com/MultiSafepay/fastcheckout-ios-sdk" target="_blank">GitHub repository</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>.
2. Add the FastCheckoutKit.xcframework as an embedded framework into your project. 
3. In Finder, open the folder where you downloaded FastCheckoutKit.framework to, and then drag it into the Project Navigator of your application’s Xcode project.
4. If you haven't already copied the framework into your project folder, click **Copy items**.
5. In the Project navigator (blue project icon), select your application project to navigate to target configuration window, and then under **Targets** in the sidebar, select the application target.
6. In the tab bar at the top of that window, open the **General** panel.
7. Under **Embedded binaries**,click **+**.
8. Select **FastCheckoutKit.xcframework**.

> **✅ Success!**
> You can now start using the FastCheckoutKit SDK in your app.

# How to integrate

To integrate the FastCheckout iOS SDK into your app, follow these steps:

1. Set up the iOS SDK:

```swift
import FastcheckoutKit

let manager = FastcheckoutManager(client: FastcheckoutClient(apiKey: "API_KEY"))
```

2. Start checkout with completion callback:

```swift
manager.startCheckout(transactionId: "ID", host: self, onCompletion: { status, error in
    if let status = status {
        print(status)
    } else {
        print(error?.localizedDescription)
    }
})
```

> **✅ Success!**
> You can now initiate a checkout and retrieve the <<glossary:transaction status>>.

# Example

```swift
import UIKit
import FastcheckoutKit

class ViewController: UIViewController {

   private let manager = FastcheckoutManager(client: FastcheckoutClient(apiKey: "API_KEY"))

   override func viewDidLoad() {
       super.viewDidLoad()

       // Add a button to the navigationBar
       let startButton = UIBarButtonItem(title: "Start",
                                         style: .done,
                                         target: self,
                                         action: #selector(self.startCheckout))
       navigationItem.rightBarButtonItem = startButton
   }

   // MARK: Actions

   @objc func startCheckout() {
       manager.startCheckout(transactionId: "id", host: self, onCompletion: { status, error in
           if let status = status {
               print(status)
               switch status.state {
                case .cancelled:
                    break
                case .completed:
                    break
                case .declined:
                    break
                case .pending:
                    break
                case .uncleared:
                    break
                @unknown default:
                    break
                }
           } else {
               print(error?.localizedDescription)
           }
       })
   }

}
```

# Environments
The SDK operates in two environments: **live** (default) and **test** (no real transactions processed). We recommend testing your integration before release. For how to select the environment, see the example below.

To customize the SDK, you need to inject properties into it. 

```swift
// Build `Settings` object to customize FCO SDK
let settings = Settings.build()
settings.environmentKey = FastcheckoutTestEnvironment
settings.debug = true
settings.biometricAuthenticationEnabled = true
settings.skipShowCartAtBeginning = true
settings.pinning = false
        
let client = FastcheckoutClient(apiKey: apiKey, settings: settings)
self.manager = FastcheckoutManager(client: client)
```

<br>

---

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:integration@multisafepay.com">integration@multisafepay.com</a></p>
</blockquote>

[Top of page](#)
