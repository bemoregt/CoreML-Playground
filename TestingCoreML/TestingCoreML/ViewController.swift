//
//  ViewController.swift
//  TestingCoreML
//
//  Created by David Cordero on 06.08.17.
//  Copyright © 2017 David Cordero. All rights reserved.
//

import UIKit
import CoreML

class ViewController: UIViewController {

    let fruitsClassifier = FruitsClassifier()

    override func viewDidLoad() {
        super.viewDidLoad()
        
        if let predition = try? fruitsClassifier.prediction(weight: 150, skin: 0) {
            print(predition.fruit)
        }
    }
}
