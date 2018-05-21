# -*- coding: utf-8 -*-
"""
Created on Mon May 21 00:37:10 2018

@author: Matthew Tarchick
"""
import os
import json
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "This writes a json config file for use with ssd file")
    parser.add_argument('-f', '--filename', help = 'The filename of the config file')
    parser.add_argument('-n', '--num_class', type = int, 
                        help = 'This is the number of classes the network tries to find, [-1 is default]'
                        )
    parser.add_argument('-i', '--input_shape', type = tuple, help = 'This is the input shape of the image [-1 is defulat]')
    parser.add_argument('-e', '--epochs', type = int, help = 'This is how many epochs the network should train')
    parser.add_argument('-m', '--save_model', help = 'this is the location or name to save model')
    parser.add_argument('-p', '--prior_pickle', help = 'this is the name of to look for the priors file')
    parser.add_argument('-x', '--img_dir', help = 'this is the folder to parse images')
    parser.add_argument('-a', '--ann_dir', help = 'this is the folder to parse XML annotations')
    parser.add_argument('-y', '--label_pickle', help = 'this is the file to save the label pickle to ')
    parser.add_argument('-r', '--reset', action = 'store_true', help = 'This resets all variables to their default state')
    #parser.add_argument('-c', '--checkpoint', help = 'This is the location to save model checkpoints')
        #Set config file name
    
    
    args = parser.parse_args()
    reset = args.reset
    
    if args.filename == None: 
        file = 'config.json'
    else:
        file = args.filename
    
    #Defaults
    config = {}
    
    if os.path.exists(file):
        print("Is a file!!")
        with open(file, 'r') as f:
            config = json.load(f)
    else:
        print("Doesn't exist!")
        with open(file, 'w') as f:
            json.dump(config, f)
    
      
        

    #set number of classes, default = 5   
    if args.num_class == -1 or reset: 
        config['num_class'] = 5
    elif args.num_class != None:
        config['num_class'] = args.num_class
    
    #set the image shape default = (300,300,3)    
    if args.input_shape == ('-', '1') or reset: 
        config['input_shape'] = (300,300,3)
    elif args.input_shape != None:
        config['input_shape'] = args.input_shape
    
    #set the number of epochs, default = 10
    if args.epochs == -1 or reset:
        config['epochs'] = 10
    elif args.epochs != None:
        config['epochs'] = args.epochs
        
    if args.save_model == '-1' or reset:
        config['save_model_path'] = 'C:\\pyscripts\\Player1\\new_model.h5'
    elif args.save_model != None:
        config['save_model_path'] = args.save_model   
        
    if args.prior_pickle == '-1' or reset:
        config['prior_pickle'] = 'C:\\pyscripts\\Player1\\prior_boxes_ssd300.pkl'
    elif args.prior_pickle != None:
        config['prior_pickle'] = args.prior_pickle
    
    if args.img_dir == '-1' or reset:
        config['img_directory'] = 'C:\\pyscripts\\Player1\\train_imgs\\'
    elif args.img_dir != None:
        config['img_directory'] = args.img_dir 

    if args.ann_dir == '-1' or reset:
        config['annotation_directory'] = 'C:\\pyscripts\\Player1\\annotations\\'
    elif args.ann_dir != None:
        config['annotation_directory'] = args.ann_dir
        
    if args.label_pickle == '-1' or reset:
        config['save_label_pickle'] = 'C:\\pyscripts\\Player1\\p1.pkl'
    elif args.label_pickle != None:
        config['save_label_pickle'] = args.label_pickle 
        
        
    print("Saving file!")
    print(config)  
    with open(file, 'w') as f:
        json.dump(config, f)
        
    print("File saved")
    

    
    
    
    