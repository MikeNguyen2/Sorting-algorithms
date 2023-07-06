import generator
import sorter
import visualizer
import cv2
import time

def bubble_sort_step_by_step(unsorted_array):
    global main_frame
    bubble_step = unsorted_array.copy()
    go = True
    while go == True:
        bubble_step, go = sorter.bubble_sort_step(bubble_step)
        main_frame = visualizer.image_within_main(main_frame, bubble_step, "bubble_sort", (0,400), (600,600))
        cv2.imshow("main_frame", main_frame)
        time.sleep(0.1)
        cv2.waitKey(1)

def radix_sort_step_by_step(unsorted_array):
    global main_frame
    max_value = max(unsorted_array)
    digit = 0
    sorted_array = unsorted_array.copy()
    while max_value > 0:
        sorted_array = sorter.counting_sort(sorted_array, digit)
        digit += 1
        max_value //= 10
        main_frame = visualizer.image_within_main(main_frame, sorted_array, "radix_sort", (600,0), (1200,200))
        cv2.imshow("main_frame", main_frame)
        time.sleep(0.1)
        cv2.waitKey(1)

def merge_sort_step_by_step(unsorted_array):
    global main_frame
    sorted_array = unsorted_array.copy()
    length = len(sorted_array)
    counter = 0
    while length > 0:
        length //= 2
        counter += 1    
    counter_2 = 0

    while counter > counter_2:
        temp_array = []
        for i in range(0,len(sorted_array),2**(counter_2+1)):
            merge_array = sorter.merge(sorted_array[i:i+2**counter_2], sorted_array[i+2**counter_2:i+2**(counter_2+1)])
            temp_array = [*temp_array, *merge_array]
        counter_2 += 1
        sorted_array = temp_array
        main_frame = visualizer.image_within_main(main_frame, sorted_array, "merge_sort", (600,200), (1200,400))
        cv2.imshow("main_frame", main_frame)
        time.sleep(0.1)
        cv2.waitKey(1)
    return sorted_array


def quick_sort_loop(unsorted_array, lower, upper):
    global main_frame
    if lower < upper: 
        sorted_array, pivot = sorter.quick_sort_pivot(unsorted_array, lower, upper)
        main_frame = visualizer.image_within_main(main_frame, sorted_array, "quick_sort", (600,400), (1200,600))
        cv2.imshow("main_frame", main_frame)
        time.sleep(0.1)
        cv2.waitKey(1)
        sorted_array_left = quick_sort_loop(sorted_array, lower, pivot-1)
        sorted_array_right = quick_sort_loop(sorted_array_left, pivot+1, upper)
        sorted_array =  [*sorted_array_left[:pivot], *sorted_array_right[pivot:]]
        return sorted_array
    return unsorted_array

def quick_sort_step_by_step(unsorted_array):
    sorted_array = quick_sort_loop(unsorted_array, 0, len(unsorted_array)-1)

def show_sorting_results(unsorted_array):
    sorted_array = sorter.sort(unsorted_array)
    bubble_sort = sorter.bubble_sort(unsorted_array)
    radix_sort = sorter.radix_sort(unsorted_array)
    merge_sort = sorter.merge_sort(unsorted_array)
    quick_sort = sorter.quick_sort(unsorted_array)

    unsorted = visualizer.array_to_image(unsorted_array, "unsorted")
    sort = visualizer.array_to_image(sorted_array, "sort")
    bubble = visualizer.array_to_image(bubble_sort, "bubble_sort")
    radix = visualizer.array_to_image(radix_sort, "radix_sort")
    merge = visualizer.array_to_image(merge_sort, "merge_sort")
    quick = visualizer.array_to_image(quick_sort, "quick_sort")
    
    result_left = cv2.vconcat([unsorted, sort, bubble])
    result_right =  cv2.vconcat([radix, merge, quick])
    result = cv2.hconcat([result_left, result_right])
    cv2.imshow("result", result)
    cv2.waitKey(0)
    
def establish_main_frame():
    unsorted_array = generator.generate()
    global main_frame
    main_frame = visualizer.create_main_frame(unsorted_array)
    
    def update(event,x,y,flags,param):
        global main_frame
        if event == cv2.EVENT_LBUTTONDOWN:#EVENT_LBUTTONDBLCLK:
            if 0 < x < 600 and 0 < y < 200: pass
            elif 0 < x < 600 and 200 < y < 400: pass
            elif 0 < x < 600 and 400 < y < 600: 
                bubble_sort_step_by_step(unsorted_array)
            elif 600 < x < 1200 and 0 < y < 200: 
                radix_sort_step_by_step(unsorted_array)
            elif 600 < x < 1200 and 200 < y < 400: 
                merge_sort_step_by_step(unsorted_array)
            elif 600 < x < 1200 and 400 < y < 600: 
                quick_sort_step_by_step(unsorted_array)
    cv2.namedWindow("main_frame", cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback('main_frame', update)

    while True:
        cv2.imshow("main_frame", main_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break


if __name__ == "__main__":
    unsorted_array = generator.generate()
    #show_sorting_results(unsorted_array)
    #bubble_sort_step_by_step(unsorted_array)
    establish_main_frame()
    #sorted_array = mergi(unsorted_array)
    #print(sorted_array)