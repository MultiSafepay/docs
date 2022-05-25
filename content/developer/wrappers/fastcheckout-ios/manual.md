---
title : "FastCheckout iOS SDK manual"
meta_title: "FastCheckout iOS SDK manual - MultiSafepay Docs"
aliases: 
    - /integrations/fastcheckout-ios/manual/
---

### Introduction

As an integrator, you only need to provide a valid MSP transaction identifier or create a transaction. The FastCheckout SDK leverages the checkout process for you, providing notifications for all possible outcomes (success, pending, cancelled, etc.) once it completes a transaction. The checkout process flow includes:

- Shipping details:
    - Preferred shipping details
    - Add shipping details
- Payment methods:
    - Preferred payment methods
    - Add payment methods
    - Gift cards
- Confirmation details

#### Features

The FastCheckout SDK provides the following additional features:

- Secure sign up and sign in functionality
- Open seamless support tickets to related orders
- List and edit users' stored payment details
- List, add, and edit shipping information

For more information, see the documentation in the SDK, which contains all classes, methods, and troubleshooting.

To learn more about creating, updating and retrieving orders, see the [API reference](https://docs-api.multisafepay.com/reference/introduction).

### Requirements

* Xcode 12.0 and iOS 15 SDK
* iOS 9+ target
* Swift 5.3 or Objective-C

### Installation

1. Copy your [site API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code) to get the SDK from our [GitHub repository](https://github.com/MultiSafepay/fastcheckout-ios-sdk).
2. Add the FastCheckoutKit.xcframework as an embedded framework into your project. 
3. In Finder, open the folder where you downloaded FastCheckoutKit.framework to, and then drag it into the Project Navigator of your application’s Xcode project.
4. If you haven't already copied the framework into your project folder, click **Copy items**.
5. In the Project navigator (blue project icon), select your application project to navigate to target configuration window, and then under **Targets** in the sidebar, select the application target.
6. In the tab bar at the top of that window, open the **General** panel.
7. Under **Embedded binaries**,click **+**.
8. Select **FastCheckoutKit.xcframework**.

You can now start using the FastCheckoutKit SDK in your app.

### Demo

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

And that’s it! Now you can start a checkout and retrieve the [transaction status](/about-payments/multisafepay-statuses/) once it completes.

###### Complete example

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

### Advanced setup
The SDK operates in two environments: LIVE (default) and TEST (no real transactions processed). We recommend testing your integration before release. Check out the example below to see how you can select which environment to use.

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

### SDK snapshots

1. The following snapshots walk you through some of features offered by the FastCheckout iOS SDK.
    - Logging in with a registered email: 
        
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/content/developer/wrappers/fastcheckout-ios/fastcheckout-ios-1.png" title="screenshot 1">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/content/developer/wrappers/fastcheckout-ios/fastcheckout-ios-2.png" title="screenshot 2">}}

    - Logging in with an unregistered email automatically takes the customer to the **Register** screen: 

      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/content/developer/wrappers/fastcheckout-ios/fastcheckout-ios-3.png" title="screenshot 3">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/content/developer/wrappers/fastcheckout-ios/fastcheckout-ios-4.png" title="screenshot 4">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/content/developer/wrappers/fastcheckout-ios/fastcheckout-ios-5.png" title="screenshot 5">}}

    - If the customer is registered and resets their email account, the SDK  automatically sends a new security code to new email provided: 

      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/content/developer/wrappers/fastcheckout-ios/fastcheckout-ios-6.png" title="screenshot 6">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/content/developer/wrappers/fastcheckout-ios/fastcheckout-ios-7.png" title="screenshot 7">}}

    - Once the customer enters the security code received by email (if the security code is received via SMS it is automatically added to the appropriate field, and the SDK moves to the following state), the SDK asks for a new security PIN. Having entered the PIN, the SDK provides biometric options, including face recognition:

      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/content/developer/wrappers/fastcheckout-ios/fastcheckout-ios-8.png" title="screenshot 8">}}

    - The checkout process follows. From the webshop checkout, the SDK enters into the checkout process. The first screen is the **Delivery** screen, with shipping options (if available). When the customer clicks **Continue**, the SDK moves to the **Payment** screen and the payment logic follows.  
    
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/content/developer/wrappers/fastcheckout-ios/fastcheckout-ios-9.png" title="screenshot 9">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/content/developer/wrappers/fastcheckout-ios/fastcheckout-ios-10.png" title="screenshot 10">}}
      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/content/developer/wrappers/fastcheckout-ios/fastcheckout-ios-11.png" title="screenshot 11">}}
    
    - Once payment is completed, the SDK proceeds to the **Transaction complete** screen. The SDK callback notifies the client app of the transaction status, e.g. Uncleared, Cancelled. When the customer clicks **Back to shop**, they are redirected back to the webshop.

      {{< zoom_able class="img-size" url="https://raw.githubusercontent.com/MultiSafepay/docs/master/content/developer/wrappers/fastcheckout-ios/fastcheckout-ios-12.png" title="screenshot 12">}}


