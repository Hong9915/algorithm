import heapq

def time_to_minutes(time_str):
    hour, minute = map(int, time_str.split(":"))
    return hour * 60 + minute

def solution(book_time):

    bookings = []
    for start, end in book_time:
        start_min = time_to_minutes(start)
        end_min = time_to_minutes(end) + 10  
        bookings.append((start_min, end_min))
    

    bookings.sort()

    room_heap = []

    for start, end in bookings:
        if room_heap and room_heap[0] <= start:
            heapq.heappop(room_heap) 

        heapq.heappush(room_heap, end)  

    return len(room_heap)
