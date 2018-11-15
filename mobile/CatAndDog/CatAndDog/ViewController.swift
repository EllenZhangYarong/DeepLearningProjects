//
//  ViewController.swift
//  CatAndDog
//
//  Created by 张亚荣 on 2018/10/7.
//  Copyright © 2018年 Angel Zhang. All rights reserved.
//

import UIKit
import CoreML
import Vision

class ViewController: UIViewController {

    @IBOutlet weak var userImageView: UIImageView!
    @IBOutlet weak var classificationLabel: UILabel!
    
//    let imagePicker = UIImagePickerController()
//    fileprivate var currentVC: UIViewController!
    

    
    override func viewDidLoad() {
        super.viewDidLoad()

    }

    @IBAction func onCameraTapped(_ sender: Any) {
        showActionSheet()
//        present(imagePicker,animated: true,completion: nil)
    }
    
    func chooseCamera() {
        if UIImagePickerController.isSourceTypeAvailable(.camera){
            let myPickerController = UIImagePickerController()
            myPickerController.delegate = self;
            myPickerController.sourceType = .camera
            myPickerController.allowsEditing = false
            
            self.present(myPickerController, animated: true, completion: nil)
        }
    }
    
    func choosePhotoes(){
        if UIImagePickerController.isSourceTypeAvailable(.photoLibrary){
            let myPickerController = UIImagePickerController()
            myPickerController.delegate = self;
            myPickerController.sourceType = .photoLibrary
            myPickerController.allowsEditing = false

            self.present(myPickerController, animated: true, completion: nil)
        }
    }
    
    
    func showActionSheet(){

        let actionSheet = UIAlertController(title: nil, message: nil, preferredStyle: .actionSheet)
        
        actionSheet.addAction(UIAlertAction(title: "Camera", style: .default, handler: { (alert) in
            self.chooseCamera()
        }))
        
        actionSheet.addAction(UIAlertAction(title: "Gallery", style: .default, handler: { (alert) in
            self.choosePhotoes()
        }))
        
        actionSheet.addAction(UIAlertAction(title: "Cancel", style: .cancel, handler: nil))
        self.present(actionSheet, animated: true, completion: nil)
        
    }
    
}

extension ViewController: UIImagePickerControllerDelegate, UINavigationControllerDelegate{
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        self.dismiss(animated: true, completion: nil)
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        
        if let userPikedImage = info[UIImagePickerController.InfoKey.originalImage] as? UIImage {

            userImageView.image = userPikedImage
        }
        
        self.dismiss(animated: true, completion: nil)
    }
    
}

