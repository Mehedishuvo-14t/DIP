import cv2

# একটি ছবি লোড করুন (আপনার কম্পিউটারের যেকোনো ছবির পাথ দিতে পারেন)
img = cv2.imread('mountail.webp')

if img is not None:
    # ছবিটিকে গ্রে-স্কেল (Black & White) এ রূপান্তর করুন
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # নতুন ছবিটি সেভ করুন
    cv2.imwrite('gray_sample.jpg', gray_img)
    print("ইমেজ প্রসেসিং সফল হয়েছে!")
else:
    print("ছবিটি খুঁজে পাওয়া যায়নি, দয়া করে সঠিক পাথ দিন।")