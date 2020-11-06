---
title : "Fastcheckout SDK iOS configuration manual"
meta_title: "Fastcheckout SDK iOS configuration manual - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
---

### Introduction

The Fastcheckout SDK is a library that you can integrate into your native Android, iOS and/or React Native application providing connection to MultiSafepay services. The Fastcheckout SDK adds a smooth, fast and native checkout experience to your mobile app, and by storing and reusing data it is the fastest checkout process available for shopping apps.

As an integrator, you only need to provide a valid MSP transaction identifier or create a transaction. The Fastcheckout SDK leverages the checkout process for you, providing notifications for all possible outcomes (success, pending, cancelled, etc.) once it completes a transaction. The checkout process flow includes:

* Shipping details:
    * Preferred shipping details
    * Add shipping details
* Payment methods:
    * Preferred payment methods
    * Add payment methods
    * Coupons
* Confirmation details

#### Additional details

The Fastcheckout SDK provides the additional following features:

* Authentication into Fastcheckout: 
    * It provides secure sign-up/login functionality
* Check orders:
    * Open seamless support tickets to related orders
* Support orders:
    * Easily open a support ticket related to an order
* Edit payment information:
    * List and edit user’s stored payment details
* Manage shipping addresses:
    * List, add and edit shipping information

*If you need more information, please check the documentation that you will find inside the SDK, which contains all classes, methods, common troubleshooting and more details.*

Please refer to the MultiSafepay API Documentation to perform different calls through which you can start transactions, update transactions, perform refunds and receive information about transactions: https://docs.multisafepay.com/api/#orders

### Requirements

* Xcode 11.0 and iOS 13 SDK
* iOS 9+ target
* Swift 5.1 or Objective-C

### Installation

First you have to access into your Back Office and get a valid API key (_Settings_ → _Website Settings_).

Once you have your valid API key, you can get the SDK on our [GitHub repository](https://github.com/MultiSafepay/fastcheckout-ios-sdk)

Add the FastcheckoutKit.xcframework as an embedded framework into your project. The next steps will guide you through the process:

1. Open the folder in Finder where you have downloaded FastcheckoutKit.framework and drag it into the Project Navigator of your application’s Xcode project.
2. Make sure you select Copy items if needed unless you have already copied the framework into your project folder.
3. Select your application project in the Project Navigator (blue project icon) to navigate to target configuration window and select the application target under the Targets heading in the sidebar.
4. In the tab bar at the top of that window, open the General panel.
5. Click on the + button under the Embedded Binaries section.
6. Select FastcheckoutKit.xcframework

You can now start using the FastcheckoutKit SDK in your App.

### Demo

You can easily integrate Fastcheckout iOS SDK into your app, you just need to follow the next steps:

1. Setup iOS SDK

```swift
import FastcheckoutKit

let manager = FastcheckoutManager(client: FastcheckoutClient(apiKey: "API_KEY"))
```

2. Start checkout with completion callback

```swift
manager.startCheckout(transactionId: "ID", host: self, onCompletion: { status, error in
    if let status = status {
        print(status)
    } else {
        print(error?.localizedDescription)
    }
})
```

And that’s it, that’s all you need to do to integrate the iOS SDK to start a checkout and retrieve the transaction status once it completes.

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
The SDK has two environments on which to operate, LIVE and TEST. You might want to test your integration in the TEST environment before release because no real transaction is performed in TEST environment. To do this you will have to customize the SDK behaviour, because by default it uses LIVE environment among other things.

To be able to customize some aspects of the SDK, the integrator will be able to inject some properties into it. Check out the example below to see how you can select which environment to use among other things. Keep in mind that you may not need to do this at all.

```swift
// Build `Settings` object to customize FCO SDK
let settings = Settings.build()
settings.environmentKey = FastcheckoutTestEnvironment
settings.debug = true
settings.biometricAuthenticationEnabled = true
settings.skipShowCartAtBeginning = true
        
let client = FastcheckoutClient(apiKey: apiKey, settings: settings)
self.manager = FastcheckoutManager(client: client)
```

### SDK Snapshots

1. The following snapshots will walk you through some of features offered by the Fastcheckout iOS SDK.
    * Logging in with a registered email: 
        
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-ios/fastcheckout-ios-1.png" title="screenshot 1">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-ios/fastcheckout-ios-2.png" title="screenshot 2">}}

    * Logging in with a non-registered email will automatically take the user to the register SDK screen: 

      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-ios/fastcheckout-ios-3.png" title="screenshot 3">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-ios/fastcheckout-ios-4.png" title="screenshot 4">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-ios/fastcheckout-ios-5.png" title="screenshot 5">}}

    * If the user is registered and resets its email account, the SDK  will automatically send a new security code to new entered email: 

      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-ios/fastcheckout-ios-6.png" title="screenshot 6">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-ios/fastcheckout-ios-7.png" title="screenshot 7">}}

    * Once the user enters the security code received by email (if the security code is received via SMS it will automatically get added to appropriate field, and the SDK will move into the following state) the SDK will ask for a new security PIN, once entered, the SDK will provide Biometric options (in iOS face recognition is also available):

      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-ios/fastcheckout-ios-8.png" title="screenshot 8">}}

    * The checkout process follows. From a merchant’s webshop checkout option, the SDK enters into the checkout process. The first view will be the delivery view with shipping options if available. Once the continue button is selected, the SDK moves into the Payment screen and the payment logic follows.
    
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-ios/fastcheckout-ios-9.png" title="screenshot 9">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-ios/fastcheckout-ios-10.png" title="screenshot 10">}}
      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-ios/fastcheckout-ios-11.png" title="screenshot 11">}}
    
    * Once the payment process is completed the SDK will proceed to the “transaction is complete” screen. The SDK callback will notify the client app about this or any other results (uncleared, cancel, etc.). Pressing the button “Back to Shop” will redirect the user to the Merchant’s webshop.

      {{< zoom_able class="img-size" url="/integrations/sdk/fastcheckout-ios/fastcheckout-ios-12.png" title="screenshot 12">}}


