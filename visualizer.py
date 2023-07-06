import numpy as np
import cv2

def array_to_image(array,name):
    height, width = 200, 600
    image = np.zeros((height, width,3),dtype = "uint8")
    pos_x = (width - 500) // 2
    pos_y = height - 30
    dist = 5

    for element in array:
        image = cv2.line(image, (pos_x, pos_y), (pos_x, pos_y - element), (255,255,0),1)
        pos_x += dist
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.putText(image, name, (30,30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    image = cv2.rectangle(image, (0,0), (width, height), (255,0,255), 1)
    return image

def create_main_frame(unsorted_array):
    unsorted = array_to_image(unsorted_array, "unsorted")
    sort = array_to_image(np.sort(unsorted_array), "sort")
    bubble = array_to_image([], "bubble_sort")
    radix = array_to_image([], "radix_sort")
    merge = array_to_image([], "merge_sort")
    quick = array_to_image([], "quick_sort")
    
    result_left = cv2.vconcat([unsorted, sort, bubble])
    result_right =  cv2.vconcat([radix, merge, quick])
    result = cv2.hconcat([result_left, result_right])
    return result

def image_within_main(image, array, name, top_left, bottom_right):
    small_image = array_to_image(array, name)
    image[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]] = small_image
    return image

if __name__ == "__main__":
    unsorted_array = np.random.randint(1, 100, 100)
    #visualize_array(unsorted_array, "unsorted")
    #array_to_image(unsorted_array,"unsorted")
    main = create_main_frame(unsorted_array)
    #main = image_within_main(main, unsorted_array, "sorted", (600,0), (1200,200))
    cv2.imshow("main", main)
    cv2.waitKey(0)