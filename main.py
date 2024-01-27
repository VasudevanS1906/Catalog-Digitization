import random
import string
import sys
import json
from PIL import Image
import numpy
print("BAGIT CATALOG DIGITIZATION")
cat = raw_input("1-Digitization,2-View Catalog \n")

if cat == "1" :
    print("Digitization")
    digi = raw_input("1-text,2-text indic,3-voice,4-voice indic,5-image,6-hybrid \n ")
    if digi == "1" :
        import time
        t0 = time.time()
        print("1-text")
        s_id = raw_input("enter sku id \n")
        s_pce = raw_input("enter price \n")
        #s_size = raw_input("enter size \n")
        s_nme = raw_input("enter product name \n")
        s_des = raw_input("enter product count \n")
        #s_clr = raw_input("enter colour \n")
        #s_brnd = raw_input("enter brand \n")
        s_prdct_img = raw_input("enter product image \n")
        print ("the product name is",s_nme)
        print ("the sku id is",s_id)
        print ("the product price is",s_pce)
        #print ("the size is",s_size)
        print ("the product count is",s_des)
        #print ("the colour is",s_clr)
        #print ("the brand of the product is",s_brnd)
        print ("the product image is",s_prdct_img)
        img = Image.open(s_prdct_img)
        img.show()
        outfile = open("C:/Python27/" + s_id +".txt", "w")
        outfile.writelines(s_prdct_img + '\n')
        outfile.writelines(s_nme + '\n')
        outfile.writelines(s_id + '\n')
        outfile.writelines(s_pce + '\n')
        #outfile.writelines(s_size + '\n')
        outfile.writelines(s_des + '\n')
        #outfile.writelines(s_clr + '\n')
        #outfile.writelines(s_brnd + '\n')
        outfile.close()
        fle = open("C:/Python27/" + s_id +".txt", "r")
        file_contents = fle.read()
        print (file_contents)
        fle.close()
        t1 = time.time()
        total = t1 - t0
        print (total)
        t_put = round(((float(s_des))/(float(total))))
        print("The throughput of digitization is "+str(t_put)+" products per second")
        multi = round(float(t_put)* float(86400))
        print("No. of products that can be digitised per day is",str(multi))

        
    elif digi == "2" :
        import time
        t0 = time.time()
        print("2-text indic")
        from translate import Translator
        #print("\nINDIAN LANGUAGE TRANSLATOR\n")
        print("lang_code language \n en English(India) \n gu-IN Gujarati(India) \n hi-IN Hindi(India) \n kn-IN Kannada(India) \n kok-IN Konkani(India) \n mr-IN Marathi(India) \n pa-IN Punjabi(India) \n sa-IN Sanskrit(India) \n ta-IN Tamil(India) \n te-IN Telugu(India)")
        say_lang=raw_input("\nEnter the source language :")
        convert_lang=raw_input("\nEnter the language you want to convert into")
        translator=Translator(from_lang = say_lang,to_lang=convert_lang)
        #sentence=raw_input("\nENTER THE SENTENCE YOU WANT TO CONVERT INTO :")
        #translation=translator.translate(sentence)
        #print(translation)
        pr_name = "enter product name"
        pr_id =  "enter product id"
        pr_price = "enter product price"
        pr_image = "enter product image"
        pr_count = "enter total product count "
        tr_pn = translator.translate(pr_name)
        tr_pid = translator.translate(pr_id)
        tr_price = translator.translate(pr_price)
        tr_image = translator.translate(pr_image)
        tr_count = translator.translate(pr_count)
        ip_pn = raw_input(tr_pn)
        ip_pid = raw_input(tr_pid)
        ip_price = raw_input(tr_price)
        ip_image = raw_input(tr_image)
        ip_count = raw_input(tr_count)

        pntmsg_name = "the product name is"
        pntmsg_id =  "the sku id is"
        pntmsg_price = "the product price is"
        pntmsg_image = "the product image is"
        pntmsg_count = "the product count is"
        pntmsg_tr_pn = translator.translate(pntmsg_name)
        pntmsg_tr_pid = translator.translate(pntmsg_id)
        pntmsg_tr_price = translator.translate(pntmsg_price)
        pntmsg_tr_image = translator.translate(pntmsg_image)
        pntmsg_tr_count = translator.translate(pntmsg_count)
        
        
        print (pntmsg_tr_pn)
        print (ip_pn)
        print (pntmsg_tr_pid)
        print (ip_pid)
        print (pntmsg_tr_price)
        print (ip_price)
        print (pntmsg_tr_count)
        print (ip_count)
        print (pntmsg_tr_image)
        print (ip_image)
        img = Image.open(ip_image)
        img.show()
        outfile = open("C:/Python27/" + ip_pid +".txt", "w")
        outfile.writelines(ip_image + '\n')
        #result.writelines("\n".join(map(str, lines))) – 
        #outfile.writelines("\n".join(map(str,pntmsg_tr_pn))
        outfile.writelines(ip_pn + '\n')
        #outfile.writelines("\n".join(map(str,pntmsg_tr_pid))
        #outfile.writelines(pntmsg_tr_pid +'\n')
        outfile.writelines(ip_pid + '\n')
        #outfile.writelines("\n".join(map(str,pntmsg_tr_price))
        #outfile.writelines(pntmsg_tr_price + '\n')
        outfile.writelines(ip_price + '\n')
        #outfile.writelines("\n".join(map(str,pntmsg_tr_count))
        #outfile.writelines(pntmsg_tr_count  + '\n')
        outfile.writelines(ip_count + '\n')
        #outfile.writelines("\n".join(map(str,pntmsg_tr_image))
        #outfile.writelines(pntmsg_tr_image + '\n')
        
        outfile.close()
        fle = open("C:/Python27/" + ip_pid +".txt", "r")
        file_contents = fle.read()
        print (file_contents)
        fle.close()
        t1 = time.time()
        total = t1 - t0
        print (total)
        t_put = round(((float(ip_count))/(float(total))))
        print("The throughput of digitization is "+str(t_put)+" products per second")
        multi = round(float(t_put)* float(86400))
        print("No. of products that can be digitised per day is",str(multi))

        
    elif digi == "3" :
        import time
        t0 = time.time()
        print("3-voice")
        from gtts import gTTS
        from playsound import playsound 
        import os
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        #print("lang_code language \n en English(India) \n gu-IN Gujarati(India) \n hi-IN Hindi(India) \n kn-IN Kannada(India) \n kok-IN Konkani(India) \n mr-IN Marathi(India) \n pa-IN Punjabi(India) \n sa-IN Sanskrit(India) \n ta-IN Tamil(India) \n te-IN Telugu(India)")
        #say_lang=raw_input("\nEnter the source language :")
        #convert_lang=raw_input("\nEnter the language you want to convert into")
        #pr_name = "enter product name"
        #pr_id =  "enter product id"
        #pr_price = "enter product price"
        #pr_image = "enter product image"
        #pr_count = "enter total product count "
        #tr_pn = translator.translate(pr_name)
        #tr_pid = translator.translate(pr_id)
        #tr_price = translator.translate(pr_price)
        #tr_image = translator.translate(pr_image)
        #tr_count = translator.translate(pr_count)
        language = 'en'
        s_id = "enter sku id \n"
        s_pce = "enter price \n"
        s_nme = "enter product name \n"
        s_prdct_img = "enter product image \n"
        s_prdct_count = "enter product count \n"
        obj_id = gTTS(text=s_id, lang=language, slow=False) 
        obj_id.save('C:/Python27/id.mp3')
        playsound('C:/Python27/id.mp3') 
        ip_s_id = raw_input("enter sku id \n")
        #os.system('mpg321 id.mp3')
        obj_pce = gTTS(text=s_pce, lang=language, slow=False) 
        obj_pce.save('C:/Python27/price.mp3')
        playsound('C:/Python27/price.mp3') 
        ip_s_pce = raw_input("enter price \n")
        obj_nme = gTTS(text=s_nme, lang=language, slow=False) 
        obj_nme.save('C:/Python27/name.mp3')
        playsound('C:/Python27/name.mp3') 
        ip_s_nme = raw_input("enter product name \n")
        obj_prdct_img = gTTS(text=s_prdct_img, lang=language, slow=False) 
        obj_prdct_img.save('C:/Python27/productimage.mp3')
        playsound('C:/Python27/productimage.mp3') 
        ip_s_prdct_img = raw_input("enter product image \n")
        obj_prdct_count = gTTS(text=s_prdct_count, lang=language, slow=False) 
        obj_prdct_count.save('C:/Python27/productcount.mp3')
        playsound('C:/Python27/productcount.mp3') 
        ip_s_prdct_count = raw_input("enter product count \n")
        
        
        
        print ("the product name is",ip_s_nme)
        print ("the sku id is",ip_s_id)
        print ("the product price is",ip_s_pce)
        print ("the product count is",ip_s_prdct_count)
        print ("the product image is",ip_s_prdct_img)
        img = Image.open(ip_s_prdct_img)
        img.show()
        outfile = open("C:/Python27/" + ip_s_id +".txt", "w")
        outfile.writelines(ip_s_prdct_img + '\n')
        outfile.writelines(ip_s_nme + '\n')
        outfile.writelines(ip_s_id + '\n')
        outfile.writelines(ip_s_pce + '\n')        
        outfile.writelines(ip_s_prdct_count + '\n')
        outfile.close()
        fle = open("C:/Python27/" + ip_s_id +".txt", "r")
        file_contents = fle.read()
        print (file_contents)
        fle.close()
        t1 = time.time()
        total = t1 - t0
        print (total)
        t_put = round(((float(ip_s_prdct_count))/(float(total))))
        print("The throughput of digitization is "+str(t_put)+" products per second")
        multi = round(float(t_put)* float(86400))
        print("No. of products that can be digitised per day is",str(multi))
        
    elif digi == "4" :
        import time
        t0 = time.time()
        print("4-voice indic")
        from translate import Translator
        from urlparse import urlparse
        from gtts import gTTS
        from playsound import playsound 
        import os
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        #print("\nINDIAN LANGUAGE TRANSLATOR\n")
        print("lang_code language \n en English(India) \n gu-IN Gujarati(India) \n hi-IN Hindi(India) \n kn-IN Kannada(India) \n kok-IN Konkani(India) \n mr-IN Marathi(India) \n pa-IN Punjabi(India) \n sa-IN Sanskrit(India) \n ta-IN Tamil(India) \n te-IN Telugu(India)")
        say_lang=raw_input("\nEnter the source language :")
        con_language=raw_input("\nEnter the language you want to convert into")
        translator=Translator(from_lang = say_lang,to_lang=con_language)
        #sentence=raw_input("\nENTER THE SENTENCE YOU WANT TO CONVERT INTO :")
        #translation=translator.translate(sentence)
        #print(translation)
        pr_name = "enter product name"
        pr_id =  "enter product id"
        pr_price = "enter product price"
        pr_image = "enter product image"
        pr_count = "enter total product count "
        tr_pn = translator.translate(pr_name)
        tr_pid = translator.translate(pr_id)
        tr_price = translator.translate(pr_price)
        tr_image = translator.translate(pr_image)
        tr_count = translator.translate(pr_count)
                
       
        language = 'en'
        obj_pid = gTTS(text=cl_id,lang=language,slow=False)
        obj_pid.save('C:/Python27/clid.mp3')
        playsound('C:/Python27/clid.mp3')
        #esng.say("'" + tr_pid, "'")
        ip_pid = raw_input(tr_pid)
        #ip_s_id = raw_input("enter sku id \n")
        #os.system('mpg321 id.mp3')
        obj_pce = gTTS(text=cl_price, lang=language, slow=False) 
        obj_pce.save('C:/Python27/price.mp3')
        playsound('C:/Python27/price.mp3')
        ip_price = raw_input(tr_price)
        #ip_s_pce = raw_input("enter price \n")
        obj_nme = gTTS(text=cl_name, lang=language, slow=False) 
        obj_nme.save('C:/Python27/name.mp3')
        playsound('C:/Python27/name.mp3')
        ip_pn = raw_input(tr_pn)
        #ip_s_nme = raw_input("enter product name \n")
        obj_prdct_img = gTTS(text=cl_image, lang=language, slow=False) 
        obj_prdct_img.save('C:/Python27/productimage.mp3')
        playsound('C:/Python27/productimage.mp3')
        ip_image = raw_input(tr_image)
        #ip_s_prdct_img = raw_input("enter product image \n")
        obj_prdct_count = gTTS(text=cl_count, lang=language, slow=False) 
        obj_prdct_count.save('C:/Python27/productcount.mp3')
        playsound('C:/Python27/productcount.mp3')
        ip_count = raw_input(tr_count)
        #ip_s_prdct_count = raw_input("enter product count \n")
                
        print ("the product name is",ip_pn)
        print ("the sku id is",ip_pid)
        print ("the product price is",ip_price)
        print ("the product count is",ip_count)
        print ("the product image is",ip_image)
        img = Image.open(ip_image)
        img.show()
        outfile = open("C:/Python27/" + ip_pid +".txt", "w")
        outfile.writelines(ip_image + '\n')
        outfile.writelines(ip_pn + '\n')
        outfile.writelines(ip_pid + '\n')
        outfile.writelines(ip_price + '\n')
        outfile.writelines(ip_count + '\n')
        outfile.close()
        fle = open("C:/Python27/" + ip_pid +".txt", "r")
        file_contents = fle.read()
        print (file_contents)
        fle.close()
        t1 = time.time()
        total = t1 - t0
        print (total)
        t_put = round(((float(ip_count))/(float(total))))
        print("The throughput of digitization is "+str(t_put)+" products per second")
        multi = round(float(t_put)* float(86400))
        print("No. of products that can be digitised per day is",str(multi))
        
    elif digi == "5" :
        import time
        t0 = time.time()
        print("5-image")
        from PIL import Image
        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Python27\tesseract.exe'  # your path may be different
        
        s_id = raw_input("enter sku id \n")
        s_pce = raw_input("enter price \n")
        s_nme = raw_input("enter product name \n")
        s_prdct_img = raw_input("enter product image \n")
        s_prdct_count = raw_input("enter product count \n")
        is_id = pytesseract.image_to_string(Image.open(s_id))
        is_pce = pytesseract.image_to_string(Image.open(s_pce))
        is_nme = pytesseract.image_to_string(Image.open(s_nme))
        #is_prdct_img = pytesseract.image_to_string(Image.open(s_prdct_img))
        ies_prdct_count = pytesseract.image_to_string(Image.open(s_prdct_count))
        print ("the product name is",is_nme)
        print ("the sku id is",is_id)
        print ("the product price is",is_pce)
        print ("the product image is",s_prdct_img)
        print ("the product count is",ies_prdct_count)
        img = Image.open(s_prdct_img)
        img.show()
        outfile = open("C:/Python27/" + is_id +".txt", "w")
        outfile.writelines(s_prdct_img + '\n')
        outfile.writelines(is_nme + '\n')
        outfile.writelines(is_id + '\n')
        outfile.writelines(is_pce + '\n')
        #outfile.writelines(s_prdct_img + '\n')
        outfile.writelines(ies_prdct_count + '\n')
        outfile.close()
        fle = open("C:/Python27/" + is_id +".txt", "r")
        file_contents = fle.read()
        print (file_contents)
        fle.close()
        t1 = time.time()
        total = t1 - t0
        print (total)
        t_put = round(((float(ies_prdct_count))/(float(total))))
        print("The throughput of digitization is "+str(t_put)+" products per second")
        multi = round(float(t_put)* float(86400))
        print("No. of products that can be digitised per day is",str(multi)) 

    else :
        import time
        t0 = time.time()
        print("6-hybrid -- combination of text,text indic,image,voice & voice indic")
        from gtts import gTTS
        from playsound import playsound 
        import os
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        from translate import Translator
        from PIL import Image
        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Python27\tesseract.exe'
        
        s_id = raw_input("enter sku id \n")        
        #print("\nINDIAN LANGUAGE TRANSLATOR\n")
        print("lang_code language \n en English(India) \n gu-IN Gujarati(India) \n hi-IN Hindi(India) \n kn-IN Kannada(India) \n kok-IN Konkani(India) \n mr-IN Marathi(India) \n pa-IN Punjabi(India) \n sa-IN Sanskrit(India) \n ta-IN Tamil(India) \n te-IN Telugu(India)")
        say_lang=raw_input("\nEnter the source language :")
        convert_lang=raw_input("\nEnter the language you want to convert into")
        translator=Translator(from_lang = say_lang,to_lang=convert_lang)

        pr_name = "enter product name"

        pr_price = "enter product price"
        tr_pn = translator.translate(pr_name)
                
        tr_price = translator.translate(pr_price)
                
        ip_pn = raw_input(tr_pn)

        pntmsg_name = "the product name is"

        pntmsg_price = "the product price is"

        pntmsg_tr_pn = translator.translate(pntmsg_name)

        pntmsg_tr_price = translator.translate(pntmsg_price)

        language = 'ta'
        cl_price = "Tayaripu vilaiyai ullidavum \n"
        obj_pce = gTTS(text=cl_price, lang=language, slow=False) 
        obj_pce.save('C:/Python27/price.mp3')
        playsound('C:/Python27/price.mp3')
        ip_price = raw_input(tr_price)

        angua = 'en'
        s_prdct_img = "enter product image \n"
        obj_prdct_img = gTTS(text=s_prdct_img, lang=angua, slow=False) 
        obj_prdct_img.save('C:/Python27/productimage.mp3')
        playsound('C:/Python27/productimage.mp3') 
        ip_s_prdct_img = raw_input("enter product image \n")

        s_prdct_count = raw_input("enter product count \n")
        #is_prdct_count = pytesseract.image_to_string()
        is_prdct_count = pytesseract.image_to_string(Image.open(s_prdct_count))

        print ("the sku id is",s_id)
        print (pntmsg_tr_pn)
        print (ip_pn)
         
        print (pntmsg_tr_price)
        print (ip_price)
        print("the product image is ",ip_s_prdct_img)
        print ("the product count is",is_prdct_count)

        img = Image.open(ip_s_prdct_img)
        img.show()
        outfile = open("C:/Python27/" + s_id +".txt", "w")
        outfile.writelines(ip_s_prdct_img + '\n')
        outfile.writelines(ip_pn + '\n')
        outfile.writelines(s_id + '\n')
        outfile.writelines(ip_price + '\n')
        #outfile.writelines(ip_s_prdct_img + '\n')
        outfile.writelines(is_prdct_count + '\n')
        outfile.close()
        fle = open("C:/Python27/" + s_id +".txt", "r")
        file_contents = fle.read()
        print (file_contents)
        fle.close()
        t1 = time.time()
        total = t1 - t0
        print (total)
        t_put = round(((float(is_prdct_count))/(float(total))))
        print("The throughput of digitization is "+str(t_put)+" products per second")
        multi = round(float(t_put)* float(86400))
        print("No. of products that can be digitised per day is",str(multi))

elif cat == "2" :
    print("View catalog")
    import glob
    import os
    from bs4 import BeautifulSoup

    for filename in glob.glob('*txt'):
        print(filename)
    s_id = input("Enter SKU id \n")
    out_ile = open("C:/Python27/" + str(s_id) +".txt", "r")
    file_contents = out_ile.read()
    print(file_contents)
    


    with open("C:/Python27/" + str(s_id) +".txt", 'r') as f:

        contents = f.read()

        soup = BeautifulSoup(contents, 'lxml')

        for el in soup.findAll('img'):
            print(os.path.split(el['src'])[-1])
    
    out_ile.close()
    
else:
    print("Enter correct input ")

