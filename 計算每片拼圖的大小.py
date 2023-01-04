while True:  
    w, h, min_w,min_h = map(int,input().split())  
    picture_w = round(w/(w//min_w),3)  
    picture_h = round(h/(h//min_h),3)  
    print(picture_w,picture_h)  
