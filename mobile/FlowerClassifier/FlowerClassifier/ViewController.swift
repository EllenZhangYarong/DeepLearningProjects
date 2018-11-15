//
//  ViewController.swift
//  FlowerClassifier
//
//  Created by 张亚荣 on 2/11/18.
//  Copyright © 2018 Angel Zhang. All rights reserved.
//

import UIKit
import CoreML
import Vision

class ViewController: UIViewController {

    let imagePicker = UIImagePickerController()
    
    @IBOutlet weak var picImageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        imagePicker.delegate = self
        imagePicker.allowsEditing = false
//        imagePicker.allowsEditing = true // can crop ...
//        imagePicker.sourceType = .photoLibrary
        imagePicker.sourceType = .camera

    }

    @IBAction func onCameraTapped(_ sender: Any) {
        present(imagePicker, animated: true, completion: nil)
    }
    
}

extension ViewController: UIImagePickerControllerDelegate{
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        
        if let userPickedImage = info[UIImagePickerController.InfoKey.originalImage] as? UIImage{
            picImageView.image = userPickedImage
            
            guard let imageWaitClassify = CIImage(image: userPickedImage) else{
                fatalError("Could not convert to CIImage!")
            }
            
            detect(image: imageWaitClassify)
        }
        
//        let userPickedImage = info[UIImagePickerController.InfoKey.editedImage]
//        picImageView.image = userPickedImage as? UIImage
        imagePicker.dismiss(animated: true, completion: nil)
    }
    
    func detect(image: CIImage) {
        guard let model = try? VNCoreMLModel(for: Inceptionv3().model) else{
            fatalError("Failed to load CoreML model!")
            
        }
        
        let request = VNCoreMLRequest(model: model) { (request, error) in
            guard let results = request.results as? [VNClassificationObservation] else{
                fatalError("Model failed to process image!")
            }
//            print(results)
            self.navigationItem.title = results.first?.identifier
        }
        
        let handler = VNImageRequestHandler(ciImage: image)
        
        do {
            try handler.perform([request])
        }catch{
            print(error)
        }
        
        
    }
}

extension ViewController: UINavigationControllerDelegate{
    
}
